import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import activity_lib as lib  # noqa: E402
import apply_audit  # noqa: E402
import audit_lib  # noqa: E402
import audit_status  # noqa: E402
import check_audit  # noqa: E402
import courses_status  # noqa: E402
from test_describing import COURSE, FOLDER, make_activity_layout  # noqa: E402

COURSES = """---
format_version: "0.1"
domain_version: "0.7"
fecha: "2026-10-14"
---

# Cursos

## Lista de cursos

| Carpeta | Curso | Nivel | Estado | Subcampos |
|---|---|---|---|---|
| demo | Analítica de prueba | posgrado | vigente | analítica descriptiva |
| data | Fundamentos de data | pregrado | vigente | ingeniería de datos para la analítica |
| big-data | Grandes datos | posgrado | vigente | analítica de grandes datos |

## Propósito

### demo

Prueba.

## Continuidad

- Autocontenidos.
"""

UNDERGRADUATE = """---
curso: "data"
nivel: "pregrado"
format_version: "0.1"
fecha: "2026-10-14"
---

# Fundamentos de data

## Propósito

Prueba.

## Resultados del curso

### RC01. Obtener datos

- Enunciado: Obtener datos de dos fuentes.
- Competencias: C001.
- Evaluación: Datos integrados [C001].

## Alcance

- Nada más.
"""

TASK = {
    "clave": "t1",
    "titulo": "Verificar la exposición antes del ranking",
    "tipo": "método",
    "que_gana": "Comprueba un supuesto antes de rankear.",
    "anclas": ["H01", "S02"],
    "alternativas": "Declararlo no basta.",
    "no_regresion": "Se conservan H01 y H02.",
    "limite": "Agrega una celda y una tabla.",
    "interacciones": "Ninguna.",
    "aceptacion": "Un highlight nuevo con la tabla de semanas.",
    "instrucciones": "Inspecciona professor/notebook.ipynb y agrega la verificación.",
}

COURSE_TASK = {
    "clave": "n1",
    "tipo": "actividad nueva",
    "titulo": "Domina el producto descriptivo completo",
    "contribucion": "Un producto completo evaluado.",
    "posicion": "Después de P100.",
    "efecto": "No desplaza actividades.",
    "caso": "Requiere definición.",
    "producto": "Explicación descriptiva con límites.",
    "aceptacion": "Notebook, pruebas y entrada de trazabilidad.",
}


def write_competency(root, cid, knowledge, skills):
    text = f"""---
id: "{cid}"
enunciado: "Hacer algo analítico, para una decisión."
subcampos: ["analítica descriptiva"]
estado: "incluida"
fecha: "2026-10-13"
---

# {cid}. Título

## Enunciado

Hacer algo.

## Conocimientos

{chr(10).join(f"- {k} [E0001 p. 5]." for k in knowledge)}

## Habilidades

{chr(10).join(f"- {s} [E0002 §3]." for s in skills)}
"""
    (root / "02-competencies" / "map" / f"{cid}.md").write_text(text, encoding="utf-8")


def write_outcome(root, rid, competencies):
    listed = ", ".join(f'"{c}"' for c in competencies)
    text = f"""---
id: "{rid}"
enunciado: "Formular algo analítico."
competencias: [{listed}]
fecha: "2026-10-13"
---

# {rid}. Título
"""
    (root / "03-learning-outcomes" / "outcomes" / f"{rid}.md").write_text(text, encoding="utf-8")


@pytest.fixture
def layout(tmp_path):
    layout = make_activity_layout(tmp_path)
    for folder in ("02-competencies/map", "03-learning-outcomes/outcomes", "04-curriculum/undergraduate"):
        (tmp_path / folder).mkdir(parents=True)
    (tmp_path / "04-curriculum" / "courses.md").write_text(COURSES, encoding="utf-8")
    (tmp_path / "04-curriculum" / "matrix.csv").write_text(
        "ra,curso,nivel,aporte,fecha\n"
        "RA01,demo,introduce,Plantea la pregunta.,2026-10-14\n"
        "RA02,demo,domina,Produce el producto completo.,2026-10-14\n",
        encoding="utf-8",
    )
    (tmp_path / "04-curriculum" / "undergraduate" / "data.md").write_text(UNDERGRADUATE, encoding="utf-8")
    write_competency(tmp_path, "C001", ["Granularidad de los datos", "Exposición y normalización"], ["Agregar datos"])
    write_competency(tmp_path, "C002", ["Comunicación de límites"], ["Presentar a interesados"])
    write_outcome(tmp_path, "RA01", ["C001"])
    write_outcome(tmp_path, "RA02", ["C002"])
    layout.implementation("data").mkdir()
    layout.traceability("data").write_text("demo/P100:\n  - data.C02\n", encoding="utf-8")
    return layout


