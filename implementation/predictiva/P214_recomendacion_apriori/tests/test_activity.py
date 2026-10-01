from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_prediction_evidence():
    expected_files = {
        "association_rules.csv",
        "recommendations.csv",
        "top_items.csv",
        "frequent_itemsets.csv",
        "basket_size_distribution.csv",
    }

    produced_files = {path.name for path in SUBMISSION_DIR.iterdir()}

    assert expected_files <= produced_files
