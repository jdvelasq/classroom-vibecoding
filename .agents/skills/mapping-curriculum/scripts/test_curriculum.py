import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_curriculum  # noqa: E402
import curriculum_lib as lib  # noqa: E402
import curriculum_status  # noqa: E402

DOMAIN = """# Dominio

Versión 0.7 (borrador)

## Subcampos

- Analítica descriptiva.
- Analítica prescriptiva.
- Ingeniería de datos para la analítica.

## Tendencia emergente: IA generativa y agéntica en la analítica

Transversal.
"""

COURSE_ROWS = [
    "| descriptiva | Analítica descriptiva | posgrado | vigente | analítica descriptiva |",
    "| prescriptiva | Analítica prescriptiva | posgrado | vigente | analítica prescriptiva |",
    "| generativa | IA generativa | posgrado | propuesto | IA generativa y agéntica (transversal) |",
    "| data | Fundamentos de data | pregrado | vigente | ingeniería de datos para la analítica |",
]


@pytest.fixture
def layout(tmp_path):
    layout = lib.Layout(tmp_path)
    for folder in (layout.home, layout.undergraduate, layout.outcomes, layout.map, layout.domain.parent):
        folder.mkdir(parents=True, exist_ok=True)
    layout.format.write_text("# Formato\n\nVersión 0.3 (borrador)\n", encoding="utf-8")
    layout.domain.write_text(DOMAIN, encoding="utf-8")
    write_courses(layout)
    write_competency(layout, "C001", ["analítica descriptiva", "analítica prescriptiva", "ingeniería de datos para la analítica"])
    write_competency(layout, "C002", ["analítica prescriptiva"])
    write_competency(layout, "C003", ["IA generativa y agéntica (transversal)"])
    write_competency(layout, "C004", ["ingeniería de datos para la analítica"], estado="candidata")
    write_outcome(layout, "RA01", ["C001"])
    write_outcome(layout, "RA02", ["C002", "C003"])
    return layout


def write_courses(layout, rows=COURSE_ROWS, purposes=None, version="0.3"):
    folders = purposes if purposes is not None else [r.split("|")[1].strip() for r in rows]
    text = f"""---
format_version: "{version}"
domain_version: "0.7"
fecha: "2026-10-14"
---

# Cursos

## Lista de cursos

| Carpeta | Curso | Nivel | Estado | Subcampos |
|---|---|---|---|---|
{chr(10).join(rows)}

## Propósito

{chr(10).join(f"### {f}{chr(10)}{chr(10)}Propósito de {f}.{chr(10)}" for f in folders)}
## Continuidad

- Autocontenidos.
"""
    layout.courses.write_text(text, encoding="utf-8")


def write_competency(layout, cid, subfields, estado="incluida", fecha="2026-10-13"):
    listed = ", ".join(f'"{s}"' for s in subfields)
    text = f"""---
id: "{cid}"
enunciado: "Hacer algo analítico, para una decisión."
subcampos: [{listed}]
estado: "{estado}"
fecha: "{fecha}"
---

# {cid}. Título

## Enunciado

Hacer algo analítico, para una decisión.
"""
    (layout.map / f"{cid}.md").write_text(text, encoding="utf-8")


def write_outcome(layout, rid, competencies, fecha="2026-10-13"):
    listed = ", ".join(f'"{c}"' for c in competencies)
    text = f"""---
id: "{rid}"
enunciado: "Formular algo analítico."
competencias: [{listed}]
nivel: "especialización"
format_version: "0.1"
fecha: "{fecha}"
---

# {rid}. Título
"""
    (layout.outcomes / f"{rid}.md").write_text(text, encoding="utf-8")


GOOD_MATRIX = [
    "RA01,descriptiva,introduce,Plantea la pregunta descriptiva.,2026-10-14",
    "RA01,prescriptiva,domina,Formula el problema completo.,2026-10-14",
    "RA02,prescriptiva,domina,Diseña la política.,2026-10-14",
    "RA02,generativa,desarrolla,Usa un agente para ejecutar la política.,2026-10-14",
]


