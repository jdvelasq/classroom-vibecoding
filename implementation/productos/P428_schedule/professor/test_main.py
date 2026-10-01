import importlib.util
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p428_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_report_aggregates_each_factory_without_running_the_schedule():
    """La frecuencia no debe ocultar el cálculo que automatiza."""

    data = pd.DataFrame(
        {
            "factory_id": ["A", "A", "B"],
            "daily_units_produced": [100, 150, 300],
        }
    )

    report = MODULE.build_report(data)

    assert report["factory_totals"] == {"A": 250, "B": 300}
    assert report["executed_at"].endswith("+00:00")
