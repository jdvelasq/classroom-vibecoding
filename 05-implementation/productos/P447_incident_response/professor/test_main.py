import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p447_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_incident_escalates_a_high_severity_alert():
    """La severidad alta necesita una prioridad que haga visible la urgencia."""

    incident = MODULE.build_incident({"alert_id": "alert-1", "severity": "high"})

    assert incident["alert_id"] == "alert-1"
    assert incident["priority"] == "P1"
    assert incident["owner"] == "data-operations"
    assert incident["status"] == "open"


def test_build_incident_assigns_p2_to_other_severities():
    incident = MODULE.build_incident({"alert_id": "alert-2", "severity": "medium"})

    assert incident["priority"] == "P2"
