"""Load and validate the synthetic RCSA process-risk pairs from CSV."""
import csv
from pathlib import Path

REQUIRED_COLUMNS = [
    "Pair ID", "Process", "Risk ID", "Risk", "Loss events (count)",
    "Loss amount (EUR)", "KRI", "Previous RCSA", "Control", "Applicable",
    "Expected result",
]
OPTIONAL_COLUMNS = ["LE flag", "KRI flag", "Scenario ID", "Anomaly"]


def _yes(value) -> bool:
    return str(value).strip().lower() in {"y", "yes", "true", "1"}


def _num(value) -> float:
    text = str(value).strip().replace(",", "").replace("EUR", "").replace("€", "")
    if text in {"", "-", "n/a", "na"}:
        return 0.0
    return float(text)


def find_default_csv() -> str | None:
    for candidate in ["data/raw/rcsa_synthetic_data.csv", "data/rcsa_synthetic_data.csv"]:
        if Path(candidate).exists():
            return candidate
    data_dir = Path("data")
    if data_dir.exists():
        for p in data_dir.rglob("rcsa_synthetic_data.csv"):
            return str(p)
    return None


def load_pairs(path: str, process: str) -> tuple[list, list]:
    """Return (pairs, errors). Errors are human-readable strings."""
    errors: list = []
    p = Path(path)
    if not p.exists():
        return [], [f"Input file not found: {path}"]

    with p.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        reader.fieldnames = [(h or "").strip() for h in (reader.fieldnames or [])]
        missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing:
            return [], [f"Missing required columns: {missing}. Found: {reader.fieldnames}"]
        rows = [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in reader]

    processes = sorted({r["Process"] for r in rows if r["Process"]})
    if process.upper() == "ALL":
        selected = rows
    else:
        selected = [r for r in rows if r["Process"].lower() == process.lower()]
        if not selected:
            return [], [f"Process '{process}' not found. Available processes: {processes}"]

    pairs = []
    for r in selected:
        try:
            pairs.append({
                "pair_id": r["Pair ID"],
                "process": r["Process"],
                "risk_id": r["Risk ID"],
                "risk": r["Risk"],
                "loss_events": int(_num(r["Loss events (count)"])),
                "loss_amount": _num(r["Loss amount (EUR)"]),
                "kri": r["KRI"],
                "previous_rcsa": _yes(r["Previous RCSA"]),
                "control": r["Control"],
                "applicable": _yes(r["Applicable"]),
                "expected_result": r["Expected result"],
                "le_flag": r.get("LE flag", ""),
                "kri_flag": r.get("KRI flag", ""),
                "scenario_id": r.get("Scenario ID", ""),
                "anomaly": r.get("Anomaly", ""),
            })
        except ValueError as exc:
            errors.append(f"Row {r.get('Pair ID', '?')}: invalid number ({exc})")
    return pairs, errors
