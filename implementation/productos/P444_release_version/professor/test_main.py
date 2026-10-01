import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p444_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_release_manifest_exposes_the_delivered_capability_version():
    """La versión permite relacionar una entrega con sus cambios documentados."""

    manifest = MODULE.build_release_manifest("2.1.0")

    assert manifest == {
        "product": "factory-risk-indicator",
        "version": "2.1.0",
        "release_notes": "CHANGELOG.md",
    }
