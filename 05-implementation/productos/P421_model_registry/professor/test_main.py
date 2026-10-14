import importlib.util
from pathlib import Path

import pytest


module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p421_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_01_promotes_the_declared_candidate_to_the_requested_stage(tmp_path):
    candidate = module.find_candidate("candidate_v1")
    module.REGISTRY_DIR = tmp_path / "model_registry"

    record = module.promote_model(candidate, "production")

    assert record["model_id"] == "candidate_v1"
    assert record["stage"] == "production"
    assert (module.REGISTRY_DIR / "production/model.pkl").is_file()
    assert (module.REGISTRY_DIR / "production/registry.json").is_file()


def test_02_rejects_a_model_that_is_not_registered_as_a_candidate():
    with pytest.raises(ValueError, match="No existe el modelo candidato"):
        module.find_candidate("missing")
