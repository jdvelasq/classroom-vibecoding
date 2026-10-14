"""Valida los artefactos de una política de posicionamiento preventivo."""

import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_policy_artifacts():
    expected_names = {
        "deployment_decisions.csv",
        "zone_assignments.csv",
        "resource_sensitivity.csv",
        "reassignment_rules.csv",
        "policy_monitoring.csv",
        "deployment_policy.json",
        "wildfire_resource_deployment_map.png",
    }
    actual_names = {
        path.name
        for path in SUBMISSION_DIR.iterdir()
        if path.is_file() and path.name != ".gitkeep"
    }

    assert expected_names <= actual_names, (
        "Ejecuta la solución y conserva la política, sus reglas de reasignación, "
        "monitoreo y mapa en submission/."
    )


def test_02_policy_contract_defines_a_governed_recurrent_decision():
    policy = json.loads((SUBMISSION_DIR / "deployment_policy.json").read_text(encoding="utf-8"))

    assert policy["authorized_base_count"] > 0
    assert len(policy["baseline_active_bases"]) == policy["authorized_base_count"]
    assert policy["cadence"]
    assert policy["objective"]
    assert policy["safeguard"]
    assert policy["human_authority"]


def test_03_reassignment_and_monitoring_make_review_observable():
    rules = pd.read_csv(SUBMISSION_DIR / "reassignment_rules.csv")
    monitoring = pd.read_csv(SUBMISSION_DIR / "policy_monitoring.csv")

    assert {"observable_trigger", "action", "authority", "response_need"} <= set(rules.columns)
    assert len(rules) >= 3
    assert rules.observable_trigger.notna().all()
    assert rules.action.notna().all()
    assert rules.authority.notna().all()
    assert {"metric", "baseline_value", "review_threshold", "cadence", "review_action"} <= set(monitoring.columns)
    assert (monitoring.baseline_value <= monitoring.review_threshold).all()
