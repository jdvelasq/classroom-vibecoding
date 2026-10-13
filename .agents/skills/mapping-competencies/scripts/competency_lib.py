from __future__ import annotations

import csv
import datetime as dt
import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

# The parser, the consensus rule and the checks below implement exactly this
# version of 02-competencies/format.md; a new version must be reviewed here
# before the map can be validated against it.
SUPPORTED_FORMAT_VERSION = "0.3"

STATES = ("incluida", "candidata", "retirada")
EXPLICIT = "explícito"
KNOWLEDGE_ONLY = "solo conocimientos"
INFERRED = re.compile(r"^inferido \((I\d+)\)$")
TRANSVERSAL = "IA generativa y agéntica (transversal)"
SECTIONS = [
    "Enunciado",
    "Subcampos",
    "Conocimientos",
    "Habilidades",
    "Fuentes",
    "Evidencia de desempeño",
]
OPTIONAL_SECTIONS = ["Notas de calibración", "Pendientes"]
HEADER_KEYS = ["id", "enunciado", "subcampos", "estado", "consenso",
               "format_version", "domain_version", "fecha"]
CONSENSUS_KEYS = ["emisores", "explicitos", "inferidos", "actual"]
LEDGER_COLUMNS = ["id", "format_version", "domain_version", "date", "competencias"]
EVIDENCE_ID = re.compile(r"\bE\d{4}\b")
COMPETENCY_ID = re.compile(r"^C\d{3}$")


