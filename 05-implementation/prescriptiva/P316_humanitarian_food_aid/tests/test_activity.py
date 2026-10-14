"""Verifica la evidencia persistente de la política de abastecimiento."""

import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_policy_and_plan():
    """La participación deja una política y el plan concreto que esa política libera."""
    assert (SUBMISSION_DIR / "shipment_plan.csv").is_file()
    assert (SUBMISSION_DIR / "policy_contract.json").is_file()


def test_policy_contract_makes_governance_visible():
    """La política no puede reducirse al resultado de un optimizador."""
    policy = json.loads((SUBMISSION_DIR / "policy_contract.json").read_text())

    assert policy["action"]
    assert policy["decision_cadence"]
    assert policy["constraints"]
    assert policy["guardrails"]
    assert policy["authority"]["approver"]
    assert policy["monitoring"]
    assert policy["review_triggers"]
