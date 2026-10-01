"""Verifica los artefactos persistentes de la actividad MapReduce."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
EXPECTED_FILES = [
    "query_1_tip_rates.csv",
    "query_2_dinner.csv",
    "query_3_dinner_large_tip.csv",
    "query_4_large_party.csv",
    "query_5_count_by_sex.csv",
]


def test_01_submission_contains_query_results():
    for filename in EXPECTED_FILES:
        assert (SUBMISSION_DIR / filename).is_file(), f"Falta submission/{filename}."
