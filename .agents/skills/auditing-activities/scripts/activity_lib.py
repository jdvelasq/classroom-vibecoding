from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import paths

ROOT = Path(__file__).resolve().parents[4]

# The checks below implement exactly this version of references/format.md;
# a new version must be reviewed here first.
SUPPORTED_FORMAT_VERSION = "0.1"

ACTIVITY_DIR = re.compile(r"^(P\d{3})_")
HIGHLIGHT = re.compile(r"^- \*\*(H\d{2}) — (.+?):\*\*", re.M)
SURFACE_ID = re.compile(r"\bS\d{2}\b")
HIGHLIGHT_ID = re.compile(r"\bH\d{2}\b")
LOG_ENTRY = re.compile(r"^## ([A-Z0-9]+)\.(P\d{3})\.(\d{2})\s*$", re.M)
BACKTICKED = re.compile(r"`([^`]+)`")
ACTIVITY_SUBFOLDERS = ("data", "notebooks", "professor", "src", "submission", "temp", "tests")
FILE_EXTENSIONS = {
    "bat", "cfg", "csv", "db", "feather", "gif", "gz", "html", "ini", "ipynb", "jpeg", "jpg", "joblib",
    "json", "jsonl", "log", "md", "parquet", "pdf", "pkl", "png", "py", "sh", "sql", "sqlite", "svg",
    "toml", "tsv", "txt", "xls", "xlsx", "xml", "yaml", "yml", "zip",
}

CASE_AND_DATA = "(caso y datos)"
LEGACY_SECTION = "Mejoras aceptadas pendientes de implementación"
DESCRIPTION_LOG = "S02"
EXCLUDED_FILES = {".gitkeep", ".DS_Store", "__init__.py"}
EXCLUDED_DIRS = {"__pycache__", ".ipynb_checkpoints", ".pytest_cache"}

SECTIONS = [
    "Actividad actual implementada",
    "Preguntas analíticas actuales",
    "Producto analítico actual y límite de identidad",
    "Highlights de contribución",
    "Inventario técnico de implementación",
    "Índice de comparación externa",
    "Relación técnica con actividades anteriores",
    "Evidencia de los highlights",
    "Superficies de cambio para revisión posterior",
    "Contrato de evidencia actual",
    "Dependencias en la secuencia",
    "Trazabilidad y auditoría",
]


@dataclass(frozen=True)
class Layout:
    root: Path

    def at(self, template: str, **names: str) -> Path:
        return self.root / template.format(**names)

    @property
    def format(self) -> Path:
        return self.at(paths.FORMAT)

    def implementation(self, course: str) -> Path:
        return self.at(paths.IMPLEMENTATION, course=course)

    def traceability(self, course: str) -> Path:
        return self.at(paths.TRACEABILITY, course=course)

    def tasks(self, course: str, folder: str) -> Path:
        return self.at(paths.TASKS, course=course, folder=folder)

    def course_tasks(self, course: str) -> Path:
        return self.at(paths.COURSE_TASKS, course=course)

    def audit(self, course: str) -> Path:
        return self.at(paths.AUDIT, course=course)

    def activity(self, course: str, folder: str) -> Path:
        return self.at(paths.ACTIVITY, course=course, folder=folder)

    def log(self, course: str, folder: str) -> Path:
        return self.at(paths.LOG, course=course, folder=folder)

    def shown(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def own_files(self, course: str, folder: str) -> set[Path]:
        return {self.activity(course, folder), self.log(course, folder), self.tasks(course, folder)}


def document_version(path: Path) -> str:
    match = re.search(r"^Versión\s+(\S+)", path.read_text(encoding="utf-8"), re.M)
    if not match:
        raise SystemExit(f"No version line found in {path}")
    return match.group(1)


def require_supported_format(layout: Layout) -> str:
    version = document_version(layout.format)
    if version != SUPPORTED_FORMAT_VERSION:
        raise SystemExit(
            f"references/format.md is version {version}, but the scripts implement "
            f"{SUPPORTED_FORMAT_VERSION}. Update activity_lib.py and its tests first."
        )
    return version


def require_course(layout: Layout, course: str) -> None:
    if not layout.implementation(course).is_dir():
        raise SystemExit(f"{layout.shown(layout.implementation(course))}/ does not exist")


def activity_dirs(layout: Layout, course: str) -> dict[str, Path]:
    found = {}
    for path in sorted(layout.implementation(course).iterdir()):
        match = ACTIVITY_DIR.match(path.name)
        if path.is_dir() and match:
            found[match.group(1)] = path
    return found


def activity_files(layout: Layout, course: str, directory: Path) -> dict[str, list[str]]:
    own = layout.own_files(course, directory.name)
    files: dict[str, list[str]] = {}
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory)
        if (not path.is_file() or path in own or path.name in EXCLUDED_FILES
                or EXCLUDED_DIRS & set(relative.parts)):
            continue
        top = relative.parts[0] if len(relative.parts) > 1 else "."
        files.setdefault(top, []).append(relative.as_posix())
    return files


