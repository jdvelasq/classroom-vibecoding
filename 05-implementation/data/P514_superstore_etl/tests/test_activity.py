from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01_submission_contains_pipeline_outputs():
    for name in ["superstore_enriched_sales.csv", "sales_by_segment_region.csv", "pipeline_report.csv", "questions.json"]:
        assert (ACTIVITY_DIR / "submission" / name).is_file()
