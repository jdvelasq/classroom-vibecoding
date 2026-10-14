from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Competency and learning-outcome files are owned by the mapping-competencies
# and writing-learning-outcomes skills. Their parser and verb lists are
# reused so that the three links of the chain read files the same way.
SKILLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS / "mapping-competencies" / "scripts"))
sys.path.insert(0, str(SKILLS / "writing-learning-outcomes" / "scripts"))
from competency_lib import (  # noqa: E402
    Competency as Document,
    collapse,
    document_version,
    domain_subfields,
    normalize,
    parse,
)
from outcomes_lib import NON_OBSERVABLE_VERBS, OUTCOME_ID, OUTCOME_REF  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]

# The checks below implement exactly this version of 04-curriculum/format.md;
# a new version must be reviewed here first.
SUPPORTED_FORMAT_VERSION = "0.1"

POSTGRADUATE = "posgrado"
UNDERGRADUATE = "pregrado"
STATUSES = ("vigente", "propuesto")
LEVELS = ("introduce", "desarrolla", "domina")
INTRODUCE, DEVELOP, MASTER = LEVELS
INCLUDED = "incluida"
MIN_COURSE_OUTCOMES = 3
MAX_COURSE_OUTCOMES = 6
MAX_COMPETENCIES_PER_COURSE_OUTCOME = 3

COURSE_COLUMNS = ["Carpeta", "Curso", "Nivel", "Estado", "Subcampos"]
COURSES_SECTIONS = ["Lista de cursos", "Propósito", "Continuidad"]
MATRIX_COLUMNS = ["ra", "curso", "nivel", "aporte", "fecha"]
UNDERGRADUATE_KEYS = ["curso", "nivel", "format_version", "fecha"]
UNDERGRADUATE_SECTIONS = ["Propósito", "Resultados del curso", "Alcance"]
COURSE_OUTCOME_LABELS = ["Enunciado", "Competencias", "Evaluación"]

FOLDER = re.compile(r"^[a-z][a-z0-9-]*$")
COURSE_OUTCOME_ID = re.compile(r"^RC\d{2}$")
COMPETENCY_REF = re.compile(r"\bC\d{3}\b")


@dataclass(frozen=True)
class Layout:
    root: Path

    @property
    def home(self) -> Path:
        return self.root / "04-curriculum"

    @property
    def format(self) -> Path:
        return self.home / "format.md"

    @property
    def courses(self) -> Path:
        return self.home / "courses.md"

    @property
    def matrix(self) -> Path:
        return self.home / "matrix.csv"

    @property
    def undergraduate(self) -> Path:
        return self.home / "undergraduate"

    @property
    def outcomes(self) -> Path:
        return self.root / "03-learning-outcomes" / "outcomes"

    @property
    def map(self) -> Path:
        return self.root / "02-competencies" / "map"

    @property
    def domain(self) -> Path:
        return self.root / "01-evidence" / "domain.md"


@dataclass(frozen=True)
class Course:
    folder: str
    name: str
    level: str
    status: str
    subfields: tuple[str, ...]


@dataclass(frozen=True)
class MatrixRow:
    ra: str
    curso: str
    nivel: str
    aporte: str
    fecha: str


@dataclass(frozen=True)
class CourseOutcome:
    id: str
    title: str
    statement: str
    competencies: tuple[str, ...]
    assessment: str
    labels: tuple[str, ...]


def require_supported_format(layout: Layout) -> str:
    version = document_version(layout.format)
    if version != SUPPORTED_FORMAT_VERSION:
        raise SystemExit(
            f"format.md is version {version}, but the scripts implement "
            f"{SUPPORTED_FORMAT_VERSION}. Update curriculum_lib.py and its tests first."
        )
    return version


def load_competencies(layout: Layout) -> dict[str, Document]:
    return {p.stem: parse(p) for p in sorted(layout.map.glob("C*.md"))}


def load_outcomes(layout: Layout) -> dict[str, Document]:
    return {p.stem: parse(p) for p in sorted(layout.outcomes.glob("RA*.md")) if OUTCOME_ID.match(p.stem)}


def course_subfields(layout: Layout) -> list[str]:
    return domain_subfields(layout)