def good_audit():
    return {
        "curso": COURSE,
        "executor": "Claude",
        "fecha": "2026-10-14",
        "senales": [
            {"id": "RA01", "categoria": "cubierta", "anclas": ["P100:H01"]},
            {"id": "RA02", "categoria": "actividad nueva", "propuesta": "n1"},
            {"id": "C001.CON01", "categoria": "cubierta", "anclas": ["P100:H01"]},
            {"id": "C001.CON02", "categoria": "mejora", "actividad": "P100", "propuesta": "t1"},
            {"id": "C001.HAB01", "categoria": "marginal", "razon": "Ya agrega por conductor.", "actividad": "P100"},
            {"id": "C002.CON01", "categoria": "fuera de alcance", "razon": "Corresponde al producto completo."},
            {"id": "C002.HAB01", "categoria": "actividad nueva", "propuesta": "n1"},
        ],
        "actividades": [
            {
                "actividad": "P100",
                "decision": "puntual",
                "resultados": ["RA01"],
                "competencias": ["C001"],
                "razon": "Refuerza la agregación con una verificación corta.",
                "propuestas": [copy.deepcopy(TASK)],
            }
        ],
        "nuevas": [copy.deepcopy(COURSE_TASK)],
    }


def save(tmp_path, audit, name="audit.json"):
    path = tmp_path / name
    path.write_text(json.dumps(audit, ensure_ascii=False), encoding="utf-8")
    return path


def check(layout, audit):
    return check_audit.check(layout, save(layout.root, audit))


def test_items_have_stable_ids_without_sources(layout):
    reqs = audit_lib.requirements(layout, COURSE)
    assert [t.id for t in reqs.targets] == ["RA01", "RA02"]
    assert [i.id for i in reqs.items] == ["C001.CON01", "C001.CON02", "C001.HAB01", "C002.CON01", "C002.HAB01"]
    assert reqs.items[0].text == "Granularidad de los datos."


def test_status_reports_targets_items_and_activities(layout):
    report = audit_status.status(layout, COURSE)
    assert report["level"] == "posgrado"
    assert report["blocked"] == []
    assert report["activities"][0]["highlights"][0].startswith("H01 — ")
    assert report["activities"][0]["traceability"] == ["demo.C02"]


def test_a_good_audit_passes(layout):
    errors, warnings = check(layout, good_audit())
    assert errors == []
    assert any("legacy entries" in w for w in warnings)


def mutate(change):
    audit = good_audit()
    change(audit)
    return audit


@pytest.mark.parametrize("change, message", [
    (lambda a: a["senales"].pop(), "C002.HAB01 has no category"),
    (lambda a: a["senales"].append({"id": "C009.CON01", "categoria": "marginal", "razon": "x"}), "C009.CON01"),
    (lambda a: a["senales"][0].update(anclas=["P100:H07"]), "H07 is not a highlight of P100"),
    (lambda a: a["senales"][0].update(anclas=["P999:H01"]), "is not Pxxx:HNN of an activity"),
    (lambda a: a["senales"][4].pop("razon"), "needs a razon"),
    (lambda a: a["actividades"][0].update(decision="igual"), "decision 'igual' takes no proposal"),
    (lambda a: a["actividades"][0]["propuestas"].append(dict(TASK, clave="t2")), "one bounded change"),
    (lambda a: a["actividades"][0].update(competencias=["C002"]), "C002 is not a competency of its resultados"),
    (lambda a: a["actividades"][0].update(competencias=["demo.C02"]), "'demo.C02' is not a competency id"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(anclas=["H09"]), "ancla H09 is not a highlight or surface"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(limite=""), "limite is empty"),
    (lambda a: a["actividades"].clear(), "P100 has no decision"),
    (lambda a: a["senales"][3].update(categoria="marginal", razon="x"), "no signal motivates this proposal"),
    (lambda a: a["nuevas"][0].update(tipo="otra"), "tipo must be one of"),
])
def test_audit_errors(layout, change, message):
    errors, _ = check(layout, mutate(change))
    assert any(message in e for e in errors), errors


