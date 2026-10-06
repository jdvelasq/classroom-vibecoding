import csv
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_01():
    assert (SUBMISSION_DIR / "model_comparison.csv").is_file()
    assert (SUBMISSION_DIR / "feature_importances.csv").is_file()
    assert (SUBMISSION_DIR / "validation_curve.png").is_file()
    assert (SUBMISSION_DIR / "partial_dependence.png").is_file()
    assert (SUBMISSION_DIR / "decision_tree.pkl").is_file()
    assert (SUBMISSION_DIR / "random_forest.pkl").is_file()
    assert (SUBMISSION_DIR / "gradient_boosting.pkl").is_file()


def _read_model_comparison():
    with (SUBMISSION_DIR / "model_comparison.csv").open(newline="", encoding="utf-8") as file:
        return {row["model"]: float(row["test_mse"]) for row in csv.DictReader(file)}


def test_02():
    mse_by_model = _read_model_comparison()

    expected_models = {"naive_mean_baseline", "linear_model", "random_forest", "gradient_boosting"}
    assert expected_models <= mse_by_model.keys()
    assert any(model.startswith("decision_tree") for model in mse_by_model)

    other_models_mse = [mse for model, mse in mse_by_model.items() if model != "naive_mean_baseline"]
    assert mse_by_model["naive_mean_baseline"] >= max(other_models_mse)


def test_03():
    mse_by_model = _read_model_comparison()

    assert min(mse_by_model["random_forest"], mse_by_model["gradient_boosting"]) < mse_by_model["linear_model"]


def test_04():
    with (SUBMISSION_DIR / "feature_importances.csv").open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {"feature", "importance", "method"}
    assert expected_columns.issubset(rows[0].keys())

    methods_present = {row["method"] for row in rows}
    assert {"impureza", "permutacion"} == methods_present

    permutation_features = {row["feature"] for row in rows if row["method"] == "permutacion"}
    assert {"Weight", "Horsepower", "Model Year", "Origin"} <= permutation_features
