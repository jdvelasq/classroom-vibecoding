"""Evalúa los productos de consultas OLAP sobre el mart de ventas."""

from pathlib import Path
import sqlite3

import pandas as pd
from pandas.testing import assert_frame_equal


MART = Path("data/sales_mart.db")
OUT = Path("submission")


def query(sql, params=None):
    with sqlite3.connect(MART) as connection:
        return pd.read_sql_query(sql, connection, params=params)


def test_01():
    assert {path.name for path in OUT.iterdir() if path.name != ".gitkeep"} == {
        "monthly_region_sales.csv",
        "north_category_sales.csv",
        "north_product_drilldown.csv",
    }


def test_02():
    expected = query(
        """
        SELECT d.year, d.month, c.region, SUM(f.net_sales) AS net_sales
        FROM fact_sales f
        JOIN dim_date d USING(date_key)
        JOIN dim_customer c USING(customer_key)
        GROUP BY d.year, d.month, c.region
        ORDER BY d.year, d.month, c.region
        """
    )
    delivered = pd.read_csv(OUT / "monthly_region_sales.csv")
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)
    assert delivered["net_sales"].sum() == query(
        "SELECT SUM(net_sales) AS net_sales FROM fact_sales"
    ).loc[0, "net_sales"]


def test_03():
    expected = query(
        """
        SELECT p.category, SUM(f.net_sales) AS net_sales, SUM(f.quantity) AS units
        FROM fact_sales f
        JOIN dim_customer c USING(customer_key)
        JOIN dim_product p USING(product_key)
        WHERE c.region = 'Norte'
        GROUP BY p.category
        ORDER BY net_sales DESC
        """
    )
    delivered = pd.read_csv(OUT / "north_category_sales.csv")
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_04():
    categories = pd.read_csv(OUT / "north_category_sales.csv")
    leading_category = categories.loc[0, "category"]
    expected = query(
        """
        SELECT p.product, SUM(f.net_sales) AS net_sales
        FROM fact_sales f
        JOIN dim_customer c USING(customer_key)
        JOIN dim_product p USING(product_key)
        WHERE c.region = ? AND p.category = ?
        GROUP BY p.product
        ORDER BY net_sales DESC
        """,
        params=["Norte", leading_category],
    )
    delivered = pd.read_csv(OUT / "north_product_drilldown.csv")
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)
