"""Evalúa los productos descriptivos del caso Retail Sales."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]

import pandas as pd
from pandas.testing import assert_frame_equal


SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def prepared_sales():
    sales = pd.read_csv(ACTIVITY_DIR / "data/sales.csv")
    sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])
    sales["OrderMonth"] = sales["OrderDate"].dt.to_period("M").dt.to_timestamp()
    sales["DayType"] = sales["OrderDate"].dt.dayofweek.map(
        lambda day: "Fin de semana" if day >= 5 else "Laboral"
    )
    sales["ReturnedAmount"] = sales["TotalAmount"].where(sales["IsReturned"].eq(1), 0)
    sales["NetAmount"] = sales["TotalAmount"] - sales["ReturnedAmount"]
    return sales


def assert_csv_equals(name, expected):
    actual = pd.read_csv(SUBMISSION_DIR / name)
    expected = expected.reset_index(drop=True)
    assert_frame_equal(actual, expected, check_dtype=False, rtol=1e-10)


def test_01():
    expected_files = {
        "category_summary.csv",
        "day_type_summary.csv",
        "kpi_summary.csv",
        "monthly_sales.csv",
        "payment_summary.csv",
        "priority_segments.csv",
        "return_risk.csv",
        "top_customers.csv",
        "top_products.csv",
    }
    actual_files = {path.name for path in SUBMISSION_DIR.glob("*.csv")}
    assert actual_files == expected_files


def test_02():
    sales = prepared_sales()
    kpi = pd.DataFrame(
        {
            "orders": [sales["OrderID"].nunique()],
            "customers": [sales["CustomerID"].nunique()],
            "gross_sales": [sales["TotalAmount"].sum()],
            "returned_amount": [sales["ReturnedAmount"].sum()],
            "net_sales": [sales["NetAmount"].sum()],
        }
    )
    kpi["return_rate_by_orders"] = sales["IsReturned"].mean()
    kpi["return_rate_by_value"] = kpi["returned_amount"] / kpi["gross_sales"]
    kpi["net_sales_per_order"] = kpi["net_sales"] / kpi["orders"]
    assert_csv_equals("kpi_summary.csv", kpi)


def test_03():
    sales = prepared_sales()
    monthly = sales.groupby("OrderMonth")[["TotalAmount", "ReturnedAmount", "NetAmount"]].sum().reset_index()
    monthly = monthly.melt(id_vars="OrderMonth", var_name="metric", value_name="amount")
    monthly["OrderMonth"] = monthly["OrderMonth"].astype(str)
    assert_csv_equals("monthly_sales.csv", monthly)


def test_04():
    sales = prepared_sales()
    category = (
        sales.groupby("Category")
        .agg(orders=("OrderID", "size"), gross_sales=("TotalAmount", "sum"), returned_amount=("ReturnedAmount", "sum"), net_sales=("NetAmount", "sum"), return_rate=("IsReturned", "mean"))
        .reset_index()
        .sort_values("net_sales", ascending=False)
    )
    payment = (
        sales.groupby("PaymentMethod")
        .agg(orders=("OrderID", "size"), gross_sales=("TotalAmount", "sum"), returned_amount=("ReturnedAmount", "sum"), net_sales=("NetAmount", "sum"), return_rate=("IsReturned", "mean"))
        .reset_index()
    )
    day_type = (
        sales.groupby("DayType")
        .agg(orders=("OrderID", "size"), gross_sales=("TotalAmount", "sum"), net_sales=("NetAmount", "sum"), return_rate=("IsReturned", "mean"))
        .reset_index()
    )
    assert_csv_equals("category_summary.csv", category)
    assert_csv_equals("payment_summary.csv", payment)
    assert_csv_equals("day_type_summary.csv", day_type)


def test_05():
    sales = prepared_sales()
    customers = (
        sales.groupby("CustomerID")
        .agg(orders=("OrderID", "size"), gross_sales=("TotalAmount", "sum"), returned_amount=("ReturnedAmount", "sum"), net_sales=("NetAmount", "sum"))
        .reset_index()
    )
    customers["return_rate_by_value"] = customers["returned_amount"] / customers["gross_sales"]
    products = (
        sales.groupby(["Category", "ProductName"])
        .agg(orders=("OrderID", "size"), net_sales=("NetAmount", "sum"), return_rate=("IsReturned", "mean"))
        .reset_index()
        .sort_values(["Category", "net_sales"], ascending=[True, False])
        .groupby("Category")
        .head(5)
    )
    assert_csv_equals("top_customers.csv", customers.nlargest(10, "net_sales"))
    assert_csv_equals("top_products.csv", products)


def test_06():
    sales = prepared_sales()
    risk = (
        sales.groupby(["Category", "SalesChannel"])
        .agg(orders=("OrderID", "size"), gross_sales=("TotalAmount", "sum"), returned_amount=("ReturnedAmount", "sum"), return_rate=("IsReturned", "mean"))
        .reset_index()
    )
    risk = risk[risk["orders"] >= 50].sort_values("return_rate", ascending=False)
    priorities = risk.copy()
    priorities["segment"] = priorities["Category"] + " — " + priorities["SalesChannel"]
    assert_csv_equals("return_risk.csv", risk)
    assert_csv_equals("priority_segments.csv", priorities.nlargest(5, "returned_amount"))
