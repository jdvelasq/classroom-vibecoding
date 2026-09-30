"""Evalúa los productos descriptivos del caso Vuelos."""

from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


OUT = Path("submission")
METRICS = ["scheduled_flights", "cancelled_flights", "operated_flights", "delayed_departure_15_flights", "positive_departure_delay_minutes"]


def rates(frame):
    result = frame.copy()
    result["cancellation_rate"] = result["cancelled_flights"] / result["scheduled_flights"]
    result["delay_rate"] = result["delayed_departure_15_flights"] / result["operated_flights"]
    result["mean_positive_delay_minutes"] = result["positive_departure_delay_minutes"] / result["operated_flights"]
    return result


def source():
    return (
        pd.read_csv("data/flights_by_carrier_day_hour.csv.gz"),
        pd.read_csv("data/flights_by_carrier_month.csv.gz"),
    )


def same(name, expected):
    assert_frame_equal(pd.read_csv(OUT / name), expected.reset_index(drop=True), check_dtype=False, rtol=1e-10)


def test_01():
    assert {p.name for p in OUT.glob("*.csv")} == {"carrier_summary.csv", "day_hour_delay.csv", "monthly_national_kpis.csv", "overall_kpis.csv", "priority_segments.csv", "seasonality.csv"}


def test_02():
    day_hour, monthly = source()
    recomputed = day_hour.groupby(["year", "month", "reporting_airline"])[METRICS].sum().reset_index().sort_values(["year", "month", "reporting_airline"]).reset_index(drop=True)
    provided = monthly.sort_values(["year", "month", "reporting_airline"]).reset_index(drop=True)
    assert_frame_equal(recomputed, provided, check_dtype=False)
    same("overall_kpis.csv", rates(monthly[METRICS].sum().to_frame().T))


def test_03():
    _, monthly = source()
    expected = rates(monthly.groupby(["year", "month"])[METRICS].sum().reset_index())
    expected["period"] = pd.to_datetime(dict(year=expected.year, month=expected.month, day=1)).astype(str)
    same("monthly_national_kpis.csv", expected)
    same("carrier_summary.csv", rates(monthly.groupby("reporting_airline")[METRICS].sum().reset_index()).sort_values("delay_rate", ascending=False))


def test_04():
    day_hour, _ = source()
    expected = rates(day_hour.groupby(["day_of_week", "scheduled_departure_hour"])[METRICS].sum().reset_index())
    same("day_hour_delay.csv", expected)


def test_05():
    day_hour, _ = source()
    names = {1:"Lunes",2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sábado",7:"Domingo"}
    critical = rates(day_hour.groupby(["reporting_airline", "day_of_week", "scheduled_departure_hour"])[METRICS].sum().reset_index())
    critical = critical[critical.operated_flights >= 25_000]
    critical["segment"] = critical.reporting_airline + " — " + critical.day_of_week.map(names) + " — " + critical.scheduled_departure_hour.map(lambda hour: f"{hour:02d}:00")
    same("priority_segments.csv", critical.nlargest(10, "delay_rate"))


def test_06():
    _, monthly = source()
    top = rates(monthly.groupby("reporting_airline")[METRICS].sum().reset_index()).nlargest(5, "operated_flights")["reporting_airline"]
    expected = rates(monthly.groupby(["month", "reporting_airline"])[METRICS].sum().reset_index())
    same("seasonality.csv", expected[expected.reporting_airline.isin(top)])
