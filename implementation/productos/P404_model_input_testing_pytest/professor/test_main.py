import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p404_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assess_inputs = module.assess_inputs
load_inputs = module.load_inputs


def test_01_accepts_the_expected_input_distribution():
    training_inputs, new_inputs, _ = load_inputs()

    _, compatible = assess_inputs(training_inputs, new_inputs)

    assert compatible


def test_02_rejects_a_shifted_input_distribution():
    training_inputs, new_inputs, _ = load_inputs()
    shifted_inputs = new_inputs.assign(
        texture_mean=lambda dataframe: dataframe["texture_mean"] + 100
    )

    _, compatible = assess_inputs(training_inputs, shifted_inputs)

    assert not compatible
