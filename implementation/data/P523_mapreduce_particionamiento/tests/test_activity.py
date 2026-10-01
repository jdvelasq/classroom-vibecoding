"""Verifica los artefactos persistentes de la actividad."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_partitioning_evidence():
    assert (SUBMISSION_DIR / "partition_loads.csv").is_file()
    assert (SUBMISSION_DIR / "shuffle_comparison.csv").is_file()