def test_an_activity_without_outcomes_goes_to_the_course(layout):
    def change(audit):
        audit["senales"][3] = {"id": "C001.CON02", "categoria": "actividad nueva", "propuesta": "n1"}
        audit["actividades"][0] = {"actividad": "P100", "decision": "igual", "resultados": [], "competencias": [],
                                   "razon": "No sirve a ningún resultado."}
    errors, _ = check(layout, mutate(change))
    assert any("only admits decision 'curso'" in e for e in errors)

    def to_course(audit):
        change(audit)
        audit["actividades"][0].update(decision="curso", curso="n1")
        audit["senales"][0] = {"id": "RA01", "categoria": "actividad nueva", "propuesta": "n1"}
        audit["senales"][2] = {"id": "C001.CON01", "categoria": "actividad nueva", "propuesta": "n1"}
    errors, _ = check(layout, mutate(to_course))
    assert errors == []


def test_an_undescribed_activity_blocks_the_audit(layout):
    layout.activity(COURSE, FOLDER).unlink()
    errors, _ = check(layout, good_audit())
    assert any("describe the activity first" in e for e in errors)
    assert audit_status.status(layout, COURSE)["blocked"][0]["actividad"] == "P100"


def test_a_course_without_matrix_rows_asks_for_the_curriculum(layout):
    (layout.root / "04-curriculum" / "matrix.csv").write_text("ra,curso,nivel,aporte,fecha\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="run mapping-curriculum first"):
        audit_lib.requirements(layout, COURSE)


def test_apply_writes_proposals_log_traceability_and_coverage(layout):
    path = save(layout.root, good_audit())
    edits = apply_audit.plan(layout, path)
    for target, text in edits.texts.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    tasks = layout.tasks(COURSE, "P100").read_text(encoding="utf-8")
    assert tasks.startswith("# P100 — Propuestas de mejora\n\n**Línea base:** `activity.md` (entrada S02 más reciente: `S02.P100.01`).")
    assert "## T01 — Verificar la exposición antes del ranking" in tasks
    assert "Auditoría `AUD.P100.01` (Claude, 2026-10-14) del curso `demo`: señales C001.CON02." in tasks
    assert "- **Límite de la actividad:** Agrega una celda y una tabla." in tasks

    course_tasks = layout.course_tasks(COURSE).read_text(encoding="utf-8")
    assert "## N01 — ⚠️ PENDIENTE DE DECISIÓN — Domina el producto descriptivo completo" in course_tasks
    assert "Auditoría del curso `demo` (Claude, 2026-10-14): señales RA02, C002.HAB01." in course_tasks

    log = layout.log(COURSE, FOLDER).read_text(encoding="utf-8")
    assert "## AUD.P100.01" in log
    assert audit_lib.fingerprint(path) in log
    assert "- **Resultado:** propone T01." in log
    assert "C001.HAB01 (marginal: Ya agrega por conductor.)" in log

    trace = lib.parse_traceability(layout.traceability(COURSE))
    assert trace.version == "0.1"
    assert trace.entries["P100"] == {"resultados": ["RA01"], "competencias": ["C001"],
                                     "decision": "puntual", "auditoria": "AUD.P100.01"}
    assert trace.entries["L101"] == ["demo.C01"]

    coverage = layout.audit(COURSE).read_text(encoding="utf-8")
    assert "| C001.CON02 | Exposición y normalización. | mejora | P100: T01 |" in coverage
    assert "| P100 | puntual | RA01 | C001 | T01 |" in coverage

    with pytest.raises(SystemExit, match="already applied"):
        apply_audit.plan(layout, path)


def test_new_ids_skip_those_used_in_tasks_and_log(layout):
    tasks = layout.tasks(COURSE, "P100")
    tasks.parent.mkdir(parents=True)
    tasks.write_text("# P100 — Propuestas de mejora\n\n## T01 — Algo\n\n- **Estado:** pendiente de discusión\n"
                     "- **Fuentes:** un benchmark.\n- **Tipo:** método\n", encoding="utf-8")
    log = layout.log(COURSE, FOLDER)
    log.write_text(log.read_text(encoding="utf-8") + "\n## DEC.P100.01\n\n- Rechazada T03.\n", encoding="utf-8")
    layout.course_tasks(COURSE).write_text("# demo — Actividades nuevas por decidir\n\n## N01 — ⚠️ PENDIENTE DE DECISIÓN — Otra\n\n"
                                           "- **Fuentes:**\n  - Un benchmark.\n- **Contribución distinta:** x\n", encoding="utf-8")

    def reinforce(audit):
        audit["actividades"][0]["refuerza"] = ["T01"]
        audit["refuerza"] = ["N01"]
    edits = apply_audit.plan(layout, save(layout.root, mutate(reinforce)))
    tasks_text = edits.texts[tasks]
    assert "## T04 — Verificar" in tasks_text
    assert "- **Fuentes:** un benchmark.\n  - Auditoría `AUD.P100.01`" in tasks_text
    course_text = edits.texts[layout.course_tasks(COURSE)]
    assert "## N02 — ⚠️" in course_text
    assert "  - Un benchmark.\n  - Auditoría del curso `demo` (Claude, 2026-10-14): refuerza con la cobertura del curso." in course_text


def test_too_many_open_proposals_is_a_warning(layout):
    tasks = layout.tasks(COURSE, "P100")
    tasks.parent.mkdir(parents=True)
    tasks.write_text("# P100\n\n" + "".join(f"## T0{n} — Algo\n\n- **Estado:** aprobada\n\n" for n in (1, 2, 3)),
                     encoding="utf-8")
    _, warnings = check(layout, good_audit())
    assert any("4 open proposals" in w for w in warnings)


def test_an_undergraduate_course_audits_borrowed_activities_in_their_owner(layout):
    audit = {
        "curso": "data",
        "executor": "Claude",
        "fecha": "2026-10-14",
        "senales": [
            {"id": "data/RC01", "categoria": "cubierta", "anclas": ["demo/P100:H01"]},
            {"id": "C001.CON01", "categoria": "cubierta", "anclas": ["demo/P100:H01"]},
            {"id": "C001.CON02", "categoria": "mejora", "actividad": "demo/P100", "propuesta": "t1"},
            {"id": "C001.HAB01", "categoria": "cubierta", "anclas": ["demo/P100:H02"]},
        ],
        "actividades": [{
            "actividad": "demo/P100", "decision": "puntual", "resultados": ["data/RC01"],
            "competencias": ["C001"], "razon": "Sirve a RC01.", "propuestas": [copy.deepcopy(TASK)],
        }],
    }
    errors, _ = check(layout, audit)
    assert errors == []
    edits = apply_audit.plan(layout, save(layout.root, audit))
    assert "del curso `data`" in edits.texts[layout.tasks(COURSE, "P100")]
    trace = lib.render_traceability(lib.parse_traceability(layout.traceability("data")))
    assert "demo/P100" in trace
    assert "resultados: [data/RC01]" in edits.texts[layout.traceability("data")]


def test_traceability_never_mixes_legacy_capabilities_and_competencies(layout):
    layout.traceability(COURSE).write_text(
        'format_version: "0.1"\nP100:\n  resultados: [RA01]\n  competencias: [demo.C02]\n  decision: igual\n'
        "  auditoria: AUD.P100.01\nL101:\n  - C001\n",
        encoding="utf-8",
    )
    errors, _ = audit_lib.validate_traceability(layout, COURSE)
    assert any("'demo.C02' among competencias" in e for e in errors)
    assert any("lists C001 as a legacy capability" in e for e in errors)


def test_courses_status_summarizes_without_auditing(layout):
    report = courses_status.status(layout)
    by_course = {c["course"]: c for c in report["courses"]}
    assert by_course["demo"]["must_cover"] == {"targets": 2, "items": 5}
    assert by_course["demo"]["to_describe"] == []
    assert by_course["data"]["activities"] == 1
    assert by_course["big-data"]["implementation"] is False
