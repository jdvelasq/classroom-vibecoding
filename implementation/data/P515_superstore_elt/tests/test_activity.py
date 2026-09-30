from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_elt_outputs():
    for name in ["superstore_elt.db", "sales_by_segment_region.csv", "elt_report.csv", "questions.json"]:
        assert (ACTIVITY_DIR / "submission" / name).is_file()
