from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_survival_evidence():
    expected_files = {
        "survival_curves.csv",
        "retention_by_contract.csv",
        "survival_curves.png",
        "model_assumptions.json",
    }

    produced_files = {path.name for path in SUBMISSION_DIR.iterdir()}

    assert expected_files <= produced_files
