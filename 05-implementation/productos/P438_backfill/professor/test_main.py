import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p438_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_select_backfill_keeps_only_the_declared_inclusive_period():
    """El rango evita que un reproceso correctivo altere fechas vecinas."""

    event_ids = MODULE.select_backfill(
        "2026-09-20",
        "2026-09-21",
        [
            {"id": "before", "date": "2026-09-19"},
            {"id": "start", "date": "2026-09-20"},
            {"id": "end", "date": "2026-09-21"},
            {"id": "after", "date": "2026-09-22"},
        ],
    )

    assert event_ids == ["start", "end"]
