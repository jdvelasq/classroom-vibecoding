import importlib.util
from pathlib import Path

import pytest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p427_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_get_api_key_reads_the_configured_secret(monkeypatch):
    monkeypatch.setenv(MODULE.SECRET_NAME, "clave-de-practica")

    assert MODULE.get_api_key() == "clave-de-practica"


def test_get_api_key_explains_the_missing_configuration(monkeypatch):
    monkeypatch.delenv(MODULE.SECRET_NAME, raising=False)

    with pytest.raises(RuntimeError, match=MODULE.SECRET_NAME):
        MODULE.get_api_key()
