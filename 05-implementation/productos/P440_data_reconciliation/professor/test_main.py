import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p440_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_reconcile_approves_equal_control_metrics():
    """Una salida solo queda lista cuando los controles coinciden con el origen."""

    result = MODULE.reconcile(
        {"rows": 10, "total_amount": 500}, {"rows": 10, "total_amount": 500}
    )

    assert result == {
        "checks": {"rows": True, "total_amount": True},
        "reconciled": True,
    }


def test_reconcile_rejects_a_changed_control_total():
    result = MODULE.reconcile(
        {"rows": 10, "total_amount": 500}, {"rows": 10, "total_amount": 499}
    )

    assert result["checks"] == {"rows": True, "total_amount": False}
    assert not result["reconciled"]
