from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Proposals, logs and their locations are owned by the auditing-activities
# skill; its layout and parsers are reused so that both skills read and
# write the same files the same way.
SKILLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS / "auditing-activities" / "scripts"))
from activity_lib import ROOT, Layout, activity_dirs, next_entry, parse_log, require_course  # noqa: E402,F401
from audit_lib import COURSE_TASK_REF, TASK_HEADING, TASK_REF, parse_tasks  # noqa: E402

DECISIONS = ("aprobada", "rechazada")
APPROVED, REJECTED = DECISIONS
PENDING_IMPLEMENTATION = "pendiente"


@dataclass(frozen=True)
class Proposal:
    scope: str
    id: str
    title: str
    state: str
    tasks: Path
    log: Path
    text: str


def activity_folders(layout: Layout, course: str) -> dict[str, Path]:
    return activity_dirs(layout, course)


def parse_target(target: str) -> tuple[str, str]:
    """`<curso>/<Pxxx>` reviews one activity; `<curso>` reviews the course proposals."""
    course, _, activity = target.strip("/").partition("/")
    if activity and not re.fullmatch(r"P\d{3}", activity):
        raise SystemExit(f"'{target}' must be <curso>/<Pxxx> or <curso>")
    return course, activity or course


def proposals(layout: Layout, course: str, only: str | None = None) -> list[Proposal]:
    """Every open proposal of the course: activity changes in order, then course changes."""
    require_course(layout, course)
    found: list[Proposal] = []
    folders = activity_folders(layout, course)
    if only and only != course and only not in folders:
        raise SystemExit(f"{only} is neither an activity of {course} nor the course itself")
    for aid, folder in folders.items():
        if only and only != aid:
            continue
        path = layout.tasks(course, folder.name)
        for entry in parse_tasks(path):
            if TASK_REF.match(entry.id):
                found.append(Proposal(aid, entry.id, entry.title, entry.state, path,
                                      layout.log(course, folder.name), entry_text(path, entry.id)))
    if not only or only == course:
        path = layout.course_tasks(course)
        for entry in parse_tasks(path):
            if COURSE_TASK_REF.match(entry.id):
                found.append(Proposal(course, entry.id, entry.title, entry.state, path,
                                      layout.course_log(course), entry_text(path, entry.id)))
    return found


def entry_bounds(text: str, task_id: str) -> tuple[int, int]:
    headings = list(TASK_HEADING.finditer(text))
    match = next((m for m in headings if m.group(1) == task_id), None)
    if match is None:
        raise SystemExit(f"{task_id} is not a proposal of this file")
    following = [m.start() for m in headings if m.start() > match.start()]
    return match.start(), following[0] if following else len(text)


def entry_text(path: Path, task_id: str) -> str:
    text = path.read_text(encoding="utf-8")
    start, end = entry_bounds(text, task_id)
    return text[start:end].strip()


def without_entry(text: str, task_id: str) -> str | None:
    """The tasks file once the proposal leaves it, or None when no proposal is left."""
    start, end = entry_bounds(text, task_id)
    remaining = (text[:start].rstrip("\n") + "\n\n" + text[end:].lstrip("\n")).rstrip("\n") + "\n"
    return remaining if TASK_HEADING.search(remaining) else None


def next_course_decision(log: Path, course: str) -> str:
    numbers = [int(n) for n in re.findall(rf"^## DEC\.{re.escape(course)}\.(\d{{2}})\s*$",
                                           log.read_text(encoding="utf-8"), re.M)] if log.exists() else []
    return f"DEC.{course}.{max(numbers, default=0) + 1:02d}"


def demoted(text: str) -> str:
    return re.sub(r"^#{2,3} ", "#### ", text, flags=re.M)


def decision_block(decision_id: str, proposal: Proposal, decision: str, reason: str,
                   executor: str, date: str) -> str:
    lines = [
        f"## {decision_id}",
        "",
        f"- **Fecha / executor:** {date} / {executor}.",
        f"- **Propuesta:** {proposal.id} — {proposal.title}",
        f"- **Decisión:** {decision}.",
        f"- **Razón:** {reason.strip()}",
    ]
    if decision == APPROVED:
        lines.append(f"- **Implementación:** {PENDING_IMPLEMENTATION}.")
    lines += ["", "### Propuesta discutida", "", demoted(proposal.text)]
    return "\n".join(lines) + "\n"


def decide(layout: Layout, course: str, scope: str, task_id: str, decision: str, reason: str,
           executor: str, date: str) -> dict[Path, str | None]:
    """The file changes of one decision: the proposal leaves tasks and enters the log."""
    if decision not in DECISIONS:
        raise SystemExit(f"decision must be one of {', '.join(DECISIONS)}")
    if not reason.strip():
        raise SystemExit("a decision needs its reason")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise SystemExit("date must be YYYY-MM-DD")
    proposal = next((p for p in proposals(layout, course, scope) if p.id == task_id and p.scope == scope), None)
    if proposal is None:
        raise SystemExit(f"{scope} has no open proposal {task_id}")
    if scope == course:
        decision_id = next_course_decision(proposal.log, course)
    else:
        decision_id = next_entry(parse_log(proposal.log), "DEC", scope)
    log_text = proposal.log.read_text(encoding="utf-8") if proposal.log.exists() else f"# Log — {scope}\n"
    block = decision_block(decision_id, proposal, decision, reason, executor, date)
    return {
        proposal.tasks: without_entry(proposal.tasks.read_text(encoding="utf-8"), task_id),
        proposal.log: log_text.rstrip("\n") + "\n\n" + block,
    }
