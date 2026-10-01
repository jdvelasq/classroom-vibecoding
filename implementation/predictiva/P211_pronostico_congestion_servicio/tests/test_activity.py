from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_forecast_evidence():
    expected_files = {
        "congestion_forecast.csv",
        "model_metrics.csv",
        "congestion_forecast.png",
        "model_assumptions.json",
    }

    produced_files = {path.name for path in SUBMISSION_DIR.iterdir()}

    assert expected_files <= produced_files
