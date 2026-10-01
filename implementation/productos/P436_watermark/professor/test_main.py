import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p436_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_process_new_events_advances_the_watermark_only_for_new_events():
    """Reanudar un flujo requiere recordar hasta qué instante ya se procesó."""

    result = MODULE.process_new_events(
        [
            {"id": "old", "timestamp": "2026-09-24T09:00:00Z"},
            {"id": "new-1", "timestamp": "2026-09-24T11:00:00Z"},
            {"id": "new-2", "timestamp": "2026-09-24T12:00:00Z"},
        ],
        "2026-09-24T10:00:00Z",
    )

    assert result == {
        "processed_ids": ["new-1", "new-2"],
        "new_watermark": "2026-09-24T12:00:00Z",
    }


def test_process_new_events_preserves_the_watermark_without_new_data():
    assert MODULE.process_new_events([], "2026-09-24T10:00:00Z") == {
        "processed_ids": [],
        "new_watermark": "2026-09-24T10:00:00Z",
    }