def write_matrix(layout, rows=GOOD_MATRIX, columns="ra,curso,nivel,aporte,fecha"):
    layout.matrix.write_text(columns + "\n" + "\n".join(rows) + "\n", encoding="utf-8")


GOOD_OUTCOMES = [
    ("RC01", "Obtener datos de dos fuentes para una pregunta dada.", "C001", "Consultas y datos [C001]."),
    ("RC02", "Describir la calidad de un conjunto de datos.", "C001", "Reporte de calidad [C001]."),
    ("RC03", "Construir un flujo reproducible de datos.", "C001", "Flujo ejecutable [C001]."),
]


def write_undergraduate(layout, outcomes=GOOD_OUTCOMES, curso="data", body_extra="", nivel="pregrado"):
    blocks = "\n".join(
        f"### {rid}. Título\n\n- Enunciado: {statement}\n- Competencias: {cids}.\n- Evaluación: {assessment}\n"
        for rid, statement, cids, assessment in outcomes
    )
    text = f"""---
curso: "{curso}"
nivel: "{nivel}"
format_version: "0.3"
fecha: "2026-10-14"
---

# Fundamentos de data

## Propósito

Presentar la ingeniería de datos para la analítica.{body_extra}

## Resultados del curso

{blocks}
## Alcance

- Fuera: administración de bases de datos.
"""
    path = layout.undergraduate / f"{curso}.md"
    path.write_text(text, encoding="utf-8")
    return path


def write_postgraduate(layout, curso, outcomes, entry="- Programación básica en Python.", nivel="posgrado"):
    bullets = "\n".join(f"- {ra}, {level}: Aporte del curso." for ra, level in outcomes)
    text = f"""---
curso: "{curso}"
nivel: "{nivel}"
format_version: "0.3"
fecha: "2026-10-14"
---

# Curso {curso}

## Propósito

Responder una pregunta analítica con un producto terminal.

## Conocimientos requeridos

{entry}

## Resultados de aprendizaje

{bullets}

## Alcance

- Fronteras con los demás cursos.
"""
    path = layout.postgraduate / f"{curso}.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


GOOD_POSTGRADUATE = {
    "descriptiva": [("RA01", "introduce")],
    "prescriptiva": [("RA01", "domina"), ("RA02", "domina")],
    "generativa": [("RA02", "desarrolla")],
}


def write_all_postgraduate(layout):
    for curso, outcomes in GOOD_POSTGRADUATE.items():
        write_postgraduate(layout, curso, outcomes)


def postgraduate_errors(layout, curso):
    rows, _ = lib.read_matrix(layout)
    _, courses = lib.load_courses(layout)
    return lib.validate_postgraduate(lib.parse(layout.postgraduate / f"{curso}.md"), courses, rows, "0.3")


def courses_errors(layout):
    document, courses = lib.load_courses(layout)
    return lib.validate_courses(document, courses, lib.course_subfields(layout), "0.3")


def matrix_check(layout):
    rows, errors = lib.read_matrix(layout)
    assert errors == []
    _, courses = lib.load_courses(layout)
    return lib.validate_matrix(rows, courses, lib.load_outcomes(layout), lib.load_competencies(layout))


def undergraduate_check(layout, curso="data"):
    _, courses = lib.load_courses(layout)
    document = lib.parse(layout.undergraduate / f"{curso}.md")
    return lib.validate_undergraduate(document, courses, lib.load_competencies(layout), "0.3")


# courses.md

def test_well_formed_courses_validate(layout):
    assert courses_errors(layout) == []


def test_the_emerging_trend_counts_as_a_subfield_that_needs_a_course(layout):
    assert "IA generativa y agéntica (transversal)" in lib.course_subfields(layout)


