import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import activity_lib as lib  # noqa: E402
import check_activities  # noqa: E402
import inventory  # noqa: E402

COURSE = "demo"

HIGHLIGHTS = """- **H01 — Reconcilia dos granularidades (caso y datos):** agrega por conductor antes de unir.
- **H02 — Persiste un resumen verificado:** la prueba lo recalcula.
"""

EVIDENCE_ROWS = """| H01 — Granularidades | S01, S02 | `05-implementation/demo/P100_demo/data/timesheet.csv`; `professor/notebook.ipynb`: celda de `groupby` | Sin normalizar. |
| H02 — Resumen | S02 | `05-implementation/demo/P100_demo/tests/test_activity.py`: `test_02` | Sólo la suma. |
"""

SURFACE_ROWS = """| S01 | Dataset | `data/timesheet.csv` | Procedencia no documentada. |
| S02 | Pruebas | `tests/test_activity.py` | Recalcula el resumen. |
"""


def description(title="P100 — Resumen de conductores", implementation="05-implementation/demo/P100_demo/",
                highlights=HIGHLIGHTS, evidence=EVIDENCE_ROWS, surfaces=SURFACE_ROWS, extra=""):
    return f"""# {title}

## Actividad actual implementada

**Implementación:** `{implementation}`.

### Preguntas analíticas actuales

- ¿Cuántas horas registró cada conductor?

### Producto analítico actual y límite de identidad

- **Producto terminal:** resumen.

### Highlights de contribución

{highlights}
### Inventario técnico de implementación

- **Introduce:** `groupby`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Agregación | H01 | `groupby` | Notebook. |

### Relación técnica con actividades anteriores

Primera.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
{evidence}
### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
{surfaces}
### Contrato de evidencia actual

- **Pruebas:** recalculan.

### Dependencias en la secuencia

- **Recibe de:** ninguna.
{extra}
## Trazabilidad y auditoría

P100 mapeada.
"""


LOG = """# Log — P100

## S02.P100.01

- **Fecha:** 2026-10-04.

## S03.P100.01

- **Resultado:** sin cambios.
"""


FOLDER = "P100_demo"


def make_activity_layout(tmp_path):
    layout = lib.Layout(tmp_path)
    layout.format.parent.mkdir(parents=True)
    layout.format.write_text("# Formato\n\nVersión 0.1 (borrador)\n", encoding="utf-8")
    folder = layout.implementation(COURSE) / FOLDER
    for name in ("data/timesheet.csv", "professor/notebook.ipynb", "tests/test_activity.py", "submission/.gitkeep"):
        (folder / name).parent.mkdir(parents=True, exist_ok=True)
        (folder / name).write_text("x\n", encoding="utf-8")
    (layout.implementation(COURSE) / "L101_lab").mkdir()
    layout.traceability(COURSE).write_text("P100:\n  - demo.C02\nL101:\n  - demo.C01\n", encoding="utf-8")
    write(layout, description())
    layout.log(COURSE, FOLDER).write_text(LOG, encoding="utf-8")
    return layout


@pytest.fixture
def layout(tmp_path):
    return make_activity_layout(tmp_path)


def write(layout, text, course=COURSE, folder=FOLDER):
    layout.activity(course, folder).write_text(text, encoding="utf-8")


def errors_of(layout):
    return check_activities.check(layout, COURSE)


def test_a_bare_file_name_may_sit_in_any_subfolder(layout):
    write(layout, description(evidence=EVIDENCE_ROWS.replace("`professor/notebook.ipynb`", "`notebook.ipynb`")))
    errors, _ = errors_of(layout)
    assert errors == []


def test_a_valid_description_passes(layout):
    errors, warnings = errors_of(layout)
    assert errors == []
    assert warnings == []


