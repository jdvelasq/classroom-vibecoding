from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from activity_lib import (
    SUPPORTED_FORMAT_VERSION,
    Activity,
    Layout,
    activity_dirs,
    parse_activity,
    parse_log,
    parse_traceability,
    validate_activity,
    validate_log,
)

# The course outcomes, the matrix and the competencies are owned by the
# mapping-curriculum skill and the skills it builds on; their parsers are
# reused so that every link of the chain reads those files the same way.
SKILLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS / "mapping-curriculum" / "scripts"))
import curriculum_lib as curriculum  # noqa: E402

CATEGORIES = ("cubierta", "marginal", "rechazada previamente", "fuera de alcance", "mejora", "actividad nueva")
COVERED, MARGINAL, REJECTED, OUT_OF_SCOPE, IMPROVEMENT, NEW_ACTIVITY = CATEGORIES
NEEDS_REASON = (MARGINAL, REJECTED, OUT_OF_SCOPE)
DECISIONS = ("igual", "puntual", "curso")
SAME, POINT_CHANGE, COURSE_DECISION = DECISIONS
TASK_TYPES = ("encuadre", "producto/evidencia", "método", "caso/datos", "proceso", "pedagogía")
COURSE_TASK_TYPES = ("actividad nueva", "reorganización")
REJECTED_STATE = "rechazada"
PENDING_STATE = "pendiente de discusión"

# A point change reinforces the activity without lengthening it: at most one
# new proposal per activity in an audit, and a warning when the proposals
# still open on one activity exceed this number.
MAX_NEW_TASKS_PER_ACTIVITY = 1
MAX_OPEN_TASKS_PER_ACTIVITY = 3

TASK_FIELDS = ["titulo", "tipo", "que_gana", "anclas", "alternativas", "no_regresion", "limite",
               "interacciones", "aceptacion", "instrucciones"]
COURSE_TASK_FIELDS = ["titulo", "tipo", "contribucion", "posicion", "efecto", "caso", "producto", "aceptacion"]
AUDIT_KEYS = ["curso", "executor", "fecha", "senales", "actividades", "nuevas", "refuerza"]

ACTIVITY_REF = re.compile(r"^(?:([a-z][a-z0-9-]*)/)?(P\d{3})$")
ANCHOR = re.compile(r"^((?:[a-z][a-z0-9-]*/)?P\d{3}):(H\d{2})$")
TASK_REF = re.compile(r"^T(\d{2})$")
COURSE_TASK_REF = re.compile(r"^N(\d{2})$")
TASK_HEADING = re.compile(r"^## ([TN]\d{2}) — (.+?)\s*$", re.M)
ITEM_ID = re.compile(r"^(C\d{3})\.(CON|HAB)(\d{2})$")
LEGACY_CAPABILITY = re.compile(r"^[a-z][a-z0-9-]*\.C\d{2}$")
COMPETENCY_ID = re.compile(r"^C\d{3}$")
SOURCES = re.compile(r"\s*\[[^\]]*\]\s*\.?\s*$")
SUPPORTED_TRACE_VERSION = SUPPORTED_FORMAT_VERSION
TRACE_FIELDS = ["resultados", "competencias", "decision", "auditoria"]


@dataclass(frozen=True)
class Target:
    id: str
    statement: str
    level: str
    contribution: str
    competencies: tuple[str, ...]


@dataclass(frozen=True)
class Item:
    id: str
    competency: str
    kind: str
    text: str


@dataclass(frozen=True)
class CourseActivity:
    ref: str
    owner: str
    id: str
    folder: Path

    def anchor(self, highlight: str) -> str:
        return f"{self.ref}:{highlight}"


@dataclass
class TaskEntry:
    id: str
    title: str
    state: str
    text: str


@dataclass
class Requirements:
    course: str
    level: str
    source: str
    targets: list[Target]
    items: list[Item]
    competency_dates: dict[str, str] = field(default_factory=dict)

    @property
    def signal_ids(self) -> list[str]:
        return [t.id for t in self.targets] + [i.id for i in self.items]


