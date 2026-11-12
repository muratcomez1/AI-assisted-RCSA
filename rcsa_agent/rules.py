"""Deterministic challenge rules. No LLM, no invented scores.

These rules only RAISE FLAGS for a human reviewer. They do not rate risk,
approve controls or decide that a control has failed.
"""

NO_CONTROL_VALUES = {"", "n/a", "na", "none", "no control", "-"}

FLAG_TEXT = {
    "APPLICABILITY_CHALLENGE": "Marked not applicable, but evidence exists (loss events, KRI, previous RCSA or a control). Applicability needs to be challenged.",
    "NOT_APPLICABLE_ACCEPTED": "Marked not applicable and no contradicting evidence was found.",
    "LOSS_EVENTS_PRESENT": "Historical loss events exist for this process-risk pair.",
    "RCSA_GAP": "Risk is applicable but was not included in the previous RCSA.",
    "NO_KRI_COVERAGE": "Risk is applicable but no KRI is assigned.",
    "NO_CONTROL": "Risk is applicable but no control is described.",
    "CONTROL_CONFLICT": "Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.",
    "DATA_ANOMALY": "The source data marks an anomaly for this pair.",
}
HIGH_ATTENTION = {"APPLICABILITY_CHALLENGE", "CONTROL_CONFLICT", "DATA_ANOMALY"}


def has_control(control: str) -> bool:
    return str(control).strip().lower() not in NO_CONTROL_VALUES


def control_effective(control: str) -> bool:
    s = str(control).strip().lower()
    return s == "effective" or s == "yes"


def evaluate_pair(pair: dict) -> dict:
    """Return {'flags': [...], 'review_priority': 'high|medium|low', 'warnings': [...]}."""
    flags = []
    warnings = []
    loss = pair["loss_events"] > 0
    kri = bool(str(pair["kri"]).strip())
    ctrl = has_control(pair["control"])

    if not pair["applicable"]:
        if loss or kri or pair["previous_rcsa"] or ctrl:
            flags.append("APPLICABILITY_CHALLENGE")
        else:
            flags.append("NOT_APPLICABLE_ACCEPTED")
    else:
        if loss:
            flags.append("LOSS_EVENTS_PRESENT")
        if not pair["previous_rcsa"]:
            flags.append("RCSA_GAP")
        if not kri:
            flags.append("NO_KRI_COVERAGE")
        if not ctrl:
            flags.append("NO_CONTROL")
        if ctrl and control_effective(pair["control"]) and loss:
            flags.append("CONTROL_CONFLICT")

    if str(pair.get("anomaly", "")).strip():
        flags.append("DATA_ANOMALY")

    # Consistency check against the source file's own flag columns (warnings only).
    le_src = str(pair.get("le_flag", "")).strip()
    if le_src and (le_src.lower() in {"y", "yes"}) != loss:
        warnings.append(f"{pair['pair_id']}: source 'LE flag'={le_src} differs from loss_events={pair['loss_events']}")
    kri_src = str(pair.get("kri_flag", "")).strip()
    if kri_src and pair["applicable"] and (kri_src.lower() in {"y", "yes"}) != (not kri):
        warnings.append(f"{pair['pair_id']}: source 'KRI flag'={kri_src} differs from the computed KRI coverage gap ({not kri})")

    if any(f in HIGH_ATTENTION for f in flags):
        priority = "high"
    elif any(f not in {"NOT_APPLICABLE_ACCEPTED"} for f in flags):
        priority = "medium"
    else:
        priority = "low"
    return {"flags": flags, "review_priority": priority, "warnings": warnings}
