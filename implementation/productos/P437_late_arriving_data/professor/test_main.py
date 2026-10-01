import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p437_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_classify_arrival_requests_a_backfill_for_historical_data():
    """Un dato cuyo evento precede el procesamiento requiere corregir el historial."""

    result = MODULE.classify_arrival(
        {"event_date": "2026-09-20", "current_processing_date": "2026-09-24"}
    )

    assert result == {"late": True, "action": "backfill"}


def test_classify_arrival_loads_current_data_normally():
    result = MODULE.classify_arrival(
        {"event_date": "2026-09-24", "current_processing_date": "2026-09-24"}
    )

    assert result == {"late": False, "action": "current_load"}
