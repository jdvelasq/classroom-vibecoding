import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p451_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_capture_feedback_links_a_use_signal_to_the_evaluated_response():
    """La adopción se interpreta junto con la salida analítica que la provocó."""

    feedback = MODULE.capture_feedback(
        True,
        "Permitió priorizar la inspección.",
        {"risk": "high"},
    )

    assert feedback == {
        "response": {"risk": "high"},
        "useful": True,
        "comment": "Permitió priorizar la inspección.",
    }


def test_capture_feedback_preserves_negative_feedback_for_improvement():
    feedback = MODULE.capture_feedback(False, "No llegó a tiempo.", {"risk": "low"})

    assert feedback["useful"] is False
    assert feedback["comment"] == "No llegó a tiempo."
