from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_superstore_mart():
    assert (ACTIVITY_DIR / "submission" / "superstore_mart.db").is_file()
