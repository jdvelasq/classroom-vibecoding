from pathlib import Path

def test_01():
    submission = Path(__file__).resolve().parents[1] / "submission"
    for name in ["adaptive_evolution.png", "forecasts.csv", "infection_rate_forecast.csv", "model_assumptions.json", "scenario_peaks.csv"]:
        assert (submission / name).is_file()
