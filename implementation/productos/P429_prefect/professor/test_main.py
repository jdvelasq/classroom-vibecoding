import importlib.util
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p429_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_summarize_operations_exposes_the_metric_of_the_flow():
    """Cada tarea conserva una responsabilidad verificable fuera del orquestador."""

    operations = pd.DataFrame(
        {
            "factory_id": ["north", "north", "south"],
            "daily_units_produced": [5, 7, 11],
        }
    )

    totals = MODULE.summarize_operations.fn(operations)

    assert totals == {"north": 12, "south": 11}
