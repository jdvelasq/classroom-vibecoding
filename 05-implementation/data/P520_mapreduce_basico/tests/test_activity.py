"""Verifica los artefactos persistentes de la actividad MapReduce."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
EXPECTED_FILE = "driver_metrics.csv"


def test_01_submission_contains_driver_metrics():
    assert (SUBMISSION_DIR / EXPECTED_FILE).is_file(), f"Falta submission/{EXPECTED_FILE}."