def curriculum_layout(layout: Layout) -> curriculum.Layout:
    return curriculum.Layout(layout.root)


def find_course(layout: Layout, course: str) -> curriculum.Course:
    _, courses = curriculum.load_courses(curriculum_layout(layout))
    found = next((c for c in courses if c.folder == course), None)
    if found is None:
        raise SystemExit(f"{course} is not a course of 04-curriculum/courses.md")
    return found


def clean(text: str) -> str:
    stripped = SOURCES.sub("", text).strip()
    return stripped if stripped.endswith(".") else stripped + "."


def requirements(layout: Layout, course: str) -> Requirements:
    cl = curriculum_layout(layout)
    info = find_course(layout, course)
    competencies = curriculum.load_competencies(cl)
    targets: list[Target] = []
    if info.level == curriculum.POSTGRADUATE:
        rows, problems = curriculum.read_matrix(cl)
        if problems:
            raise SystemExit("; ".join(problems))
        rows = [r for r in rows if r.curso == course]
        if not rows:
            raise SystemExit(
                f"{curriculum_layout(layout).matrix.relative_to(layout.root)} assigns no learning outcome to "
                f"{course}; run mapping-curriculum first"
            )
        outcomes = curriculum.load_outcomes(cl)
        for row in rows:
            outcome = outcomes.get(row.ra)
            if outcome is None:
                raise SystemExit(f"matrix.csv cites {row.ra}, which is not a learning outcome")
            targets.append(Target(row.ra, str(outcome.header.get("enunciado", "")), row.nivel, row.aporte,
                                  tuple(outcome.header.get("competencias", []))))
        source = cl.matrix.relative_to(layout.root).as_posix()
    else:
        written = curriculum.load_undergraduate(cl)
        if course not in written:
            raise SystemExit(f"04-curriculum/undergraduate/{course}.md does not exist; run mapping-curriculum first")
        for outcome in curriculum.parse_course_outcomes(written[course]):
            targets.append(Target(f"{course}/{outcome.id}", outcome.statement, "introductorio",
                                  outcome.title, outcome.competencies))
        source = (cl.undergraduate / f"{course}.md").relative_to(layout.root).as_posix()
    items: list[Item] = []
    dates: dict[str, str] = {}
    for cid in sorted({c for t in targets for c in t.competencies}):
        competency = competencies.get(cid)
        if competency is None:
            raise SystemExit(f"{cid} is cited by the course outcomes but is not in the competency map")
        dates[cid] = str(competency.header.get("fecha", ""))
        for kind, section in (("CON", "Conocimientos"), ("HAB", "Habilidades")):
            for number, text in enumerate(competency.bullets(section), start=1):
                items.append(Item(f"{cid}.{kind}{number:02d}", cid, kind, clean(text)))
    return Requirements(course, info.level, source, targets, items, dates)


def course_activities(layout: Layout, course: str) -> list[CourseActivity]:
    found = [CourseActivity(aid, course, aid, folder) for aid, folder in activity_dirs(layout, course).items()]
    for key in parse_traceability(layout.traceability(course)).entries:
        match = ACTIVITY_REF.match(key)
        if not match or not match.group(1) or match.group(1) == course:
            continue
        owner, aid = match.group(1), match.group(2)
        folder = activity_dirs(layout, owner).get(aid) if layout.implementation(owner).is_dir() else None
        if folder is None:
            raise SystemExit(f"{layout.shown(layout.traceability(course))} cites {key}, which has no folder")
        found.append(CourseActivity(key, owner, aid, folder))
    return found


def describe_problems(layout: Layout, activity: CourseActivity) -> list[str]:
    path = layout.activity(activity.owner, activity.folder.name)
    if not path.exists():
        return [f"{layout.shown(path)}: the description does not exist; describe the activity first"]
    errors, _ = validate_activity(parse_activity(path), layout, activity.owner)
    log_errors, _ = validate_log(layout.log(activity.owner, activity.folder.name), layout, activity.id)
    return errors + log_errors


def load_description(layout: Layout, activity: CourseActivity) -> Activity:
    return parse_activity(layout.activity(activity.owner, activity.folder.name))


