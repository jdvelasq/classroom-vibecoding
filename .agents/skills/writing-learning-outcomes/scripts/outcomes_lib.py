from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Competency files follow 02-competencies/format.md, owned by the
# mapping-competencies skill. Its parser also reads the learning-outcome
# files, which share the same YAML-header-plus-sections shape.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "mapping-competencies" / "scripts"))
from competency_lib import (  # noqa: E402
    Competency as Document,
    accepted,
    collapse,
    document_version,
    normalize,
    parse,
    read_index,
)

ROOT = Path(__file__).resolve().parents[4]

# The checks below implement exactly this version of
# 03-learning-outcomes/format.md; a new version must be reviewed here first.
SUPPORTED_FORMAT_VERSION = "0.1"

LEVEL = "especialización"
MIN_OUTCOMES = 6
MAX_OUTCOMES = 10
MAX_COMPETENCIES_PER_OUTCOME = 3
INCLUDED = "incluida"
NO_SOURCE = "Ninguna fuente"

HEADER_KEYS = ["id", "enunciado", "competencias", "nivel", "format_version", "fecha"]
SECTIONS = ["Enunciado", "Partes del enunciado", "Competencias", "Evaluación", "Trazabilidad"]
OPTIONAL_SECTIONS = ["Notas", "Pendientes"]
PARTS = ["Verbo", "Objeto", "Condición", "Nivel"]

PROFILE_KEYS = ["programa", "nivel", "format_version", "fecha"]
PROFILE_SECTIONS = ["Perfil de egreso", "Desempeños", "Alcance"]

NON_OBSERVABLE_VERBS = {
    "conocer", "comprender", "entender", "saber", "aprender", "familiarizarse",
    "apreciar", "valorar", "interiorizar", "asimilar",
}
BELOW_LEVEL_VERBS = {
    "definir", "describir", "enumerar", "identificar", "listar", "nombrar",
    "recordar", "reconocer", "repetir", "memorizar",
}

OUTCOME_ID = re.compile(r"^RA\d{2}$")
OUTCOME_REF = re.compile(r"\bRA\d{2}\b")
COMPETENCY_REF = re.compile(r"\bC\d{3}\b")
EVIDENCE_REF = re.compile(r"\bE\d{4}\b")


@dataclass(frozen=True)
class Layout:
    root: Path

    @property
    def outcomes_home(self) -> Path:
        return self.root / "03-learning-outcomes"

    @property
    def outcomes(self) -> Path:
        return self.outcomes_home / "outcomes"

    @property
    def profile(self) -> Path:
        return self.outcomes_home / "profile.md"

    @property
    def format(self) -> Path:
        return self.outcomes_home / "format.md"

    @property
    def map(self) -> Path:
        return self.root / "02-competencies" / "map"

    @property
    def index(self) -> Path:
        return self.root / "01-evidence" / "index.csv"


def require_supported_format(layout: Layout) -> str:
    version = document_version(layout.format)
    if version != SUPPORTED_FORMAT_VERSION:
        raise SystemExit(
            f"format.md is version {version}, but the scripts implement "
            f"{SUPPORTED_FORMAT_VERSION}. Update outcomes_lib.py and its tests first."
        )
    return version


def load_competencies(layout: Layout) -> dict[str, Document]:
    return {p.stem: parse(p) for p in sorted(layout.map.glob("C*.md"))}


def load_outcomes(layout: Layout) -> list[Document]:
    return [parse(p) for p in sorted(layout.outcomes.glob("RA*.md"))]


def included(competencies: dict[str, Document]) -> list[str]:
    return [cid for cid, c in competencies.items() if c.header.get("estado") == INCLUDED]


def next_id(layout: Layout) -> str:
    numbers = [int(p.stem[2:]) for p in layout.outcomes.glob("RA*.md") if OUTCOME_ID.match(p.stem)]
    return f"RA{max(numbers, default=0) + 1:02d}"


