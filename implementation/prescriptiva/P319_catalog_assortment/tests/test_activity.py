"""Valida la evidencia final de la política de surtido."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_evidence():
    """La solución debe entregar la política, su contrato y su monitoreo."""
    expected = {
        "assortment_policy.csv",
        "policy_contract.json",
        "policy_monitoring.csv",
    }
    delivered = {path.name for path in SUBMISSION_DIR.iterdir() if path.is_file()}

    assert expected.issubset(delivered), (
        "Ejecuta la solución y guarda la política de surtido, su contrato y monitoreo."
    )