def labelled_value(text: str, label: str) -> str:
    match = re.search(rf"^- \*\*{re.escape(label)}:\*\*\s*(.*)$", text, re.M)
    return match.group(1).strip() if match else ""


def parse_tasks(path: Path) -> list[TaskEntry]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    matches = list(TASK_HEADING.finditer(text))
    entries = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end():end]
        entries.append(TaskEntry(match.group(1), match.group(2), labelled_value(body, "Estado"), body))
    return entries


def activity_tasks(layout: Layout, activity: CourseActivity) -> list[TaskEntry]:
    return [e for e in parse_tasks(layout.tasks(activity.owner, activity.id)) if TASK_REF.match(e.id)]


def open_tasks(entries: list[TaskEntry]) -> list[TaskEntry]:
    return [e for e in entries if e.state != REJECTED_STATE]


def course_tasks(layout: Layout, course: str) -> list[TaskEntry]:
    return [e for e in parse_tasks(layout.course_tasks(course)) if COURSE_TASK_REF.match(e.id)]


def used_task_numbers(layout: Layout, activity: CourseActivity) -> set[int]:
    """Rejected proposals may have left the tasks file; their ids live on in the log."""
    numbers = {int(e.id[1:]) for e in activity_tasks(layout, activity)}
    log = layout.log(activity.owner, activity.folder.name)
    if log.exists():
        numbers |= {int(n) for n in re.findall(r"\bT(\d{2})\b", log.read_text(encoding="utf-8"))}
    return numbers


def used_course_task_numbers(layout: Layout, course: str) -> set[int]:
    return {int(e.id[1:]) for e in course_tasks(layout, course)}


def fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_audit(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: the audit must be a JSON object")
    return data


def as_list(value: object) -> list:
    return value if isinstance(value, list) else []


def validate_audit(layout: Layout, audit: dict, course: str) -> tuple[list[str], list[str]]:
    """Checks the model's audit against the course requirements and descriptions."""
    errors: list[str] = []
    warnings: list[str] = []
    unknown_keys = sorted(set(audit) - set(AUDIT_KEYS))
    if unknown_keys:
        errors.append(f"unknown keys: {', '.join(unknown_keys)}")
    if audit.get("curso") != course:
        errors.append(f"curso is '{audit.get('curso')}', the audited course is '{course}'")
    if not str(audit.get("executor", "")).strip():
        errors.append("executor is empty")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(audit.get("fecha", ""))):
        errors.append("fecha must be YYYY-MM-DD")

    reqs = requirements(layout, course)
    activities = {a.ref: a for a in course_activities(layout, course)}
    for activity in activities.values():
        errors += describe_problems(layout, activity)
    if errors:
        return errors, warnings
    descriptions = {ref: load_description(layout, a) for ref, a in activities.items()}
    targets = {t.id: t for t in reqs.targets}
    open_course = {e.id for e in open_tasks(course_tasks(layout, course))}

    new_course = {}
    for proposal in as_list(audit.get("nuevas")):
        key = proposal.get("clave") if isinstance(proposal, dict) else None
        if not key or key in new_course:
            errors.append("every entry of nuevas needs a unique clave")
            continue
        new_course[key] = proposal
        for name in COURSE_TASK_FIELDS:
            if not str(proposal.get(name, "")).strip():
                errors.append(f"nuevas {key}: {name} is empty")
        if proposal.get("tipo") not in COURSE_TASK_TYPES:
            errors.append(f"nuevas {key}: tipo must be one of {', '.join(COURSE_TASK_TYPES)}")
    for ref in as_list(audit.get("refuerza")):
        if ref not in open_course:
            errors.append(f"refuerza cites {ref}, which is not a course proposal of {course}")

    def course_reference(ref: object, where: str) -> None:
        if ref not in new_course and ref not in open_course:
            errors.append(f"{where} cites the course proposal '{ref}', which is neither in nuevas nor in tasks")

    entries = {}
    for entry in as_list(audit.get("actividades")):
        ref = entry.get("actividad") if isinstance(entry, dict) else None
        if ref not in activities:
            errors.append(f"actividades cites '{ref}', which is not an activity of {course}")
            continue
        if ref in entries:
            errors.append(f"{ref} appears more than once in actividades")
        entries[ref] = entry
    for ref in activities:
        if ref not in entries:
            errors.append(f"{ref} has no decision in actividades")

    point_proposals: dict[str, dict[str, dict]] = {}
    for ref, entry in entries.items():
        activity = activities[ref]
        description = descriptions[ref]
        decision = entry.get("decision")
        results = as_list(entry.get("resultados"))
        competencies = as_list(entry.get("competencias"))
        proposals = as_list(entry.get("propuestas"))
        reinforced = as_list(entry.get("refuerza"))
        where = f"{ref}"
        if decision not in DECISIONS:
            errors.append(f"{where}: decision must be one of {', '.join(DECISIONS)}")
        if not str(entry.get("razon", "")).strip():
            errors.append(f"{where}: razon is empty")
        for rid in results:
            if rid not in targets:
                errors.append(f"{where}: {rid} is not an outcome {course} must cover")
        allowed = {c for rid in results if rid in targets for c in targets[rid].competencies}
        for cid in competencies:
            if LEGACY_CAPABILITY.match(str(cid)) or not COMPETENCY_ID.match(str(cid)):
                errors.append(f"{where}: '{cid}' is not a competency id Cnnn")
            elif cid not in allowed:
                errors.append(f"{where}: {cid} is not a competency of its resultados")
        if results and not competencies:
            errors.append(f"{where}: resultados need at least one of their competencias")
        if not results and decision != COURSE_DECISION:
            errors.append(f"{where}: an activity that serves no outcome of {course} only admits decision '{COURSE_DECISION}'")

        open_ids = {e.id for e in open_tasks(activity_tasks(layout, activity))}
        for task in reinforced:
            if task not in open_ids:
                errors.append(f"{where}: refuerza cites {task}, which is not an open proposal of {activity.id}")
        keys: dict[str, dict] = {}
        for proposal in proposals:
            key = proposal.get("clave") if isinstance(proposal, dict) else None
            if not key or key in keys or key in new_course:
                errors.append(f"{where}: every proposal needs a clave unique in the audit")
                continue
            keys[key] = proposal
            for name in TASK_FIELDS:
                value = proposal.get(name)
                if name == "anclas":
                    if not as_list(value):
                        errors.append(f"{where} {key}: anclas is empty")
                elif not str(value or "").strip():
                    errors.append(f"{where} {key}: {name} is empty")
            if proposal.get("tipo") not in TASK_TYPES:
                errors.append(f"{where} {key}: tipo must be one of {', '.join(TASK_TYPES)}")
            for anchor in as_list(proposal.get("anclas")):
                if anchor not in description.highlight_ids() and anchor not in description.surface_ids():
                    errors.append(f"{where} {key}: ancla {anchor} is not a highlight or surface of {activity.id}")
        point_proposals[ref] = keys

        if decision == SAME and (proposals or reinforced or entry.get("curso")):
            errors.append(f"{where}: decision '{SAME}' takes no proposal")
        if decision == POINT_CHANGE:
            if len(proposals) > MAX_NEW_TASKS_PER_ACTIVITY:
                errors.append(
                    f"{where}: a point change is one bounded change; {len(proposals)} new proposals lengthen "
                    f"the activity, so the rest belongs to a course decision"
                )
            if not proposals and not reinforced:
                errors.append(f"{where}: decision '{POINT_CHANGE}' needs a new proposal or an open one to reinforce")
            if entry.get("curso"):
                errors.append(f"{where}: decision '{POINT_CHANGE}' takes no course proposal")
            if len(open_ids) + len(proposals) > MAX_OPEN_TASKS_PER_ACTIVITY:
                warnings.append(
                    f"{where}: {len(open_ids) + len(proposals)} open proposals; check that the activity stays a short, "
                    f"well-defined problem"
                )
        if decision == COURSE_DECISION:
            if proposals or reinforced:
                errors.append(f"{where}: decision '{COURSE_DECISION}' takes no activity proposal")
            course_reference(entry.get("curso"), where)

    seen: set[str] = set()
    used_keys: set[str] = set()
    for signal in as_list(audit.get("senales")):
        sid = signal.get("id") if isinstance(signal, dict) else None
        if sid not in reqs.signal_ids:
            errors.append(f"senales cites '{sid}', which is not an outcome or item of {course}")
            continue
        if sid in seen:
            errors.append(f"{sid} appears more than once in senales")
        seen.add(sid)
        category = signal.get("categoria")
        if category not in CATEGORIES:
            errors.append(f"{sid}: categoria must be one of {', '.join(CATEGORIES)}")
        elif category == COVERED:
            anchors = as_list(signal.get("anclas"))
            if not anchors:
                errors.append(f"{sid}: a covered signal needs anclas Pxxx:HNN")
            for anchor in anchors:
                match = ANCHOR.match(str(anchor))
                if not match or match.group(1) not in activities:
                    errors.append(f"{sid}: ancla '{anchor}' is not Pxxx:HNN of an activity of {course}")
                elif match.group(2) not in descriptions[match.group(1)].highlight_ids():
                    errors.append(f"{sid}: {match.group(2)} is not a highlight of {match.group(1)}")
        elif category in NEEDS_REASON:
            if not str(signal.get("razon", "")).strip():
                errors.append(f"{sid}: a {category} signal needs a razon")
        elif category == IMPROVEMENT:
            ref = signal.get("actividad")
            proposal = signal.get("propuesta")
            if ref not in entries:
                errors.append(f"{sid}: actividad '{ref}' is not an audited activity")
            elif entries[ref].get("decision") != POINT_CHANGE:
                errors.append(f"{sid}: {ref} must take decision '{POINT_CHANGE}' to receive an improvement")
            elif proposal not in point_proposals.get(ref, {}) and proposal not in as_list(entries[ref].get("refuerza")):
                errors.append(f"{sid}: propuesta '{proposal}' is neither a new nor a reinforced proposal of {ref}")
            used_keys.add(str(proposal))
        elif category == NEW_ACTIVITY:
            course_reference(signal.get("propuesta"), sid)
            used_keys.add(str(signal.get("propuesta")))
    for sid in reqs.signal_ids:
        if sid not in seen:
            errors.append(f"{sid} has no category in senales")
    for ref, keys in point_proposals.items():
        for key in keys:
            if key not in used_keys:
                errors.append(f"{ref} {key}: no signal motivates this proposal")
    referenced = used_keys | {str(e.get("curso")) for e in entries.values()}
    for key in new_course:
        if key not in referenced:
            errors.append(f"nuevas {key}: no signal or activity motivates this course proposal")
    return errors, warnings


