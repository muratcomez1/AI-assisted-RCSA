from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]


def retrieve_evidence(state: dict) -> dict:
    """Retrieve historical loss, KRI and control evidence."""

    evidence_results = []

    losses_path = ROOT / "data/raw/loss_events.csv"
    controls_path = ROOT / "data/raw/controls.csv"

    if not losses_path.exists() or not controls_path.exists():
        return {
            "evidence_results": [],
            "errors": state.get("errors", []) + [
                "Evidence retrieval failed: required CSV files not found."
            ]
        }

    losses = pd.read_csv(losses_path).fillna("")
    controls = pd.read_csv(controls_path).fillna("")

    for record in state.get("input_data", []):
        process_id = record.get("Process ID")

        if process_id is None:
            continue

        process_losses = losses[
            losses["process_id"] == process_id
        ]

        process_controls = controls[
            controls["process_id"] == process_id
        ]

        evidence_results.append({
            "pair_id": record.get("Pair ID"),
            "process_id": process_id,
            "historical_losses": process_losses.to_dict("records"),
            "controls": process_controls.to_dict("records"),
            "loss_event_count": len(process_losses),
            "control_count": len(process_controls),
        })

    return {
        "evidence_results": evidence_results
    }
