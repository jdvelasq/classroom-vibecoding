"""Verifica la evidencia persistente de particionamiento."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_partition_summary():
    assert (SUBMISSION_DIR / "lake_summary.csv").is_file()
