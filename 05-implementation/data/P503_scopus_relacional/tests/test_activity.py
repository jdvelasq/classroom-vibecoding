from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
REQUIRED_ARTIFACTS = [
    "scopus_proptech.db",
    "documents_by_year.csv",
    "authors_by_documents.csv",
    "sources_by_documents.csv",
    "questions.json",
]


def test_01_submission_contains_required_artifacts():
    missing = [
        artifact
        for artifact in REQUIRED_ARTIFACTS
        if not (SUBMISSION_DIR / artifact).is_file()
    ]
    assert not missing, f"Faltan entregables en submission/: {', '.join(missing)}"
