import hashlib
import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p431_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_describe_data_records_schema_and_content_identity(tmp_path):
    """El manifiesto permite detectar cambios aunque el nombre no cambie."""

    data_path = tmp_path / "daily_operations.csv"
    data_path.write_text("factory_id,daily_units_produced\nA,12\n", encoding="utf-8")

    manifest = MODULE.describe_data(data_path)

    assert manifest["version"] == "daily-operations-v1"
    assert manifest["path"] == "data/raw/daily_operations.csv"
    assert manifest["columns"] == ["factory_id", "daily_units_produced"]
    assert manifest["bytes"] == data_path.stat().st_size
    assert manifest["sha256"] == hashlib.sha256(data_path.read_bytes()).hexdigest()
