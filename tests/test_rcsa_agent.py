"""Run with:  pytest -q   (graph test needs langgraph installed)."""
from pathlib import Path

import pytest

from rcsa_agent import external
from rcsa_agent.data_loader import load_pairs
from rcsa_agent.llm import _validate, fallback_challenge
from rcsa_agent.retriever import load_chunks, retrieve
from rcsa_agent.rules import evaluate_pair

FIXTURE = str(Path(__file__).parent / "fixtures" / "mini_rcsa.csv")


def _pairs(process="Payment Processing"):
    pairs, errors = load_pairs(FIXTURE, process)
    assert not errors
    return {p["pair_id"]: p for p in pairs}


def test_loader_reads_pairs_and_rejects_unknown_process():
    assert len(_pairs()) == 6
    pairs, errors = load_pairs(FIXTURE, "Nope")
    assert pairs == [] and "not found" in errors[0]


def test_loader_reports_missing_file_and_columns(tmp_path):
    assert "not found" in load_pairs(str(tmp_path / "x.csv"), "ALL")[1][0]
    bad = tmp_path / "bad.csv"
    bad.write_text("a,b\n1,2\n")
    assert "Missing required columns" in load_pairs(str(bad), "ALL")[1][0]


def test_rules_gap_case():
    r = evaluate_pair(_pairs()["P08"])
    assert {"LOSS_EVENTS_PRESENT", "RCSA_GAP", "NO_KRI_COVERAGE", "NO_CONTROL", "ACTION_REQUIRED"} <= set(r["flags"])
    assert r["review_priority"] == "medium" and r["scenario_result"] == "High - residual = inherent"


def test_rules_control_conflict_is_flagged_for_review_not_decided():
    r = evaluate_pair(_pairs()["P09"])
    assert "CONTROL_CONFLICT" in r["flags"] and r["review_priority"] == "high"


def test_rules_not_applicable_accepted_and_challenged():
    assert evaluate_pair(_pairs("ALL")["P01"])["flags"] == ["NOT_APPLICABLE_ACCEPTED"]
    r = evaluate_pair(_pairs()["P12"])
    assert r["flags"] == ["APPLICABILITY_CHALLENGE"] and r["review_priority"] == "high"


def test_rules_not_effective_control_needs_action():
    r = evaluate_pair(_pairs()["P13"])
    assert {"CONTROL_NOT_EFFECTIVE", "ACTION_REQUIRED"} <= set(r["flags"])
    assert r["scenario_result"] == "High - action required"


def test_rules_match_all_22_scenarios():
    """Build one pair per scenario and compare with the scenario file's own columns."""
    import csv
    rows = list(csv.DictReader(open(str(Path(__file__).parent / "fixtures" / "scenarios_22.csv"))))
    assert len(rows) == 22
    for s in rows:
        applicable = s["Applicable"] == "Yes"
        pair = {"pair_id": "S" + s["Scenario ID"], "loss_events": 1 if s["Loss event"] == "Y" else 0,
                "kri": "KRI" if s["KRI"] == "Y" else "", "previous_rcsa": s["Previous RCSA"] == "Y",
                "control": s["Control"], "applicable": applicable, "anomaly": "", "expected_result": s["Expected result"]}
        r = evaluate_pair(pair)
        flags = set(r["flags"])
        assert r["scenario_result"] == s["Expected result"], s["Scenario ID"]
        assert r["warnings"] == [], (s["Scenario ID"], r["warnings"])
        if applicable:
            assert ("RCSA_GAP" in flags) == (s["Not in previous RCSA"] == "Yes"), s["Scenario ID"]
            assert ("NO_KRI_COVERAGE" in flags) == (s["No KRI coverage"] == "Yes"), s["Scenario ID"]
            assert ("CONTROL_CONFLICT" in flags) == (s["Control conflict"] == "Yes"), s["Scenario ID"]
            assert ("ACTION_REQUIRED" in flags) == (s["Action required"] == "Yes"), s["Scenario ID"]
        else:
            assert flags == {"NOT_APPLICABLE_ACCEPTED"}


def test_rules_anomaly_and_partial_control():
    r = evaluate_pair(_pairs()["P11"])
    assert {"DATA_ANOMALY", "OUTSIDE_SCENARIOS"} <= set(r["flags"]) and "CONTROL_CONFLICT" not in r["flags"]


def test_retriever_returns_cited_chunks():
    chunks = load_chunks("knowledge")
    assert len(chunks) >= 8
    top = retrieve("loss events although the control is effective", chunks, k=2)
    assert top and top[0]["source_id"].startswith("G-") and "effective" in top[0]["title"].lower()


def test_llm_validation_drops_unknown_sources_and_rejects_bad_json():
    ok = _validate({"challenge": "c", "questions_for_owner": ["q"], "suggested_action": "a",
                    "evidence_used": ["DATA:P08", "FAKE"]}, {"DATA:P08"})
    assert ok["evidence_used"] == ["DATA:P08"] and "FAKE" in ok["note"]
    with pytest.raises(ValueError):
        _validate({"challenge": "c"}, set())


def test_fallback_is_explicit():
    finding = {"pair": _pairs()["P08"], "flags": ["NO_CONTROL"]}
    fb = fallback_challenge(finding, "LLM not used")
    assert fb["source"] == "deterministic_fallback" and fb["note"]


def test_external_failure_is_reported_not_raised(monkeypatch):
    monkeypatch.setattr(external, "RETRY_DELAY", 0)
    monkeypatch.setattr(external, "_http_json", lambda *a, **k: (_ for _ in ()).throw(TimeoutError("boom")))
    res = external.gdelt_search("Payment Processing")
    assert res["status"] == "failed" and res["attempts"] == 3 and "boom" in res["error"]


def test_tavily_skipped_without_key(monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    assert external.tavily_search("x")["status"] == "skipped"


def test_full_graph_offline(tmp_path, monkeypatch):
    pytest.importorskip("langgraph")
    from rcsa_agent.graph import build_graph
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    final = build_graph().invoke({"data_path": FIXTURE, "process": "Payment Processing",
                                  "out_dir": str(tmp_path), "use_llm": False, "use_external": False,
                                  "run_log": []})
    assert final["status"] in {"COMPLETED", "COMPLETED_WITH_WARNINGS"}
    report = Path(final["report_path"]).read_text(encoding="utf-8")
    assert "P09" in report and "CONTROL_CONFLICT" in report and "Pending" in report


def test_full_graph_failure_path_still_writes_report(tmp_path):
    pytest.importorskip("langgraph")
    from rcsa_agent.graph import build_graph
    final = build_graph().invoke({"data_path": str(tmp_path / "missing.csv"), "process": "X",
                                  "out_dir": str(tmp_path), "run_log": []})
    assert final["status"] == "FAILED" and Path(final["report_path"]).exists()
