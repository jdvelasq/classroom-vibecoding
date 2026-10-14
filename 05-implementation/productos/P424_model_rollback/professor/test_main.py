import importlib.util
import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p424_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_rollback_restores_a_registered_version(tmp_path, monkeypatch):
    """El cambio queda verificable sin tocar la evidencia que se distribuye."""

    monkeypatch.setattr(MODULE, "OUTPUT_DIR", tmp_path / "production")

    record = MODULE.rollback("v1")

    assert record["previous_version"] == "v2"
    assert record["production_version"] == "v1"
    assert (tmp_path / "production" / "model.pkl").read_bytes() == (
        ACTIVITY_DIR / "MODEL_V1.pkl"
    ).read_bytes()
    saved_record = json.loads(
        (tmp_path / "production" / "rollback_record.json").read_text(encoding="utf-8")
    )
    assert saved_record["production_version"] == "v1"


def test_rollback_rejects_an_unknown_version(tmp_path, monkeypatch):
    monkeypatch.setattr(MODULE, "OUTPUT_DIR", tmp_path / "production")

    try:
        MODULE.rollback("v3")
    except ValueError as error:
        assert "Versión no registrada" in str(error)
    else:
        raise AssertionError("Una versión ausente no puede quedar en producción.")
