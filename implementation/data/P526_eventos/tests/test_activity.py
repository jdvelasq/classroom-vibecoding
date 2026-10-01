"""Verifica la evidencia persistente del análisis de eventos."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_event_analysis():
    assert (SUBMISSION_DIR / "event_replay.csv").is_file()
    assert (SUBMISSION_DIR / "session_conversion.csv").is_file()
    assert (SUBMISSION_DIR / "event_summary.csv").is_file()
