import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p442_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_observability_report_accepts_healthy_signals():
    """La salud exige que todas las señales declaradas estén dentro de su contrato."""

    report = MODULE.build_observability_report(
        {
            "age_days": 1,
            "maximum_age_days": 1,
            "rows": 100,
            "minimum_rows": 100,
            "schema_valid": True,
        }
    )

    assert report["healthy"]
    assert all(report["checks"].values())


def test_build_observability_report_flags_a_broken_schema():
    report = MODULE.build_observability_report(
        {
            "age_days": 0,
            "maximum_age_days": 1,
            "rows": 100,
            "minimum_rows": 50,
            "schema_valid": False,
        }
    )

    assert report["checks"]["schema"] is False
    assert report["healthy"] is False
