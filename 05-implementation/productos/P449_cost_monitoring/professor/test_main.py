import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p449_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_monitor_cost_allows_an_exact_budget():
    """Alcanzar el presupuesto no es excederlo."""

    report = MODULE.monitor_cost({"runs": ["1.25", "0.75"], "budget": "2.00"})

    assert report == {"cost": 2.0, "budget": 2.0, "alert": False}


def test_monitor_cost_alerts_when_runs_exceed_the_budget():
    report = MODULE.monitor_cost({"runs": [1.25, 0.76], "budget": 2})

    assert report["cost"] == 2.01
    assert report["alert"] is True