def table_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_courses(document: Document) -> list[Course]:
    courses = []
    for line in document.sections.get("Lista de cursos", "").splitlines():
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if len(cells) != len(COURSE_COLUMNS) or cells == COURSE_COLUMNS or set(cells[0]) <= {"-", ":"}:
            continue
        subfields = tuple(s.strip() for s in cells[4].split(";") if s.strip())
        courses.append(Course(cells[0], cells[1], cells[2], cells[3], subfields))
    return courses


def load_courses(layout: Layout) -> tuple[Document, list[Course]]:
    document = parse(layout.courses)
    return document, parse_courses(document)


def postgraduate(courses: list[Course]) -> list[Course]:
    return [c for c in courses if c.level == POSTGRADUATE]


def undergraduate(courses: list[Course]) -> list[Course]:
    return [c for c in courses if c.level == UNDERGRADUATE]


def purpose_headings(document: Document) -> list[str]:
    return re.findall(r"^### (.+?)\s*$", document.sections.get("Propósito", ""), re.M)


def validate_courses(document: Document, courses: list[Course], subfields: list[str],
                     format_version: str) -> list[str]:
    errors: list[str] = []
    if document.header.get("format_version") != format_version:
        errors.append(f"courses.md: format_version is {document.header.get('format_version')}, format.md is {format_version}")
    required = [s for s in document.section_order if s in COURSES_SECTIONS]
    if required != COURSES_SECTIONS:
        errors.append(f"courses.md: sections must be, in order: {', '.join(COURSES_SECTIONS)}")
    if not courses:
        return errors + ["courses.md: the course table is empty or malformed"]
    folders = [c.folder for c in courses]
    for folder in sorted({f for f in folders if folders.count(f) > 1}):
        errors.append(f"courses.md: folder '{folder}' appears more than once")
    purposes = purpose_headings(document)
    for course in courses:
        if not FOLDER.match(course.folder):
            errors.append(f"courses.md: folder '{course.folder}' must be lowercase letters, digits and hyphens")
        if course.level not in (POSTGRADUATE, UNDERGRADUATE):
            errors.append(f"courses.md: {course.folder} has level '{course.level}'; use {POSTGRADUATE} or {UNDERGRADUATE}")
        if course.status not in STATUSES:
            errors.append(f"courses.md: {course.folder} has status '{course.status}'; use {' or '.join(STATUSES)}")
        if not course.subfields:
            errors.append(f"courses.md: {course.folder} has no subfields")
        for subfield in course.subfields:
            if subfield not in subfields:
                errors.append(f"courses.md: {course.folder} cites '{subfield}', which is not a subfield of domain.md")
        if course.folder not in purposes:
            errors.append(f"courses.md: Propósito lacks a '### {course.folder}' subsection")
    taught = {s for c in courses for s in c.subfields}
    for subfield in subfields:
        if subfield not in taught:
            errors.append(f"courses.md: no course teaches the subfield '{subfield}'")
    if not postgraduate(courses):
        errors.append("courses.md: there is no postgraduate course")
    return errors


def read_matrix(layout: Layout) -> tuple[list[MatrixRow], list[str]]:
    if not layout.matrix.exists():
        return [], []
    with layout.matrix.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != MATRIX_COLUMNS:
            return [], [f"matrix.csv: columns must be {','.join(MATRIX_COLUMNS)}"]
        rows = [MatrixRow(*(collapse(r[c] or "") for c in MATRIX_COLUMNS)) for r in reader]
    return rows, []


def subfields_of(outcome: Document, competencies: dict[str, Document]) -> set[str]:
    found: set[str] = set()
    for cid in outcome.header.get("competencias", []):
        found.update(competencies[cid].header.get("subcampos", []) if cid in competencies else [])
    return found


