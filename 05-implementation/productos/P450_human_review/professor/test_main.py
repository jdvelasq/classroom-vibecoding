import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p450_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_review_recommendation_authorizes_only_an_explicit_approval():
    """La automatización no reemplaza la responsabilidad de quien revisa la decisión."""

    review = MODULE.review_recommendation("approve", {"action": "increase_capacity"})

    assert review["action_authorized"] is True
    assert review["recommendation"] == {"action": "increase_capacity"}


def test_review_recommendation_keeps_a_rejected_action_unauthorized():
    review = MODULE.review_recommendation("reject", {"action": "increase_capacity"})

    assert review["human_decision"] == "reject"
    assert review["action_authorized"] is False
