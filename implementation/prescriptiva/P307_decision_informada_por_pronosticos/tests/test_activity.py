from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_order_policy():
    policy_path = SUBMISSION_DIR / "order_policy.csv"

    assert policy_path.exists(), (
        "Guarda la política de pedido semanal en submission/order_policy.csv."
    )


def test_02_order_policy_makes_the_decision_auditable():
    policy = pd.read_csv(SUBMISSION_DIR / "order_policy.csv")

    assert len(policy) == 1
    assert {
        "decision_cadence",
        "selected_order_quantity",
        "expected_value",
        "stockout_probability",
        "service_level",
        "approval_required",
        "review_trigger",
    }.issubset(policy.columns)
