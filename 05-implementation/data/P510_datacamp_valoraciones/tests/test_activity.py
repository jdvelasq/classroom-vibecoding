from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_course_ratings():
    assert (ACTIVITY_DIR / "submission" / "course_ratings.csv").is_file()
