from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_enriched_sales():
    assert (ACTIVITY_DIR / "submission" / "superstore_enriched_sales.csv").is_file()


def test_02_submission_contains_analytical_answer():
    assert (ACTIVITY_DIR / "submission" / "sales_by_segment_region_category.csv").is_file()
