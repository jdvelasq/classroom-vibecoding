import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p425_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_score_accepts_a_valid_contract():
    client = MODULE.app.test_client()

    response = client.post("/score", json={"daily_units_produced": 4200})

    assert response.status_code == 200
    assert response.get_json() == {"risk": "high", "threshold": 4500}


def test_score_explains_a_missing_field():
    client = MODULE.app.test_client()

    response = client.post("/score", json={})

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Se requiere el campo daily_units_produced."
    }


def test_score_rejects_a_non_integer_measurement():
    client = MODULE.app.test_client()

    response = client.post("/score", json={"daily_units_produced": "4200"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "daily_units_produced debe ser un entero."}
