import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p439_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_assess_freshness_accepts_data_at_the_declared_limit():
    """El límite permitido no debe generar una alerta prematura."""

    report = MODULE.assess_freshness(
        {
            "data_as_of": "2026-09-20",
            "checked_at": "2026-09-23",
            "maximum_age_days": 3,
        }
    )

    assert report == {"age_days": 3, "maximum_age_days": 3, "alert": False}


def test_assess_freshness_alerts_when_data_is_too_old():
    report = MODULE.assess_freshness(
        {
            "data_as_of": "2026-09-20",
            "checked_at": "2026-09-24",
            "maximum_age_days": 3,
        }
    )

    assert report["alert"]
