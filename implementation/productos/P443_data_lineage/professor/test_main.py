import importlib.util
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p443_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_factory_totals_preserves_the_grain_declared_by_lineage():
    """Cada fila curada representa una fábrica y puede rastrearse hasta el insumo."""

    raw_data = pd.DataFrame(
        {
            "factory_id": ["A", "A", "B"],
            "daily_units_produced": [10, 5, 7],
        }
    )

    curated_data = MODULE.build_factory_totals(raw_data)

    assert curated_data.to_dict(orient="records") == [
        {"factory_id": "A", "daily_units_produced": 15},
        {"factory_id": "B", "daily_units_produced": 7},
    ]
