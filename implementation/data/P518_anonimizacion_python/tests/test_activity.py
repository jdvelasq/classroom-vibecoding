from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_shared_sales():
    assert (ACTIVITY_DIR / "submission" / "shared_sales.csv").is_file()