def validate_traceability(layout: Layout, course: str, targets: dict[str, Target] | None = None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = layout.shown(layout.traceability(course))
    try:
        trace = parse_traceability(layout.traceability(course))
    except ValueError as problem:
        return [str(problem)], warnings
    legacy = []
    for key, value in trace.entries.items():
        if isinstance(value, dict):
            if list(value) != TRACE_FIELDS:
                errors.append(f"{name}: {key} must have the fields {', '.join(TRACE_FIELDS)}, in order")
            if value.get("decision") not in DECISIONS:
                errors.append(f"{name}: {key} has decision '{value.get('decision')}'")
            for cid in as_list(value.get("competencias")):
                if not COMPETENCY_ID.match(cid):
                    errors.append(f"{name}: {key} cites '{cid}' among competencias; use Cnnn")
            for rid in as_list(value.get("resultados")):
                if targets is not None and rid not in targets:
                    errors.append(f"{name}: {key} cites {rid}, which is not an outcome of {course}")
        else:
            legacy.append(key)
            for ref in value or []:
                if COMPETENCY_ID.match(ref):
                    errors.append(f"{name}: {key} lists {ref} as a legacy capability; audited entries use a mapping")
    if legacy:
        warnings.append(f"{name}: legacy entries kept as they are: {', '.join(legacy)}")
    return errors, warnings
