import csv
from pathlib import Path


def test_01():
    assert Path("submission/coverage_summary.csv").is_file()
    assert Path("submission/nearest_neighbors.csv").is_file()
    assert Path("submission/recommendations.csv").is_file()


def test_02():
    holdout_path = Path("submission/holdout_evaluation.csv")
    assert holdout_path.is_file()

    with holdout_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {"method", "n_predicted", "coverage", "mae", "rmse"}
    assert expected_columns.issubset(rows[0].keys())
    assert len(rows) == 2
    assert {"Línea base (promedio de película)", "Filtrado colaborativo"} == {
        row["method"] for row in rows
    }
