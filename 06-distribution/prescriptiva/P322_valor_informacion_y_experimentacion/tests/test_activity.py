"""Valida que la actividad entregue al menos un artefacto final."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_policy_evidence():
    expected_artifacts = {
        "information_value.csv",
        "policy_contract.json",
        "policy_monitoring.csv",
    }

    generated_artifacts = {
        path.name
        for path in SUBMISSION_DIR.iterdir()
        if path.is_file() and path.name != ".gitkeep"
    }

    assert expected_artifacts <= generated_artifacts, (
        "Guarda la comparación, el contrato de política y su plan de monitoreo en submission/."
    )