def labelled_bullets(document: Document, section: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for bullet in document.bullets(section):
        label, _, text = bullet.partition(":")
        found[label.strip()] = text.strip().rstrip(".").strip()
    return found


def table_rows(document: Document, section: str) -> list[list[str]]:
    rows = []
    for line in document.sections.get(section, "").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and COMPETENCY_REF.fullmatch(cells[0]):
            rows.append(cells)
    return rows


def performance_evidence_ids(competency: Document) -> set[str]:
    return set(EVIDENCE_REF.findall(competency.sections.get("Evidencia de desempeño", "")))


def first_word(statement: str) -> str:
    words = statement.split()
    return normalize(words[0]) if words else ""


def verb_problem(verb: str) -> str | None:
    if verb in NON_OBSERVABLE_VERBS:
        return f"'{verb}' is not observable"
    if verb in BELOW_LEVEL_VERBS:
        return f"'{verb}' sets a level below postgraduate"
    if not re.search(r"(ar|er|ir)$", verb):
        return f"'{verb}' is not an infinitive"
    return None


def validate_outcome(outcome: Document, competencies: dict[str, Document],
                     index: dict[str, dict[str, str]], format_version: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = outcome.path.name
    header = outcome.header

    def error(message: str) -> None:
        errors.append(f"{name}: {message}")

    missing = [k for k in HEADER_KEYS if k not in header]
    if missing:
        error(f"header lacks {', '.join(missing)}")
        return errors, warnings
    if not OUTCOME_ID.match(outcome.id) or outcome.path.stem != outcome.id:
        error(f"id '{outcome.id}' must be RA00-style and match the file name")
    if header["nivel"] != LEVEL:
        error(f"nivel must be '{LEVEL}'")
    if header["format_version"] != format_version:
        error(f"format_version is {header['format_version']}, format.md is {format_version}")

    required = [s for s in outcome.section_order if s in SECTIONS]
    if required != SECTIONS:
        error(f"sections must be, in order: {', '.join(SECTIONS)}")
    unknown = [s for s in outcome.section_order if s not in SECTIONS + OPTIONAL_SECTIONS]
    if unknown:
        error(f"unknown sections: {', '.join(unknown)}")

    statement = collapse(outcome.sections.get("Enunciado", ""))
    if collapse(str(header["enunciado"])) != statement:
        error("the header 'enunciado' differs from the Enunciado section")
    if not statement.endswith(".") or re.search(r"\.\s+\S", statement):
        error("the Enunciado must be a single sentence ending in a period")

    parts = labelled_bullets(outcome, "Partes del enunciado")
    if list(parts) != PARTS:
        error(f"Partes del enunciado must have, in order: {', '.join(PARTS)}")
    for part in PARTS:
        if part in parts and not parts[part]:
            error(f"the part '{part}' is empty")
    verb = normalize(parts.get("Verbo", ""))
    if verb and verb != first_word(statement):
        error(f"the Verbo '{verb}' is not the first word of the Enunciado")
    problem = verb_problem(verb) if verb else None
    if problem:
        error(f"verb {problem}")

    declared = list(header["competencias"])
    if not 1 <= len(declared) <= MAX_COMPETENCIES_PER_OUTCOME:
        error(f"an outcome covers 1 to {MAX_COMPETENCIES_PER_OUTCOME} competencies, not {len(declared)}")
    for cid in declared:
        competency = competencies.get(cid)
        if competency is None:
            error(f"{cid} is not in the competency map")
        elif competency.header.get("estado") != INCLUDED:
            error(f"{cid} is '{competency.header.get('estado')}'; only included competencies enter")
        elif str(competency.header.get("fecha", "")) > str(header["fecha"]):
            warnings.append(f"{name}: {cid} changed after this outcome was written; review it")
    described = labelled_bullets(outcome, "Competencias")
    if sorted(described) != sorted(declared):
        error("the Competencias section must have one bullet per header competency")

    assessments = outcome.bullets("Evaluación")
    if not assessments:
        error("Evaluación is empty")
    for item in assessments:
        cited = re.search(r"\[([^\]]*)\]\.?$", item)
        refs = set(COMPETENCY_REF.findall(cited.group(1))) if cited else set()
        if not refs:
            error(f"Evaluación item lacks its competencies in a final bracket: '{item[:60]}'")
        elif refs - set(declared):
            error(f"Evaluación item cites undeclared {', '.join(sorted(refs - set(declared)))}")

    rows = table_rows(outcome, "Trazabilidad")
    traced = {row[0] for row in rows}
    for cid in declared:
        if cid not in traced:
            error(f"{cid} has no row in Trazabilidad")
    for cid, evidence, product in rows:
        if cid not in declared:
            error(f"Trazabilidad cites undeclared {cid}")
            continue
        if not product:
            error(f"Trazabilidad row for {cid} lacks the evaluable product")
        competency = competencies.get(cid)
        if competency is None:
            continue
        available = performance_evidence_ids(competency)
        if evidence.startswith(NO_SOURCE):
            if available:
                error(f"{cid} has performance evidence; cite it instead of '{NO_SOURCE}'")
            else:
                warnings.append(f"{name}: {cid} has no performance evidence; the assessment is proposed, not traced")
            continue
        ids = EVIDENCE_REF.findall(evidence)
        if not ids:
            error(f"Trazabilidad row for {cid} cites no evidence id")
        for evidence_id in ids:
            if not accepted(index, evidence_id):
                error(f"{evidence_id} is not an accepted document in index.csv")
            elif evidence_id not in available:
                error(f"{evidence_id} is not in the Evidencia de desempeño of {cid}")
    return errors, warnings


def validate_profile(layout: Layout, outcome_ids: list[str], format_version: str) -> list[str]:
    if not layout.profile.exists():
        return ["profile.md is missing"]
    profile = parse(layout.profile)
    errors: list[str] = []
    missing = [k for k in PROFILE_KEYS if k not in profile.header]
    if missing:
        return [f"profile.md: header lacks {', '.join(missing)}"]
    if profile.header["nivel"] != LEVEL:
        errors.append(f"profile.md: nivel must be '{LEVEL}'")
    if profile.header["format_version"] != format_version:
        errors.append(f"profile.md: format_version is {profile.header['format_version']}, format.md is {format_version}")
    required = [s for s in profile.section_order if s in PROFILE_SECTIONS]
    if required != PROFILE_SECTIONS:
        errors.append(f"profile.md: sections must be, in order: {', '.join(PROFILE_SECTIONS)}")
    referenced = set(OUTCOME_REF.findall(profile.sections.get("Desempeños", "")))
    for outcome_id in sorted(set(outcome_ids) - referenced):
        errors.append(f"profile.md: Desempeños does not mention {outcome_id}")
    for outcome_id in sorted(referenced - set(outcome_ids)):
        errors.append(f"profile.md: Desempeños mentions {outcome_id}, which does not exist")
    return errors


def coverage(outcomes: list[Document], competencies: dict[str, Document]) -> dict[str, list[str]]:
    covered: dict[str, list[str]] = {cid: [] for cid in included(competencies)}
    for outcome in outcomes:
        for cid in outcome.header.get("competencias", []):
            if cid in covered:
                covered[cid].append(outcome.id)
    return covered


def validate_set(layout: Layout, outcomes: list[Document], competencies: dict[str, Document],
                 format_version: str) -> list[str]:
    errors: list[str] = []
    if not MIN_OUTCOMES <= len(outcomes) <= MAX_OUTCOMES:
        errors.append(f"the program has {len(outcomes)} outcomes; it needs {MIN_OUTCOMES} to {MAX_OUTCOMES}")
    for cid, outcome_ids in coverage(outcomes, competencies).items():
        if not outcome_ids:
            errors.append(f"{cid} is included in the map but no outcome covers it")
    errors += validate_profile(layout, [o.id for o in outcomes], format_version)
    return errors

