from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_required_artifacts():
    required_artifacts = ["recent_sources.csv", "questions.json"]
    missing = [
        artifact
        for artifact in required_artifacts
        if not (SUBMISSION_DIR / artifact).is_file()
    ]
    assert not missing, f"Faltan entregables en submission/: {', '.join(missing)}"