@dataclass(frozen=True)
class Layout:
    root: Path

    @property
    def competencies(self) -> Path:
        return self.root / "02-competencies"

    @property
    def map(self) -> Path:
        return self.competencies / "map"

    @property
    def format(self) -> Path:
        return self.competencies / "format.md"

    @property
    def ledger(self) -> Path:
        return self.competencies / "mapped.csv"

    @property
    def index(self) -> Path:
        return self.root / "01-evidence" / "index.csv"

    @property
    def domain(self) -> Path:
        return self.root / "01-evidence" / "domain.md"

    def shown(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def evidence_text(self, row: dict[str, str]) -> str:
        # Accepted PDFs live in pdf/<category>/ with their conversion in
        # md/<category>/; syntheses are indexed by their own .md file.
        file = row["file"]
        if file.endswith(".md"):
            return file
        return file.replace("01-evidence/pdf/", "01-evidence/md/", 1)[: -len(".pdf")] + ".md"


def document_version(path: Path) -> str:
    match = re.search(r"^Versión\s+(\S+)", path.read_text(encoding="utf-8"), re.M)
    if not match:
        raise SystemExit(f"No version line found in {path}")
    return match.group(1)


def require_supported_format(layout: Layout) -> str:
    version = document_version(layout.format)
    if version != SUPPORTED_FORMAT_VERSION:
        raise SystemExit(
            f"format.md is version {version}, but the scripts implement "
            f"{SUPPORTED_FORMAT_VERSION}. Update competency_lib.py and its tests first."
        )
    return version


def normalize(text: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", ascii_text.lower()).strip()


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def domain_subfields(layout: Layout) -> list[str]:
    text = layout.domain.read_text(encoding="utf-8")
    block = re.search(r"^## Subcampos\n(.*?)(?=^## )", text, re.M | re.S)
    if not block:
        raise SystemExit("No '## Subcampos' section found in domain.md")
    names = []
    for line in block.group(1).splitlines():
        if line.startswith("- "):
            name = re.sub(r"\s*\(.*?\)", "", line[2:]).strip().rstrip(".")
            names.append(name[0].lower() + name[1:])
    return names + [TRANSVERSAL]


def read_index(layout: Layout) -> dict[str, dict[str, str]]:
    with layout.index.open(newline="", encoding="utf-8") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def accepted(index: dict[str, dict[str, str]], evidence_id: str) -> bool:
    return index.get(evidence_id, {}).get("decision") == "accept"


@dataclass
class SourceRow:
    id: str
    issuer: str
    role: str
    location: str
    support: str

    @property
    def explicit(self) -> bool:
        return self.support == EXPLICIT

    @property
    def chain(self) -> str | None:
        match = INFERRED.match(self.support)
        return match.group(1) if match else None


@dataclass
class Competency:
    path: Path
    header: dict[str, object]
    header_lines: list[str]
    body: str
    sections: dict[str, str] = field(default_factory=dict)
    section_order: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        return str(self.header.get("id", ""))

    def bullets(self, section: str) -> list[str]:
        items: list[str] = []
        for line in self.sections.get(section, "").splitlines():
            if line.startswith("- "):
                items.append(line[2:])
            elif line.startswith("  ") and items:
                items[-1] += " " + line.strip()
            elif not line.strip() and items:
                continue
            elif line.startswith("#"):
                break
        return [collapse(item) for item in items]

    def sources(self) -> list[SourceRow]:
        rows: list[SourceRow] = []
        for line in self.sections.get("Fuentes", "").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 5 and EVIDENCE_ID.fullmatch(cells[0]):
                rows.append(SourceRow(*cells))
        return rows

    def chains(self) -> dict[str, str]:
        fuentes = self.sections.get("Fuentes", "")
        part = fuentes.split("### Cadenas de inferencia", 1)
        if len(part) == 1:
            return {}
        found: dict[str, list[str]] = {}
        current = None
        for line in part[1].splitlines():
            match = re.match(r"^(I\d+)\.", line)
            if match:
                current = match.group(1)
                found[current] = []
            if current:
                found[current].append(line)
        return {k: "\n".join(v) for k, v in found.items()}


def parse_header(lines: list[str]) -> dict[str, object]:
    """Reads the small, fixed YAML header that format.md defines."""
    header: dict[str, object] = {}
    nested: dict[str, object] | None = None
    for line in lines:
        if not line.strip():
            continue
        key, _, raw = line.strip().partition(":")
        raw = raw.split(" #", 1)[0].strip()
        if line.startswith("  ") and nested is not None:
            nested[key] = json.loads(raw)
        elif raw == "":
            nested = {}
            header[key] = nested
        else:
            nested = None
            header[key] = json.loads(raw)
    return header


def parse(path: Path) -> Competency:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{path.name}: missing YAML header")
    end = text.index("\n---\n", 4)
    header_lines = text[4:end].splitlines()
    body = text[end + 5:]
    competency = Competency(path, parse_header(header_lines), header_lines, body)
    for match in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", body, re.M | re.S):
        name = match.group(1).strip()
        competency.section_order.append(name)
        competency.sections[name] = match.group(2)
    return competency


def load_map(layout: Layout) -> list[Competency]:
    return [parse(p) for p in sorted(layout.map.glob("C*.md"))]


@dataclass(frozen=True)
class Consensus:
    emisores: int
    explicitos: int
    inferidos: int
    actual: int
    explicit_and_actual: bool

    def as_header(self) -> dict[str, int]:
        return {"emisores": self.emisores, "explicitos": self.explicitos,
                "inferidos": self.inferidos, "actual": self.actual}


def issuer_key(row: SourceRow) -> str:
    return normalize(row.issuer)


def consensus(rows: list[SourceRow]) -> Consensus:
    """Counts distinct issuers, as format.md requires, from the sources table."""
    by_issuer: dict[str, list[SourceRow]] = {}
    for row in rows:
        by_issuer.setdefault(issuer_key(row), []).append(row)
    explicit = sum(1 for group in by_issuer.values() if any(r.explicit for r in group))
    actual = sum(1 for group in by_issuer.values() if any(r.role == "actual" for r in group))
    return Consensus(
        emisores=len(by_issuer),
        explicitos=explicit,
        inferidos=len(by_issuer) - explicit,
        actual=actual,
        explicit_and_actual=any(r.explicit and r.role == "actual" for r in rows),
    )


def decide(subfields: list[object], live_rows: list[SourceRow]) -> str:
    """Consensus rule of format.md 0.3."""
    if not subfields or not live_rows:
        return "retirada"
    result = consensus(live_rows)
    if result.emisores >= 2 and result.explicit_and_actual:
        return "incluida"
    return "candidata"


def issuer_matches(table_issuer: str, index_issuer: str) -> bool:
    if normalize(index_issuer) == "propio":
        return True
    table_words = normalize(table_issuer).split()
    index_words = normalize(index_issuer).split()
    width = len(table_words)
    return width > 0 and any(
        index_words[i:i + width] == table_words for i in range(len(index_words) - width + 1)
    )


def cited_ids(competency: Competency) -> set[str]:
    return set(EVIDENCE_ID.findall(competency.body))


def validate(competency: Competency, layout: Layout, index: dict[str, dict[str, str]],
             subfields: list[str], format_version: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = competency.path.name
    header = competency.header

    def error(message: str) -> None:
        errors.append(f"{name}: {message}")

    for key in HEADER_KEYS:
        if key not in header:
            error(f"header lacks '{key}'")
    if errors:
        return errors, warnings
    if not COMPETENCY_ID.match(competency.id) or competency.path.stem != competency.id:
        error(f"id '{competency.id}' must be C000-style and match the file name")
    if header["estado"] not in STATES:
        error(f"estado must be one of {', '.join(STATES)}")
    if header["format_version"] != format_version:
        error(f"format_version is {header['format_version']}, format.md is {format_version}")
    if header["domain_version"] != document_version(layout.domain):
        warnings.append(f"{name}: written under domain.md {header['domain_version']}; review its subfields")
    if sorted(header["consenso"]) != sorted(CONSENSUS_KEYS):
        error(f"consenso must have exactly {', '.join(CONSENSUS_KEYS)}")

    required = [s for s in competency.section_order if s in SECTIONS]
    if required != SECTIONS:
        error(f"sections must be, in order: {', '.join(SECTIONS)}")
    unknown = [s for s in competency.section_order if s not in SECTIONS + OPTIONAL_SECTIONS]
    if unknown:
        error(f"unknown sections: {', '.join(unknown)}")

    statement = collapse(competency.sections.get("Enunciado", ""))
    if collapse(str(header["enunciado"])) != statement:
        error("the header 'enunciado' differs from the Enunciado section")

    declared = list(header["subcampos"])
    for subfield in declared:
        if subfield not in subfields:
            error(f"subfield '{subfield}' is not in domain.md")
    justified: dict[str, str] = {}
    for bullet in competency.bullets("Subcampos"):
        label, _, justification = bullet.partition(":")
        justified[label.strip()] = justification.strip()
    if sorted(justified) != sorted(declared):
        error("the Subcampos section must have one bullet per header subfield")
    for subfield, justification in justified.items():
        explicit = justification.startswith("explícita") and EVIDENCE_ID.search(justification)
        if not (explicit or justification.startswith("por domain.md")):
            error(f"subfield '{subfield}' needs 'explícita [Exxxx ...]' or 'por domain.md'")

    for section in ("Conocimientos", "Habilidades"):
        items = competency.bullets(section)
        if not items:
            error(f"{section} is empty")
        for item in items:
            citation = re.search(r"\[[^\]]*(E\d{4}|inferido)[^\]]*\]\.?$", item)
            if not citation:
                error(f"{section} item lacks a final citation: '{item[:60]}'")

    for item in competency.bullets("Evidencia de desempeño") or [""]:
        if not (item.startswith("Ninguna fuente") or EVIDENCE_ID.search(item)):
            error(f"Evidencia de desempeño item lacks a citation: '{item[:60]}'")

    rows = competency.sources()
    if not rows:
        error("the Fuentes table has no rows")
    live = [r for r in rows if accepted(index, r.id)]
    for row in rows:
        indexed = index.get(row.id)
        if indexed is None:
            error(f"{row.id} is not in index.csv")
            continue
        if not accepted(index, row.id) and live:
            error(f"{row.id} is no longer accepted; remove it or let the competency retire")
        if not issuer_matches(row.issuer, indexed["issuer"]):
            error(f"{row.id}: issuer '{row.issuer}' is not part of '{indexed['issuer']}'")
        if row.role != indexed["role"]:
            error(f"{row.id}: role '{row.role}' differs from index.csv '{indexed['role']}'")
        if not (row.explicit or row.support == KNOWLEDGE_ONLY or row.chain):
            error(f"{row.id}: support must be '{EXPLICIT}', 'inferido (In)' or '{KNOWLEDGE_ONLY}'")

    table_ids = {r.id for r in rows}
    for evidence_id in sorted(cited_ids(competency) - table_ids):
        error(f"{evidence_id} is cited but missing from the Fuentes table")

    chains = competency.chains()
    referenced = {r.chain for r in rows if r.chain} | set(re.findall(r"cadena (I\d+)", competency.body))
    for chain_id in sorted(referenced):
        chain = chains.get(chain_id)
        if chain is None:
            error(f"inference chain {chain_id} is referenced but not written")
            continue
        steps = len(re.findall(r"→ Paso", chain))
        if not 1 <= steps <= 2 or "⇒" not in chain:
            error(f"inference chain {chain_id} must have one or two '→ Paso' steps and a '⇒' conclusion")

    if not errors:
        expected_state = decide(declared, live)
        expected_consensus = consensus(live).as_header()
        if header["estado"] != expected_state:
            error(f"estado is '{header['estado']}', the consensus rule gives '{expected_state}'")
        if header["consenso"] != expected_consensus:
            error(f"consenso is {header['consenso']}, the sources table gives {expected_consensus}")
    return errors, warnings


def fix_consensus(competency: Competency, index: dict[str, dict[str, str]]) -> bool:
    """Rewrites the computed header fields; returns whether the file changed."""
    live = [r for r in competency.sources() if accepted(index, r.id)]
    values = consensus(live).as_header()
    state = decide(list(competency.header.get("subcampos", [])), live)
    lines: list[str] = []
    in_consensus = False
    for line in competency.header_lines:
        if line.startswith("estado:"):
            line = f'estado: "{state}"'
        if line.startswith("consenso:"):
            in_consensus = True
        elif in_consensus and line.startswith("  "):
            key = line.strip().partition(":")[0]
            line = f"  {key}: {values[key]}"
        else:
            in_consensus = False
        lines.append(line)
    if lines == competency.header_lines:
        return False
    competency.path.write_text("---\n" + "\n".join(lines) + "\n---\n" + competency.body, encoding="utf-8")
    return True


def next_id(layout: Layout) -> str:
    # Retired competencies keep their files, so identifiers are never reused.
    numbers = [int(p.stem[1:]) for p in layout.map.glob("C*.md") if COMPETENCY_ID.match(p.stem)]
    return f"C{max(numbers, default=0) + 1:03d}"


def read_ledger(layout: Layout) -> dict[str, dict[str, str]]:
    if not layout.ledger.exists():
        return {}
    with layout.ledger.open(newline="", encoding="utf-8") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def write_ledger(layout: Layout, rows: dict[str, dict[str, str]]) -> None:
    with layout.ledger.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LEDGER_COLUMNS)
        writer.writeheader()
        writer.writerows(rows[k] for k in sorted(rows))


def today() -> str:
    return dt.date.today().isoformat()
