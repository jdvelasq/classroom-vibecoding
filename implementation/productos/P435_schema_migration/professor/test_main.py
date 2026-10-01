import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p435_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_migrate_v1_to_v2_preserves_the_analytics_value():
    """Una migración cambia el esquema sin perder la decisión que consume el producto."""

    migrated_record = MODULE.migrate_v1_to_v2({"factory": "north", "risk": "high"})

    assert migrated_record == {
        "schema_version": "2.0",
        "factory_id": "north",
        "risk": "high",
    }
