"""Verifica la evidencia persistente de la política de aceptación."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_evidence():
    """La actividad debe dejar decisiones y un contrato de política visibles."""
    expected_artifacts = ["booking_decisions.csv", "policy_contract.json"]
    missing_artifacts = [
        artifact
        for artifact in expected_artifacts
        if not (SUBMISSION_DIR / artifact).is_file()
    ]

    assert not missing_artifacts, (
        "Ejecuta la solución y guarda en submission/: "
        + ", ".join(missing_artifacts)
    )