@pytest.mark.parametrize("change, message", [
    (dict(title="P101 — Otro"), "the title must be"),
    (dict(implementation="05-implementation/demo/P999_otro/"), "Implementación is"),
    (dict(evidence=EVIDENCE_ROWS.replace("timesheet.csv`", "missing.csv`", 1)), "H01 points to `05-implementation/demo/P100_demo/data/missing.csv`"),
    (dict(evidence=EVIDENCE_ROWS.replace("| S02 | `05", "| — | `05")), "H02 is linked to no surface"),
    (dict(evidence=EVIDENCE_ROWS.replace("S01, S02", "S01, S07")), "H01 is linked to S07"),
    (dict(evidence=EVIDENCE_ROWS.splitlines()[0] + "\n"), "H02 has no row"),
    (dict(surfaces=SURFACE_ROWS.replace("`tests/test_activity.py`", "`tests/test_otro.py`")), "surface S02 points to"),
    (dict(highlights=HIGHLIGHTS.replace("H02", "H01")), "repeated highlight ids"),
    (dict(highlights="- H01 sin formato\n"), "there are no highlights"),
    (dict(extra="\n## Mejoras aceptadas pendientes de implementación\n\n- Algo.\n"), "still has content"),
])
def test_description_errors(layout, change, message):
    write(layout, description(**change))
    errors, _ = errors_of(layout)
    assert any(message in e for e in errors), errors


def test_function_names_in_backticks_are_not_paths(layout):
    activity = lib.parse_activity(layout.activity(COURSE, FOLDER))
    cell = "`groupby`; `pd.merge`; `pickle.dump/load`; `.pkl`; `data/x.csv`; `notebook.ipynb`; `submission/`"
    assert lib.file_references(cell) == ["data/x.csv", "notebook.ipynb", "submission/"]
    assert activity.surface_ids() == ["S01", "S02"]


def test_missing_case_and_data_marker_is_a_warning(layout):
    write(layout, description(highlights=HIGHLIGHTS.replace(" (caso y datos)", "")))
    errors, warnings = errors_of(layout)
    assert errors == []
    assert any("(caso y datos)" in w for w in warnings)


def test_missing_description_and_log_are_errors(layout):
    layout.activity(COURSE, FOLDER).unlink()
    layout.log(COURSE, FOLDER).unlink()
    errors, _ = errors_of(layout)
    assert any("the description does not exist" in e for e in errors)
    assert any("the log does not exist" in e for e in errors)


def test_log_numbering_is_checked(layout):
    layout.log(COURSE, FOLDER).write_text(LOG.replace("S02.P100.01", "S02.P100.02"), encoding="utf-8")
    _, warnings = errors_of(layout)
    assert any("S02 entries are not numbered" in w for w in warnings)


def test_inventory_lists_only_workshops_and_the_next_entry(layout):
    report = inventory.inventory(layout, COURSE)
    assert [a["id"] for a in report["activities"]] == ["P100"]
    p100 = report["activities"][0]
    assert p100["next_description"] == "S02.P100.02"
    assert p100["traceability"] == ["demo.C02"]
    assert p100["files"]["data"] == ["data/timesheet.csv"]
    assert "submission" not in p100["files"]
    assert "." not in p100["files"]
    assert p100["surfaces"] == ["S01", "S02"]
    assert report["to_describe"] == []


def test_inventory_lists_activities_without_description(layout):
    layout.activity(COURSE, FOLDER).unlink()
    report = inventory.inventory(layout, COURSE)
    assert report["to_describe"] == ["P100"]


def test_scripts_refuse_another_format_version(layout):
    layout.format.write_text("# Formato\n\nVersión 0.2 (borrador)\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="Update activity_lib.py"):
        inventory.inventory(layout, COURSE)


def test_traceability_round_trip(tmp_path):
    text = """format_version: "0.1"
P001:
  - S04.F08
P103:
  resultados: [RA02, RA03]
  competencias: [C002]
  decision: puntual
  auditoria: AUD.P103.01
descriptiva/P100:
  - fundamentos.C05
"""
    path = tmp_path / "traceability.yaml"
    path.write_text(text, encoding="utf-8")
    trace = lib.parse_traceability(path)
    assert trace.version == "0.1"
    assert trace.entries["P103"]["resultados"] == ["RA02", "RA03"]
    assert trace.entries["descriptiva/P100"] == ["fundamentos.C05"]
    assert lib.render_traceability(trace) == text
