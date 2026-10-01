"""Valida los artefactos de participación de la política de reasentamiento."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_artifacts():
    """La solución deja una recomendación, su contrato y su seguimiento."""
    expected = {
        "policy_contract.json",
        "decision_queue.csv",
        "monitoring_plan.csv",
    }
    artifacts = {path.name for path in SUBMISSION_DIR.iterdir() if path.is_file()}

    assert expected <= artifacts, (
        "Ejecuta la solución y guarda el contrato, la cola de decisiones y el plan "
        "de monitoreo en submission/."
    )
