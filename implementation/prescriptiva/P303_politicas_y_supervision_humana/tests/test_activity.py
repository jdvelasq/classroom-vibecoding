"""Valida la evidencia persistente de la actividad guiada."""

import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_artifacts():
    """La solución debe dejar una política y sus decisiones trazables."""
    policy_path = SUBMISSION_DIR / "review_policy.csv"
    contract_path = SUBMISSION_DIR / "policy_contract.json"

    assert policy_path.is_file(), "Falta submission/review_policy.csv."
    assert contract_path.is_file(), "Falta submission/policy_contract.json."

    policy = pd.read_csv(policy_path)
    required_columns = {
        "application_id",
        "action",
        "reason",
        "human_authority",
        "decision_cadence",
        "review_trigger",
    }
    assert required_columns.issubset(policy.columns), (
        "La política debe hacer visible la acción, razón, autoridad, cadencia "
        "y gatillo de revisión."
    )

    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    assert contract["safeguards"], "El contrato debe declarar sus salvaguardas."
    assert contract["review_trigger"], "El contrato debe declarar cuándo se revisa."
