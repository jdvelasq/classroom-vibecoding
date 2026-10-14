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

POSTGRADUATE = """---
curso: "demo"
nivel: "posgrado"
format_version: "0.5"
fecha: "2026-10-14"
---

# Analítica de prueba

## Propósito

Prueba.

## Identidad

- Pregunta: qué ocurre y para quién.
- Producto terminal: una explicación con evidencia.
- Disciplinas contribuyentes: estadística y visualización.
- Riesgo: confundirse con un curso de visualización.

## Conocimientos requeridos

- Python básico.

## Resultados de aprendizaje

- RA01, introduce: Plantea la pregunta.
- RA02, domina: Produce el producto completo.

## Resultados del curso

### RC01. Plantear la pregunta

- Enunciado: Formular la pregunta descriptiva del caso.
- Resultados de aprendizaje: RA01.
- Evaluación: Pregunta formulada [RA01].

### RC02. Producir la explicación

- Enunciado: Construir la explicación completa del caso.
- Resultados de aprendizaje: RA02.
- Evaluación: Explicación con evidencia [RA02].

## Alcance

- La predicción queda fuera.
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
    "metodologico": "Un ranking supone exposición igual.",
    "tecnico": "Cuenta semanas por conductor con groupby.",
    "pedagogico": "El estudiante comprueba antes de concluir.",
    "identidad": "Refuerza la pregunta descriptiva, no agrega técnica.",
    "aceptacion": "Un highlight nuevo con la tabla de semanas.",
    "instrucciones": "Inspecciona professor/notebook.ipynb y agrega la verificación.",
}

COURSE_TASK = {
    "clave": "n1",
    "tipo": "actividad nueva",
    "titulo": "Domina el producto descriptivo completo",
    "contribucion": "Un producto completo evaluado.",
    "posicion": "Después de P100.",
    "desplaza": "Ninguna; ocupa la sesión de cierre.",
    "efecto": "Un grupo lento no la ve y conserva lo demás.",
    "metodologico": "El producto completo se evalúa entero.",
    "tecnico": "Integra lo construido en P100.",
    "pedagogico": "Cierra la secuencia con autonomía.",
    "identidad": "Termina en una explicación descriptiva, no en una herramienta.",
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
    (tmp_path / "04-curriculum" / "postgraduate").mkdir()
    (tmp_path / "04-curriculum" / "postgraduate" / "demo.md").write_text(POSTGRADUATE, encoding="utf-8")
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
            {"id": "demo/RC01", "categoria": "cubierta", "anclas": [{"hito": "P100:H01", "nivel": "introduce"}]},
            {"id": "demo/RC02", "categoria": "actividad nueva", "propuesta": "n1",
             "anclas": [{"hito": "P100:H02", "nivel": "introduce"}]},
            {"id": "C001.CON01", "categoria": "cubierta", "anclas": [{"hito": "P100:H01", "nivel": "introduce"}]},
            {"id": "C001.CON02", "categoria": "mejora", "actividad": "P100", "propuesta": "t1"},
            {"id": "C001.HAB01", "categoria": "marginal", "razon": "Ya agrega por conductor.", "actividad": "P100"},
            {"id": "C002.CON01", "categoria": "fuera de alcance", "razon": "Corresponde al producto completo."},
            {"id": "C002.HAB01", "categoria": "actividad nueva", "propuesta": "n1"},
        ],
        "actividades": [
            {
                "actividad": "P100",
                "decision": "puntual",
                "resultados": ["demo/RC01"],
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


def anchor(hito, nivel="introduce"):
    return {"hito": hito, "nivel": nivel}


def test_targets_are_course_outcomes_with_the_level_the_course_owes(layout):
    reqs = audit_lib.requirements(layout, COURSE)
    assert [(t.id, t.level, t.program_outcomes) for t in reqs.targets] == [
        ("demo/RC01", "introduce", ("RA01",)), ("demo/RC02", "domina", ("RA02",))]
    assert [i.id for i in reqs.items] == ["C001.CON01", "C001.CON02", "C001.HAB01", "C002.CON01", "C002.HAB01"]
    assert reqs.items[0].text == "Granularidad de los datos."
    assert reqs.identity["Riesgo"] == "confundirse con un curso de visualización."
    assert reqs.required_knowledge == ["Python básico."]


def test_status_reports_identity_targets_and_activities(layout):
    report = audit_status.status(layout, COURSE)
    assert report["level"] == "posgrado"
    assert report["blocked"] == []
    assert report["identity"]["Producto terminal"] == "una explicación con evidencia."
    assert report["targets"][1]["nivel"] == "domina"
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
    (lambda a: a["senales"][0].update(anclas=[anchor("P100:H07")]), "H07 is not a highlight of P100"),
    (lambda a: a["senales"][0].update(anclas=[anchor("P999:H01")]), "is not Pxxx:HNN of an activity"),
    (lambda a: a["senales"][0].update(anclas=["P100:H01"]), "needs a nivel"),
    (lambda a: a["senales"][1].update(categoria="cubierta"), "the course owes it at 'domina'"),
    (lambda a: a["senales"][4].pop("razon"), "needs a razon"),
    (lambda a: a["actividades"][0].update(decision="igual"), "decision 'igual' takes no proposal"),
    (lambda a: a["actividades"][0]["propuestas"].append(dict(TASK, clave="t2")), "one bounded change"),
    (lambda a: a["actividades"][0].update(resultados=["RA01"]), "RA01 is not a course outcome"),
    (lambda a: a["actividades"][0].update(competencias=["C002"]), "C002 is not a competency of its resultados"),
    (lambda a: a["actividades"][0].update(competencias=["demo.C02"]), "'demo.C02' is not a competency id"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(anclas=["H09"]), "ancla H09 is not a highlight or surface"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(limite=""), "limite is empty"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(pedagogico=""), "pedagogico is empty"),
    (lambda a: a["nuevas"][0].update(desplaza=""), "desplaza is empty"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(instrucciones="Añade una celda Markdown."),
     "instrucciones mentions markdown"),
    (lambda a: a["nuevas"][0].update(aceptacion="Un notebook con markdown."), "aceptacion mentions markdown"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(aceptacion="Una prueba que lo recalcule desde data/."),
     "aceptacion asks to recompute"),
    (lambda a: a["actividades"][0]["propuestas"][0].update(instrucciones="Añade una prueba con assert_frame_equal."),
     "instrucciones asks to recompute"),
    (lambda a: a["nuevas"][0].update(identidad=""), "identidad is empty"),
    (lambda a: a["actividades"].clear(), "P100 has no decision"),
    (lambda a: a["senales"][3].update(categoria="marginal", razon="x"), "no signal or highlight motivates"),
    (lambda a: a["nuevas"][0].update(tipo="otra"), "tipo must be one of"),
    (lambda a: a["senales"][1].pop("anclas"), "P100 H02 serves no signal"),
])
def test_audit_errors(layout, change, message):
    errors, _ = check(layout, mutate(change))
    assert any(message in e for e in errors), errors


def test_a_notebook_step_may_recompute_but_a_test_may_not(layout):
    def notebook(audit):
        audit["actividades"][0]["propuestas"][0]["instrucciones"] = (
            "Recalcula el resumen en el notebook. Añade una prueba que verifique que el archivo existe.")
    assert check(layout, mutate(notebook))[0] == []


def test_markdown_may_only_be_discarded_as_an_alternative(layout):
    def discard(audit):
        audit["actividades"][0]["propuestas"][0]["alternativas"] = "Declararlo en markdown no deja evidencia."
    assert check(layout, mutate(discard))[0] == []


def test_a_highlight_outside_the_course_is_kept_or_trimmed(layout):
    def keep(audit):
        audit["senales"][1].pop("anclas")
        audit["actividades"][0]["fuera"] = [{"hito": "H02", "accion": "conservar", "razon": "Sostiene el resumen."}]
    assert check(layout, mutate(keep))[0] == []

    def trim_without_proposal(audit):
        keep(audit)
        audit["actividades"][0]["fuera"][0].update(accion="recortar")
    errors, _ = check(layout, mutate(trim_without_proposal))
    assert any("recortar needs a propuesta" in e for e in errors)

    def trim(audit):
        trim_without_proposal(audit)
        audit["actividades"][0]["fuera"][0]["propuesta"] = "t1"
    assert check(layout, mutate(trim))[0] == []

    def both(audit):
        audit["actividades"][0]["fuera"] = [{"hito": "H02", "accion": "conservar", "razon": "x"}]
    errors, _ = check(layout, mutate(both))
    assert any("anchored by a signal and listed in fuera" in e for e in errors)


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
        audit["senales"][0] = {"id": "demo/RC01", "categoria": "actividad nueva", "propuesta": "n1",
                               "anclas": [anchor("P100:H01")]}
        audit["senales"][2] = {"id": "C001.CON01", "categoria": "actividad nueva", "propuesta": "n1"}
    errors, _ = check(layout, mutate(to_course))
    assert errors == []


def test_an_undescribed_activity_blocks_the_audit(layout):
    layout.activity(COURSE, FOLDER).unlink()
    errors, _ = check(layout, good_audit())
    assert any("describe the activity first" in e for e in errors)
    assert audit_status.status(layout, COURSE)["blocked"][0]["actividad"] == "P100"


def test_a_course_without_its_course_file_asks_for_the_curriculum(layout):
    (layout.root / "04-curriculum" / "postgraduate" / "demo.md").unlink()
    with pytest.raises(SystemExit, match="run mapping-curriculum first"):
        audit_lib.requirements(layout, COURSE)


def test_a_course_outcome_from_an_unassigned_outcome_is_refused(layout):
    (layout.root / "04-curriculum" / "matrix.csv").write_text(
        "ra,curso,nivel,aporte,fecha\nRA01,demo,introduce,Plantea.,2026-10-14\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="RA02, which the matrix does not assign"):
        audit_lib.requirements(layout, COURSE)


def write_all(edits):
    for target, text in edits.texts.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")


def test_apply_writes_proposals_log_traceability_and_coverage(layout):
    layout.log(COURSE, FOLDER).unlink()
    path = save(layout.root, good_audit())
    write_all(apply_audit.plan(layout, path))

    tasks = layout.tasks(COURSE, FOLDER).read_text(encoding="utf-8")
    assert tasks.startswith("# P100 — Propuestas de mejora\n\n**Línea base:** `activity.md`.")
    assert "## T01 — Verificar la exposición antes del ranking" in tasks
    assert "Auditoría `AUD.P100.01` (Claude, 2026-10-14) del curso `demo`: señales C001.CON02." in tasks
    assert "- **Límite de la actividad:** Agrega una celda y una tabla." in tasks
    assert "- **Justificación pedagógica:** El estudiante comprueba antes de concluir." in tasks
    assert "- **Identidad del curso:** Refuerza la pregunta descriptiva" in tasks

    course_tasks = layout.course_tasks(COURSE).read_text(encoding="utf-8")
    assert layout.course_tasks(COURSE) == layout.implementation(COURSE) / "tasks.md"
    assert "## N01 — ⚠️ PENDIENTE DE DECISIÓN — Domina el producto descriptivo completo" in course_tasks
    assert "Auditoría del curso `demo` (Claude, 2026-10-14): señales demo/RC02, C002.HAB01." in course_tasks
    assert "- **Desplaza o fusiona:** Ninguna; ocupa la sesión de cierre." in course_tasks

    log = layout.log(COURSE, FOLDER).read_text(encoding="utf-8")
    assert log.startswith("# Log — P100\n\n## AUD.P100.01")
    assert audit_lib.fingerprint(path) in log
    assert "- **Resultado:** propone T01." in log
    assert "demo/RC01 (cubierta: H01 introduce)" in log
    assert "C001.HAB01 (marginal: Ya agrega por conductor.)" in log

    trace = lib.parse_traceability(layout.traceability(COURSE))
    assert trace.version == "0.1"
    assert trace.entries["P100"] == {"resultados": ["demo/RC01"], "competencias": ["C001"],
                                     "decision": "puntual", "auditoria": "AUD.P100.01"}
    assert trace.entries["L101"] == ["demo.C01"]

    coverage = layout.audit(COURSE).read_text(encoding="utf-8")
    assert "| C001.CON02 | Exposición y normalización. | mejora | P100: T01 |" in coverage
    assert "| demo/RC02 | Construir la explicación completa del caso. (nivel: domina) | actividad nueva | N01; parcial en P100:H02 (introduce) |" in coverage
    assert "| P100 | puntual | demo/RC01 | C001 | T01 |" in coverage

    with pytest.raises(SystemExit, match="already applied"):
        apply_audit.plan(layout, path)


def test_new_ids_skip_those_used_in_tasks_and_log(layout):
    tasks = layout.tasks(COURSE, FOLDER)
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
    layout.tasks(COURSE, FOLDER).write_text(
        "# P100\n\n" + "".join(f"## T0{n} — Algo\n\n- **Estado:** aprobada\n\n" for n in (1, 2, 3)),
        encoding="utf-8")
    _, warnings = check(layout, good_audit())
    assert any("4 open proposals" in w for w in warnings)


def test_an_undergraduate_course_audits_borrowed_activities_in_their_owner(layout):
    audit = {
        "curso": "data",
        "executor": "Claude",
        "fecha": "2026-10-14",
        "senales": [
            {"id": "data/RC01", "categoria": "cubierta", "anclas": [anchor("demo/P100:H01")]},
            {"id": "C001.CON01", "categoria": "cubierta", "anclas": [anchor("demo/P100:H01")]},
            {"id": "C001.CON02", "categoria": "mejora", "actividad": "demo/P100", "propuesta": "t1"},
            {"id": "C001.HAB01", "categoria": "cubierta", "anclas": [anchor("demo/P100:H02")]},
        ],
        "actividades": [{
            "actividad": "demo/P100", "decision": "puntual", "resultados": ["data/RC01"],
            "competencias": ["C001"], "razon": "Sirve a RC01.", "propuestas": [copy.deepcopy(TASK)],
        }],
    }
    errors, _ = check(layout, audit)
    assert errors == []
    edits = apply_audit.plan(layout, save(layout.root, audit))
    assert "del curso `data`" in edits.texts[layout.tasks(COURSE, FOLDER)]
    assert "resultados: [data/RC01]" in edits.texts[layout.traceability("data")]


def test_traceability_never_mixes_legacy_capabilities_and_competencies(layout):
    layout.traceability(COURSE).write_text(
        'format_version: "0.1"\nP100:\n  resultados: [demo/RC01]\n  competencias: [demo.C02]\n  decision: igual\n'
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


def test_a_reaudit_marks_a_pending_proposal_obsolete_without_removing_it(layout):
    tasks = layout.tasks(COURSE, FOLDER)
    tasks.write_text("# P100 — Propuestas de mejora\n\n## T01 — Algo viejo\n\n"
                     "- **Estado:** pendiente de discusión\n- **Anclas actuales:** H01, H07.\n", encoding="utf-8")
    assert audit_status.status(layout, COURSE)["activities"][0]["proposals"][0]["missing_anchors"] == ["H07"]
    _, warnings = check(layout, good_audit())
    assert any("T01: its anchors H07 no longer exist" in w for w in warnings)

    def obsolete(audit):
        audit["actividades"][0]["obsoletas"] = [{"propuesta": "T01", "razon": "H07 ya no existe."}]
    audit = mutate(obsolete)
    errors, warnings = check(layout, audit)
    assert errors == [] and not any("no longer exist" in w for w in warnings)
    edits = apply_audit.plan(layout, save(layout.root, audit))
    text = edits.texts[tasks]
    assert "## T01 — Algo viejo\n\n- **Estado:** obsoleta según `AUD.P100.01` (Claude, 2026-10-14): H07 ya no existe." in text
    assert "## T02 — Verificar" in text
    assert "marca obsoleta T01" in edits.texts[layout.log(COURSE, FOLDER)]


def test_an_obsolete_mark_needs_an_open_proposal_and_a_reason(layout):
    def bad(audit):
        audit["actividades"][0]["obsoletas"] = [{"propuesta": "T05", "razon": ""}]
    errors, _ = check(layout, mutate(bad))
    assert any("obsoletas cites 'T05'" in e for e in errors)