@pytest.mark.parametrize(
    "rows, message",
    [
        (COURSE_ROWS[:1] + COURSE_ROWS[2:], "no course teaches the subfield 'analítica prescriptiva'"),
        (COURSE_ROWS + ["| x | X | posgrado | vigente | estadística |"], "'estadística', which is not a subfield"),
        (COURSE_ROWS + ["| x | X | doctorado | vigente | analítica descriptiva |"], "level 'doctorado'"),
        (COURSE_ROWS + ["| x | X | posgrado | soñado | analítica descriptiva |"], "status 'soñado'"),
        (COURSE_ROWS + [COURSE_ROWS[0]], "'descriptiva' appears more than once"),
        (COURSE_ROWS + ["| Big Data | X | posgrado | vigente | analítica descriptiva |"], "lowercase letters"),
        (COURSE_ROWS[3:] + ["| y | Y | pregrado | vigente | analítica descriptiva; analítica prescriptiva; IA generativa y agéntica (transversal) |"],
         "there is no postgraduate course"),
    ],
)
def test_course_list_rules(layout, rows, message):
    write_courses(layout, rows=rows)
    errors = courses_errors(layout)
    assert any(message in e for e in errors), errors


def test_every_course_has_a_purpose(layout):
    write_courses(layout, purposes=["descriptiva", "prescriptiva", "data"])
    assert any("'### generativa'" in e for e in courses_errors(layout))


def test_the_real_courses_md_validates():
    real = lib.Layout(lib.ROOT)
    assert courses_errors(real) == []


# matrix.csv

def test_a_good_matrix_validates(layout):
    write_matrix(layout)
    assert matrix_check(layout) == ([], [])


def test_every_outcome_reaches_mastery(layout):
    write_matrix(layout, rows=[GOOD_MATRIX[0], GOOD_MATRIX[2], GOOD_MATRIX[3]])
    errors, _ = matrix_check(layout)
    assert any("RA01 never reaches 'domina'" in e for e in errors), errors


def test_no_postgraduate_course_is_left_without_outcomes(layout):
    write_matrix(layout, rows=GOOD_MATRIX[:3])
    errors, _ = matrix_check(layout)
    assert "generativa has no learning outcome in the matrix" in errors


def test_a_first_appearance_as_develop_breaks_self_containment(layout):
    rows = ["RA01,descriptiva,desarrolla,Formula.,2026-10-14"] + GOOD_MATRIX[1:]
    write_matrix(layout, rows=rows)
    errors, _ = matrix_check(layout)
    assert any("first appears in descriptiva as 'desarrolla'" in e for e in errors), errors


def test_mastering_at_first_appearance_is_allowed(layout):
    rows = ["RA01,descriptiva,domina,Formula.,2026-10-14"] + GOOD_MATRIX[2:]
    write_matrix(layout, rows=rows)
    assert matrix_check(layout)[0] == []


def test_introducing_after_mastery_is_a_warning(layout):
    rows = GOOD_MATRIX + ["RA01,generativa,introduce,Lo retoma con un asistente.,2026-10-14"]
    write_matrix(layout, rows=rows)
    errors, warnings = matrix_check(layout)
    assert errors == []
    assert any("RA01 is mastered before generativa" in w for w in warnings), warnings


@pytest.mark.parametrize(
    "row, message",
    [
        ("RA09,descriptiva,introduce,Algo.,2026-10-14", "RA09 is not a learning outcome"),
        ("RA01,data,introduce,Algo.,2026-10-14", "data is a pregrado course; the matrix only takes postgraduate courses"),
        ("RA01,big-data,introduce,Algo.,2026-10-14", "big-data is not a course in courses.md"),
        ("RA02,descriptiva,domina,,2026-10-14", "aporte is empty"),
        ("RA02,descriptiva,experto,Algo.,2026-10-14", "nivel 'experto'"),
        ("RA02,descriptiva,introduce,Algo.,14/10/2026", "must be YYYY-MM-DD"),
        ("RA01,descriptiva,introduce,Otra vez.,2026-10-14", "RA01 × descriptiva appears more than once"),
    ],
)
def test_matrix_row_rules(layout, row, message):
    write_matrix(layout, rows=GOOD_MATRIX + [row])
    errors, _ = matrix_check(layout)
    assert any(message in e for e in errors), errors


