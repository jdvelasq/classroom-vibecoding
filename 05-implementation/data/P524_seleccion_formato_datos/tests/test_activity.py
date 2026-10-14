"""Verifica la evidencia persistente de selección de formato."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_format_comparison():
    assert (SUBMISSION_DIR / "format_comparison.csv").is_file()
