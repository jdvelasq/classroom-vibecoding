import json
import sqlite3
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "superstore_orders.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
QUESTION = "¿Qué interfaces permiten responder la evolución mensual de ventas y la contribución de cada categoría?"


def load_sales():
    sales = pd.read_csv(DATA_FILE, sep=";", encoding="latin1", decimal=",")
    sales.columns = [column.removeprefix("ï»¿") for column in sales.columns]
    sales["Order Date"] = pd.to_datetime(sales["Order Date"], format="%d/%m/%y")
    return sales


def build_monthly_sales(sales):
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


def build_category_sales(sales):
    return (
        sales.groupby("Product Category", as_index=False)
        .agg(sales=("Sales", "sum"), profit=("Profit", "sum"))
        .sort_values("sales", ascending=False)
    )


def build_manifest():
    return pd.DataFrame(
        [
            ["sales_detail.csv", "Una fila por producto dentro de una orden", "CSV", "Analista", "Detalle para exploración y trazabilidad"],
            ["monthly_sales", "Una fila por mes", "SQLite", "Dashboard", "Indicadores mensuales de ventas"],
            ["category_sales", "Una fila por categoría", "SQLite", "Dashboard", "Comparación de categorías"],
        ],
        columns=["artifact", "grain", "interface", "consumer", "purpose"],
    )


def main():
    SUBMISSION_DIR.mkdir(exist_ok=True)
    sales = load_sales()
    detail_columns = [
        "Order ID",
        "Order Date",
        "Customer ID",
        "Product Category",
        "Product Name",
        "Region",
        "Sales",
        "Profit",
        "Discount",
    ]
    sales[detail_columns].to_csv(SUBMISSION_DIR / "sales_detail.csv", index=False)
    with sqlite3.connect(SUBMISSION_DIR / "sales_serving.db") as database:
        build_monthly_sales(sales).to_sql("monthly_sales", database, index=False, if_exists="replace")
        build_category_sales(sales).to_sql("category_sales", database, index=False, if_exists="replace")
    build_manifest().to_csv(SUBMISSION_DIR / "serving_manifest.csv", index=False)
    questions = [{"pregunta": QUESTION, "archivo_respuesta": "sales_serving.db"}]
    (SUBMISSION_DIR / "questions.json").write_text(
        json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
