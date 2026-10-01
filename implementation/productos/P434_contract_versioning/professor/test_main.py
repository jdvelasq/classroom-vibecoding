import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p434_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_is_compatible_honors_the_versions_declared_by_the_contract():
    """La versión del consumidor, no una suposición, determina si puede integrarse."""

    contract = {"compatible_with": ["1.0", "2.0"]}

    assert MODULE.is_compatible("1.0", contract)
    assert MODULE.is_compatible("2.0", contract)
    assert not MODULE.is_compatible("3.0", contract)
