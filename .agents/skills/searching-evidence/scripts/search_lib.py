from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "selecting-evidence" / "scripts"))

from evidence_lib import AGENT_INBOX, Layout, document_version, normalize, read_index, sha256, today  # noqa: E402,F401

ROOT = Path(__file__).resolve().parents[4]

# fetch.py and the log format implement exactly this version of sources.md;
# a new version must be reviewed here before a search can run.
SUPPORTED_SOURCES_VERSION = "0.4"

UNIVERSITIES = "universities"

LOG_COLUMNS = ["date", "source", "target", "query", "url", "file", "sha256", "status"]
FETCHED = "fetched"


def sources_path(layout: Layout) -> Path:
    return layout.evidence / "sources.md"


def log_path(layout: Layout) -> Path:
    return layout.evidence / "searches.csv"


def agent_inbox(layout: Layout) -> Path:
    return layout.ingest / AGENT_INBOX


@dataclass
class Plan:
    version: str
    universities: dict[str, list[str]]
    per_university_limit: int
    universities_run_limit: int
    university_category: str
    terms: dict[str, str] = field(default_factory=dict)


def section(text: str, heading: str) -> str:
    match = re.search(rf"^#+ {re.escape(heading)}.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        raise SystemExit(f"sources.md has no section '{heading}'")
    return match.group(1)


def first_int(pattern: str, text: str) -> int:
    match = re.search(pattern, text)
    if not match:
        raise SystemExit(f"sources.md does not match /{pattern}/")
    return int(match.group(1))


def category(text: str) -> str:
    match = re.search(r"\*\*Categoría de destino\*\*: `([^`]+)`", text)
    if not match:
        raise SystemExit("sources.md section without a destination category")
    return match.group(1)


def read_plan(layout: Layout) -> Plan:
    path = sources_path(layout)
    text = path.read_text(encoding="utf-8")
    version = document_version(layout, path)
    if version != SUPPORTED_SOURCES_VERSION:
        raise SystemExit(
            f"sources.md is version {version}; the scripts implement {SUPPORTED_SOURCES_VERSION}."
        )

    universities_text = section(text, "Fuente: syllabus")
    universities: dict[str, list[str]] = {}
    group = None
    for line in universities_text.splitlines():
        heading = re.fullmatch(r"\*\*(.+)\*\*", line.strip())
        if heading:
            group = heading.group(1)
            universities[group] = []
        elif group and line.startswith("- "):
            universities[group].append(line[2:].rstrip("."))

    terms = dict(re.findall(r"^- \*\*([^*]+)\*\*: (.+?)(?=^- |\Z)", section(text, "Términos de búsqueda"), re.M | re.S))
    return Plan(
        version=version,
        universities=universities,
        per_university_limit=first_int(r"hasta (\d+) documentos por universidad", universities_text),
        universities_run_limit=first_int(r"por universidad y (\d+) por corrida", universities_text),
        university_category=category(universities_text),
        terms={k: " ".join(v.split()) for k, v in terms.items()},
    )


def read_log(layout: Layout) -> list[dict[str, str]]:
    if not log_path(layout).exists():
        return []
    with log_path(layout).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_log(layout: Layout, rows: list[dict[str, str]]) -> None:
    path = log_path(layout)
    is_new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LOG_COLUMNS)
        if is_new:
            writer.writeheader()
        writer.writerows(rows)


def slug(text: str, limit: int = 60) -> str:
    return normalize(text).replace(" ", "-")[:limit].strip("-") or "page"
