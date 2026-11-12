"""Build the Markdown RCSA Challenge Report and compute the run status."""
from datetime import datetime

from .rules import FLAG_TEXT


def compute_status(state: dict) -> str:
    if state.get("fatal_error"):
        return "FAILED"
    bad = {"degraded", "warning", "failed"}
    if any(e.get("status") in bad for e in state.get("run_log", [])):
        return "COMPLETED_WITH_WARNINGS"
    return "COMPLETED"


def _cell(text) -> str:
    return str(text).replace("|", "/").replace("\n", " ").strip() or "-"


def build_report(state: dict) -> str:
    status = compute_status(state)
    process = state.get("process", "?")
    findings = state.get("findings", [])
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# RCSA Challenge Report: {process}",
        "",
        f"- Generated: {ts}",
        f"- Run status: **{status}**",
        "- Data: synthetic demonstration data only",
        "- Review: **human Second Line review required**. Approval: **Pending**",
        "- This report supports a reviewer. It does not rate risk, approve controls or decide compliance.",
        "",
    ]

    if state.get("fatal_error"):
        lines += ["## Run failed", "", f"{state['fatal_error']}", ""]

    if findings:
        applicable = sum(1 for f in findings if f["pair"]["applicable"])
        flag_counts: dict = {}
        for f in findings:
            for fl in f["flags"]:
                flag_counts[fl] = flag_counts.get(fl, 0) + 1
        high = [f["pair"]["pair_id"] for f in findings if f["review_priority"] == "high"]
        lines += ["## 1. Summary", "",
                  f"- Process-risk pairs analysed: {len(findings)} ({applicable} marked applicable by the First Line)",
                  f"- High review priority: {', '.join(high) if high else 'none'}",
                  "- Flags raised: " + (", ".join(f"{k} x{v}" for k, v in sorted(flag_counts.items())) or "none"),
                  "", "## 2. Overview", "",
                  "| Pair | Process | Risk | Applicable | Loss events | KRI | Prev. RCSA | Control | Flags | Scenario result (rules) | Review priority |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for f in findings:
            p = f["pair"]
            lines.append("| " + " | ".join(_cell(x) for x in [
                p["pair_id"], p["process"], f"{p['risk_id']} {p['risk']}", "Yes" if p["applicable"] else "No",
                f"{p['loss_events']} ({p['loss_amount']:,.0f} EUR)", p["kri"], "Y" if p["previous_rcsa"] else "N",
                p["control"], ", ".join(f["flags"]), f.get("scenario_result", ""), f["review_priority"]]) + " |")

        lines += ["", "## 3. Detailed challenges", ""]
        for f in findings:
            p, ch = f["pair"], f.get("challenge", {})
            lines += [f"### {p['pair_id']}: {p['risk']} ({p['process']})", ""]
            lines += [f"- {fl}: {FLAG_TEXT[fl]}" for fl in f["flags"]] or ["- No flags"]
            lines += ["", f"**Challenge:** {ch.get('challenge', '-')}", ""]
            qs = ch.get("questions_for_owner", [])
            if qs:
                lines += ["**Questions for the process owner:**"] + [f"- {q}" for q in qs] + [""]
            lines += [f"**Suggested follow-up:** {ch.get('suggested_action', '-')}", ""]
            lines += [f"Evidence cited: {', '.join(ch.get('evidence_used', [])) or '-'} "
                      f"(challenge source: {ch.get('source', '-')})"]
            if ch.get("note"):
                lines += [f"Note: {ch['note']}"]
            g = f.get("guidance", [])
            if g:
                lines += ["Guidance retrieved: " + "; ".join(f"{x['source_id']} ({x['title']})" for x in g)]
            lines += ["", "Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate", ""]

    ext = state.get("external", {})
    lines += ["## 4. External context (context only, not proof of internal control effectiveness)", ""]
    if not ext:
        lines += ["No external research was run.", ""]
    for name, res in ext.items():
        lines += [f"**{res['tool']}**: status `{res['status']}`, attempts {res['attempts']}"
                  + (f", error: {res['error']}" if res["error"] else "")]
        for i, item in enumerate(res["items"], start=1):
            lines += [f"- {item['title']} ({item['url']})"]
        lines += [""]

    lines += ["## 5. Run log", "", "| Time | Node | Status | Detail |", "|---|---|---|---|"]
    for e in state.get("run_log", []):
        lines.append(f"| {_cell(e['ts'])} | {_cell(e['node'])} | {_cell(e['status'])} | {_cell(e['detail'])} |")
    lines += ["", "## 6. Limitations", "",
              "- Synthetic data. No real bank records are used.",
              "- No numeric inherent or residual risk scores are produced.",
              "- A loss event alone does not prove a control failure.",
              "- Challenge text from the LLM is a draft for human review.", ""]
    return "\n".join(lines)
