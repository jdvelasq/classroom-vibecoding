from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_contract_report():
    assert (ACTIVITY_DIR / "submission" / "contract_report.csv").is_file()
