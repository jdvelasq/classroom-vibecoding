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
    parse_traceability,
    validate_activity,
    validate_log,
)

# The course files, the matrix and the competencies are owned by the
# mapping-curriculum skill and the skills it builds on; their parsers are
# reused so that every link of the chain reads those files the same way.
SKILLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS / "mapping-curriculum" / "scripts"))
import curriculum_lib as curriculum  # noqa: E402

CATEGORIES = ("cubierta", "marginal", "rechazada previamente", "fuera de alcance", "mejora", "actividad nueva")
COVERED, MARGINAL, REJECTED, OUT_OF_SCOPE, IMPROVEMENT, NEW_ACTIVITY = CATEGORIES
NEEDS_REASON = (MARGINAL, REJECTED, OUT_OF_SCOPE)
LEVELS = curriculum.LEVELS
UNDERGRADUATE_LEVEL = curriculum.INTRODUCE
DECISIONS = ("igual", "puntual", "curso")
SAME, POINT_CHANGE, COURSE_DECISION = DECISIONS
OUTSIDE_ACTIONS = ("conservar", "recortar")
KEEP, TRIM = OUTSIDE_ACTIONS
TASK_TYPES = ("encuadre", "producto/evidencia", "método", "caso/datos", "proceso", "pedagogía")
COURSE_TASK_TYPES = ("actividad nueva", "reorganización")
REJECTED_STATE = "rechazada"
PENDING_STATE = "pendiente de discusión"

# A point change reinforces the activity without lengthening it: at most one
# new proposal per activity in an audit, and a warning when the proposals
# still open on one activity exceed this number.
MAX_NEW_TASKS_PER_ACTIVITY = 1
MAX_OPEN_TASKS_PER_ACTIVITY = 3

JUSTIFICATION_FIELDS = ["metodologico", "tecnico", "pedagogico", "identidad"]
TASK_FIELDS = ["titulo", "tipo", "que_gana", "anclas", "alternativas", "no_regresion", "limite",
               "interacciones", *JUSTIFICATION_FIELDS, "aceptacion", "instrucciones"]
COURSE_TASK_FIELDS = ["titulo", "tipo", "contribucion", "posicion", "desplaza", "efecto", "caso", "producto",
                      *JUSTIFICATION_FIELDS, "aceptacion"]
AUDIT_KEYS = ["curso", "executor", "fecha", "estado", "sin_verificar", "defectos_del_curso",
              "senales", "actividades", "nuevas", "refuerza"]
COURSE_STATES = ("listo", "listo con condiciones", "no listo")

ACTIVITY_REF = re.compile(r"^(?:([a-z][a-z0-9-]*)/)?(P\d{3})$")
ANCHOR = re.compile(r"^((?:[a-z][a-z0-9-]*/)?P\d{3}):(H\d{2})$")
TASK_REF = re.compile(r"^T(\d{2})$")
COURSE_TASK_REF = re.compile(r"^N(\d{2})$")
TASK_HEADING = re.compile(r"^## ([TN]\d{2}) — (.+?)\s*$", re.M)
LEGACY_CAPABILITY = re.compile(r"^[a-z][a-z0-9-]*\.C\d{2}$")
COMPETENCY_ID = re.compile(r"^C\d{3}$")
SOURCES = re.compile(r"\s*\[[^\]]*\]\s*\.?\s*$")
TRACE_FIELDS = ["resultados", "competencias", "decision", "auditoria"]
SUPPORTED_TRACE_VERSION = SUPPORTED_FORMAT_VERSION
# Activity notebooks have no markdown cells by definition; a proposal may
# only mention markdown to discard it as an alternative.
MARKDOWN = re.compile(r"\bmarkdown\b", re.I)
MARKDOWN_ALLOWED_FIELDS = {"alternativas"}
# Activity tests show participation in class: they check that the artifacts
# a session generates exist in submission/, never recompute their content.
STRICT_TEST = re.compile(
    r"(prueba|test)[^.;]*(recalcul|recomput|recompon|reconstru|assert_frame_equal|assert_allclose)"
    r"|(recalcul|recomput|recompon|reconstru)[^.;]*(prueba|test)", re.I)
