from pathlib import Path


def test_01():
    submission = Path(__file__).resolve().parents[1] / "submission"
    for name in [
        "adoption_forecast.csv",
        "model_metrics.csv",
        "adoption_forecast.png",
        "model_assumptions.json",
    ]:
        assert (submission / name).is_file()
