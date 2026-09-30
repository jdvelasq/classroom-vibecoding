"""Evalúa el mart de ventas y su respuesta analítica."""

import json
from pathlib import Path
import sqlite3

import pandas as pd
from pandas.testing import assert_frame_equal


DATA = Path("data")
MART = Path("submission/sales_mart.db")
QUESTIONS = [
    {
        "pregunta": "¿Qué combinación de región y categoría aporta más ventas netas en el mart?",
        "archivo_respuesta": "region_category_sales.csv",
    }
]


def expected_fact_sales():
    lines = pd.read_csv(DATA / "order_lines.csv")
    products = pd.read_csv(DATA / "products.csv")
    facts = lines.merge(
        products[["product_id", "unit_price"]], on="product_id", validate="many_to_one"
    )
    facts["order_date"] = pd.to_datetime(facts["order_date"])
    facts["gross_sales"] = facts["quantity"] * facts["unit_price"]
    facts["net_sales"] = facts["gross_sales"] * (1 - facts["discount_pct"])
    dim_date = pd.DataFrame({"date": sorted(facts["order_date"].unique())})
    dim_date["date_key"] = range(1, len(dim_date) + 1)
    expected = (
        facts.merge(
            dim_date[["date", "date_key"]],
            left_on="order_date",
            right_on="date",
            validate="many_to_one",
        )[
            [
                "order_id",
                "line_id",
                "date_key",
                "customer_id",
                "product_id",
                "quantity",
                "gross_sales",
                "discount_pct",
                "net_sales",
            ]
        ]
        .rename(columns={"customer_id": "customer_key", "product_id": "product_key"})
        .sort_values(["order_id", "line_id"], ignore_index=True)
    )
    return expected


def test_01():
    assert MART.is_file()
    with sqlite3.connect(MART) as connection:
        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type = 'table'", connection
        )
    assert set(tables["name"]) == {
        "dim_date",
        "dim_customer",
        "dim_product",
        "fact_sales",
    }


def test_02():
    with sqlite3.connect(MART) as connection:
        dim_date = pd.read_sql_query("SELECT * FROM dim_date", connection)
        dim_customer = pd.read_sql_query("SELECT * FROM dim_customer", connection)
        dim_product = pd.read_sql_query("SELECT * FROM dim_product", connection)
        fact_sales = pd.read_sql_query(
            "SELECT * FROM fact_sales ORDER BY order_id, line_id", connection
        )
    assert dim_date["date_key"].is_unique
    assert dim_customer["customer_key"].is_unique
    assert dim_product["product_key"].is_unique
    assert fact_sales[["order_id", "line_id"]].duplicated().sum() == 0
    assert set(fact_sales["date_key"]).issubset(set(dim_date["date_key"]))
    assert set(fact_sales["customer_key"]).issubset(set(dim_customer["customer_key"]))
    assert set(fact_sales["product_key"]).issubset(set(dim_product["product_key"]))


def test_03():
    with sqlite3.connect(MART) as connection:
        delivered = pd.read_sql_query(
            "SELECT * FROM fact_sales ORDER BY order_id, line_id", connection
        )
    expected = expected_fact_sales()
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_04():
    with sqlite3.connect(MART) as connection:
        expected = pd.read_sql_query(
            """
            SELECT c.region, p.category, SUM(f.net_sales) AS net_sales
            FROM fact_sales f
            JOIN dim_customer c USING(customer_key)
            JOIN dim_product p USING(product_key)
            GROUP BY c.region, p.category
            ORDER BY net_sales DESC
            """,
            connection,
        )
    delivered = pd.read_csv("submission/region_category_sales.csv")
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)
    assert json.loads(Path("submission/questions.json").read_text(encoding="utf-8")) == QUESTIONS
