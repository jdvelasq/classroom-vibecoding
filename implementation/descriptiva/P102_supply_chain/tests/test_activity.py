"""Evalúa los productos descriptivos del caso Supply Chain."""

from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


OUT = Path("submission")
FILES = {"country_mode_summary.csv", "country_summary.csv", "freight_by_mode.csv", "mode_summary.csv", "monthly_summary.csv", "overall_kpis.csv", "priority_countries.csv", "priority_segments.csv"}


def prepared():
    s = pd.read_csv("data/supply_chain.csv")
    for col in ["Scheduled Delivery Date", "Delivered to Client Date"]:
        s[col] = pd.to_datetime(s[col], format="%d-%b-%y")
    s["days"] = (s["Delivered to Client Date"] - s["Scheduled Delivery Date"]).dt.days
    s["late"] = s["days"] > 0
    s["month"] = s["Delivered to Client Date"].dt.to_period("M").dt.to_timestamp()
    s["freight"] = pd.to_numeric(s["Freight Cost (USD)"], errors="coerce")
    return s


def test_01():
    assert {p.name for p in OUT.glob("*.csv")} == FILES


def test_02():
    s = prepared()
    kpi = pd.read_csv(OUT / "overall_kpis.csv").set_index("indicador")["valor"]
    assert kpi["envíos"] == len(s)
    assert kpi["valor_total_usd"] == s["Line Item Value"].sum()
    assert kpi["cumplimiento_a_tiempo"] == 1 - s["late"].mean()
    assert kpi["valor_enviado_tarde_usd"] == s.loc[s.late, "Line Item Value"].sum()


def test_03():
    s = prepared()
    mode = pd.read_csv(OUT / "mode_summary.csv")
    assert mode["envíos"].sum() == len(s)
    assert mode["valor_total_usd"].sum() == s["Line Item Value"].sum()
    assert mode["cumplimiento_a_tiempo"].between(0, 1).all()
    country = pd.read_csv(OUT / "country_summary.csv")
    assert (country["envíos"] >= 50).all()
    assert country["cumplimiento_a_tiempo"].between(0, 1).all()


def test_04():
    s = prepared()
    monthly = pd.read_csv(OUT / "monthly_summary.csv")
    assert monthly["envíos"].sum() == len(s)
    assert monthly["cumplimiento_a_tiempo"].between(0, 1).all()
    segments = pd.read_csv(OUT / "priority_segments.csv")
    assert (segments["envíos"] >= 30).all()
    assert segments["cumplimiento_a_tiempo"].between(0, 1).all()


def test_05():
    s = prepared()
    freight = pd.read_csv(OUT / "freight_by_mode.csv")
    assert freight["envíos"].sum() == len(s)
    assert freight["cobertura_valor_con_flete"].between(0, 1).all()
    expected = s.groupby("Shipment Mode", dropna=False)["freight"].sum().sort_index()
    actual = freight.set_index("Shipment Mode")["flete_numérico_usd"].sort_index()
    assert_series = pd.testing.assert_series_equal
    assert_series(actual, expected, check_names=False, check_dtype=False, rtol=1e-10)
