import csv
from datetime import date
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01_submission_contains_forecast_evidence():
    expected_files = {
        "congestion_forecast.csv",
        "model_metrics.csv",
        "congestion_forecast.png",
        "model_assumptions.json",
    }

    produced_files = {path.name for path in SUBMISSION_DIR.iterdir()}

    assert expected_files <= produced_files


def test_02_rolling_origin_errors():
    rolling_path = SUBMISSION_DIR / "rolling_origin_errors.csv"
    assert rolling_path.is_file()

    with rolling_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {"origin", "model", "forecast", "actual", "abs_error"}
    assert expected_columns.issubset(rows[0].keys())

    models_present = {row["model"] for row in rows}
    assert {"Línea base estacional", "Regresión operacional rezagada"}.issubset(models_present)

    origins = sorted({row["origin"] for row in rows})
    assert len(origins) >= 24

    origin_dates = [date.fromisoformat(value) for value in origins]
    for earlier, later in zip(origin_dates, origin_dates[1:]):
        month_gap = (later.year - earlier.year) * 12 + (later.month - earlier.month)
        assert month_gap == 1

    with (SUBMISSION_DIR / "congestion_forecast.csv").open(newline="", encoding="utf-8") as file:
        forecast_rows = list(csv.DictReader(file))
    observed_by_date = {
        row["date"]: float(row["observed_average_speed_seconds"]) for row in forecast_rows
    }

    for row in rows:
        if row["origin"] in observed_by_date:
            assert float(row["actual"]) == observed_by_date[row["origin"]]


def test_03_forecast_intervals():
    intervals_path = SUBMISSION_DIR / "forecast_intervals.csv"
    assert intervals_path.is_file()
    assert (SUBMISSION_DIR / "forecast_intervals.png").is_file()

    with intervals_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {"month", "forecast", "lower_80", "upper_80", "actual"}
    assert expected_columns.issubset(rows[0].keys())
    assert len(rows) == 12

    for row in rows:
        lower, forecast, upper = (
            float(row["lower_80"]), float(row["forecast"]), float(row["upper_80"]),
        )
        assert lower <= forecast <= upper
