import importlib.util
from pathlib import Path

import pandas as pd


module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p422_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_01_does_not_alert_for_an_unchanged_feature_distribution():
    reference = pd.DataFrame({"quality": [5, 6, 7]})

    comparison = module.compare_feature(reference, reference, "quality")

    assert not comparison["alert"]


def test_02_alerts_for_a_shifted_feature_distribution():
    reference = pd.DataFrame({"quality": [5, 6, 7]})
    production = pd.DataFrame({"quality": [15, 16, 17]})

    comparison = module.compare_feature(reference, production, "quality")

    assert comparison["alert"]
