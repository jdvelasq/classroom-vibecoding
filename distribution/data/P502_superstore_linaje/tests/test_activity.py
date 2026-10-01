from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
REQUIRED_ARTIFACTS = [
    "data_catalog.csv",
    "column_catalog.csv",
    "lineage.csv",
    "questions.json",
]


def test_01_submission_contains_required_artifacts():
    missing = [
        artifact
        for artifact in REQUIRED_ARTIFACTS
        if not (SUBMISSION_DIR / artifact).is_file()
    ]
    assert not missing, f"Faltan entregables en submission/: {', '.join(missing)}"
