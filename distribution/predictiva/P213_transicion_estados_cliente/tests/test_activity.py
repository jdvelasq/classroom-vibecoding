from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_transition_evidence():
    expected_files = {
        "transition_matrix.csv",
        "state_forecasts.csv",
        "model_metrics.csv",
        "transition_matrix.png",
        "model_assumptions.json",
    }

    produced_files = {path.name for path in SUBMISSION_DIR.iterdir()}

    assert expected_files <= produced_files