def validate_matrix(rows: list[MatrixRow], courses: list[Course], outcomes: dict[str, Document],
                    competencies: dict[str, Document]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    graduate = postgraduate(courses)
    order = {c.folder: i for i, c in enumerate(graduate)}
    by_folder = {c.folder: c for c in courses}
    seen: set[tuple[str, str]] = set()
    valid: list[MatrixRow] = []

    for number, row in enumerate(rows, start=2):
        where = f"matrix.csv line {number}"
        problems = []
        if row.ra not in outcomes:
            problems.append(f"{row.ra or 'an empty ra'} is not a learning outcome in 03-learning-outcomes")
        if row.curso not in order:
            course = by_folder.get(row.curso)
            if course is not None:
                problems.append(f"{row.curso} is a {course.level} course; the matrix only takes postgraduate courses")
            else:
                problems.append(f"{row.curso or 'an empty curso'} is not a course in courses.md")
        if row.nivel not in LEVELS:
            problems.append(f"nivel '{row.nivel}' must be one of {', '.join(LEVELS)}")
        if not row.aporte:
            problems.append("aporte is empty")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row.fecha):
            problems.append(f"fecha '{row.fecha}' must be YYYY-MM-DD")
        if (row.ra, row.curso) in seen:
            problems.append(f"{row.ra} × {row.curso} appears more than once")
        seen.add((row.ra, row.curso))
        errors += [f"{where}: {p}" for p in problems]
        if problems:
            continue
        valid.append(row)
        outcome = outcomes[row.ra]
        if str(outcome.header.get("fecha", "")) > row.fecha:
            warnings.append(f"{where}: {row.ra} changed after this row was set; review it")
        shared = set(by_folder[row.curso].subfields) & subfields_of(outcome, competencies)
        if not shared:
            warnings.append(f"{where}: {row.curso} shares no subfield with the competencies of {row.ra}; justify it in aporte")

    for ra in outcomes:
        path = sorted((r for r in valid if r.ra == ra), key=lambda r: order[r.curso])
        if not any(r.nivel == MASTER for r in path):
            errors.append(f"{ra} never reaches '{MASTER}' in a postgraduate course")
        if path and path[0].nivel == DEVELOP:
            errors.append(
                f"{ra} first appears in {path[0].curso} as '{DEVELOP}'; no earlier postgraduate course "
                f"introduces it, so the course would not be self-contained"
            )
        mastered = False
        for r in path:
            if mastered and r.nivel == INTRODUCE:
                warnings.append(f"{ra} is mastered before {r.curso}, which marks it '{INTRODUCE}' again")
            mastered = mastered or r.nivel == MASTER
    for course in graduate:
        if not any(r.curso == course.folder for r in valid):
            errors.append(f"{course.folder} has no learning outcome in the matrix")
    return errors, warnings


def matrix_view(rows: list[MatrixRow], courses: list[Course], outcomes: dict[str, Document]) -> list[str]:
    graduate = [c.folder for c in postgraduate(courses)]
    cell = {(r.ra, r.curso): r.nivel for r in rows}
    width = max([len(f) for f in graduate] + [len(level) for level in LEVELS])
    lines = ["ra    " + " ".join(f.ljust(width) for f in graduate)]
    for ra in sorted(set(outcomes) | {r.ra for r in rows}):
        lines.append(ra.ljust(6) + " ".join(cell.get((ra, f), "·").ljust(width) for f in graduate))
    return lines


def labelled(block: str) -> list[tuple[str, str]]:
    items: list[str] = []
    for line in block.splitlines():
        if line.startswith("- "):
            items.append(line[2:])
        elif line.startswith("  ") and items:
            items[-1] += " " + line.strip()
    pairs = []
    for item in items:
        label, _, text = item.partition(":")
        pairs.append((label.strip(), collapse(text)))
    return pairs


