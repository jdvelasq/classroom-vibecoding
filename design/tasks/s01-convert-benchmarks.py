# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "pymupdf4llm==0.0.27",
#   "pymupdf==1.26.5",
# ]
# ///
"""S01 — Convertir los benchmarks PDF a Markdown.

Ejecución (desde la raíz del repositorio):

    uv run design/tasks/s01-convert-benchmarks.py            # incremental
    uv run design/tasks/s01-convert-benchmarks.py --force    # reconvierte todo
    uv run design/tasks/s01-convert-benchmarks.py RUTA.pdf   # sólo esos PDFs

Sin uv: `pip install pymupdf4llm==0.0.27 pymupdf==1.26.5` y ejecutar con
`python`. Versiones elegidas por compatibilidad con Python 3.9 y con el
`requirements.txt` de la raíz (verificado con Python 3.9.1).

Contrato:

- Lee `design/benchmarks-pdf/**.pdf` y escribe `design/benchmarks-md/**.md`
  con la misma estructura de carpetas y el mismo nombre de archivo.
- Es determinista y no usa LLM. Prioriza fidelidad conceptual: texto completo,
  orden de lectura, títulos, listas, tablas y marcas de página citables.
- No aplica OCR. Las páginas con poco texto extraíble se marcan para revisión
  humana.
- Estrategia por página: se convierte detectando gráficos vectoriales (así se
  conservan las tablas); si una página pierde texto nativo —cobertura de
  palabras menor que COVERAGE_MIN, típico en folletos de diseño—, esa página
  se repite ignorando gráficos. La cobertura mínima queda en la cabecera.
- Es incremental: un PDF se reconvierte sólo si cambió su SHA-256 o la
  versión del conversor registrada en la cabecera del `.md`.
- Nunca borra archivos: los `.md` sin PDF de origen sólo se reportan.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path

import pymupdf
import pymupdf4llm

ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "design" / "benchmarks-pdf"
MD_DIR = ROOT / "design" / "benchmarks-md"

TOOL = (
    f"pymupdf4llm {pymupdf4llm.__version__} + pymupdf {pymupdf.__version__} "
    "(por página, respaldo sin gráficos; limpieza v1)"
)
COVERAGE_MIN = 0.95  # fracción de palabras nativas presentes en el markdown
LOW_TEXT_CHARS = 200  # página con menos texto extraíble que esto se marca
WORD = re.compile(r"[^\W\d_]{3,}")
# Líneas de puntos de índices con glifos sin mapeo ("Tema ����� 7").
LEADER_RUN = re.compile(r"[ \t]*(?:\ufffd[ \t]*){3,}")
# Caracteres de control distintos de tabulador y salto de línea.
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
REPLACEMENT = "�"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_header(md: Path) -> dict[str, str]:
    """Lee la cabecera YAML simple (clave: valor) de un .md existente."""
    if not md.exists():
        return {}
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    header = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            header[key.strip()] = value.strip().strip('"')
    return header


def low_text_pages(doc: pymupdf.Document) -> list[int]:
    """Páginas (1-based) con poco texto nativo y al menos una imagen."""
    return [
        i + 1
        for i, page in enumerate(doc)
        if len(page.get_text().strip()) < LOW_TEXT_CHARS and page.get_images()
    ]


def clean(body: str) -> str:
    """Limpieza conservadora: sólo elimina ruido que no lleva contenido.

    Las secuencias de 3+ glifos sin mapeo son líneas de puntos de índices y
    se reemplazan por " … ". Los glifos aislados se conservan y se reportan,
    porque pueden ocultar contenido (viñetas, subíndices) no recuperable.
    """
    body = CONTROL.sub("", body)
    return LEADER_RUN.sub(" … ", body)


def coverage(native: str, md: str) -> float:
    """Fracción de palabras del texto nativo que aparecen en el markdown."""
    words = [w.lower() for w in WORD.findall(native)]
    if not words:
        return 1.0
    present = {w.lower() for w in WORD.findall(md)}
    return sum(w in present for w in words) / len(words)


def convert(pdf: Path) -> tuple[str, dict]:
    doc = pymupdf.open(pdf)
    chunks = pymupdf4llm.to_markdown(
        doc, page_chunks=True, ignore_images=True, show_progress=False
    )
    flagged = set(low_text_pages(doc))
    parts, redone, covs = [], [], []
    for i, chunk in enumerate(chunks):
        n = i + 1
        native = doc[i].get_text()
        text = chunk["text"]
        cov = coverage(native, text)
        if cov < COVERAGE_MIN:
            alt = pymupdf4llm.to_markdown(
                doc,
                pages=[i],
                ignore_images=True,
                ignore_graphics=True,
                show_progress=False,
            )
            alt_cov = coverage(native, alt)
            if alt_cov > cov:
                text, cov = alt, alt_cov
                redone.append(n)
        covs.append(cov)
        note = (
            f"> ⚠️ S01: página {n} con poco texto extraíble; "
            "puede tener contenido en imagen no convertido.\n\n"
            if n in flagged
            else ""
        )
        parts.append(f"{text.rstrip()}\n\n{note}<!-- fin de página {n} -->\n")
    body = clean("\n".join(parts))

    warnings = []
    if flagged:
        warnings.append(f"páginas con poco texto: {sorted(flagged)}")
    low = [i + 1 for i, c in enumerate(covs) if c < COVERAGE_MIN]
    if low:
        warnings.append(f"páginas con cobertura < {COVERAGE_MIN}: {low}")
    bad = body.count(REPLACEMENT)
    if bad:
        warnings.append(f"{bad} glifos sin mapeo de fuente aislados (U+FFFD)")
    meta = {
        "pages": doc.page_count,
        "min_coverage": round(min(covs), 3) if covs else 1.0,
        "redone": redone,
        "warnings": warnings,
    }
    return body, meta


def build_header(pdf: Path, digest: str, meta: dict) -> str:
    rel = pdf.relative_to(ROOT).as_posix()
    lines = [
        "---",
        f'source: "{rel}"',
        f"source_sha256: {digest}",
        f"family: {pdf.relative_to(PDF_DIR).parts[0]}",
        f"pages: {meta['pages']}",
        f"min_text_coverage: {meta['min_coverage']}",
        f"pages_without_graphics: {meta['redone']}",
        f'converter: "{TOOL}"',
        f"converted: {dt.date.today().isoformat()}",
    ]
    if meta["warnings"]:
        lines.append("warnings:")
        lines += [f'  - "{w}"' for w in meta["warnings"]]
    lines.append("---\n")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdfs", nargs="*", type=Path, help="PDFs específicos")
    ap.add_argument("--force", action="store_true", help="reconvierte todo")
    args = ap.parse_args()

    pdfs = (
        [p.resolve() for p in args.pdfs]
        if args.pdfs
        else sorted(PDF_DIR.rglob("*.pdf"))
    )
    converted, skipped, warned, failed = [], [], [], []

    for pdf in pdfs:
        if PDF_DIR not in pdf.parents:
            print(f"✗ fuera de {PDF_DIR.relative_to(ROOT)}: {pdf}")
            failed.append(pdf)
            continue
        rel = pdf.relative_to(PDF_DIR)
        md = (MD_DIR / rel).with_suffix(".md")
        digest = sha256(pdf)
        old = read_header(md)
        if (
            not args.force
            and old.get("source_sha256") == digest
            and old.get("converter") == TOOL
        ):
            skipped.append(rel)
            continue
        try:
            body, meta = convert(pdf)
        except Exception as exc:  # noqa: BLE001 — se reporta y se sigue
            print(f"✗ {rel}: {exc}")
            failed.append(rel)
            continue
        md.parent.mkdir(parents=True, exist_ok=True)
        md.write_text(build_header(pdf, digest, meta) + body, encoding="utf-8")
        converted.append(rel)
        status = "⚠" if meta["warnings"] else "✓"
        print(f"{status} {rel} ({meta['pages']} págs)")
        for w in meta["warnings"]:
            print(f"    {w}")
        if meta["warnings"]:
            warned.append(rel)

    orphans = (
        [
            md.relative_to(MD_DIR)
            for md in sorted(MD_DIR.rglob("*.md"))
            if not (PDF_DIR / md.relative_to(MD_DIR)).with_suffix(".pdf").exists()
        ]
        if MD_DIR.exists()
        else []
    )

    print(
        f"\nConvertidos: {len(converted)} · sin cambios: {len(skipped)} · "
        f"con advertencias: {len(warned)} · fallidos: {len(failed)}"
    )
    for o in orphans:
        print(f"  .md sin PDF de origen (no se borró): {o}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