def test_a_course_outside_the_outcome_subfields_is_a_warning(layout):
    write_matrix(layout, rows=GOOD_MATRIX + ["RA01,generativa,desarrolla,Usa un asistente.,2026-10-14"])
    errors, warnings = matrix_check(layout)
    assert errors == []
    assert any("generativa shares no subfield with the competencies of RA01" in w for w in warnings), warnings


def test_an_outcome_changed_after_its_row_is_a_warning(layout):
    write_outcome(layout, "RA01", ["C001"], fecha="2026-11-01")
    write_matrix(layout)
    errors, warnings = matrix_check(layout)
    assert errors == []
    assert any("RA01 changed after this row was set" in w for w in warnings), warnings


def test_the_matrix_columns_are_fixed(layout):
    write_matrix(layout, columns="ra,course,level,aporte,fecha")
    _, errors = lib.read_matrix(layout)
    assert errors == ["matrix.csv: columns must be ra,curso,nivel,aporte,fecha"]


def test_the_matrix_view_shows_every_outcome_by_course(layout):
    write_matrix(layout)
    rows, _ = lib.read_matrix(layout)
    _, courses = lib.load_courses(layout)
    view = lib.matrix_view(rows, courses, lib.load_outcomes(layout))
    assert view[0].split() == ["ra", "descriptiva", "prescriptiva", "generativa"]
    assert view[1].split() == ["RA01", "introduce", "domina", "·"]


# undergraduate/<folder>.md

def test_a_good_undergraduate_course_validates(layout):
    write_undergraduate(layout)
    assert undergraduate_check(layout) == ([], [])


def test_introductory_verbs_are_allowed_but_not_unobservable_ones(layout):
    outcomes = GOOD_OUTCOMES[:2] + [("RC03", "Comprender los flujos de datos.", "C001", "Examen [C001].")]
    write_undergraduate(layout, outcomes=outcomes)
    errors, _ = undergraduate_check(layout)
    assert errors == ["undergraduate/data.md: data/RC03: verb 'comprender' is not observable"]


@pytest.mark.parametrize(
    "outcomes, message",
    [
        (GOOD_OUTCOMES[:2], "it needs 3 to 6"),
        ([GOOD_OUTCOMES[0], GOOD_OUTCOMES[2], ("RC02",) + GOOD_OUTCOMES[1][1:]], "must be RC01, RC02, RC03, in order"),
        (GOOD_OUTCOMES[:2] + [("RC03", "Construir un flujo.", "C004", "Flujo [C004].")], "C004 is 'candidata'"),
        (GOOD_OUTCOMES[:2] + [("RC03", "Construir un flujo.", "C099", "Flujo [C099].")], "C099 is not in the competency map"),
        (GOOD_OUTCOMES[:2] + [("RC03", "Construir un flujo.", "C001", "Flujo ejecutable.")], "lacks its competencies"),
        (GOOD_OUTCOMES[:2] + [("RC03", "Construir un flujo.", "C001", "Flujo [C002].")], "cites undeclared C002"),
        (GOOD_OUTCOMES[:2] + [("RC03", "Construir un flujo. Luego otro.", "C001", "Flujo [C001].")], "single sentence"),
        (GOOD_OUTCOMES[:2] + [("RC03", "Flujos reproducibles de datos.", "C001", "Flujo [C001].")], "not an infinitive"),
    ],
)
def test_undergraduate_outcome_rules(layout, outcomes, message):
    write_undergraduate(layout, outcomes=outcomes)
    errors, _ = undergraduate_check(layout)
    assert any(message in e for e in errors), errors


def test_every_subfield_of_the_course_is_covered(layout):
    outcomes = [(rid, s, "C002", a.replace("C001", "C002")) for rid, s, _, a in GOOD_OUTCOMES]
    write_undergraduate(layout, outcomes=outcomes)
    errors, _ = undergraduate_check(layout)
    assert any("no course outcome covers the subfield 'ingeniería de datos para la analítica'" in e for e in errors), errors


