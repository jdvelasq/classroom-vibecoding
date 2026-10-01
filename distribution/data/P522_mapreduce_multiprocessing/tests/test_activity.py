"""Verifica los artefactos persistentes de la actividad."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_mapreduce_results():
    assert (SUBMISSION_DIR / "origin_flights.csv").is_file()
    assert (SUBMISSION_DIR / "benchmark.csv").is_file()
