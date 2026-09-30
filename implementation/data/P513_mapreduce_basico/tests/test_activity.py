"""Evalúa los resultados persistentes de las cinco consultas MapReduce."""

import csv
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tips.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def test_01_tip_rates():
    source = read_csv(DATA_FILE)
    result = read_csv(SUBMISSION_DIR / "query_1_tip_rates.csv")
    assert len(result) == len(source)
    assert all(
        abs(float(row["tip_rate"]) - round(float(row["tip"]) / float(row["total_bill"]), 6)) < 1e-6
        for row in result
    )


def test_02_dinner_filter():
    result = read_csv(SUBMISSION_DIR / "query_2_dinner.csv")
    assert result
    assert all(row["time"] == "Dinner" for row in result)
    assert len(result) == 176


def test_03_dinner_large_tip_filter():
    result = read_csv(SUBMISSION_DIR / "query_3_dinner_large_tip.csv")
    assert result
    assert all(row["time"] == "Dinner" and float(row["tip"]) > 5.0 for row in result)
    assert len(result) == 15


def test_04_large_party_filter():
    result = read_csv(SUBMISSION_DIR / "query_4_large_party.csv")
    assert result
    assert all(
        int(row["size"]) >= 5 or float(row["total_bill"]) > 45.0
        for row in result
    )
    assert len(result) == 13


def test_05_count_by_sex():
    result = read_csv(SUBMISSION_DIR / "query_5_count_by_sex.csv")
    assert result == [
        {"sex": "Female", "count": "87"},
        {"sex": "Male", "count": "157"},
    ]
