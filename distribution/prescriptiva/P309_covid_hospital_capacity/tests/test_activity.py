"""Valida la evidencia persistente de la política de capacidad."""

import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_artifacts():
    """La actividad debe conservar una acción gobernada y su contrato."""
    policy_path = SUBMISSION_DIR / "capacity_policy.csv"
    contract_path = SUBMISSION_DIR / "policy_contract.json"

    assert policy_path.is_file(), "Falta submission/capacity_policy.csv."
    assert contract_path.is_file(), "Falta submission/policy_contract.json."

    policy = pd.read_csv(policy_path)
    required_columns = {
        "policy_step",
        "observable_context",
        "action",
        "decision_cadence",
        "response_need",
        "human_authority",
        "safeguard",
        "review_trigger",
    }
    assert required_columns.issubset(policy.columns), (
        "La política debe hacer visibles contexto, acción, autoridad, "
        "salvaguardas y revisión."
    )
    assert {"activar_un_bloque", "escalar_un_segundo_bloque"}.issubset(
        set(policy.action)
    )

    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    assert contract["safeguards"], "El contrato debe declarar salvaguardas."
    assert contract["monitoring"], "El contrato debe declarar monitoreo."
    assert contract["review_trigger"], "El contrato debe declarar un gatillo de revisión."
