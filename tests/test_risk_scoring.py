import pandas as pd

from src.assessment.risk_scoring import classify_exposure, run_assessment


def test_exposure_boundaries():
    assert classify_exposure(0) == "Low"
    assert classify_exposure(6250) == "Low"
    assert classify_exposure(6251) == "Medium"
    assert classify_exposure(25000) == "Medium"
    assert classify_exposure(25001) == "High"
    assert classify_exposure(100000) == "High"
    assert classify_exposure(100001) == "Significant"


def test_assessment_creates_five_process_results():
    run_assessment()
    results = pd.read_csv("outputs/initial_risk_assessment.csv")

    assert len(results) == 5
    assert results["process_id"].nunique() == 5


def test_historical_loss_totals():
    results = pd.read_csv("outputs/initial_risk_assessment.csv")

    expected = {
        "P001": 20700,
        "P002": 42000,
        "P003": 77000,
        "P004": 24500,
        "P005": 18000,
    }

    actual = dict(zip(results["process_id"], results["historical_loss_eur"]))
    assert actual == expected


def test_all_assessments_require_human_review():
    results = pd.read_csv("outputs/initial_risk_assessment.csv")

    assert (results["assessment_status"] == "Requires Human Review").all()


def test_control_counts():
    results = pd.read_csv("outputs/initial_risk_assessment.csv")

    assert (results["control_count"] == 2).all()
    assert results["ineffective_or_partial_controls"].tolist() == [1, 1, 2, 1, 1]
