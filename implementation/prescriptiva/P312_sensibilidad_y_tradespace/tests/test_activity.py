from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_evidence():
    expected_artifacts = [
        SUBMISSION_DIR / "tradespace.csv",
        SUBMISSION_DIR / "sensitivity_review.csv",
        SUBMISSION_DIR / "delivery_promise_policy.json",
    ]

    assert all(path.exists() for path in expected_artifacts), (
        "Ejecuta la solución y conserva el análisis de sensibilidad y la política en submission/."
    )
