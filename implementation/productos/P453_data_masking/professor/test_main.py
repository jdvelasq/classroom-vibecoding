import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p453_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_mask_email_keeps_only_the_minimum_identifier_needed():
    """El reporte debe permitir reconocer el tipo de contacto sin revelar el correo."""

    masked_email = MODULE.mask_email("ana.gomez@example.com")

    assert masked_email == "a***@example.com"
    assert "ana.gomez" not in masked_email
