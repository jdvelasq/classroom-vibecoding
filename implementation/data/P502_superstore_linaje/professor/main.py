import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
QUESTION = "¿Cuál es el linaje desde Superstore hasta las interfaces que responden ventas mensuales y ventas por categoría?"


def build_data_catalog():
    return pd.DataFrame(
        [
            ["superstore_orders", "Fuente original de líneas de pedido", "Una fila por producto dentro de una orden", "data", "Privado"],
            ["sales_detail", "Detalle publicado para exploración", "Una fila por producto dentro de una orden", "submission", "Analista"],
            ["monthly_sales", "Métricas mensuales de ventas", "Una fila por mes", "sales_serving.db", "Dashboard"],
            ["category_sales", "Ventas y utilidad por categoría", "Una fila por categoría", "sales_serving.db", "Dashboard"],
        ],
        columns=["dataset", "description", "grain", "location", "consumer"],
    )


def build_column_catalog():
    return pd.DataFrame(
        [
            ["superstore_orders", "Order ID", "Identificador de orden", "Clave de negocio"],
            ["superstore_orders", "Order Date", "Fecha de la orden", "Dimensión temporal"],
            ["superstore_orders", "Sales", "Valor de ventas", "Métrica fuente"],
            ["superstore_orders", "Profit", "Utilidad", "Métrica fuente"],
            ["monthly_sales", "average_order_value", "Ventas divididas por órdenes", "Métrica derivada"],
            ["category_sales", "Product Category", "Categoría de producto", "Dimensión de análisis"],
        ],
        columns=["dataset", "column", "description", "role"],
    )


def build_lineage():
    return pd.DataFrame(
        [
            ["superstore_orders", "sales_detail", "Selección de campos para exploración"],
            ["superstore_orders", "monthly_sales", "Agregación mensual de ventas, utilidad y órdenes"],
            ["superstore_orders", "category_sales", "Agregación de ventas y utilidad por categoría"],
        ],
        columns=["source_dataset", "target_dataset", "transformation"],
    )


def main():
    build_data_catalog().to_csv(SUBMISSION_DIR / "data_catalog.csv", index=False)
    build_column_catalog().to_csv(SUBMISSION_DIR / "column_catalog.csv", index=False)
    build_lineage().to_csv(SUBMISSION_DIR / "lineage.csv", index=False)
    questions = [{"pregunta": QUESTION, "archivo_respuesta": "lineage.csv"}]
    (SUBMISSION_DIR / "questions.json").write_text(
        json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
