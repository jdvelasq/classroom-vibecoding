import importlib.util
import json
from pathlib import Path


module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p417_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_01_publishes_factory_totals_from_input_to_output():
    output_path = module.run_pipeline()

    assert json.loads(output_path.read_text()) == {
        "factory_totals": {"1": 9303, "2": 9300}
    }