def table_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if all(set(c) <= {"-", ":", " "} for c in cells):
            continue
        rows.append(cells)
    return rows[1:]


@dataclass
class Activity:
    path: Path
    title: str
    sections: dict[str, str] = field(default_factory=dict)
    section_order: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        return self.path.parent.name.split("_", 1)[0]

    @property
    def implementation(self) -> str | None:
        match = re.search(r"^\*\*Implementación:\*\*\s*`([^`]+)`",
                          self.sections.get("Actividad actual implementada", ""), re.M)
        return match.group(1) if match else None

    def highlights(self) -> list[tuple[str, str]]:
        return HIGHLIGHT.findall(self.sections.get("Highlights de contribución", ""))

    def highlight_ids(self) -> list[str]:
        return [h for h, _ in self.highlights()]

    def evidence(self) -> list[list[str]]:
        return table_rows(self.sections.get("Evidencia de los highlights", ""))

    def surfaces(self) -> list[list[str]]:
        return table_rows(self.sections.get("Superficies de cambio para revisión posterior", ""))

    def surface_ids(self) -> list[str]:
        return [row[0] for row in self.surfaces() if SURFACE_ID.fullmatch(row[0])]


def parse_activity(path: Path) -> Activity:
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+?)\s*$", text, re.M)
    activity = Activity(path, title.group(1) if title else "")
    for match in re.finditer(r"^#{2,3} (.+?)\n(.*?)(?=^#{2,3} |\Z)", text, re.M | re.S):
        name = match.group(1).strip()
        activity.section_order.append(name)
        activity.sections[name] = match.group(2)
    return activity


def is_file_reference(token: str) -> bool:
    if " " in token or "(" in token or token.startswith("."):
        return False
    if token.endswith("/"):
        return True
    name = token.rsplit("/", 1)[-1]
    if "." in name and name.rsplit(".", 1)[1].lower() in FILE_EXTENSIONS:
        return True
    return "/" in token and token.split("/", 1)[0] in ACTIVITY_SUBFOLDERS + ("05-implementation",)


def file_references(cell: str) -> list[str]:
    return [t.strip() for t in BACKTICKED.findall(cell) if is_file_reference(t.strip())]


def reference_exists(reference: str, root: Path, activity_dir: Path) -> bool:
    """A bare file name may sit anywhere in the activity or at the course level."""
    for base in (root, activity_dir, activity_dir.parent):
        if any(ch in reference for ch in "*?["):
            if any(base.glob(reference)):
                return True
        elif (base / reference).exists():
            return True
    if "/" not in reference:
        return any(activity_dir.rglob(reference))
    return False


