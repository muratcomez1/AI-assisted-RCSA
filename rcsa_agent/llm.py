"""LLM challenge node logic: structured JSON, source-id validation, retries, deterministic fallback."""
import json
import os
import time

from .rules import FLAG_TEXT

SYSTEM_PROMPT = """You support a Second Line Operational Risk reviewer who is challenging a First Line \
Risk and Control Self-Assessment (RCSA).

Rules you must follow:
- Use ONLY the evidence supplied in the user message. Never invent loss events, amounts, KRIs, controls, \
sources or regulations.
- Do NOT assign numeric scores or risk ratings, do NOT approve or reject controls and do NOT state that \
anything is compliant or non-compliant. You draft a challenge for a human reviewer.
- A loss event does not by itself prove that a control failed. Raise it as a question.
- The absence of loss events, KRIs or a previous RCSA entry alone does not prove a risk is not applicable.
- External sources give context only. They are not proof about this institution's controls.
- Cite the evidence ids you used (for example "DATA:P08", "G-rcsa_challenge_guidance#2", "X1").
- Be concise and specific. Write in English.

Return ONLY a JSON object with exactly these keys:
{"challenge": "2-4 sentences", "questions_for_owner": ["..", ".."], "suggested_action": "1-2 sentences", \
"evidence_used": ["id", "id"]}"""

QUESTIONS = {
    "APPLICABILITY_CHALLENGE": "What evidence supports treating this risk as not applicable, given the loss events, KRI, control or previous RCSA entry on record?",
    "LOSS_EVENTS_PRESENT": "What were the root causes of the recorded loss events and have they been addressed?",
    "RCSA_GAP": "Why was this risk not covered in the previous RCSA, and what changed since?",
    "NO_KRI_COVERAGE": "Which KRI could monitor this risk, and who would own it?",
    "NO_CONTROL": "Which control mitigates this risk, and who owns it?",
    "CONTROL_CONFLICT": "Why is the control rated Effective although loss events exist? What testing evidence supports the rating?",
    "DATA_ANOMALY": "Can the owner provide the supporting evidence behind the anomaly flagged in the source data?",
    "CONTROL_NOT_EFFECTIVE": "Why is the control not effective, and what is the plan and timeline to fix it?",
    "ACTION_REQUIRED": "Which action, owner and deadline will close the control gap?",
    "OUTSIDE_SCENARIOS": "How should this control status be classified, and what evidence supports it?",
}
ACTIONS = {
    "APPLICABILITY_CHALLENGE": "Request evidence supporting the not-applicable decision before accepting it.",
    "CONTROL_CONFLICT": "Request control testing evidence and the loss event root-cause analysis; escalate if not provided.",
    "NO_CONTROL": "Ask the owner to define and assign a control.",
    "NO_KRI_COVERAGE": "Agree a suitable KRI with the owner.",
    "RCSA_GAP": "Confirm the risk is added to the current RCSA.",
    "LOSS_EVENTS_PRESENT": "Review the loss events with the owner.",
    "DATA_ANOMALY": "Ask the owner to clarify the data anomaly.",
    "CONTROL_NOT_EFFECTIVE": "Agree a remediation plan with an owner and a deadline.",
    "ACTION_REQUIRED": "Agree an action, owner and deadline.",
    "OUTSIDE_SCENARIOS": "Ask the reviewer to classify the control status.",
}


def make_client():
    from openai import OpenAI
    return OpenAI(timeout=40.0, max_retries=0)


def fallback_challenge(finding: dict, reason: str) -> dict:
    flags = finding["flags"]
    texts = [FLAG_TEXT[f] for f in flags if f in FLAG_TEXT]
    questions = [QUESTIONS[f] for f in flags if f in QUESTIONS]
    actions = [ACTIONS[f] for f in flags if f in ACTIONS]
    return {
        "challenge": " ".join(texts) or "No challenge points were raised by the deterministic rules.",
        "questions_for_owner": questions,
        "suggested_action": " ".join(actions[:2]) or "No follow-up required beyond standard review.",
        "evidence_used": [f"DATA:{finding['pair']['pair_id']}"],
        "source": "deterministic_fallback",
        "note": reason,
    }


def _payload(finding: dict, external_items: list) -> tuple[str, set]:
    pair = finding["pair"]
    allowed = {f"DATA:{pair['pair_id']}"}
    guidance = []
    for g in finding.get("guidance", []):
        allowed.add(g["source_id"])
        guidance.append({"id": g["source_id"], "title": g["title"], "text": g["text"]})
    ext = []
    for i, item in enumerate(external_items, start=1):
        ext.append({"id": f"X{i}", "title": item["title"], "url": item["url"], "snippet": item.get("snippet", "")})
        allowed.add(f"X{i}")
    body = {
        "evidence": {"id": f"DATA:{pair['pair_id']}", "process": pair["process"], "risk_id": pair["risk_id"],
                     "risk": pair["risk"], "first_line_applicable": pair["applicable"],
                     "loss_events": pair["loss_events"], "loss_amount_eur": pair["loss_amount"],
                     "kri": pair["kri"] or None, "in_previous_rcsa": pair["previous_rcsa"],
                     "control": pair["control"], "source_anomaly": pair["anomaly"] or None},
        "scenario_result": finding.get("scenario_result"),
        "rule_flags": [{"flag": f, "meaning": FLAG_TEXT[f]} for f in finding["flags"]],
        "guidance": guidance,
        "external_context": ext,
    }
    return json.dumps(body, ensure_ascii=False, indent=1), allowed


def _validate(obj: dict, allowed: set) -> dict:
    if not isinstance(obj, dict):
        raise ValueError("response is not a JSON object")
    for key in ("challenge", "questions_for_owner", "suggested_action", "evidence_used"):
        if key not in obj:
            raise ValueError(f"missing key '{key}'")
    if not isinstance(obj["questions_for_owner"], list) or not isinstance(obj["evidence_used"], list):
        raise ValueError("questions_for_owner and evidence_used must be lists")
    cited = [str(e) for e in obj["evidence_used"]]
    unknown = [e for e in cited if e not in allowed]
    return {
        "challenge": str(obj["challenge"]).strip(),
        "questions_for_owner": [str(q) for q in obj["questions_for_owner"]],
        "suggested_action": str(obj["suggested_action"]).strip(),
        "evidence_used": [e for e in cited if e in allowed],
        "source": "llm",
        "note": f"Removed unknown source ids: {unknown}" if unknown else "",
    }


def challenge_pair(finding: dict, external_items: list, client, model: str, attempts: int = 2) -> dict:
    """Call the LLM. On repeated failure return the deterministic fallback with the reason (never silent)."""
    user_msg, allowed = _payload(finding, external_items)
    last_error = ""
    for attempt in range(1, attempts + 1):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_msg}],
                response_format={"type": "json_object"},
            )
            return _validate(json.loads(resp.choices[0].message.content), allowed)
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < attempts:
                time.sleep(2.0)
    return fallback_challenge(finding, f"LLM failed after {attempts} attempts ({last_error})")
