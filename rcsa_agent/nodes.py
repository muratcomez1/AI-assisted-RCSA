"""LangGraph nodes. Each node takes the state and returns only what it changes."""
import json
import os
import re
from datetime import datetime
from pathlib import Path

from . import external as ext_tools
from . import llm as llm_mod
from .data_loader import find_default_csv, load_pairs
from .envloader import load_env
from .report import build_report as render_report
from .report import compute_status
from .retriever import load_chunks, retrieve
from .rules import FLAG_TEXT, evaluate_pair


def _log(node: str, status: str, detail: str) -> dict:
    return {"ts": datetime.now().strftime("%H:%M:%S"), "node": node, "status": status, "detail": detail}


def validate_input(state: dict) -> dict:
    load_env()
    log = []
    path = state.get("data_path") or os.environ.get("RCSA_SHEET_URL", "").strip() or find_default_csv()
    if not path:
        msg = "No input found. Pass --data (file or Google Sheet CSV link) or set RCSA_SHEET_URL in .env"
        return {"fatal_error": msg, "pairs": [], "run_log": [_log("validate_input", "failed", msg)]}

    pairs, errors = load_pairs(path, state.get("process", "Payment Processing"))
    if not pairs:
        msg = "; ".join(errors) or "No process-risk pairs loaded"
        return {"fatal_error": msg, "pairs": [], "run_log": [_log("validate_input", "failed", msg)]}

    updates = {"pairs": pairs, "data_path": path}
    for e in errors:
        log.append(_log("validate_input", "warning", e))
    log.append(_log("validate_input", "ok", f"Loaded {len(pairs)} process-risk pairs from {path}"))

    if state.get("use_llm", True) and not os.environ.get("OPENAI_API_KEY", "").strip():
        updates["use_llm"] = False
        log.append(_log("validate_input", "degraded", "OPENAI_API_KEY not set: using deterministic fallback instead of the LLM"))
    updates["run_log"] = log
    return updates


def route_after_validation(state: dict) -> str:
    return "abort" if state.get("fatal_error") else "continue"


def apply_rules(state: dict) -> dict:
    findings, log = [], []
    for pair in state["pairs"]:
        result = evaluate_pair(pair)
        findings.append({"pair": pair, "flags": result["flags"], "scenario_result": result["scenario_result"],
                         "review_priority": result["review_priority"]})
        for w in result["warnings"]:
            log.append(_log("apply_rules", "warning", w))
    high = sum(1 for f in findings if f["review_priority"] == "high")
    log.append(_log("apply_rules", "ok", f"Rules applied to {len(findings)} pairs; {high} high review priority"))
    return {"findings": findings, "run_log": log}


def retrieve_evidence(state: dict) -> dict:
    chunks = load_chunks("knowledge")
    if not chunks:
        return {"run_log": [_log("retrieve_evidence", "degraded", "No knowledge chunks found in ./knowledge")]}
    findings = []
    for f in state["findings"]:
        query = f["pair"]["risk"] + " " + " ".join(FLAG_TEXT[x] for x in f["flags"])
        findings.append(dict(f, guidance=retrieve(query, chunks, k=3)))
    return {"findings": findings,
            "run_log": [_log("retrieve_evidence", "ok", f"Retrieved guidance for {len(findings)} pairs from {len(chunks)} chunks")]}


def external_research(state: dict) -> dict:
    if not state.get("use_external", True):
        return {"external": {}, "run_log": [_log("external_research", "skipped", "Disabled with --no-external")]}
    process = state.get("process", "Payment Processing")
    label = "banking operations" if process.upper() == "ALL" else process
    results = {"gdelt": ext_tools.gdelt_search(label), "tavily": ext_tools.tavily_search(label)}
    log = []
    for res in results.values():
        status = {"ok": "ok", "empty": "warning", "failed": "degraded", "skipped": "skipped"}[res["status"]]
        detail = f"{res['tool']}: {res['status']}, {len(res['items'])} items, {res['attempts']} attempts"
        if res["error"]:
            detail += f" ({res['error']})"
        log.append(_log("external_research", status, detail))
    return {"external": results, "run_log": log}


def llm_challenge(state: dict) -> dict:
    external_items = []
    for res in state.get("external", {}).values():
        external_items += res["items"]
    external_items = external_items[:6]

    use_llm = state.get("use_llm", True)
    client, model = None, os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    log = []
    if use_llm:
        try:
            client = llm_mod.make_client()
        except Exception as exc:
            use_llm = False
            log.append(_log("llm_challenge", "degraded", f"Could not create OpenAI client: {exc}"))

    findings, fallbacks = [], 0
    for f in state["findings"]:
        if use_llm:
            ch = llm_mod.challenge_pair(f, external_items, client, model)
        else:
            ch = llm_mod.fallback_challenge(f, "LLM not used in this run")
        if ch["source"] != "llm":
            fallbacks += 1
            if use_llm:
                log.append(_log("llm_challenge", "degraded", f"{f['pair']['pair_id']}: {ch['note']}"))
        findings.append(dict(f, challenge=ch))
    n = len(findings)
    log.append(_log("llm_challenge", "ok" if fallbacks == 0 else "degraded",
                    f"{n - fallbacks}/{n} challenges written by the LLM ({model}); {fallbacks} deterministic fallback"))
    return {"findings": findings, "run_log": log}


def build_report(state: dict) -> dict:
    return {"report_md": render_report(state),
            "run_log": [_log("build_report", "ok", "Report assembled")]}


def finalize(state: dict) -> dict:
    """Write the report and the machine-readable run log. Human review is the next (manual) step."""
    out_dir = Path(state.get("out_dir", "outputs/reports"))
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "_", state.get("process", "run").lower()).strip("_")
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = out_dir / f"rcsa_challenge_{slug}_{stamp}.md"
    log_path = out_dir / f"rcsa_run_log_{slug}_{stamp}.json"

    log = list(state.get("run_log", []))
    status = compute_status(state)
    report_md = state.get("report_md") or render_report(state)  # failure path has no report yet
    report_path.write_text(report_md, encoding="utf-8")
    final_entry = _log("finalize", "ok", f"Report saved to {report_path}. Pending human review")
    log.append(final_entry)
    log_path.write_text(json.dumps({"status": status, "process": state.get("process"),
                                    "run_log": log, "external": state.get("external", {})},
                                   indent=2, ensure_ascii=False), encoding="utf-8")
    return {"report_path": str(report_path), "log_path": str(log_path), "status": status, "run_log": [final_entry]}
