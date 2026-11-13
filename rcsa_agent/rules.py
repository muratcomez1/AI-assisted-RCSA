"""Deterministic challenge rules that follow the 22-scenario matrix.

Derived from rcsa_scenarios.csv:
  * Not in previous RCSA flag  = risk was not in the previous RCSA
  * No KRI coverage flag       = loss events exist AND no KRI is assigned (information only: a missing KRI says
                                 nothing about control effectiveness, so it does not raise review priority)
  * Control conflict flag      = loss events exist AND control is Effective
  * Action required            = control is None or Not effective
  * Result                     = None -> High - residual = inherent
                                 Not effective -> High - action required
                                 Effective, no loss events -> Residual reduced, accepted
                                 Effective, loss events -> Conflict - effectiveness downgraded, residual floor applied

The rules only RAISE FLAGS for a human reviewer. They do not rate risk, approve controls
or decide that a control has failed. No numeric scores are produced.
"""

NO_CONTROL_VALUES = {"", "n/a", "na", "none", "no control", "-"}

FLAG_TEXT = {
    "APPLICABILITY_CHALLENGE": "Marked not applicable, but evidence exists (loss events, KRI, previous RCSA or a control). Applicability needs to be challenged.",
    "NOT_APPLICABLE_ACCEPTED": "Marked not applicable and no contradicting evidence was found.",
    "LOSS_EVENTS_PRESENT": "Historical loss events exist for this process-risk pair.",
    "RCSA_GAP": "Risk is applicable but was not included in the previous RCSA.",
    "NO_KRI_COVERAGE": "Information only: loss events exist but no KRI is assigned. A missing KRI says nothing about control effectiveness; the owner may not have needed one.",
    "NO_CONTROL": "Risk is applicable but no control is described.",
    "CONTROL_NOT_EFFECTIVE": "The control is described as Not effective.",
    "ACTION_REQUIRED": "Action required: there is no control or the control is not effective.",
    "CONTROL_CONFLICT": "Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.",
    "OUTSIDE_SCENARIOS": "The control status is outside the 22-scenario matrix and needs human review.",
    "DATA_ANOMALY": "The source data marks an anomaly for this pair.",
}
INFO_ONLY = {"NOT_APPLICABLE_ACCEPTED", "NO_KRI_COVERAGE"}  # do not raise review priority
HIGH_ATTENTION = {"APPLICABILITY_CHALLENGE", "CONTROL_CONFLICT", "DATA_ANOMALY"}


def _norm(control) -> str:
    return str(control).strip().lower()


def has_control(control) -> bool:
    return _norm(control) not in NO_CONTROL_VALUES


def control_effective(control) -> bool:
    return _norm(control) in {"effective", "yes"}


def control_not_effective(control) -> bool:
    return _norm(control) in {"not effective", "ineffective"}


def _has_evidence(pair: dict) -> bool:
    return (pair["loss_events"] > 0 or bool(str(pair["kri"]).strip())
            or pair["previous_rcsa"] or has_control(pair["control"]))


def scenario_result(pair: dict) -> str:
    """Result text from the 22-scenario matrix for this pair."""
    if not pair["applicable"]:
        return "Not applicable - challenge needed" if _has_evidence(pair) else "Not applicable - accepted"
    ctrl = pair["control"]
    if not has_control(ctrl):
        return "High - residual = inherent"
    if control_not_effective(ctrl):
        return "High - action required"
    if control_effective(ctrl):
        if pair["loss_events"] > 0:
            return "Conflict - effectiveness downgraded, residual floor applied"
        return "Residual reduced, accepted"
    return "Outside the 22 scenarios - human review"


def evaluate_pair(pair: dict) -> dict:
    """Return flags, scenario result, review priority and consistency warnings."""
    flags, warnings = [], []
    loss = pair["loss_events"] > 0
    kri = bool(str(pair["kri"]).strip())
    ctrl = pair["control"]

    if not pair["applicable"]:
        flags.append("APPLICABILITY_CHALLENGE" if _has_evidence(pair) else "NOT_APPLICABLE_ACCEPTED")
    else:
        if loss:
            flags.append("LOSS_EVENTS_PRESENT")
        if not pair["previous_rcsa"]:
            flags.append("RCSA_GAP")
        if loss and not kri:
            flags.append("NO_KRI_COVERAGE")
        if not has_control(ctrl):
            flags += ["NO_CONTROL", "ACTION_REQUIRED"]
        elif control_not_effective(ctrl):
            flags += ["CONTROL_NOT_EFFECTIVE", "ACTION_REQUIRED"]
        elif control_effective(ctrl):
            if loss:
                flags.append("CONTROL_CONFLICT")
        else:
            flags.append("OUTSIDE_SCENARIOS")

    if str(pair.get("anomaly", "")).strip():
        flags.append("DATA_ANOMALY")

    result = scenario_result(pair)

    # Consistency checks against the source file's own columns (warnings only).
    pid = pair["pair_id"]
    le_src = str(pair.get("le_flag", "")).strip()
    if le_src and (le_src.lower() in {"y", "yes"}) != loss:
        warnings.append(f"{pid}: source 'LE flag'={le_src} differs from loss_events={pair['loss_events']}")
    kri_src = str(pair.get("kri_flag", "")).strip()
    if kri_src and (kri_src.lower() in {"y", "yes"}) != kri:
        warnings.append(f"{pid}: source 'KRI flag'={kri_src} differs from KRI present={kri}")
    expected = str(pair.get("expected_result", "")).strip()
    if expected and expected.lower() != result.lower():
        warnings.append(f"{pid}: source expected result '{expected}' differs from rule result '{result}'")

    if any(f in HIGH_ATTENTION for f in flags):
        priority = "high"
    elif any(f not in INFO_ONLY for f in flags):
        priority = "medium"
    else:
        priority = "low"
    return {"flags": flags, "scenario_result": result, "review_priority": priority, "warnings": warnings}
