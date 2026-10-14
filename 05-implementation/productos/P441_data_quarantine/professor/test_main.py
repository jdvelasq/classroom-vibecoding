import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p441_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_quarantine_invalid_records_preserves_valid_and_rejected_evidence():
    """Un registro inválido no debe contaminar la salida ni desaparecer sin explicación."""

    result = MODULE.quarantine_invalid_records(
        [{"id": "valid", "amount": 10}, {"id": "invalid", "amount": -2}]
    )

    assert result["valid"] == [{"id": "valid", "amount": 10}]
    assert result["quarantined"] == [
        {
            "id": "invalid",
            "amount": -2,
            "rejection_reason": "amount_must_be_non_negative",
        }
    ]
