import csv
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_outcomes  # noqa: E402
import outcomes_lib as lib  # noqa: E402
import outcomes_status  # noqa: E402

INDEX = [
    # id, decision
    ("E0001", "accept"),
    ("E0002", "accept"),
    ("E0009", "reject"),
]

STATEMENT = ("Formular, para una decisión de una organización, un problema analítico "
             "con medidas de éxito justificadas ante los interesados.")


@pytest.fixture
def layout(tmp_path):
    layout = lib.Layout(tmp_path)
    layout.outcomes.mkdir(parents=True)
    layout.map.mkdir(parents=True)
    layout.index.parent.mkdir(parents=True)
    layout.format.write_text("# Formato\n\nVersión 0.1 (borrador)\n", encoding="utf-8")
    with layout.index.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "decision"])
        writer.writerows(INDEX)
    write_competency(layout, "C001", evidence="- Enunciado del problema analítico [E0001 p. 5].")
    write_competency(layout, "C002", evidence="- Ninguna fuente describe un producto evaluable.")
    write_competency(layout, "C003", estado="candidata", evidence="- Un producto [E0002 p. 1].")
    return layout


def write_competency(layout, cid, estado="incluida", evidence="", fecha="2026-10-13"):
    text = f"""---
id: "{cid}"
enunciado: "Hacer algo analítico, para una decisión."
subcampos: ["analítica descriptiva"]
estado: "{estado}"
fecha: "{fecha}"
---

# {cid}. Título

## Enunciado

Hacer algo analítico, para una decisión.

## Evidencia de desempeño

{evidence}

## Pendientes

- Buscar más evidencia.
"""
    (layout.map / f"{cid}.md").write_text(text, encoding="utf-8")


def write_outcome(layout, rid="RA01", competencies=("C001",), statement=STATEMENT, verb="formular",
                  parts=None, assessments=None, rows=None, nivel="especialización", fecha="2026-10-13"):
    parts = parts if parts is not None else [
        f"Verbo: {verb}.",
        "Objeto: un problema analítico con medidas de éxito.",
        "Condición: una decisión de una organización.",
        "Nivel: delimita el problema con autonomía.",
    ]
    cited = "; ".join(competencies)
    assessments = assessments if assessments is not None else [f"Documento de planteamiento [{cited}]."]
    rows = rows if rows is not None else [
        f"| {cid} | {'E0001 p. 5' if cid == 'C001' else 'Ninguna fuente'} | Un producto |" for cid in competencies
    ]
    competency_list = ", ".join(f'"{c}"' for c in competencies)
    text = f"""---
id: "{rid}"
enunciado: "{statement}"
competencias: [{competency_list}]
nivel: "{nivel}"
format_version: "0.1"
fecha: "{fecha}"
---

# {rid}. Título

## Enunciado

{statement}

## Partes del enunciado

{chr(10).join("- " + p for p in parts)}

## Competencias

{chr(10).join(f"- {c}: lo que toma." for c in competencies)}

## Evaluación

{chr(10).join("- " + a for a in assessments)}

## Trazabilidad

| Competencia | Evidencia | Producto evaluable |
|---|---|---|
{chr(10).join(rows)}
"""
    path = layout.outcomes / f"{rid}.md"
    path.write_text(text, encoding="utf-8")
    return path


def write_profile(layout, mentions=("RA01",), nivel="especialización"):
    text = f"""---
programa: "Posgrado en Analítica"
nivel: "{nivel}"
format_version: "0.1"
fecha: "2026-10-13"
---

# Perfil de egreso

## Perfil de egreso

La persona egresada apoya decisiones con productos analíticos.

## Desempeños

- Plantea problemas analíticos [{", ".join(mentions)}].

## Alcance

- Especialización.
"""
    layout.profile.write_text(text, encoding="utf-8")


def check(layout, rid="RA01"):
    outcome = lib.parse(layout.outcomes / f"{rid}.md")
    return lib.validate_outcome(outcome, lib.load_competencies(layout), lib.read_index(layout), "0.1")


@pytest.fixture
def small_program(monkeypatch):
    monkeypatch.setattr(lib, "MIN_OUTCOMES", 1)


def test_a_well_formed_outcome_validates(layout):
    write_outcome(layout)
    assert check(layout) == ([], [])


@pytest.mark.parametrize(
    "verb, statement, message",
    [
        ("comprender", "Comprender los problemas analíticos de una organización.", "not observable"),
        ("describir", "Describir los problemas analíticos de una organización.", "below postgraduate"),
        ("formulación", "Formulación de problemas analíticos de una organización.", "not an infinitive"),
        ("diseñar", STATEMENT, "not the first word"),
    ],
)
def test_the_verb_must_be_observable_and_postgraduate(layout, verb, statement, message):
    write_outcome(layout, verb=verb, statement=statement)
    errors, _ = check(layout)
    assert any(message in e for e in errors), errors


def test_the_statement_is_one_sentence(layout):
    write_outcome(layout, statement="Formular un problema analítico. Luego comunicarlo a los interesados.")
    errors, _ = check(layout)
    assert any("single sentence" in e for e in errors), errors


def test_all_four_parts_are_required_in_order(layout):
    write_outcome(layout, parts=["Verbo: formular.", "Objeto: un problema.", "Nivel: autonomía."])
    errors, _ = check(layout)
    assert any("Partes del enunciado" in e for e in errors), errors


def test_the_level_is_specialization(layout):
    write_outcome(layout, nivel="pregrado")
    errors, _ = check(layout)
    assert any("nivel must be" in e for e in errors), errors


