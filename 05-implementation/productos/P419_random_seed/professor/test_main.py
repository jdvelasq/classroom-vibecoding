import importlib.util
from pathlib import Path


module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p419_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_01_repeats_the_same_sample_for_the_same_seed():
    assert module.select_sample(123) == module.select_sample(123)