def test_undergraduate_courses_do_not_cite_program_outcomes(layout):
    write_undergraduate(layout, body_extra=" Prepara para RA01.")
    errors, _ = undergraduate_check(layout)
    assert any("does not cite the program's learning outcomes" in e for e in errors), errors


def test_a_postgraduate_course_cannot_have_an_undergraduate_file(layout):
    write_undergraduate(layout, curso="descriptiva")
    errors, _ = undergraduate_check(layout, curso="descriptiva")
    assert errors == ["undergraduate/descriptiva.md: curso 'descriptiva' is not an undergraduate course in courses.md"]


def test_a_competency_changed_after_the_course_is_a_warning(layout):
    write_competency(layout, "C001", ["ingeniería de datos para la analítica"], fecha="2026-11-01")
    write_undergraduate(layout)
    errors, warnings = undergraduate_check(layout)
    assert errors == []
    assert any("C001 changed after data/RC01" in w for w in warnings), warnings


# postgraduate/<folder>.md

def test_good_postgraduate_files_validate(layout):
    write_matrix(layout)
    write_all_postgraduate(layout)
    for curso in GOOD_POSTGRADUATE:
        assert postgraduate_errors(layout, curso) == []


@pytest.mark.parametrize(
    "outcomes, message",
    [
        ([("RA01", "domina")], "matrix.csv puts RA02 in prescriptiva as 'domina', but the file does not list it"),
        ([("RA01", "domina"), ("RA02", "domina"), ("RA03", "introduce")], "RA03 is listed but matrix.csv has no row"),
        ([("RA01", "desarrolla"), ("RA02", "domina")], "RA01 is 'desarrolla' here but 'domina' in matrix.csv"),
        ([("RA02", "domina"), ("RA01", "domina")], "must be in id order"),
    ],
)
def test_postgraduate_outcomes_match_the_matrix(layout, outcomes, message):
    write_matrix(layout)
    write_postgraduate(layout, "prescriptiva", outcomes)
    errors = postgraduate_errors(layout, "prescriptiva")
    assert any(message in e for e in errors), errors


def test_a_postgraduate_course_does_not_presuppose_an_undergraduate_one(layout):
    write_matrix(layout)
    write_postgraduate(layout, "prescriptiva", GOOD_POSTGRADUATE["prescriptiva"], entry="- Lo visto en el curso `data`.")
    errors = postgraduate_errors(layout, "prescriptiva")
    assert any("does not cite the undergraduate course data" in e for e in errors), errors


@pytest.mark.parametrize(
    "entry, message",
    [
        ("Ninguno.", "must list, one bullet each"),
        ("- Lo visto en el curso `descriptiva`.", "presupposes knowledge, not courses; it cites descriptiva"),
        ("- Lo visto en Analítica descriptiva.", "presupposes knowledge, not courses; it cites descriptiva"),
    ],
)
def test_required_knowledge_is_knowledge_not_courses(layout, entry, message):
    write_matrix(layout)
    write_postgraduate(layout, "prescriptiva", GOOD_POSTGRADUATE["prescriptiva"], entry=entry)
    errors = postgraduate_errors(layout, "prescriptiva")
    assert any(message in e for e in errors), errors


def test_an_undergraduate_course_cannot_have_a_postgraduate_file(layout):
    write_matrix(layout)
    write_postgraduate(layout, "data", [])
    assert postgraduate_errors(layout, "data") == [
        "postgraduate/data.md: curso 'data' is not a postgraduate course in courses.md"
    ]


def test_a_malformed_outcome_bullet_is_an_error(layout):
    write_matrix(layout)
    path = write_postgraduate(layout, "descriptiva", GOOD_POSTGRADUATE["descriptiva"])
    path.write_text(path.read_text(encoding="utf-8").replace("- RA01, introduce:", "- RA01 introduce"), encoding="utf-8")
    errors = postgraduate_errors(layout, "descriptiva")
    assert any("must read '- RA00, nivel: aporte.'" in e for e in errors), errors


# The whole run and the status report

