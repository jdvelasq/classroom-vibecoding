"""Comprueba que el estudiante participó en la demostración guiada."""

import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
NOTEBOOK = ACTIVITY_DIR / "notebooks/notebook.ipynb"


def test_01():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert len(notebook["cells"]) > 0, "Agrega al menos una celda al notebook."
