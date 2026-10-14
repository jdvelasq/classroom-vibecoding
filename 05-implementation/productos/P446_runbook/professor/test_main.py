import importlib.util
from pathlib import Path

import pytest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p446_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_get_runbook_returns_the_procedure_for_a_freshness_alert():
    """El operador debe recibir una guía que evita publicar datos vencidos."""

    runbook = MODULE.get_runbook("freshness_alert")

    assert "No publique un reporte nuevo" in runbook
    assert "Solicite la actualización de la fuente" in runbook


def test_get_runbook_rejects_an_unknown_symptom():
    with pytest.raises(ValueError, match="No hay runbook"):
        MODULE.get_runbook("unknown_alert")
