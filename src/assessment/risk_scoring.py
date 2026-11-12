
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Prototype exposure thresholds based on the RCSA
# methodology reference supplied for this project.
def classify_exposure(amount):
    if amount <= 6250:
        return "Low"
    elif amount <= 25000:
        return "Medium"
    elif amount <= 100000:
        return "High"
    return "Significant"


def analyze_historical_losses(losses):
    """Summarise historical loss events for each process."""

    results = []

    for process_id, group in losses.groupby("process_id"):
        root_causes = group["root_cause"].value_counts()

        results.append({
            "process_id": process_id,
            "historical_loss_eur": group["financial_impact_eur"].sum(),
            "loss_event_count": len(group),
            "average_loss_eur": round(
                group["financial_impact_eur"].mean(), 2
            ),
            "largest_loss_eur": group["financial_impact_eur"].max(),
            "latest_event_date": group["event_date"].max(),
            "most_common_root_cause": root_causes.index[0],
            "repeated_root_cause": root_causes.max() > 1,
        })

    return pd.DataFrame(results)


def analyze_controls(controls):
    """Evaluate control effectiveness at process level."""

    results = []

    for process_id, group in controls.groupby("process_id"):
        effective = (group["effectiveness"] == "Effective").sum()
        partial = (
            group["effectiveness"] == "Partially Effective"
        ).sum()
        ineffective = (
            group["effectiveness"] == "Ineffective"
        ).sum()

        total = len(group)

        if ineffective > 0:
            rating = "Weak"
        elif partial > 0:
            rating = "Partially Effective"
        else:
            rating = "Effective"

        results.append({
            "process_id": process_id,
            "control_count": total,
            "effective_controls": int(effective),
            "partially_effective_controls": int(partial),
            "ineffective_controls": int(ineffective),
            "control_effectiveness_rate": round(
                effective / total * 100, 1
            ) if total else 0,
            "overall_control_rating": rating,
        })

    return pd.DataFrame(results)


def run_assessment():
    processes = pd.read_csv(ROOT / "data/raw/processes.csv")
    losses = pd.read_csv(ROOT / "data/raw/loss_events.csv")
    controls = pd.read_csv(ROOT / "data/raw/controls.csv")

    # Analyse historical loss evidence.
    loss_analysis = analyze_historical_losses(losses)

    # Analyse control effectiveness.
    control_analysis = analyze_controls(controls)

    # Combine both evidence sources with process information.
    results = processes.merge(
        loss_analysis, on="process_id", how="left"
    )

    results = results.merge(
        control_analysis, on="process_id", how="left"
    )

    results["historical_exposure_band"] = (
        results["historical_loss_eur"].apply(classify_exposure)
    )

    results["assessment_status"] = "Requires Human Review"

    results["assessment_basis"] = (
        "Historical loss evidence and control effectiveness"
    )

    output_dir = ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "rcsa_analysis.csv"
    results.to_csv(output_path, index=False)

    print("\nRCSA INTELLIGENCE ANALYSIS")
    print(results.to_string(index=False))
    print(f"\nReport saved to: {output_path}")

    return results


if __name__ == "__main__":
    run_assessment()
