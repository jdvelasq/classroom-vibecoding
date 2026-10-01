import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p432_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_factory_totals_applies_the_declared_sql_transformation(tmp_path):
    """La tabla destino debe agregar todas las observaciones de cada fábrica."""

    data_path = tmp_path / "daily_operations.csv"
    data_path.write_text(
        "factory_id,daily_units_produced\nB,5\nA,8\nB,7\n", encoding="utf-8"
    )

    totals = MODULE.build_factory_totals(data_path)

    assert totals == [("A", 8), ("B", 12)]
