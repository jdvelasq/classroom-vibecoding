import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pending  # noqa: E402
import review_lib as lib  # noqa: E402

COURSE = "demo"
FOLDER = "P100_demo"

ACTIVITY_TASKS = """# P100 — Propuestas de mejora

**Línea base:** `activity.md`.

## T01 — Verificar la exposición

- **Estado:** pendiente de discusión
- **Tipo:** método

### Instrucciones de ejecución

Añade una tabla de semanas.

## T02 — Rotular el gráfico

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
"""

COURSE_TASKS = """# demo — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Producto completo

- **Tipo:** actividad nueva
- **Contribución distinta:** cierra el curso.
"""


@pytest.fixture
def layout(tmp_path):
    layout = lib.Layout(tmp_path)
    folder = layout.implementation(COURSE) / FOLDER
    folder.mkdir(parents=True)
    (layout.implementation(COURSE) / "P101_otro").mkdir()
    layout.tasks(COURSE, FOLDER).write_text(ACTIVITY_TASKS, encoding="utf-8")
    layout.course_tasks(COURSE).write_text(COURSE_TASKS, encoding="utf-8")
    return layout


def apply(changes):
    for path, text in changes.items():
        if text is None:
            path.unlink()
        else:
            path.write_text(text, encoding="utf-8")


def decide(layout, scope, task, decision="rechazada", reason="No cabe en la sesión."):
    apply(lib.decide(layout, COURSE, scope, task, decision, reason, "Claude", "2026-10-14"))


def test_pending_shows_one_proposal_of_one_activity_at_a_time(layout):
    report = pending.pending(layout, f"{COURSE}/P100")
    assert report["open"] == 2
    assert report["next"]["scope"] == "P100"
    assert report["next"]["id"] == "T01"
    assert report["next"]["text"].startswith("## T01 — Verificar la exposición")
    assert "Rotular" not in report["next"]["text"]
    assert [(q["scope"], q["id"]) for q in report["queue"]] == [("P100", "T02")]


def test_the_course_proposals_are_reviewed_apart(layout):
    report = pending.pending(layout, COURSE)
    assert report["open"] == 1
    assert report["next"]["id"] == "N01"
    assert pending.pending(layout, f"{COURSE}/P101")["next"] is None


@pytest.mark.parametrize("target, message", [
    (f"{COURSE}/P999", "neither an activity"),
    (f"{COURSE}/otro", "must be <curso>/<Pxxx>"),
])
def test_an_unknown_target_is_refused(layout, target, message):
    with pytest.raises(SystemExit, match=message):
        pending.pending(layout, target)


def test_a_rejection_leaves_tasks_and_enters_the_log(layout):
    decide(layout, "P100", "T01")
    tasks = layout.tasks(COURSE, FOLDER).read_text(encoding="utf-8")
    assert "T01" not in tasks
    assert tasks.startswith("# P100 — Propuestas de mejora\n\n**Línea base:** `activity.md`.\n\n## T02")
    log = layout.log(COURSE, FOLDER).read_text(encoding="utf-8")
    assert log.startswith("# Log — P100\n\n## DEC.P100.01\n")
    assert "- **Decisión:** rechazada." in log
    assert "- **Razón:** No cabe en la sesión." in log
    assert "- **Implementación:**" not in log
    assert "#### T01 — Verificar la exposición" in log
    assert "#### Instrucciones de ejecución" in log


def test_an_approval_is_logged_with_its_implementation_pending(layout):
    decide(layout, "P100", "T01")
    decide(layout, "P100", "T02", decision="aprobada", reason="Mejora la lectura.")
    log = layout.log(COURSE, FOLDER).read_text(encoding="utf-8")
    assert "## DEC.P100.02" in log
    assert "- **Implementación:** pendiente." in log
    assert not layout.tasks(COURSE, FOLDER).exists()


def test_a_course_proposal_goes_to_the_course_log(layout):
    decide(layout, COURSE, "N01")
    assert not layout.course_tasks(COURSE).exists()
    log = layout.course_log(COURSE).read_text(encoding="utf-8")
    assert log.startswith("# Log — demo\n\n## DEC.demo.01\n")
    assert "#### N01 — ⚠️ PENDIENTE DE DECISIÓN — Producto completo" in log


def test_decided_ids_are_never_reused_by_an_audit(layout):
    import audit_lib

    decide(layout, COURSE, "N01")
    assert audit_lib.used_course_task_numbers(layout, COURSE) == {1}
    assert audit_lib.course_decisions(layout, COURSE) == ["DEC.demo.01"]


@pytest.mark.parametrize("scope, task, decision, reason, message", [
    ("P100", "T09", "rechazada", "x", "has no open proposal T09"),
    ("P100", "T01", "quizás", "x", "decision must be one of"),
    ("P100", "T01", "aprobada", " ", "needs its reason"),
])
def test_invalid_decisions_are_refused(layout, scope, task, decision, reason, message):
    with pytest.raises(SystemExit, match=message):
        lib.decide(layout, COURSE, scope, task, decision, reason, "Claude", "2026-10-14")
