"""Verifica el artefacto persistente de los operadores MapReduce."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
EXPECTED_FILE = "operator_walkthrough.csv"


def test_01_submission_contains_operator_walkthrough():
    assert (SUBMISSION_DIR / EXPECTED_FILE).is_file(), f"Falta submission/{EXPECTED_FILE}."