def validate_activity(activity: Activity, layout: Layout, course: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = layout.shown(activity.path)
    activity_dir = activity.path.parent

    def error(message: str) -> None:
        errors.append(f"{name}: {message}")

    def warn(message: str) -> None:
        warnings.append(f"{name}: {message}")

    if not re.match(rf"^{activity.id} — \S", activity.title):
        error(f"the title must be '# {activity.id} — Nombre'")
    present = [s for s in activity.section_order if s in SECTIONS]
    missing = [s for s in SECTIONS if s not in activity.sections]
    if missing:
        error(f"missing sections: {', '.join(missing)}")
    elif present != SECTIONS:
        error("the sections are not in the order of format.md")

    expected = layout.shown(activity_dir) + "/"
    implementation = activity.implementation
    if implementation is None:
        error("**Implementación:** with the path of the activity is missing")
    elif implementation.rstrip("/") + "/" != expected:
        error(f"Implementación is `{implementation}`, but the activity folder is `{expected}`")

    ids = activity.highlight_ids()
    if not ids:
        error("there are no highlights written as '- **HNN — Título:**'")
    if len(set(ids)) != len(ids):
        error(f"repeated highlight ids: {', '.join(sorted({h for h in ids if ids.count(h) > 1}))}")
    if ids != sorted(ids):
        error("highlight ids must increase in order")
    if ids and not any(CASE_AND_DATA in title for _, title in activity.highlights()):
        warn(f"no highlight is marked {CASE_AND_DATA}; record the absence as a limit if there is none")

    surfaces = activity.surface_ids()
    if len(set(surfaces)) != len(surfaces):
        error("repeated surface ids")
    for row in activity.surfaces():
        for reference in file_references(row[2] if len(row) > 2 else ""):
            if not reference_exists(reference, layout.root, activity_dir):
                error(f"surface {row[0]} points to `{reference}`, which does not exist")

    evidence = {}
    for row in activity.evidence():
        found = HIGHLIGHT_ID.search(row[0])
        if found:
            evidence[found.group(0)] = row
    for hid in ids:
        row = evidence.get(hid)
        if row is None:
            error(f"{hid} has no row in the evidence table")
            continue
        linked = SURFACE_ID.findall(row[1] if len(row) > 1 else "")
        if not linked:
            error(f"{hid} is linked to no surface")
        for sid in linked:
            if sid not in surfaces:
                error(f"{hid} is linked to {sid}, which is not in the surfaces table")
        references = file_references(row[2] if len(row) > 2 else "")
        if not references:
            error(f"{hid} has no backing path in the evidence table")
        for reference in references:
            if not reference_exists(reference, layout.root, activity_dir):
                error(f"{hid} points to `{reference}`, which does not exist")
    for hid in evidence:
        if hid not in ids:
            error(f"the evidence table cites {hid}, which is not a highlight")

    legacy = activity.sections.get(LEGACY_SECTION)
    if legacy is not None:
        if legacy.strip():
            error(f"the inherited section '{LEGACY_SECTION}' still has content; record it in the log as an ambiguity")
        else:
            warn(f"remove the empty inherited section '{LEGACY_SECTION}'")
    return errors, warnings


@dataclass(frozen=True)
class LogEntry:
    prefix: str
    activity: str
    number: int
    text: str

    @property
    def id(self) -> str:
        return f"{self.prefix}.{self.activity}.{self.number:02d}"


def parse_log(path: Path) -> list[LogEntry]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    matches = list(LOG_ENTRY.finditer(text))
    entries = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        entries.append(LogEntry(match.group(1), match.group(2), int(match.group(3)), text[match.end():end]))
    return entries


def next_entry(entries: list[LogEntry], prefix: str, activity: str) -> str:
    numbers = [e.number for e in entries if e.prefix == prefix]
    return f"{prefix}.{activity}.{max(numbers, default=0) + 1:02d}"


def latest_entry(entries: list[LogEntry], prefix: str) -> str | None:
    found = [e for e in entries if e.prefix == prefix]
    return found[-1].id if found else None


def validate_log(path: Path, layout: Layout, activity: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = layout.shown(path)
    if not path.exists():
        return errors, warnings
    entries = parse_log(path)
    if not path.read_text(encoding="utf-8").startswith(f"# Log — {activity}"):
        errors.append(f"{name}: the first line must be '# Log — {activity}'")
    for entry in entries:
        if entry.activity != activity:
            errors.append(f"{name}: entry {entry.id} belongs to another activity")
    if not any(e.prefix == DESCRIPTION_LOG for e in entries):
        warnings.append(f"{name}: there is no {DESCRIPTION_LOG} entry")
    by_prefix: dict[str, list[int]] = {}
    for entry in entries:
        by_prefix.setdefault(entry.prefix, []).append(entry.number)
    for prefix, numbers in by_prefix.items():
        if numbers != list(range(1, len(numbers) + 1)):
            warnings.append(f"{name}: {prefix} entries are not numbered 01, 02, … in order")
    return errors, warnings


@dataclass
class Traceability:
    version: str | None = None
    entries: dict[str, object] = field(default_factory=dict)


def parse_flow_list(raw: str) -> list[str]:
    inner = raw.strip()[1:-1]
    return [item.strip().strip('"') for item in inner.split(",") if item.strip()]


def parse_traceability(path: Path) -> Traceability:
    """Reads the small YAML subset that format.md defines for traceability.yaml."""
    trace = Traceability()
    if not path.exists():
        return trace
    current: str | None = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            key, _, raw = line.partition(":")
            key, raw = key.strip(), raw.strip()
            if key == "format_version":
                trace.version = raw.strip('"')
                current = None
            elif raw:
                raise ValueError(f"{path}: line {number}: '{key}' must hold a list or a mapping")
            else:
                current = key
                trace.entries[key] = None
            continue
        if current is None:
            raise ValueError(f"{path}: line {number}: indented line outside an entry")
        stripped = line.strip()
        value = trace.entries[current]
        if stripped.startswith("- "):
            if isinstance(value, dict):
                raise ValueError(f"{path}: line {number}: {current} mixes a list and a mapping")
            trace.entries[current] = (value or []) + [stripped[2:].strip().strip('"')]
        else:
            if isinstance(value, list):
                raise ValueError(f"{path}: line {number}: {current} mixes a list and a mapping")
            key, _, raw = stripped.partition(":")
            raw = raw.strip()
            mapping = value or {}
            mapping[key.strip()] = parse_flow_list(raw) if raw.startswith("[") else raw.strip('"')
            trace.entries[current] = mapping
    return trace


def render_traceability(trace: Traceability) -> str:
    lines = []
    if trace.version:
        lines.append(f'format_version: "{trace.version}"')
    for key, value in trace.entries.items():
        lines.append(f"{key}:")
        if isinstance(value, dict):
            for field_name, item in value.items():
                shown = f"[{', '.join(item)}]" if isinstance(item, list) else item
                lines.append(f"  {field_name}: {shown}")
        else:
            lines.extend(f"  - {item}" for item in value or [])
    return "\n".join(lines) + "\n"
