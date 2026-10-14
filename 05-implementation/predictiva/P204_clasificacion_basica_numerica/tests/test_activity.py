import csv
from pathlib import Path


def test_01():
    activity_dir = Path(__file__).resolve().parents[1]
    submission_dir = activity_dir / "submission"

    assert (submission_dir / "base_estimator.pkl").is_file()
    assert (submission_dir / "flexible_estimator.pkl").is_file()
    assert (submission_dir / "metrics.json").is_file()
    assert (submission_dir / "model_comparison.csv").is_file()


def test_02():
    activity_dir = Path(__file__).resolve().parents[1]
    submission_dir = activity_dir / "submission"
    difference_path = submission_dir / "difference_bootstrap.csv"

    assert difference_path.is_file()

    with difference_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {
        "metric",
        "observed_difference",
        "ci_low",
        "ci_high",
        "n_resamples",
    }
    assert expected_columns.issubset(rows[0].keys())

    metrics_present = {row["metric"] for row in rows}
    assert {"auc", "accuracy"}.issubset(metrics_present)

    for row in rows:
        assert float(row["ci_low"]) <= float(row["ci_high"])
