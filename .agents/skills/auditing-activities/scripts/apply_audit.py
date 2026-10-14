"""Applies a checked audit: proposals, log entries, traceability and coverage.

Usage (from the repository root):

    python3 .agents/skills/auditing-activities/scripts/apply_audit.py <audit.json> [--write]

Without --write it prints what it would change. With --write it assigns the
ids of the new proposals, appends them to the course tasks file, adds the
audit as a source of the proposals it reinforces, appends an AUD entry to the
log of every audited activity, rewrites the audited entries of
traceability.yaml and rewrites the course audit file. It never modifies an
activity's implementation or description, and it refuses an audit that has
errors or was already applied.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from activity_lib import (
    ROOT,
    Layout,
    latest_entry,
    next_entry,
    parse_log,
    parse_traceability,
    render_traceability,
)
from audit_lib import (
    COURSE_DECISION,
    COURSE_TASK_REF,
    COVERED,
    IMPROVEMENT,
    NEW_ACTIVITY,
    PENDING_STATE,
    SUPPORTED_TRACE_VERSION,
    TASK_HEADING,
    CourseActivity,
    anchor_parts,
    as_list,
    course_activities,
    fingerprint,
    load_audit,
    requirements,
    used_course_task_numbers,
    used_task_numbers,
)
from check_audit import check


class Edits:
    def __init__(self) -> None:
        self.texts: dict[Path, str] = {}

    def read(self, path: Path, default: str = "") -> str:
        if path not in self.texts:
            self.texts[path] = path.read_text(encoding="utf-8") if path.exists() else default
        return self.texts[path]

    def write(self, path: Path, text: str) -> None:
        self.texts[path] = text

    def append(self, path: Path, block: str, default: str = "") -> None:
        text = self.read(path, default).rstrip("\n")
        self.write(path, f"{text}\n\n{block.strip()}\n" if text else block.strip() + "\n")


def signals_for(audit: dict, proposal: str) -> list[str]:
    return [s["id"] for s in as_list(audit.get("senales"))
            if s.get("categoria") in (IMPROVEMENT, NEW_ACTIVITY) and s.get("propuesta") == proposal]


def course_motivation(audit: dict, proposal: str) -> str:
    signals = signals_for(audit, proposal)
    activities = [e["actividad"] for e in as_list(audit.get("actividades")) if e.get("curso") == proposal]
    parts = ([f"señales {', '.join(signals)}"] if signals else []) + \
        ([f"decisión de {', '.join(activities)}"] if activities else [])
    return "; ".join(parts) or "la cobertura del curso"


def signals_of_activity(audit: dict, ref: str) -> list[str]:
    lines = []
    for signal in as_list(audit.get("senales")):
        category = signal.get("categoria")
        anchors = [f"{hito.split(':', 1)[1]} {level}" for hito, level in map(anchor_parts, as_list(signal.get("anclas")))
                   if hito.split(":", 1)[0] == ref]
        if anchors:
            lines.append(f"{signal['id']} ({category}: {', '.join(anchors)})")
        elif signal.get("actividad") == ref:
            detail = signal.get("propuesta") or signal.get("razon", "")
            lines.append(f"{signal['id']} ({category}: {detail})")
    return lines


def justification(proposal: dict) -> str:
    return f"""- **Justificación metodológica:** {proposal['metodologico']}
- **Justificación técnica:** {proposal['tecnico']}
- **Justificación pedagógica:** {proposal['pedagogico']}
- **Identidad del curso:** {proposal['identidad']}"""


def task_block(task_id: str, proposal: dict, source: str) -> str:
    anchors = ", ".join(as_list(proposal["anclas"]))
    return f"""## {task_id} — {proposal['titulo']}

- **Estado:** {PENDING_STATE}
- **Tipo:** {proposal['tipo']}
- **Fuentes:**
  - {source}
- **Qué gana el estudiante:** {proposal['que_gana']}
- **Anclas actuales:** {anchors}.
- **Alternativas menores descartadas:** {proposal['alternativas']}
- **Contrato de no regresión:** {proposal['no_regresion']}
- **Límite de la actividad:** {proposal['limite']}
- **Interacciones:** {proposal['interacciones']}
{justification(proposal)}
- **Criterio de aceptación:** {proposal['aceptacion']}

