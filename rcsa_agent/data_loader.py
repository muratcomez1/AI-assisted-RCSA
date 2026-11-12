"""Load and validate the synthetic RCSA process-risk pairs from CSV."""
import csv
import io
import ssl
import urllib.request
from pathlib import Path

try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:  # pragma: no cover
    _CTX = ssl.create_default_context()


def _read_text(path: str) -> str:
    """Local CSV path or an https link (for example a Google Sheet published as CSV)."""
    if str(path).lower().startswith("http"):
        req = urllib.request.Request(path, headers={"User-Agent": "rcsa-agent/1.0"})
        with urllib.request.urlopen(req, timeout=20, context=_CTX) as resp:
            return resp.read().decode("utf-8-sig", errors="replace")
    return Path(path).read_text(encoding="utf-8-sig")

REQUIRED_COLUMNS = [
    "Pair ID", "Process", "Risk ID", "Risk", "Loss events (count)",
    "Loss amount (EUR)", "KRI", "Previous RCSA", "Control", "Applicable",
]
OPTIONAL_COLUMNS = ["Expected result", "LE flag", "KRI flag", "Scenario ID", "Anomaly"]


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
    is_url = str(path).lower().startswith("http")
    if not is_url and not Path(path).exists():
        return [], [f"Input file not found: {path}"]
    try:
        text = _read_text(path)
    except Exception as exc:
        return [], [f"Could not read input ({type(exc).__name__}: {exc}). "
                    "For a Google Sheet use File > Share > Publish to web > CSV."]
    if text.lstrip().lower().startswith("<!doctype html") or "<html" in text[:200].lower():
        return [], ["The link returned a web page, not CSV. Publish the sheet to the web as CSV."]

    reader = csv.DictReader(io.StringIO(text))
    reader.fieldnames = [(h or "").strip() for h in (reader.fieldnames or [])]
    missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
    if missing:
        return [], [f"Missing required columns: {missing}. Found: {reader.fieldnames}"]
    rows = [{(k or "").strip(): (v or "").strip() for k, v in r.items() if k} for r in reader]
    rows = [r for r in rows if r.get("Pair ID")]  # ignore empty sheet rows

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
                "expected_result": r.get("Expected result", ""),
                "le_flag": r.get("LE flag", ""),
                "kri_flag": r.get("KRI flag", ""),
                "scenario_id": r.get("Scenario ID", ""),
                "anomaly": r.get("Anomaly", ""),
            })
        except ValueError as exc:
            errors.append(f"Row {r.get('Pair ID', '?')}: invalid number ({exc})")
    return pairs, errors
