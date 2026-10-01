from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_submission_contains_governed_policy_evidence():
    expected = {
        "equity_audit.csv",
        "policy_correction_decisions.csv",
        "policy_contract.json",
        "policy_monitoring.csv",
    }
    delivered = {path.name for path in SUBMISSION_DIR.iterdir() if path.is_file()}

    assert expected.issubset(delivered), (
        "Ejecuta la solución y guarda la auditoría, la decisión de corrección, "
        "el contrato de política y su monitoreo."
    )