STRICT_TEST_FIELDS = {"aceptacion", "instrucciones"}


@dataclass(frozen=True)
class Target:
    id: str
    statement: str
    level: str
    assessment: str
    competencies: tuple[str, ...]
    program_outcomes: tuple[str, ...] = ()


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
    identity: dict[str, str] = field(default_factory=dict)
    required_knowledge: list[str] = field(default_factory=list)
    scope: list[str] = field(default_factory=list)
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


def level_rank(level: str) -> int:
    return LEVELS.index(level) if level in LEVELS else -1


def collapse_bullet(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def requirements(layout: Layout, course: str) -> Requirements:
    """What the course must teach: its course outcomes, at the level it owes them, and their competency items."""
    cl = curriculum_layout(layout)
    info = find_course(layout, course)
    competencies = curriculum.load_competencies(cl)
    if info.level == curriculum.POSTGRADUATE:
        files = curriculum.load_postgraduate(cl)
        folder = cl.postgraduate
    else:
        files = curriculum.load_undergraduate(cl)
        folder = cl.undergraduate
    if course not in files:
        raise SystemExit(f"{(folder / (course + '.md')).relative_to(layout.root)} does not exist; "
                         f"run mapping-curriculum first")
    document = files[course]
    outcomes = curriculum.parse_course_outcomes(document)
    if not outcomes:
        raise SystemExit(f"the course file of {course} has no course outcomes; run mapping-curriculum first")

    targets: list[Target] = []
    if info.level == curriculum.POSTGRADUATE:
        rows, problems = curriculum.read_matrix(cl)
        if problems:
            raise SystemExit("; ".join(problems))
        levels = {r.ra: r.nivel for r in rows if r.curso == course}
        program = curriculum.load_outcomes(cl)
        for outcome in outcomes:
            missing = [ra for ra in outcome.program_outcomes if ra not in levels or ra not in program]
            if missing:
                raise SystemExit(f"{course}/{outcome.id} derives from {', '.join(missing)}, which the matrix does "
                                 f"not assign to {course}; run mapping-curriculum first")
            cids = tuple(dict.fromkeys(c for ra in outcome.program_outcomes
                                       for c in program[ra].header.get("competencias", [])))
            level = max((levels[ra] for ra in outcome.program_outcomes), key=level_rank)
            targets.append(Target(f"{course}/{outcome.id}", outcome.statement, level, outcome.assessment,
                                  cids, outcome.program_outcomes))
    else:
        for outcome in outcomes:
            targets.append(Target(f"{course}/{outcome.id}", outcome.statement, UNDERGRADUATE_LEVEL,
                                  outcome.assessment, outcome.competencies))

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
    identity = dict(curriculum.labelled(document.sections.get(curriculum.IDENTITY, "")))
    return Requirements(
        course=course,
        level=info.level,
        source=(folder / f"{course}.md").relative_to(layout.root).as_posix(),
        targets=targets,
        items=items,
        identity=identity,
        required_knowledge=[collapse_bullet(b) for b in document.bullets(curriculum.REQUIRED_KNOWLEDGE)],
        scope=[collapse_bullet(b) for b in document.bullets("Alcance")],
        competency_dates=dates,
    )


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


def missing_anchors(entry: TaskEntry, description: Activity) -> list[str]:
    """Anchors a pending proposal names that the current description no longer has."""
    anchors = re.findall(r"\b[HS]\d{2}\b", labelled_value(entry.text, "Anclas actuales"))
    present = set(description.highlight_ids()) | set(description.surface_ids())
    return [a for a in dict.fromkeys(anchors) if a not in present]


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
    return [e for e in parse_tasks(layout.tasks(activity.owner, activity.folder.name)) if TASK_REF.match(e.id)]


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
    """Decided course proposals leave the tasks file; their ids live on in the course log."""
    numbers = {int(e.id[1:]) for e in course_tasks(layout, course)}
    log = layout.course_log(course)
    if log.exists():
        numbers |= {int(n) for n in re.findall(r"\bN(\d{2})\b", log.read_text(encoding="utf-8"))}
    return numbers


def course_decisions(layout: Layout, course: str) -> list[str]:
    log = layout.course_log(course)
    if not log.exists():
        return []
    return re.findall(rf"^## (DEC\.{re.escape(course)}\.\d{{2}})\s*$", log.read_text(encoding="utf-8"), re.M)


def fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_audit(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: the audit must be a JSON object")
    return data


def as_list(value: object) -> list:
    return value if isinstance(value, list) else []


def anchor_parts(anchor: object) -> tuple[str, str]:
    """An anchor is {"hito": "P103:H01", "nivel": "introduce"}."""
    if isinstance(anchor, dict):
        return str(anchor.get("hito", "")), str(anchor.get("nivel", ""))
    return str(anchor), ""


def validate_proposal(proposal: dict, fields: list[str], where: str) -> list[str]:
    errors = []
    for name in fields:
        if name not in MARKDOWN_ALLOWED_FIELDS and MARKDOWN.search(str(proposal.get(name, ""))):
            errors.append(f"{where}: {name} mentions markdown; activity notebooks have no markdown cells")
        if name in STRICT_TEST_FIELDS and STRICT_TEST.search(str(proposal.get(name, ""))):
            errors.append(f"{where}: {name} asks to recompute an artifact; activity tests only check that "
                          f"the artifacts of submission/ exist")
    for name in fields:
        value = proposal.get(name)
        if name == "anclas":
            if not as_list(value):
                errors.append(f"{where}: anclas is empty")
        elif not str(value or "").strip():
            errors.append(f"{where}: {name} is empty")
    return errors


def validate_audit(layout: Layout, audit: dict, course: str) -> tuple[list[str], list[str]]:
    """Checks the model's audit against what the course must teach and what its activities achieve."""
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
    if audit.get("estado") not in COURSE_STATES:
        errors.append(f"estado must be one of {', '.join(COURSE_STATES)}")
    for name in ("sin_verificar", "defectos_del_curso"):
        if not isinstance(audit.get(name, []), list) or not all(str(x).strip() for x in audit.get(name, [])):
            errors.append(f"{name} must be a list of non-empty texts")

    reqs = requirements(layout, course)
    activities = {a.ref: a for a in course_activities(layout, course)}
    for activity in activities.values():
        errors += describe_problems(layout, activity)
    if errors:
        return errors, warnings
    descriptions = {ref: load_description(layout, a) for ref, a in activities.items()}
    targets = {t.id: t for t in reqs.targets}
    open_course = {e.id for e in open_tasks(course_tasks(layout, course))}

    new_course: dict[str, dict] = {}
    for proposal in as_list(audit.get("nuevas")):
        key = proposal.get("clave") if isinstance(proposal, dict) else None
        if not key or key in new_course:
            errors.append("every entry of nuevas needs a unique clave")
            continue
        new_course[key] = proposal
        errors += validate_proposal(proposal, COURSE_TASK_FIELDS, f"nuevas {key}")
        if proposal.get("tipo") not in COURSE_TASK_TYPES:
            errors.append(f"nuevas {key}: tipo must be one of {', '.join(COURSE_TASK_TYPES)}")
    for ref in as_list(audit.get("refuerza")):
        if ref not in open_course:
            errors.append(f"refuerza cites {ref}, which is not an open course proposal of {course}")

    def course_reference(ref: object, where: str) -> None:
        if ref not in new_course and ref not in open_course:
            errors.append(f"{where} cites the course proposal '{ref}', which is neither in nuevas nor open")

    entries: dict[str, dict] = {}
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
    open_by_activity: dict[str, set[str]] = {}
    for ref, entry in entries.items():
        activity = activities[ref]
        description = descriptions[ref]
        decision = entry.get("decision")
        results = as_list(entry.get("resultados"))
        competencies = as_list(entry.get("competencias"))
        proposals = as_list(entry.get("propuestas"))
        reinforced = as_list(entry.get("refuerza"))
        if decision not in DECISIONS:
            errors.append(f"{ref}: decision must be one of {', '.join(DECISIONS)}")
        if not str(entry.get("razon", "")).strip():
            errors.append(f"{ref}: razon is empty")
        for rid in results:
            if rid not in targets:
                errors.append(f"{ref}: {rid} is not a course outcome of {course}")
        allowed = {c for rid in results if rid in targets for c in targets[rid].competencies}
        for cid in competencies:
            if LEGACY_CAPABILITY.match(str(cid)) or not COMPETENCY_ID.match(str(cid)):
                errors.append(f"{ref}: '{cid}' is not a competency id Cnnn")
            elif cid not in allowed:
                errors.append(f"{ref}: {cid} is not a competency of its resultados")
        if results and not competencies:
            errors.append(f"{ref}: resultados need at least one of their competencias")
        if not results and decision != COURSE_DECISION:
            errors.append(f"{ref}: an activity that serves no course outcome only admits decision '{COURSE_DECISION}'")

        open_ids = {e.id for e in open_tasks(activity_tasks(layout, activity))}
        open_by_activity[ref] = open_ids
        for task in reinforced:
            if task not in open_ids:
                errors.append(f"{ref}: refuerza cites {task}, which is not an open proposal of {activity.id}")
        obsolete = {}
        for item in as_list(entry.get("obsoletas")):
            task = item.get("propuesta") if isinstance(item, dict) else None
            if task not in open_ids:
                errors.append(f"{ref}: obsoletas cites '{task}', which is not an open proposal of {activity.id}")
            elif not str(item.get("razon", "")).strip():
                errors.append(f"{ref}: obsoleta {task} needs a razon")
            if task in reinforced:
                errors.append(f"{ref}: {task} cannot be reinforced and marked obsolete at once")
            obsolete[task] = item
        for task_entry in open_tasks(activity_tasks(layout, activity)):
            gone = missing_anchors(task_entry, description)
            if gone and task_entry.id not in obsolete:
                warnings.append(f"{ref} {task_entry.id}: its anchors {', '.join(gone)} no longer exist; "
                                f"mark it in obsoletas if it no longer applies")
        keys: dict[str, dict] = {}
        for proposal in proposals:
            key = proposal.get("clave") if isinstance(proposal, dict) else None
            if not key or key in keys or key in new_course:
                errors.append(f"{ref}: every proposal needs a clave unique in the audit")
                continue
            keys[key] = proposal
            errors += validate_proposal(proposal, TASK_FIELDS, f"{ref} {key}")
            if proposal.get("tipo") not in TASK_TYPES:
                errors.append(f"{ref} {key}: tipo must be one of {', '.join(TASK_TYPES)}")
            for anchor in as_list(proposal.get("anclas")):
                if anchor not in description.highlight_ids() and anchor not in description.surface_ids():
                    errors.append(f"{ref} {key}: ancla {anchor} is not a highlight or surface of {activity.id}")
        point_proposals[ref] = keys

        if decision == SAME and (proposals or reinforced or entry.get("curso")):
            errors.append(f"{ref}: decision '{SAME}' takes no proposal")
        if decision == POINT_CHANGE:
            if len(proposals) > MAX_NEW_TASKS_PER_ACTIVITY:
                errors.append(
                    f"{ref}: a point change is one bounded change; {len(proposals)} new proposals lengthen "
                    f"the activity, so the rest belongs to a course decision"
                )
            if not proposals and not reinforced:
                errors.append(f"{ref}: decision '{POINT_CHANGE}' needs a new proposal or an open one to reinforce")
            if entry.get("curso"):
                errors.append(f"{ref}: decision '{POINT_CHANGE}' takes no course proposal")
            if len(open_ids) + len(proposals) > MAX_OPEN_TASKS_PER_ACTIVITY:
                warnings.append(
                    f"{ref}: {len(open_ids) + len(proposals)} open proposals; check that the activity stays a short, "
                    f"well-defined problem"
                )
        if decision == COURSE_DECISION:
            if proposals or reinforced:
                errors.append(f"{ref}: decision '{COURSE_DECISION}' takes no activity proposal")
            course_reference(entry.get("curso"), ref)

    anchored: dict[str, set[str]] = {ref: set() for ref in activities}
    seen: set[str] = set()
    used_keys: set[str] = set()
    for signal in as_list(audit.get("senales")):
        sid = signal.get("id") if isinstance(signal, dict) else None
        if sid not in reqs.signal_ids:
            errors.append(f"senales cites '{sid}', which is not a course outcome or item of {course}")
            continue
        if sid in seen:
            errors.append(f"{sid} appears more than once in senales")
        seen.add(sid)
        category = signal.get("categoria")
        reached = -1
        for anchor in as_list(signal.get("anclas")):
            hito, level = anchor_parts(anchor)
            match = ANCHOR.match(hito)
            if not match or match.group(1) not in activities:
                errors.append(f"{sid}: ancla '{hito}' is not Pxxx:HNN of an activity of {course}")
            elif match.group(2) not in descriptions[match.group(1)].highlight_ids():
                errors.append(f"{sid}: {match.group(2)} is not a highlight of {match.group(1)}")
            else:
                anchored[match.group(1)].add(match.group(2))
            if level not in LEVELS:
                errors.append(f"{sid}: ancla '{hito}' needs a nivel among {', '.join(LEVELS)}")
            reached = max(reached, level_rank(level))
        if category not in CATEGORIES:
            errors.append(f"{sid}: categoria must be one of {', '.join(CATEGORIES)}")
        elif category == COVERED:
            if not as_list(signal.get("anclas")):
                errors.append(f"{sid}: a covered signal needs anclas")
            elif sid in targets and reached < level_rank(targets[sid].level):
                errors.append(
                    f"{sid}: the course owes it at '{targets[sid].level}', but its anclas reach less; "
                    f"classify it as {IMPROVEMENT} or {NEW_ACTIVITY}"
                )
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

    for ref, entry in entries.items():
        outside: dict[str, dict] = {}
        for item in as_list(entry.get("fuera")):
            hid = item.get("hito") if isinstance(item, dict) else None
            where = f"{ref} {hid}"
            if hid not in descriptions[ref].highlight_ids():
                errors.append(f"{ref}: fuera cites '{hid}', which is not a highlight of {activities[ref].id}")
                continue
            outside[hid] = item
            if hid in anchored[ref]:
                errors.append(f"{where} is anchored by a signal and listed in fuera at once")
            if item.get("accion") not in OUTSIDE_ACTIONS:
                errors.append(f"{where}: accion must be one of {', '.join(OUTSIDE_ACTIONS)}")
            if not str(item.get("razon", "")).strip():
                errors.append(f"{where}: razon is empty")
            if item.get("accion") == TRIM:
                target = item.get("propuesta")
                known = (set(point_proposals.get(ref, {})) | set(as_list(entry.get("refuerza")))
                         | set(new_course) | open_course)
                if target not in known:
                    errors.append(f"{where}: recortar needs a propuesta of {ref} or a course proposal")
                used_keys.add(str(target))
        for hid in descriptions[ref].highlight_ids():
            if hid not in anchored[ref] and hid not in outside:
                errors.append(f"{ref} {hid} serves no signal; anchor it or list it in fuera")

    for ref, keys in point_proposals.items():
        for key in keys:
            if key not in used_keys:
                errors.append(f"{ref} {key}: no signal or highlight motivates this proposal")
    referenced = used_keys | {str(e.get("curso")) for e in entries.values()}
    for key in new_course:
        if key not in referenced:
            errors.append(f"nuevas {key}: no signal, activity or highlight motivates this course proposal")
    return errors, warnings


def validate_traceability(layout: Layout, course: str,
                          targets: dict[str, Target] | None = None) -> tuple[list[str], list[str]]:
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
                    errors.append(f"{name}: {key} cites {rid}, which is not a course outcome of {course}")
        else:
            legacy.append(key)
            for ref in value or []:
                if COMPETENCY_ID.match(ref):
                    errors.append(f"{name}: {key} lists {ref} as a legacy capability; audited entries use a mapping")
    if legacy:
        warnings.append(f"{name}: legacy entries kept as they are: {', '.join(legacy)}")
    return errors, warnings
