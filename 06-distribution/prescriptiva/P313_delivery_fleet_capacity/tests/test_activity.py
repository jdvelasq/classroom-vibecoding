"""Verifica la evidencia persistente de la política de flota."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_and_validation():
    expected_artifacts = {
        "fleet_policy.csv",
        "fleet_policy_validation.csv",
        "delivery_fleet_capacity_planner.png",
    }
    produced_artifacts = {
        path.name
        for path in SUBMISSION_DIR.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    }

    assert expected_artifacts <= produced_artifacts, (
        "Ejecuta la actividad y conserva en submission/ la política, su validación "
        "por simulación y el planeador de capacidad."
    )
