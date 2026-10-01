import importlib.util
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p426_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_containerized_service_preserves_the_analytics_contract():
    """El contenedor entrega la misma decisión que el servicio que encapsula."""

    client = MODULE.app.test_client()

    response = client.post("/score", json={"daily_units_produced": 4500})

    assert response.status_code == 200
    assert response.get_json() == {"risk": "low", "threshold": 4500}


def test_containerized_service_rejects_invalid_input():
    client = MODULE.app.test_client()

    response = client.post("/score", json={"daily_units_produced": 4200.0})

    assert response.status_code == 400
    assert response.get_json() == {"error": "daily_units_produced debe ser un entero."}
