"""Evalúa los productos agregados del diagnóstico salarial."""

import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]

import pandas as pd
from pandas.testing import assert_frame_equal


DATA = ACTIVITY_DIR / "data/salarios.csv"
OUT = ACTIVITY_DIR / "submission"
EXPECTED = {
    "analysis_conclusions.csv",
    "questions.json",
    "compensation_recommendations.csv",
    "department_pay_gap.csv",
    "high_salary_by_career.csv",
}


def salary_data():
    data = pd.read_csv(DATA)
    data["banda_experiencia"] = pd.cut(
        data["experiencia_tecnica_anios"],
        bins=[-1, 4, 9, 14, 100],
        labels=["0-4", "5-9", "10-14", "15+"],
    )
    peer_columns = ["categoria", "trayectoria", "banda_experiencia"]
    data["salario_mediano_pares_cop"] = data.groupby(
        peer_columns, observed=True
    )["salario_mensual_cop"].transform("median")
    data["brecha_vs_pares_pct"] = (
        data["salario_mensual_cop"] / data["salario_mediano_pares_cop"] - 1
    )
    return data


def test_01():
    assert {path.name for path in OUT.iterdir() if path.name != ".gitkeep"} == EXPECTED


def test_02():
    questions = json.loads((OUT / "questions.json").read_text(encoding="utf-8"))
    assert questions == [
        {
            "pregunta": (
                "¿En qué áreas debemos revisar los salarios porque los "
                "profesionales podrían ganar menos que pares comparables "
                "dentro de la empresa?"
            ),
            "archivo_respuesta": "department_pay_gap.csv",
        },
        {
            "pregunta": (
                "¿Un profesional técnico puede alcanzar los salarios más "
                "altos sin tener que convertirse en directivo?"
            ),
            "archivo_respuesta": "high_salary_by_career.csv",
        },
    ]


def test_03():
    data = salary_data()
    delivered = pd.read_csv(OUT / "department_pay_gap.csv")
    expected = (
        data.groupby(["gerencia", "departamento"], as_index=False)
        .agg(
            profesionales=("employee_id", "size"),
            salario_mediano_cop=("salario_mensual_cop", "median"),
            brecha_mediana_vs_pares_pct=("brecha_vs_pares_pct", "median"),
            proporcion_mas_de_5_pct_debajo=(
                "brecha_vs_pares_pct",
                lambda value: (value <= -0.05).mean(),
            ),
        )
        .query("profesionales >= 30")
        .sort_values("brecha_mediana_vs_pares_pct", ignore_index=True)
    )
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_04():
    data = salary_data()
    department_gap = (
        data.groupby(["gerencia", "departamento"], as_index=False)
        .agg(
            profesionales=("employee_id", "size"),
            brecha_mediana_vs_pares_pct=("brecha_vs_pares_pct", "median"),
            proporcion_mas_de_5_pct_debajo=(
                "brecha_vs_pares_pct",
                lambda value: (value <= -0.05).mean(),
            ),
        )
        .query("profesionales >= 30")
    )
    expected_departments = set(
        department_gap.query(
            "brecha_mediana_vs_pares_pct <= -0.05 and "
            "proporcion_mas_de_5_pct_debajo >= 0.50"
        )["departamento"]
    )
    delivered = pd.read_csv(OUT / "compensation_recommendations.csv")
    assert set(delivered["departamento"]) == expected_departments
    assert delivered["alternativa_1"].str.contains("banda salarial").all()
    assert delivered["alternativa_3"].str.contains("sin divulgar salarios").all()


def test_05():
    data = salary_data()
    threshold = data["salario_mensual_cop"].quantile(0.90)
    data["salario_alto"] = data["salario_mensual_cop"].ge(threshold)
    expected = (
        data.groupby("trayectoria", as_index=False)
        .agg(
            profesionales=("employee_id", "size"),
            salario_mediano_cop=("salario_mensual_cop", "median"),
            profesionales_con_salario_alto=("salario_alto", "sum"),
            proporcion_con_salario_alto=("salario_alto", "mean"),
        )
        .sort_values("trayectoria", ignore_index=True)
    )
    delivered = pd.read_csv(OUT / "high_salary_by_career.csv").sort_values(
        "trayectoria", ignore_index=True
    )
    assert_frame_equal(delivered, expected, check_dtype=False, rtol=1e-10)


def test_06():
    delivered = pd.read_csv(OUT / "analysis_conclusions.csv")
    assert list(delivered.columns) == ["pregunta", "respuesta", "límite"]
    assert len(delivered) == 2
    assert delivered["límite"].str.contains(
        "no identifica su causa|no prueba que.*cause", regex=True
    ).all()
    assert delivered["respuesta"].str.len().gt(30).all()