### Instrucciones de ejecución

{proposal['instrucciones'].strip()}
"""


def course_task_block(task_id: str, proposal: dict, source: str) -> str:
    return f"""## {task_id} — ⚠️ PENDIENTE DE DECISIÓN — {proposal['titulo']}

- **Estado:** {PENDING_STATE}
- **Tipo:** {proposal['tipo']}
- **Fuentes:**
  - {source}
- **Contribución distinta:** {proposal['contribucion']}
- **Posición propuesta:** {proposal['posicion']}
- **Desplaza o fusiona:** {proposal['desplaza']}
- **Efecto en la secuencia:** {proposal['efecto']}
- **Caso y datos:** {proposal['caso']}
- **Producto de Analytics:** {proposal['producto']}
{justification(proposal)}
- **Criterio de aceptación de una primera versión:** {proposal['aceptacion']}
"""


def set_state(text: str, task_id: str, state: str) -> str:
    """Rewrites the Estado bullet of one pending proposal, keeping everything else."""
    headings = list(TASK_HEADING.finditer(text))
    match = next(m for m in headings if m.group(1) == task_id)
    following = [m.start() for m in headings if m.start() > match.start()]
    end = following[0] if following else len(text)
    body = text[match.end():end]
    if re.search(r"^- \*\*Estado:\*\*.*$", body, re.M):
        body = re.sub(r"^- \*\*Estado:\*\*.*$", f"- **Estado:** {state}", body, count=1, flags=re.M)
    else:
        body = re.sub(r"^(- \*\*)", f"- **Estado:** {state}\n\\1", body, count=1, flags=re.M)
    return text[:match.end()] + body + text[end:]


def add_source(text: str, task_id: str, source: str) -> str:
    """Adds one source line to the Fuentes bullet of an existing proposal."""
    headings = list(TASK_HEADING.finditer(text))
    match = next(m for m in headings if m.group(1) == task_id)
    following = [m.start() for m in headings if m.start() > match.start()]
    end = following[0] if following else len(text)
    lines = text[match.end():end].split("\n")
    start = next((i for i, line in enumerate(lines) if line.startswith("- **Fuentes:**")), None)
    if start is None:
        first = next((i for i, line in enumerate(lines) if line.startswith("- **")), 1)
        lines[first:first] = ["- **Fuentes:**", f"  - {source}"]
    else:
        stop = next((i for i in range(start + 1, len(lines))
                     if not lines[i].startswith("  ") or not lines[i].strip()), len(lines))
        lines.insert(stop, f"  - {source}")
    return text[:match.end()] + "\n".join(lines) + text[end:]


def coverage_report(audit: dict, reqs, digest: str, ids: dict[str, str]) -> str:
    texts = {t.id: f"{t.statement} (nivel: {t.level})" for t in reqs.targets} | {i.id: i.text for i in reqs.items}
    outside = [f"| {e['actividad']} | {o['hito']} | {o['accion']} | {ids.get(str(o.get('propuesta')), o.get('propuesta') or '—')} "
               f"| {o['razon']} |"
               for e in as_list(audit.get("actividades")) for o in as_list(e.get("fuera"))]
    dates = ", ".join(f"{cid} ({date})" for cid, date in reqs.competency_dates.items())
    rows = []
    for entry in as_list(audit.get("actividades")):
        proposals = [ids[p["clave"]] for p in as_list(entry.get("propuestas"))] + as_list(entry.get("refuerza"))
        if entry.get("curso"):
            proposals.append(ids.get(entry["curso"], entry["curso"]))
        rows.append(
            f"| {entry['actividad']} | {entry['decision']} | {', '.join(as_list(entry.get('resultados'))) or '—'} "
            f"| {', '.join(as_list(entry.get('competencias'))) or '—'} | {', '.join(proposals) or '—'} "
            f"| {entry['razon']} |"
        )
    signals = []
    for signal in as_list(audit.get("senales")):
        anchors = ", ".join(f"{hito} ({level})" for hito, level in map(anchor_parts, as_list(signal.get("anclas"))))
        if signal.get("categoria") == COVERED:
            detail = anchors
        elif signal.get("propuesta"):
            proposal = ids.get(signal["propuesta"], signal["propuesta"])
            detail = f"{signal.get('actividad')}: {proposal}" if signal.get("actividad") else proposal
        else:
            detail = signal.get("razon", "")
        if anchors and signal.get("categoria") != COVERED:
            detail = f"{detail}; parcial en {anchors}"
        signals.append(f"| {signal['id']} | {texts[signal['id']]} | {signal['categoria']} | {detail} |")
    return f"""# {audit['curso']} — Auditoría de actividades