def test_a_matrix_without_postgraduate_files_does_not_pass(layout, capsys):
    write_matrix(layout)
    write_undergraduate(layout)
    assert check_curriculum.run(layout) == 1
    out = capsys.readouterr().out
    for curso in GOOD_POSTGRADUATE:
        assert f"postgraduate/{curso}.md is missing" in out


def test_full_curriculum_passes(layout, capsys):
    write_matrix(layout)
    write_all_postgraduate(layout)
    write_undergraduate(layout)
    assert check_curriculum.run(layout) == 0
    assert "0 errors" in capsys.readouterr().out


def test_missing_parts_are_errors(layout, capsys):
    assert check_curriculum.run(layout) == 1
    out = capsys.readouterr().out
    assert "matrix.csv is missing" in out
    assert "undergraduate/data.md is missing" in out


def test_undergraduate_part_can_be_checked_before_any_outcome_exists(layout, capsys):
    for path in layout.outcomes.glob("*.md"):
        path.unlink()
    write_undergraduate(layout)
    assert check_curriculum.run(layout, matrix=False) == 0
    assert check_curriculum.run(layout, undergrad=False) == 1
    assert "no learning outcomes yet" in capsys.readouterr().out


def test_status_says_the_postgraduate_part_waits_for_the_learning_outcomes(layout):
    for path in layout.outcomes.glob("*.md"):
        path.unlink()
    report = curriculum_status.status(layout)
    assert report["pending"][:2] == [
        "03-learning-outcomes has no learning outcomes: run writing-learning-outcomes first", "matrix.csv",
    ]


def test_scripts_refuse_another_format_version(layout):
    layout.format.write_text("# Formato\n\nVersión 0.1 (borrador)\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="Update curriculum_lib.py"):
        curriculum_status.status(layout)


def test_status_lists_what_must_be_mapped(layout):
    write_matrix(layout, rows=GOOD_MATRIX[:1])
    report = curriculum_status.status(layout)
    json.dumps(report, ensure_ascii=False)
    assert report["pending"] == [
        "postgraduate/descriptiva.md", "postgraduate/prescriptiva.md", "postgraduate/generativa.md", "undergraduate/data.md",
    ]
    assert report["postgraduate_order"] == ["descriptiva", "prescriptiva", "generativa"]
    assert report["not_mastered"] == ["RA01", "RA02"]
    assert report["courses_without_outcomes"] == ["prescriptiva", "generativa"]
    assert report["outcomes"][0]["cells"] == {"descriptiva": "introduce"}
    assert report["outcomes"][1]["subfields"] == ["IA generativa y agéntica (transversal)", "analítica prescriptiva"]
    assert [c["id"] for c in report["included_competencies"]] == ["C001", "C002", "C003"]
    assert report["undergraduate"] == [{"folder": "data", "file_exists": False, "outcomes": []}]


# The worked example of format.md

def test_the_worked_examples_of_format_md_validate_against_the_real_repository(tmp_path):
    real = lib.Layout(lib.ROOT)
    text = real.format.read_text(encoding="utf-8")
    _, courses = lib.load_courses(real)

    matrix = re.search(r"^```csv\n(.*?)^```$", text, re.M | re.S).group(1)
    sample = lib.Layout(tmp_path)
    sample.home.mkdir()
    sample.matrix.write_text(matrix, encoding="utf-8")
    rows, errors = lib.read_matrix(sample)
    assert errors == [] and rows
    graduate = {c.folder for c in lib.postgraduate(courses)}
    assert all(r.curso in graduate and r.nivel in lib.LEVELS and r.aporte for r in rows)

    graduate_example, undergraduate_example = re.findall(r"^````markdown\n(.*?)^````$", text, re.M | re.S)
    path = tmp_path / "prescriptiva.md"
    path.write_text(graduate_example, encoding="utf-8")
    assert lib.validate_postgraduate(lib.parse(path), courses, rows, "0.3") == []
    path = tmp_path / "data.md"
    path.write_text(undergraduate_example, encoding="utf-8")
    errors, _ = lib.validate_undergraduate(lib.parse(path), courses, lib.load_competencies(real), "0.3")
    assert errors == []
