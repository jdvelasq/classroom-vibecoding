import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p445_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_evaluate_service_level_meets_an_exact_target():
    """Una meta de servicio se cumple también en su límite exacto."""

    report = MODULE.evaluate_service_level(
        {"successful": 99, "total": 100, "target": 0.99}
    )

    assert report == {"availability": 0.99, "target": 0.99, "met": True}


def test_evaluate_service_level_flags_a_missed_target():
    report = MODULE.evaluate_service_level(
        {"successful": 98, "total": 100, "target": 0.99}
    )

    assert report["availability"] == 0.98
    assert report["met"] is False
