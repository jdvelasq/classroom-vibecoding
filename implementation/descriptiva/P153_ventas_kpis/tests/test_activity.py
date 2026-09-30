"""Evalúa los KPI de ventas y su decisión analítica de publicación."""

import json
from pathlib import Path
import sqlite3

import pandas as pd
from pandas.testing import assert_frame_equal


MART = Path("data/sales_mart.db")
OUT = Path("submission")
EXPECTED = {
    "kpi_catalog.csv",
    "kpi_publication_decision.csv",
    "kpi_quality_report.csv",
    "metric_lineage.csv",
    "questions.json",
}


def mart_tables():
    with sqlite3.connect(MART) as connection:
        return (
            pd.read_sql_query("SELECT * FROM fact_sales", connection),
            pd.read_sql_query("SELECT * FROM dim_date", connection),
        )


def test_01():
    assert {path.name for path in OUT.iterdir() if path.name != ".gitkeep"} == EXPECTED
    catalog = pd.read_csv(OUT / "kpi_catalog.csv")
    assert list(catalog.columns) == [
        "kpi",
        "numerador_o_formula",
        "denominador",
        "grano",
        "período",
        "propietario",
        "fuente",
    ]
    assert set(catalog["kpi"]) == {
        "Ventas netas",
        "Unidades vendidas",
        "Descuento promedio ponderado",
    }
    assert catalog[["grano", "período", "propietario", "fuente"]].notna().all().all()


def test_02():
    fact_sales, dim_date = mart_tables()
    expected = pd.DataFrame(
        [
            ["Llave de hecho única", not fact_sales[["order_id", "line_id"]].duplicated().any()],
            ["Ventas netas no negativas", fact_sales["net_sales"].ge(0).all()],
            ["Cantidades positivas", fact_sales["quantity"].gt(0).all()],
            ["Fechas del hecho presentes", fact_sales["date_key"].isin(dim_date["date_key"]).all()],
        ],
        columns=["regla", "pasa"],
    )
    expected["estado"] = expected["pasa"].map({True: "PASS", False: "FAIL"})
    delivered = pd.read_csv(OUT / "kpi_quality_report.csv")
    delivered["pasa"] = delivered["pasa"].astype(bool)
    assert_frame_equal(delivered, expected, check_dtype=False)


def test_03():
    catalog = pd.read_csv(OUT / "kpi_catalog.csv")
    lineage = pd.read_csv(OUT / "metric_lineage.csv")
    assert set(lineage["kpi"]) == set(catalog["kpi"])
    assert lineage["campo_origen"].str.startswith("fact_sales.").all()
    assert lineage["transformación"].str.len().gt(8).all()


def test_04():
    quality = pd.read_csv(OUT / "kpi_quality_report.csv")
    decision = pd.read_csv(OUT / "kpi_publication_decision.csv")
    expected_status = "APROBADO" if quality["pasa"].all() else "BLOQUEADO"
    assert list(decision.columns) == ["decisión", "estado", "razón"]
    assert decision.loc[0, "estado"] == expected_status
    assert decision.loc[0, "decisión"] == "Publicar catálogo de KPI"


def test_05():
    expected = [
        {
            "pregunta": "¿Podemos publicar estos KPI para la gerencia sin ocultar problemas de calidad o definición?",
            "archivo_respuesta": "kpi_publication_decision.csv",
        }
    ]
    assert json.loads((OUT / "questions.json").read_text(encoding="utf-8")) == expected