- **Fecha / executor:** {audit['fecha']} / {audit['executor']}.
- **Huella de la auditoría:** `sha256:{digest}`.
- **Entrada:** `{reqs.source}`; competencias {dates}.

## Decisiones por actividad

| Actividad | Decisión | Resultados | Competencias | Propuestas | Razón |
| --- | --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Señales

| Señal | Texto | Categoría | Anclas, propuesta o razón |
| --- | --- | --- | --- |
{chr(10).join(signals)}

## Hitos fuera de lo que el curso debe enseñar

| Actividad | Hito | Acción | Propuesta | Razón |
| --- | --- | --- | --- | --- |
{chr(10).join(outside) or "| — | — | — | — | — |"}
"""


def already_applied(layout: Layout, course: str, activities: list[CourseActivity], digest: str) -> bool:
    paths = [layout.audit(course)] + [layout.log(a.owner, a.folder.name) for a in activities]
    return any(p.exists() and digest in p.read_text(encoding="utf-8") for p in paths)


def plan(layout: Layout, audit_path: Path) -> Edits:
    audit = load_audit(audit_path)
    errors, _ = check(layout, audit_path)
    if errors:
        raise SystemExit(f"the audit has {len(errors)} errors; run check_audit.py and fix them first")
    course = audit["curso"]
    digest = fingerprint(audit_path)
    activities = {a.ref: a for a in course_activities(layout, course)}
    if already_applied(layout, course, list(activities.values()), digest):
        raise SystemExit("this audit was already applied")
    reqs = requirements(layout, course)
    edits = Edits()
    who = f"({audit['executor']}, {audit['fecha']})"

    audit_ids: dict[str, str] = {}
    for entry in audit["actividades"]:
        activity = activities[entry["actividad"]]
        audit_ids[activity.ref] = next_entry(parse_log(layout.log(activity.owner, activity.folder.name)), "AUD", activity.id)

    ids: dict[str, str] = {}
    next_course = max(used_course_task_numbers(layout, course), default=0)
    for proposal in as_list(audit.get("nuevas")):
        next_course += 1
        ids[proposal["clave"]] = f"N{next_course:02d}"
    for entry in audit["actividades"]:
        activity = activities[entry["actividad"]]
        number = max(used_task_numbers(layout, activity), default=0)
        for proposal in as_list(entry.get("propuestas")):
            number += 1
            ids[proposal["clave"]] = f"T{number:02d}"

    def tasks_header(activity: CourseActivity, audit_id: str) -> str:
        baseline = latest_entry(parse_log(layout.log(activity.owner, activity.folder.name)), "S02")
        since = f" (entrada S02 más reciente: `{baseline}`)" if baseline else ""
        return f"# {activity.id} — Propuestas de mejora\n\n**Línea base:** `activity.md`{since}.\n"

    for entry in audit["actividades"]:
        activity = activities[entry["actividad"]]
        tasks = layout.tasks(activity.owner, activity.folder.name)
        source = f"Auditoría `{audit_ids[activity.ref]}` {who} del curso `{course}`"
        for proposal in as_list(entry.get("propuestas")):
            signals = signals_for(audit, proposal["clave"])
            block = task_block(ids[proposal["clave"]], proposal, f"{source}: señales {', '.join(signals)}.")
            edits.append(tasks, block, tasks_header(activity, audit_ids[activity.ref]))
        for task_id in as_list(entry.get("refuerza")):
            signals = signals_for(audit, task_id)
            line = f"{source}: refuerza con las señales {', '.join(signals) or 'de la decisión'}."
            edits.write(tasks, add_source(edits.read(tasks), task_id, line))
        for item in as_list(entry.get("obsoletas")):
            state = f"obsoleta según `{audit_ids[activity.ref]}` {who}: {item['razon'].strip()}"
            edits.write(tasks, set_state(edits.read(tasks), item["propuesta"], state))

    course_tasks = layout.course_tasks(course)
    course_source = f"Auditoría del curso `{course}` {who}"
    for proposal in as_list(audit.get("nuevas")):
        block = course_task_block(ids[proposal["clave"]], proposal,
                                  f"{course_source}: {course_motivation(audit, proposal['clave'])}.")
        edits.append(course_tasks, block, f"# {course} — Actividades nuevas por decidir\n")
    referenced = as_list(audit.get("refuerza"))
    referenced += [e["curso"] for e in audit["actividades"] if e.get("curso")]
    referenced += [s["propuesta"] for s in audit["senales"] if s.get("categoria") == NEW_ACTIVITY]
    referenced += [o["propuesta"] for e in audit["actividades"] for o in as_list(e.get("fuera"))
                   if COURSE_TASK_REF.match(str(o.get("propuesta", "")))]
    for task_id in dict.fromkeys(r for r in referenced if r not in ids):
        line = f"{course_source}: refuerza con {course_motivation(audit, task_id)}."
        edits.write(course_tasks, add_source(edits.read(course_tasks), task_id, line))

    trace_path = layout.traceability(course)
    trace = parse_traceability(trace_path)
    trace.version = SUPPORTED_TRACE_VERSION
    for entry in audit["actividades"]:
        ref = entry["actividad"]
        activity = activities[ref]
        log_path = layout.log(activity.owner, activity.folder.name)
        outcome = []
        outcome += [f"propone {ids[p['clave']]}" for p in as_list(entry.get("propuestas"))]
        outcome += [f"refuerza {t}" for t in as_list(entry.get("refuerza"))]
        outcome += [f"marca obsoleta {o['propuesta']}" for o in as_list(entry.get("obsoletas"))]
        if entry["decision"] == COURSE_DECISION:
            outcome.append(f"aporta a {ids.get(entry['curso'], entry['curso'])}")
        anchored = signals_of_activity(audit, ref)
        description_entry = latest_entry(parse_log(log_path), "S02") or "activity.md"
        outside = [f"{o['hito']} ({o['accion']}"
                   + (f": {ids.get(str(o.get('propuesta')), o.get('propuesta'))}" if o.get("propuesta") else "")
                   + f"; {o['razon']})" for o in as_list(entry.get("fuera"))]
        block = f"""## {audit_ids[ref]}

