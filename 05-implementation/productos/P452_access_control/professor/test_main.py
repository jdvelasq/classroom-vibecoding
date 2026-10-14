import importlib.util
from pathlib import Path

import pytest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p452_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_get_factory_risk_report_allows_a_role_declared_in_policy():
    """La autorización se decide desde la política, no desde el cálculo del riesgo."""

    report = MODULE.get_factory_risk_report(
        "operations_manager",
        {"factory_risk_report": ["operations_manager"]},
    )

    assert report == {"factory_id": 2, "risk": "high"}


def test_get_factory_risk_report_rejects_an_undeclared_role():
    with pytest.raises(PermissionError, match="Rol no autorizado"):
        MODULE.get_factory_risk_report(
            "visitor", {"factory_risk_report": ["operations_manager"]}
        )
