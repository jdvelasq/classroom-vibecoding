import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "superstore_orders.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
QUESTION = (
    "¿Cómo evolucionan mensualmente las ventas, la utilidad, el número de "
    "órdenes y el valor promedio por orden?"
)


def load_sales():
    sales = pd.read_csv(DATA_FILE, sep=";", encoding="latin1", decimal=",")
    sales.columns = [column.removeprefix("ï»¿") for column in sales.columns]
    sales["Order Date"] = pd.to_datetime(sales["Order Date"], format="%d/%m/%y")
    return sales


def build_contract():
    return {
        "dataset": "superstore_orders.csv",
        "source_format": {
            "delimiter": ";",
            "encoding": "latin1",
            "decimal_mark": ",",
            "date_format": "%d/%m/%y",
        },
        "grain": (
            "Una fila por producto dentro de una orden; Row ID no es una clave "
            "única global."
        ),
        "quality_checks": [
            "Order ID + Product Name es único",
            "Order Date se interpreta con formato día/mes/año",
            "Discount está entre 0 y 1",
            "Product Base Margin tiene 16 valores faltantes y no se usa en estas métricas",
        ],
        "tool_boundary": (
            "Las métricas se definen independientemente de la herramienta; "
            "Python solo ejecuta la definición."
        ),
        "metrics": [
            {"name": "sales", "formula": "sum(Sales)", "grain": "Mes"},
            {"name": "profit", "formula": "sum(Profit)", "grain": "Mes"},
            {"name": "order_count", "formula": "count_distinct(Order ID)", "grain": "Mes"},
            {
                "name": "average_order_value",
                "formula": "sales / order_count",
                "grain": "Mes",
            },
        ],
    }


def build_monthly_metrics(sales):
    sales["month"] = sales["Order Date"].dt.strftime("%Y-%m")
    monthly = (
        sales.groupby("month", as_index=False)
        .agg(
            sales=("Sales", "sum"),
            profit=("Profit", "sum"),
            order_count=("Order ID", "nunique"),
        )
        .sort_values("month")
    )
    monthly["average_order_value"] = monthly["sales"] / monthly["order_count"]
    return monthly


def main():
    sales = load_sales()
    required_fields = {
        "Order ID", "Order Date", "Product Name", "Sales", "Profit", "Discount"
    }
    assert required_fields <= set(sales.columns)
    assert sales["Order Date"].notna().all()
    assert not sales.duplicated(["Order ID", "Product Name"]).any()
    assert sales["Discount"].between(0, 1).all()
    contract_path = SUBMISSION_DIR / "metric_contract.json"
    contract_path.write_text(
        json.dumps(build_contract(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    build_monthly_metrics(sales).to_csv(SUBMISSION_DIR / "monthly_sales_metrics.csv", index=False)
    questions = [{"pregunta": QUESTION, "archivo_respuesta": "monthly_sales_metrics.csv"}]
    (SUBMISSION_DIR / "questions.json").write_text(
        json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
