"""Verifica que la actividad deje evidencia de la política diseñada."""

import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_policy_contract_is_submitted():
    """La política operable debe quedar disponible para su revisión."""
    policy_path = SUBMISSION_DIR / "hydrothermal_policy.json"

    assert policy_path.exists(), "Ejecuta la solución y guarda hydrothermal_policy.json en submission/."

    policy = json.loads(policy_path.read_text(encoding="utf-8"))

    for field in [
        "action",
        "constraints",
        "guardrails",
        "authority",
        "monitoring",
        "review_triggers",
    ]:
        assert policy.get(field), f"El contrato de política debe declarar {field}."