@pytest.mark.parametrize(
    "competencies, message",
    [
        (("C003",), "'candidata'; only included competencies enter"),
        (("C099",), "not in the competency map"),
        (("C001", "C002", "C003", "C099"), "1 to 3 competencies"),
    ],
)
def test_only_included_competencies_in_bounded_number(layout, competencies, message):
    write_outcome(layout, competencies=competencies)
    errors, _ = check(layout)
    assert any(message in e for e in errors), errors


def test_assessment_cites_only_declared_competencies(layout):
    write_outcome(layout, assessments=["Documento [C002]."])
    errors, _ = check(layout)
    assert any("cites undeclared C002" in e for e in errors), errors


def test_assessment_needs_its_competencies(layout):
    write_outcome(layout, assessments=["Documento de planteamiento."])
    errors, _ = check(layout)
    assert any("final bracket" in e for e in errors), errors


@pytest.mark.parametrize(
    "rows, message",
    [
        ([], "C001 has no row in Trazabilidad"),
        (["| C001 | E0002 p. 1 | Un producto |"], "not in the Evidencia de desempeño of C001"),
        (["| C001 | E0009 p. 1 | Un producto |"], "not an accepted document"),
        (["| C001 | p. 5 | Un producto |"], "cites no evidence id"),
        (["| C001 | Ninguna fuente | Un producto |"], "cite it instead"),
        (["| C001 | E0001 p. 5 |  |"], "lacks the evaluable product"),
    ],
)
def test_traceability_reaches_the_performance_evidence(layout, rows, message):
    write_outcome(layout, rows=rows)
    errors, _ = check(layout)
    assert any(message in e for e in errors), errors


def test_competency_without_evidence_is_a_warning(layout):
    write_outcome(layout, competencies=("C001", "C002"))
    errors, warnings = check(layout)
    assert errors == []
    assert any("C002 has no performance evidence" in w for w in warnings)


def test_competency_changed_after_the_outcome_is_a_warning(layout):
    write_competency(layout, "C001", evidence="- Enunciado [E0001 p. 5].", fecha="2026-11-01")
    write_outcome(layout)
    errors, warnings = check(layout)
    assert errors == []
    assert any("C001 changed after" in w for w in warnings)


def test_full_program_passes(layout, small_program, capsys):
    write_outcome(layout, competencies=("C001", "C002"))
    write_profile(layout)
    assert check_outcomes.run(layout, []) == 0
    out = capsys.readouterr().out
    assert "coverage: C001 <- RA01" in out
    assert "C003" not in out.split("warning")[0]


def test_uncovered_included_competency_is_an_error(layout, small_program, capsys):
    write_outcome(layout)
    write_profile(layout)
    assert check_outcomes.run(layout, []) == 1
    out = capsys.readouterr().out
    assert "coverage: C002 <- none" in out
    assert "C002 is included in the map but no outcome covers it" in out


def test_the_number_of_outcomes_is_bounded(layout, capsys):
    write_outcome(layout, competencies=("C001", "C002"))
    write_profile(layout)
    assert check_outcomes.run(layout, []) == 1
    assert "it needs 6 to 10" in capsys.readouterr().out


@pytest.mark.parametrize(
    "mentions, message",
    [
        ((), "does not mention RA01"),
        (("RA01", "RA07"), "mentions RA07, which does not exist"),
    ],
)
def test_the_profile_mentions_every_outcome(layout, small_program, mentions, message):
    write_outcome(layout, competencies=("C001", "C002"))
    write_profile(layout, mentions=mentions)
    errors = lib.validate_set(layout, lib.load_outcomes(layout), lib.load_competencies(layout), "0.1")
    assert any(message in e for e in errors), errors


def test_missing_profile_is_an_error(layout, small_program):
    write_outcome(layout, competencies=("C001", "C002"))
    errors = lib.validate_set(layout, lib.load_outcomes(layout), lib.load_competencies(layout), "0.1")
    assert errors == ["profile.md is missing"]


def test_checking_some_ids_skips_the_set_rules(layout):
    write_outcome(layout)
    assert check_outcomes.run(layout, ["RA01"]) == 0


def test_scripts_refuse_another_format_version(layout):
    layout.format.write_text("# Formato\n\nVersión 0.2 (borrador)\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="Update outcomes_lib.py"):
        outcomes_status.status(layout)


def test_status_lists_what_must_be_covered(layout):
    write_outcome(layout)
    report = outcomes_status.status(layout)
    json.dumps(report, ensure_ascii=False)
    assert report["next_id"] == "RA02"
    assert report["uncovered"] == ["C002"]
    assert [c["id"] for c in report["included"]] == ["C001", "C002"]
    assert report["included"][0]["covered_by"] == ["RA01"]
    assert report["included"][0]["evidencia_de_desempeno"] == ["Enunciado del problema analítico [E0001 p. 5]."]
    assert report["included"][0]["pendientes"] == "- Buscar más evidencia."
    assert report["excluded"] == [{"id": "C003", "estado": "candidata", "enunciado": "Hacer algo analítico, para una decisión."}]
    assert report["profile_exists"] is False


def test_the_worked_example_of_format_md_validates_against_the_real_map(tmp_path):
    real = lib.Layout(lib.ROOT)
    examples = re.findall(r"^````markdown\n(.*?)^````$", real.format.read_text(encoding="utf-8"), re.M | re.S)
    assert examples, "format.md has no worked example"
    competencies = lib.load_competencies(real)
    index = lib.read_index(real)
    for example in examples:
        rid = re.search(r'^id: "(RA\d{2})"', example, re.M).group(1)
        path = tmp_path / f"{rid}.md"
        path.write_text(example, encoding="utf-8")
        errors, _ = lib.validate_outcome(lib.parse(path), competencies, index, lib.document_version(real.format))
        assert errors == [], errors
