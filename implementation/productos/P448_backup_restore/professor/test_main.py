import importlib.util
import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p448_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_backup_and_restore_recovers_the_original_operational_artifact(tmp_path):
    """Una restauración válida debe reconstruir exactamente el contenido respaldado."""

    source = tmp_path / "registry.json"
    source.write_text(json.dumps({"production_version": "v2"}), encoding="utf-8")
    backup = tmp_path / "registry.backup.json"
    restored = tmp_path / "registry.restored.json"

    recovered = MODULE.backup_and_restore(source, backup, restored)

    assert recovered == {"production_version": "v2"}
    assert backup.read_bytes() == source.read_bytes()
    assert restored.read_bytes() == source.read_bytes()
