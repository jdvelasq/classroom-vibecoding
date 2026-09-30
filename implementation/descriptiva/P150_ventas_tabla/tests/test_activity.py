"""Evalúa la tabla y la respuesta analítica construidas desde las fuentes."""

import json
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


DATA = Path("data")
OUT = Path("submission/sales_analytics.csv")
QUESTIONS = [
    {
        "pregunta": "¿Cómo cambian las ventas netas mensuales por categoría después de integrar las fuentes?",
        "archivo_respuesta": "monthly_category_sales.csv",
    }
]


def expected_sales_analytics():
    order_lines = pd.read_csv(DATA / "order_lines.csv")
    customers = pd.read_csv(DATA / "customers.csv")
    products = pd.read_csv(DATA / "products.csv")
    expected = (
        order_lines.merge(customers, on="customer_id", validate="many_to_one")
        .merge(products, on="product_id", validate="many_to_one")
    )
    expected["order_date"] = pd.to_datetime(expected["order_date"])
    expected["gross_sales"] = expected["quantity"] * expected["unit_price"]
    expected["discount_amount"] = expected["gross_sales"] * expected["discount_pct"]
    expected["net_sales"] = expected["gross_sales"] - expected["discount_amount"]
    return expected.sort_values(["order_id", "line_id"], ignore_index=True)


def test_01():
    assert OUT.is_file()


def test_02():
    delivered = pd.read_csv(OUT, parse_dates=["order_date"]).sort_values(
        ["order_id", "line_id"], ignore_index=True
    )
    expected = expected_sales_analytics()
    assert len(delivered) == len(expected)
    assert not delivered[["order_id", "line_id"]].duplicated().any()
    assert_frame_equal(
        delivered[expected.columns], expected, check_dtype=False, rtol=1e-10
    )


def test_03():
    delivered = pd.read_csv(OUT)
    assert delivered[["region", "segment", "product", "category"]].notna().all().all()
    assert (
        delivered["net_sales"]
        == delivered["gross_sales"] - delivered["discount_amount"]
    ).all()
    assert delivered["net_sales"].le(delivered["gross_sales"]).all()


def test_04():
    monthly = pd.read_csv("submission/monthly_category_sales.csv")
    delivered = pd.read_csv(OUT, parse_dates=["order_date"])
    delivered["month"] = delivered["order_date"].dt.to_period("M").dt.to_timestamp()
    expected = (
        delivered.groupby(["month", "category"], as_index=False)["net_sales"]
        .sum()
        .sort_values(["month", "category"], ignore_index=True)
    )
    assert_frame_equal(monthly, expected, check_dtype=False, rtol=1e-10)
    assert json.loads(Path("submission/questions.json").read_text(encoding="utf-8")) == QUESTIONS
