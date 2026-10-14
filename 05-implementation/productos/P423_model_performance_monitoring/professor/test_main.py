import importlib.util
from pathlib import Path

import pandas as pd


module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p423_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_01_does_not_alert_when_accuracy_meets_the_minimum():
    outcomes = pd.DataFrame({"prediction": [1, 1, 0, 0], "actual": [1, 1, 0, 1]})

    report = module.evaluate_performance(outcomes)

    assert report["accuracy"] == 0.75
    assert not report["alert"]


def test_02_alerts_when_accuracy_falls_below_the_minimum():
    outcomes = pd.DataFrame({"prediction": [1, 1, 0, 0], "actual": [0, 1, 1, 1]})

    report = module.evaluate_performance(outcomes)

    assert report["accuracy"] == 0.25
    assert report["alert"]