- **Fecha / executor:** {audit['fecha']} / {audit['executor']}.
- **Curso auditado:** `{course}`; huella `sha256:{digest}`.
- **Entrada:** `{reqs.source}`; línea base `{description_entry}`.
- **Decisión:** {entry['decision']}. {entry['razon']}
- **Resultados y competencias:** {', '.join(as_list(entry.get('resultados'))) or 'ninguno'}; {', '.join(as_list(entry.get('competencias'))) or 'ninguna'}.
- **Resultado:** {'; '.join(outcome) or 'sin cambios'}.
- **Señales:** {'; '.join(anchored) or 'ninguna anclada a esta actividad'}.
- **Hitos fuera de lo que el curso debe enseñar:** {'; '.join(outside) or 'ninguno'}.
"""
        edits.append(log_path, block, f"# Log — {activity.id}\n")
        trace.entries[ref] = {
            "resultados": as_list(entry.get("resultados")),
            "competencias": as_list(entry.get("competencias")),
            "decision": entry["decision"],
            "auditoria": audit_ids[ref],
        }
    edits.write(trace_path, render_traceability(trace))
    edits.write(layout.audit(course), coverage_report(audit, reqs, digest, ids))
    return edits


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("audit", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    layout = Layout(ROOT)
    edits = plan(layout, args.audit)
    for path, text in edits.texts.items():
        before = path.read_text(encoding="utf-8") if path.exists() else ""
        if text == before:
            continue
        added = re.findall(r"^## (\S+)", text[len(before):] if text.startswith(before) else text, re.M)
        print(f"{'write' if args.write else 'would write'} {layout.shown(path)}"
              + (f": {', '.join(added)}" if added else ""))
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
