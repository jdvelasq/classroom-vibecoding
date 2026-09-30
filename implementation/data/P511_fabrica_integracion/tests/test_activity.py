from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_daily_performance():
    assert (ACTIVITY_DIR / "submission" / "factory_daily_performance.csv").is_file()
