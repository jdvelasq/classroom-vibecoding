import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p403_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

MIN_ACCURACY = module.MIN_ACCURACY
MIN_AUC = module.MIN_AUC
MIN_BALANCED_ACCURACY = module.MIN_BALANCED_ACCURACY
load_model_and_test_set = module.load_model_and_test_set
model_metrics = module.model_metrics


def test_01_model_satisfies_its_operational_thresholds():
    model, inputs, target, _ = load_model_and_test_set()

    metrics = model_metrics(model, inputs, target)

    assert metrics["accuracy"] >= MIN_ACCURACY
    assert metrics["balanced_accuracy"] >= MIN_BALANCED_ACCURACY
    assert metrics["auc"] >= MIN_AUC
