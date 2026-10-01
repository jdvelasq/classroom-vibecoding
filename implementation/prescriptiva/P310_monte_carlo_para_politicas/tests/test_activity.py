from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_risk_evidence():
    assert (SUBMISSION_DIR / "project_risk_summary.csv").is_file(), (
        "Guarda el resumen de riesgo de la simulación en submission/."
    )


def test_submission_contains_a_decision_policy():
    assert (SUBMISSION_DIR / "investment_policy.csv").is_file(), (
        "Guarda la política de inversión en submission/."
    )
