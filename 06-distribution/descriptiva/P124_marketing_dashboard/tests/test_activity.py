"""Evalúa los productos analíticos persistentes del tablero de marketing."""

from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]

import pandas as pd
from pandas.testing import assert_frame_equal


DATA = ACTIVITY_DIR / "data/campaign_data.csv"
OUT = ACTIVITY_DIR / "submission"
EXPECTED = {
    "campaign_summary.csv",
    "daily_summary.csv",
    "kpis.csv",
    "questions.json",
    "source_summary.csv",
}


def source_data():
    data = pd.read_csv(DATA, parse_dates=["utc_date"])
    data["gross_profit"] = data["revenue"] - data["ad_spend"]
    return data


def test_01():
    assert {path.name for path in OUT.iterdir() if path.name != ".gitkeep"} == EXPECTED


def test_02():
    data = source_data()
    delivered = pd.read_csv(OUT / "kpis.csv")
    expected = pd.DataFrame(
        [
            {
                "impressions": data["impressions"].sum(),
                "paid_clicks": data["paid_clicks"].sum(),
                "revenue": data["revenue"].sum(),
                "ad_spend": data["ad_spend"].sum(),
                "gross_profit": data["gross_profit"].sum(),
                "roas": data["revenue"].sum() / data["ad_spend"].sum(),
                "cpc": data["ad_spend"].sum() / data["paid_clicks"].sum(),
            }
        ]
    )
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_03():
    data = source_data()
    delivered = pd.read_csv(OUT / "daily_summary.csv", parse_dates=["utc_date"])
    expected = (
        data.groupby("utc_date", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            ad_spend=("ad_spend", "sum"),
            gross_profit=("gross_profit", "sum"),
        )
        .sort_values("utc_date", ignore_index=True)
    )
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_04():
    data = source_data()
    delivered = pd.read_csv(OUT / "source_summary.csv")
    expected = (
        data.groupby("traffic_source", as_index=False)
        .agg(
            impressions=("impressions", "sum"),
            paid_clicks=("paid_clicks", "sum"),
            revenue=("revenue", "sum"),
            ad_spend=("ad_spend", "sum"),
            gross_profit=("gross_profit", "sum"),
        )
        .sort_values("gross_profit", ascending=False, ignore_index=True)
    )
    expected["roas"] = expected["revenue"] / expected["ad_spend"]
    expected["cpc"] = expected["ad_spend"] / expected["paid_clicks"]
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_05():
    data = source_data()
    delivered = pd.read_csv(OUT / "campaign_summary.csv")
    expected = (
        data.groupby("template_name", as_index=False)
        .agg(
            impressions=("impressions", "sum"),
            paid_clicks=("paid_clicks", "sum"),
            revenue=("revenue", "sum"),
            ad_spend=("ad_spend", "sum"),
            gross_profit=("gross_profit", "sum"),
        )
        .sort_values("gross_profit", ascending=False, ignore_index=True)
    )
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)
