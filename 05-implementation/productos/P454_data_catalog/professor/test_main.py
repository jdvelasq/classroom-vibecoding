import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p454_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_load_catalog_entry_exposes_operational_responsibility_and_use():
    """Un catálogo permite saber quién responde por el dato y para qué se consume."""

    entry = MODULE.load_catalog_entry()

    assert entry["dataset"] == "factory_risk"
    assert entry["owner"] == "data-operations"
    assert entry["consumer"] == "operations_manager"
    assert entry["frequency"] == "daily"
    assert entry["contract_version"] == "2.0"
