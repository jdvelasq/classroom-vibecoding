"""Valida que la actividad entregue al menos un artefacto final."""

from pathlib import Path
import runpy


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
PROFESSOR_DIR = ACTIVITY_DIR / "professor"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
IS_PROFESSOR = any(
    (path / ".PROFESSOR").exists() for path in ACTIVITY_DIR.parents
) and (PROFESSOR_DIR / "main.py").exists()


def test_submission_contains_an_artifact():
    """La solución debe producir al menos un archivo final en submission/."""
    if IS_PROFESSOR:
        runpy.run_path(PROFESSOR_DIR / "main.py", run_name="__main__")

    artifacts = [
        path
        for path in SUBMISSION_DIR.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    ]

    assert artifacts, (
        "Ejecuta la solución y guarda al menos un artefacto final en submission/."
    )
