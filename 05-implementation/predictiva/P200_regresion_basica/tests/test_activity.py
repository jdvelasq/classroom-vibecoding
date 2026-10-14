import csv
import math
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01():
    assert (SUBMISSION_DIR / "features_preprocessor.pkl").is_file()
    assert (SUBMISSION_DIR / "flexible_features_preprocessor.pkl").is_file()
    assert (SUBMISSION_DIR / "linear_flexible_model.pkl").is_file()
    assert (SUBMISSION_DIR / "mlp.pkl").is_file()
    assert (SUBMISSION_DIR / "model_comparison.csv").is_file()


def _read_model_comparison():
    with (SUBMISSION_DIR / "model_comparison.csv").open(newline="", encoding="utf-8") as file:
        return {row["model"]: float(row["test_mse"]) for row in csv.DictReader(file)}


def test_02():
    mse_by_model = _read_model_comparison()

    assert "naive_mean_baseline" in mse_by_model
    other_models_mse = [mse for model, mse in mse_by_model.items() if model != "naive_mean_baseline"]
    assert other_models_mse
    assert mse_by_model["naive_mean_baseline"] >= min(other_models_mse)


def test_03():
    mse_by_model = _read_model_comparison()

    assert "log_horsepower_model" in mse_by_model
    log_mse = mse_by_model["log_horsepower_model"]
    assert math.isfinite(log_mse)
    assert log_mse > 0
    assert (SUBMISSION_DIR / "residual_diagnostics.png").is_file()
