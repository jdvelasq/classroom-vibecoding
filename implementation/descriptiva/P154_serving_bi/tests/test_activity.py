"""Evalúa la capa de serving publicada para el dashboard de ventas."""

from pathlib import Path
import sqlite3

import pandas as pd
from pandas.testing import assert_frame_equal


MART = Path("data/sales_mart.db")
OUT = Path("submission")
SERVING_DB = OUT / "bi_serving.db"


def expected_dashboard_sales():
    with sqlite3.connect(MART) as connection:
        return pd.read_sql_query(
            """
            SELECT d.year, d.month, c.region, p.category,
                   SUM(f.net_sales) AS net_sales,
                   SUM(f.quantity) AS units_sold,
                   COUNT(DISTINCT f.order_id) AS orders
            FROM fact_sales f
            JOIN dim_date d USING(date_key)
            JOIN dim_customer c USING(customer_key)
            JOIN dim_product p USING(product_key)
            GROUP BY d.year, d.month, c.region, p.category
            ORDER BY d.year, d.month, c.region, p.category
            """,
            connection,
        )


def test_01():
    assert {path.name for path in OUT.iterdir() if path.name != ".gitkeep"} == {
        "bi_serving.db",
        "dashboard_sales.csv",
        "serving_manifest.csv",
    }


def test_02():
    expected = expected_dashboard_sales()
    delivered = pd.read_csv(OUT / "dashboard_sales.csv")
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)
    assert not delivered[["year", "month", "region", "category"]].duplicated().any()


def test_03():
    csv_data = pd.read_csv(OUT / "dashboard_sales.csv")
    with sqlite3.connect(SERVING_DB) as connection:
        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type = 'table'", connection
        )
        database_data = pd.read_sql_query(
            "SELECT * FROM dashboard_sales ORDER BY year, month, region, category",
            connection,
        )
    assert set(tables["name"]) == {"dashboard_sales"}
    assert_frame_equal(database_data, csv_data, check_dtype=False, rtol=1e-10)


def test_04():
    manifest = pd.read_csv(OUT / "serving_manifest.csv")
    assert list(manifest.columns) == ["tabla", "grano", "métricas", "consumidor"]
    assert manifest.loc[0, "tabla"] == "dashboard_sales"
    assert "mes, región y categoría" in manifest.loc[0, "grano"]
    assert "Ventas netas" in manifest.loc[0, "métricas"]
