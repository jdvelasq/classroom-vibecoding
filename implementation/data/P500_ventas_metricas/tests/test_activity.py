import json
import runpy
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
IS_PROFESSOR = any((path / ".PROFESSOR").exists() for path in ACTIVITY_DIR.parents)
CODE_DIR = ACTIVITY_DIR / ("professor" if IS_PROFESSOR else "src")
DATA_FILE = ACTIVITY_DIR / "data" / "superstore_orders.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
QUESTION = "¿Cómo evolucionan mensualmente las ventas, la utilidad, el número de órdenes y el valor promedio por orden?"


def run_main(monkeypatch):
    monkeypatch.chdir(ACTIVITY_DIR.parent)
    runpy.run_path(str(CODE_DIR / "main.py"), run_name="__main__")


def expected_monthly_metrics():
    sales = pd.read_csv(DATA_FILE, sep=";", encoding="latin1", decimal=",")
    sales.columns = [column.removeprefix("ï»¿") for column in sales.columns]
    sales["Order Date"] = pd.to_datetime(sales["Order Date"], format="%d/%m/%y")
    sales["month"] = sales["Order Date"].dt.strftime("%Y-%m")
    expected = sales.groupby("month", as_index=False).agg(sales=("Sales", "sum"), profit=("Profit", "sum"), order_count=("Order ID", "nunique")).sort_values("month", ignore_index=True)
    expected["average_order_value"] = expected["sales"] / expected["order_count"]
    return expected


def test_01_generates_required_outputs(monkeypatch):
    run_main(monkeypatch)
    assert (SUBMISSION_DIR / "metric_contract.json").is_file()
    assert (SUBMISSION_DIR / "monthly_sales_metrics.csv").is_file()
    assert (SUBMISSION_DIR / "questions.json").is_file()


def test_02_defines_metrics_and_source_limits(monkeypatch):
    run_main(monkeypatch)
    contract = json.loads((SUBMISSION_DIR / "metric_contract.json").read_text(encoding="utf-8"))
    assert contract["dataset"] == "superstore_orders.csv"
    assert contract["source_format"] == {"delimiter": ";", "encoding": "latin1", "decimal_mark": ",", "date_format": "%d/%m/%y"}
    assert contract["grain"] == "Una fila por producto dentro de una orden; Row ID no es una clave única global."
    assert [metric["name"] for metric in contract["metrics"]] == ["sales", "profit", "order_count", "average_order_value"]
    assert len(contract["quality_checks"]) == 4


def test_03_calculates_monthly_metrics(monkeypatch):
    run_main(monkeypatch)
    assert_frame_equal(pd.read_csv(SUBMISSION_DIR / "monthly_sales_metrics.csv"), expected_monthly_metrics(), check_dtype=False, rtol=1e-10, atol=1e-10)


def test_04_links_the_question_to_its_answer(monkeypatch):
    run_main(monkeypatch)
    assert json.loads((SUBMISSION_DIR / "questions.json").read_text(encoding="utf-8")) == [{"pregunta": QUESTION, "archivo_respuesta": "monthly_sales_metrics.csv"}]
