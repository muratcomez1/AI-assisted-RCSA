from typing import Any


REQUIRED_FIELDS = {
    "Pair ID",
    "Process",
    "Risk ID",
    "Risk",
    "Applicable",
    "Expected result",
}


def validate_input(state: dict[str, Any]) -> dict[str, Any]:
    """Validate incoming RCSA process-risk assessment records."""

    records = state.get("input_data", [])
    errors = []

    if not isinstance(records, list) or not records:
        return {
            "errors": ["Input must contain a non-empty list of assessment records."]
        }

    seen_pair_ids = set()

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"Record {index + 1} is not a valid dictionary.")
            continue

        missing = REQUIRED_FIELDS - record.keys()

        if missing:
            errors.append(
                f"Record {index + 1}: missing fields {sorted(missing)}"
            )
            continue

        pair_id = record["Pair ID"]

        if not pair_id:
            errors.append(f"Record {index + 1}: Pair ID is empty.")
        elif pair_id in seen_pair_ids:
            errors.append(f"Duplicate Pair ID: {pair_id}")
        else:
            seen_pair_ids.add(pair_id)

        if record["Applicable"] not in ("Yes", "No", "Not Applicable"):
            errors.append(
                f"Record {index + 1}: invalid applicability value."
            )

    return {
        "errors": errors,
        "input_valid": len(errors) == 0,
    }
