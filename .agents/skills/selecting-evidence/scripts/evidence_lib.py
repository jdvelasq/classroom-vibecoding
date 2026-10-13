from __future__ import annotations

import csv
import datetime as dt
import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

INDEX_COLUMNS = [
    "id",
    "sha256",
    "file",
    "title",
    "issuer",
    "year",
    "source",
    "decision",
    "category",
    "role",
    "criteria_version",
    "date",
]
CATEGORIES = {
    "authoritative",
    "governmental",
    "institutional",
    "literature-derived",
    "professional-learning",
}
ROLES = {"actual", "precursor"}
CRITERIA = ["pertinencia", "autoridad", "especificidad", "vigencia", "acceso"]
# The decision rule in `decide` implements exactly this version of
# criteria.md; a new version must be reviewed here before it can be applied.
SUPPORTED_CRITERIA_VERSION = "0.2"
# Documents placed in this inbox subfolder were found by the agent; every
# other document in the inbox is presumed contributed by david.
AGENT_INBOX = "agent"


@dataclass(frozen=True)
class Layout:
    root: Path

    @property
    def evidence(self) -> Path:
        return self.root / "01-evidence"

    @property
    def ingest(self) -> Path:
        return self.evidence / "ingest"

    @property
    def index(self) -> Path:
        return self.evidence / "index.csv"

    @property
    def criteria(self) -> Path:
        return self.evidence / "criteria.md"

    @property
    def decisions(self) -> Path:
        return self.evidence / "decisions"

    @property
    def rejected(self) -> Path:
        return self.evidence / "rejected"

    def accepted_pdf_dir(self, category: str) -> Path:
        return self.evidence / "pdf" / category

    def accepted_md_dir(self, category: str) -> Path:
        return self.evidence / "md" / category

    def shown(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def criteria_version(layout: Layout) -> str:
    match = re.search(r"^Versión\s+(\S+)", layout.criteria.read_text(encoding="utf-8"), re.M)
    if not match:
        raise SystemExit(f"No version line found in {layout.shown(layout.criteria)}")
    return match.group(1)


def ensure_index(layout: Layout) -> None:
    if not layout.index.exists():
        layout.index.parent.mkdir(parents=True, exist_ok=True)
        with layout.index.open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(INDEX_COLUMNS)


def read_index(layout: Layout) -> list[dict[str, str]]:
    ensure_index(layout)
    with layout.index.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_index(layout: Layout, row: dict[str, str]) -> None:
    ensure_index(layout)
    with layout.index.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=INDEX_COLUMNS).writerow(row)


def next_id(rows: list[dict[str, str]]) -> str:
    numbers = [int(r["id"][1:]) for r in rows if re.fullmatch(r"E\d+", r["id"])]
    return f"E{max(numbers, default=0) + 1:04d}"


def normalize(text: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", ascii_text.lower()).strip()


def md_header(md: Path) -> dict[str, object]:
    """Reads the simple YAML header written by the S01 converter."""
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    header: dict[str, object] = {}
    warnings: list[str] = []
    for line in text[4:end].splitlines():
        if line.startswith("  - "):
            warnings.append(line[4:].strip().strip('"'))
            continue
        key, sep, value = line.partition(":")
        if sep:
            header[key.strip()] = value.strip().strip('"')
    header["warnings"] = warnings
    return header


def source_of(layout: Layout, pdf: Path) -> str:
    rel = pdf.relative_to(layout.ingest)
    return "agent" if rel.parts[0] == AGENT_INBOX else "david"


def decide(source: str, scores: dict[str, int | None], material_warnings: bool) -> str:
    """Decision rule of criteria.md 0.2, applied in order; first match wins."""
    if scores["pertinencia"] == 0:
        return "reject"
    if material_warnings or scores["acceso"] == 0:
        return "review"
    if source == "david":
        return "accept" if scores["pertinencia"] == 2 else "review"
    values = [scores[c] for c in CRITERIA]
    if any(v is None for v in values):
        raise ValueError("agent-found documents need all five scores")
    total = sum(values)
    if 0 not in values and total >= 8:
        return "accept"
    if total <= 5 or 0 in values:
        return "reject"
    return "review"


def today() -> str:
    return dt.date.today().isoformat()
