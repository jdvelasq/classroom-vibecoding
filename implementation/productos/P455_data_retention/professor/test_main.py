import importlib.util
from datetime import date
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p455_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_apply_retention_policy_keeps_the_cutoff_date_and_records_expiration():
    """La política debe ser repetible: la misma fecha de corte produce la misma decisión."""

    result = MODULE.apply_retention_policy(
        date(2026, 9, 1),
        [
            {"event_id": "at-cutoff", "event_date": "2026-06-03"},
            {"event_id": "expired", "event_date": "2026-06-02"},
        ],
    )

    assert result["cutoff"] == "2026-06-03"
    assert result["retained"] == [{"event_id": "at-cutoff", "event_date": "2026-06-03"}]
    assert result["expired"] == [
        {"event_id": "expired", "reason": "retention_period_expired"}
    ]
