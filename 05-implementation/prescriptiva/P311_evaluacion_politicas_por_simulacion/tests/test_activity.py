from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_evidence():
    expected_artifacts = [
        SUBMISSION_DIR / "capacity_policy_comparison.csv",
        SUBMISSION_DIR / "capacity_policy_decision.json",
    ]

    assert all(path.exists() for path in expected_artifacts), (
        "Ejecuta la solución y conserva la comparación y el registro de política en submission/."
    )
