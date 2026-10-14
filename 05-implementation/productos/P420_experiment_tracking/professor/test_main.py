import importlib.util
from pathlib import Path

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


module_path = Path(__file__).resolve().with_name("main.py")
spec = importlib.util.spec_from_file_location("p420_professor_main", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_01_builds_the_declared_model_alternatives():
    assert isinstance(module.build_model("tree"), DecisionTreeClassifier)
    assert isinstance(module.build_model("knn"), KNeighborsClassifier)


def test_02_reuses_the_same_data_partition_for_comparison():
    first = module.prepare_data()
    second = module.prepare_data()

    for first_part, second_part in zip(first, second):
        assert first_part.equals(second_part)
