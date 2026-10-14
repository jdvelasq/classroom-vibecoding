from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_policy_register():
    policy_register = SUBMISSION_DIR / "policy_register.csv"

    assert policy_register.exists(), (
        "Ejecuta la actividad y guarda el registro operativo en submission/."
    )


def test_02_policy_register_makes_governance_visible():
    policy_register = pd.read_csv(SUBMISSION_DIR / "policy_register.csv")
    required_columns = {
        "recommended_action",
        "assumption",
        "decision_authority",
        "indicator",
        "review_trigger",
        "review_owner",
    }

    assert required_columns.issubset(policy_register.columns)