def parse_course_outcomes(document: Document) -> list[CourseOutcome]:
    text = document.sections.get("Resultados del curso", "")
    found = []
    for match in re.finditer(r"^### (\S+?)\.\s*(.*?)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
        pairs = labelled(match.group(3))
        values = dict(pairs)
        found.append(CourseOutcome(
            id=match.group(1),
            title=match.group(2).strip(),
            statement=values.get("Enunciado", ""),
            competencies=tuple(COMPETENCY_REF.findall(values.get("Competencias", ""))),
            assessment=values.get("Evaluación", ""),
            labels=tuple(label for label, _ in pairs),
        ))
    return found


def load_undergraduate(layout: Layout) -> dict[str, Document]:
    return {p.stem: parse(p) for p in sorted(layout.undergraduate.glob("*.md"))}


def first_word(statement: str) -> str:
    words = statement.split()
    return normalize(words[0]) if words else ""


def validate_undergraduate(document: Document, courses: list[Course], competencies: dict[str, Document],
                           format_version: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = f"undergraduate/{document.path.name}"
    header = document.header

    def error(message: str) -> None:
        errors.append(f"{name}: {message}")

    missing = [k for k in UNDERGRADUATE_KEYS if k not in header]
    if missing:
        error(f"header lacks {', '.join(missing)}")
        return errors, warnings
    course = next((c for c in undergraduate(courses) if c.folder == header["curso"]), None)
    if course is None:
        error(f"curso '{header['curso']}' is not an undergraduate course in courses.md")
        return errors, warnings
    if document.path.stem != course.folder:
        error(f"the file must be named {course.folder}.md")
    if header["nivel"] != UNDERGRADUATE:
        error(f"nivel must be '{UNDERGRADUATE}'")
    if header["format_version"] != format_version:
        error(f"format_version is {header['format_version']}, format.md is {format_version}")
    required = [s for s in document.section_order if s in UNDERGRADUATE_SECTIONS]
    if required != UNDERGRADUATE_SECTIONS:
        error(f"sections must be, in order: {', '.join(UNDERGRADUATE_SECTIONS)}")
    if OUTCOME_REF.search(document.body):
        error("an undergraduate course does not cite the program's learning outcomes (RA00)")

    outcomes = parse_course_outcomes(document)
    if not MIN_COURSE_OUTCOMES <= len(outcomes) <= MAX_COURSE_OUTCOMES:
        error(f"the course has {len(outcomes)} outcomes; it needs {MIN_COURSE_OUTCOMES} to {MAX_COURSE_OUTCOMES}")
    expected = [f"RC{i:02d}" for i in range(1, len(outcomes) + 1)]
    if [o.id for o in outcomes] != expected:
        error(f"course outcome ids must be {', '.join(expected) or 'RC01, …'}, in order")

    covered: set[str] = set()
    for outcome in outcomes:
        label = f"{course.folder}/{outcome.id}"
        if list(outcome.labels) != COURSE_OUTCOME_LABELS:
            error(f"{label} must have the bullets {', '.join(COURSE_OUTCOME_LABELS)}, in order")
        statement = outcome.statement
        if not statement.endswith(".") or re.search(r"\.\s+\S", statement):
            error(f"{label}: the Enunciado must be a single sentence ending in a period")
        verb = first_word(statement)
        if verb in NON_OBSERVABLE_VERBS:
            error(f"{label}: verb '{verb}' is not observable")
        elif verb and not re.search(r"(ar|er|ir)$", verb):
            error(f"{label}: '{verb}' is not an infinitive")
        if not 1 <= len(outcome.competencies) <= MAX_COMPETENCIES_PER_COURSE_OUTCOME:
            error(f"{label} covers 1 to {MAX_COMPETENCIES_PER_COURSE_OUTCOME} competencies, not {len(outcome.competencies)}")
        for cid in outcome.competencies:
            competency = competencies.get(cid)
            if competency is None:
                error(f"{label}: {cid} is not in the competency map")
            elif competency.header.get("estado") != INCLUDED:
                error(f"{label}: {cid} is '{competency.header.get('estado')}'; only included competencies enter")
            else:
                covered.update(competency.header.get("subcampos", []))
                if str(competency.header.get("fecha", "")) > str(header["fecha"]):
                    warnings.append(f"{name}: {cid} changed after {label} was written; review it")
        cited = re.search(r"\[([^\]]*)\]\.?$", outcome.assessment)
        refs = set(COMPETENCY_REF.findall(cited.group(1))) if cited else set()
        if not refs:
            error(f"{label}: Evaluación lacks its competencies in a final bracket")
        elif refs - set(outcome.competencies):
            error(f"{label}: Evaluación cites undeclared {', '.join(sorted(refs - set(outcome.competencies)))}")
    for subfield in course.subfields:
        if subfield not in covered:
            error(f"no course outcome covers the subfield '{subfield}', which courses.md assigns to {course.folder}")
    return errors, warnings
