import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import competency_lib as lib  # noqa: E402
import record  # noqa: E402
import status  # noqa: E402
import validate as validate_  # noqa: E402

INDEX = [
    # id, issuer, role, decision, file
    ("E0001", "INFORMS", "actual", "accept", "01-evidence/pdf/authoritative/informs.pdf"),
    ("E0002", "INFORMS - Analytics Certification Board", "actual", "accept", "01-evidence/pdf/authoritative/cap.pdf"),
    ("E0003", "SAS", "precursor", "accept", "01-evidence/pdf/professional-learning/sas.pdf"),
    ("E0004", "MIT", "actual", "accept", "01-evidence/pdf/professional-learning/mit.pdf"),
    ("E0005", "propio", "actual", "accept", "01-evidence/syntheses/datacamp.md"),
    ("E0006", "Blog", "actual", "reject", "01-evidence/rejected/blog.pdf"),
]

DOMAIN = """# Dominio

Versión 0.7 (borrador)

## Subcampos

- Analítica descriptiva.
- Analítica predictiva.
- Analítica de grandes datos (*Big Data Analytics*).
- Productos de datos.

## Precursores
"""


@pytest.fixture
def layout(tmp_path):
    layout = lib.Layout(tmp_path)
    layout.map.mkdir(parents=True)
    layout.index.parent.mkdir(parents=True)
    layout.format.write_text("# Formato\n\nVersión 0.3 (aprobada)\n", encoding="utf-8")
    layout.domain.write_text(DOMAIN, encoding="utf-8")
    with layout.index.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "issuer", "role", "decision", "file", "title", "category"])
        for evidence_id, issuer, role, decision, file in INDEX:
            writer.writerow([evidence_id, issuer, role, decision, file, f"Title {evidence_id}", "authoritative"])
    return layout


def source(evidence_id, issuer, role, support="explícito"):
    return f"| {evidence_id} | {issuer} | {role} | p. 3 | {support} |"


def write_competency(layout, cid="C001", rows=None, subfields=("analítica predictiva",),
                     estado="incluida", consenso=(2, 2, 0, 2), knowledge=None,
                     evidence=None, chains="", extra="", statement="Construir modelos predictivos validados, para estimar un resultado."):
    rows = rows if rows is not None else [source("E0001", "INFORMS", "actual"), source("E0004", "MIT", "actual")]
    cited = sorted({r.split("|")[1].strip() for r in rows})
    knowledge = knowledge if knowledge is not None else [f"Validación fuera de muestra [{cited[0]} p. 3]."]
    evidence = evidence if evidence is not None else [f"Un modelo validado [{cited[0]} p. 3]."]
    emisores, explicitos, inferidos, actual = consenso
    subfield_list = ", ".join(f'"{s}"' for s in subfields)
    justification = "\n".join(f"- {s}: explícita [{cited[0]} p. 3]." for s in subfields)
    text = f"""---
id: "{cid}"
enunciado: "{statement}"
subcampos: [{subfield_list}]
estado: "{estado}"
consenso:
  emisores: {emisores}
  explicitos: {explicitos}
  inferidos: {inferidos}
  actual: {actual}
format_version: "0.3"
domain_version: "0.7"
fecha: "2026-10-13"
---

# {cid}. Título

## Enunciado

{statement}

## Subcampos

{justification}

## Conocimientos

{chr(10).join("- " + k for k in knowledge)}

## Habilidades

- Comparar modelos [{cited[0]} p. 3].

## Fuentes

| id | Emisor | Rol | Ubicación | Respaldo |
|---|---|---|---|---|
{chr(10).join(rows)}
{chains}
## Evidencia de desempeño

{chr(10).join("- " + e for e in evidence)}
{extra}"""
    path = layout.map / f"{cid}.md"
    path.write_text(text, encoding="utf-8")
    return path


def check(layout, cid="C001"):
    competency = lib.parse(layout.map / f"{cid}.md")
    return lib.validate(competency, layout, lib.read_index(layout), lib.domain_subfields(layout), "0.3")


def test_domain_subfields_are_read_from_domain_md(layout):
    assert lib.domain_subfields(layout) == [
        "analítica descriptiva",
        "analítica predictiva",
        "analítica de grandes datos",
        "productos de datos",
        lib.TRANSVERSAL,
    ]


def test_a_well_formed_competency_validates(layout):
    write_competency(layout)
    assert check(layout) == ([], [])


@pytest.mark.parametrize(
    "rows, expected_state, expected_counts",
    [
        # Two issuers, one explicit and actual.
        ([source("E0001", "INFORMS", "actual"), source("E0003", "SAS", "precursor")], "incluida", (2, 2, 0, 1)),
        # A single issuer is never enough.
        ([source("E0001", "INFORMS", "actual")], "candidata", (1, 1, 0, 1)),
        # Documents of one organization count once.
        ([source("E0001", "INFORMS", "actual"), source("E0002", "INFORMS", "actual")], "candidata", (1, 1, 0, 1)),
        # Precursors count but are not enough alone.
        ([source("E0003", "SAS", "precursor"), source("E0005", "DataCamp", "actual", "solo conocimientos")], "candidata", (2, 1, 1, 1)),
        # The explicit row must itself be actual.
        ([source("E0003", "SAS", "precursor"), source("E0004", "MIT", "actual", "solo conocimientos")], "candidata", (2, 1, 1, 1)),
    ],
)
def test_consensus_rule(rows, expected_state, expected_counts):
    parsed = [lib.SourceRow(*[c.strip() for c in r.strip("|").split("|")]) for r in rows]
    counts = lib.consensus(parsed).as_header()
    assert lib.decide(["analítica predictiva"], parsed) == expected_state
    assert tuple(counts.values()) == expected_counts


def test_no_accepted_source_retires_the_competency(layout):
    write_competency(layout, rows=[source("E0006", "Blog", "actual")], consenso=(1, 1, 0, 1))
    competency = lib.parse(layout.map / "C001.md")
    assert lib.fix_consensus(competency, lib.read_index(layout))
    fixed = lib.parse(layout.map / "C001.md")
    assert fixed.header["estado"] == "retirada"
    assert fixed.header["consenso"] == {"emisores": 0, "explicitos": 0, "inferidos": 0, "actual": 0}
    assert check(layout)[0] == []


def test_fix_rewrites_only_the_computed_fields(layout):
    path = write_competency(layout, estado="candidata", consenso=(9, 9, 9, 9))
    before = path.read_text(encoding="utf-8")
    assert validate_.run(layout, [], fix=True) == 0
    after = path.read_text(encoding="utf-8")
    assert 'estado: "incluida"' in after
    assert "  emisores: 2" in after
    assert before.split("---\n", 2)[2] == after.split("---\n", 2)[2]


def test_wrong_consensus_is_an_error_without_fix(layout):
    write_competency(layout, consenso=(3, 3, 0, 3))
    errors, _ = check(layout)
    assert any("consenso is" in e for e in errors)


@pytest.mark.parametrize(
    "rows, message",
    [
        ([source("E0001", "SAS", "actual"), source("E0004", "MIT", "actual")], "is not part of"),
        ([source("E0001", "INFORMS", "precursor"), source("E0004", "MIT", "actual")], "role 'precursor'"),
        ([source("E0009", "Nobody", "actual"), source("E0004", "MIT", "actual")], "not in index.csv"),
        ([source("E0006", "Blog", "actual"), source("E0004", "MIT", "actual")], "no longer accepted"),
        ([source("E0001", "INFORMS", "actual", "probable"), source("E0004", "MIT", "actual")], "support must be"),
    ],
)
def test_source_rows_are_checked_against_index(layout, rows, message):
    write_competency(layout, rows=rows)
    errors, _ = check(layout)
    assert any(message in e for e in errors), errors


def test_synthesis_issuer_is_the_provider(layout):
    write_competency(layout, rows=[source("E0005", "DataCamp", "actual"), source("E0004", "MIT", "actual")])
    assert check(layout) == ([], [])


def test_cited_document_must_be_in_the_sources_table(layout):
    write_competency(layout, knowledge=["Validación [E0001 p. 3; E0003 p. 4]."])
    errors, _ = check(layout)
    assert any("E0003 is cited but missing" in e for e in errors)


def test_knowledge_and_evidence_need_citations(layout):
    write_competency(layout, knowledge=["Validación fuera de muestra."], evidence=["Un modelo validado."])
    errors, _ = check(layout)
    assert any("Conocimientos item lacks" in e for e in errors)
    assert any("Evidencia de desempeño item lacks" in e for e in errors)


def test_evidence_may_state_that_no_source_shows_a_product(layout):
    write_competency(layout, evidence=["Ninguna fuente muestra un producto concreto."])
    assert check(layout) == ([], [])


CHAIN = """
### Cadenas de inferencia

```
I1. E0003 p. 4: «texto».
    → Paso 1 (domain.md): razón.
{extra}    ⇒ Conclusión.
```
"""


@pytest.mark.parametrize(
    "extra_steps, ok",
    [("", True), ("    → Paso 2 (E0001 p. 2): razón.\n", True),
     ("    → Paso 2 (E0001 p. 2): razón.\n    → Paso 3 (E0001 p. 3): razón.\n", False)],
)
def test_inference_chains_have_at_most_two_steps(layout, extra_steps, ok):
    rows = [source("E0001", "INFORMS", "actual"), source("E0003", "SAS", "precursor", "inferido (I1)")]
    write_competency(layout, rows=rows, consenso=(2, 1, 1, 1), chains=CHAIN.format(extra=extra_steps))
    errors, _ = check(layout)
    assert (errors == []) is ok, errors


def test_referenced_chain_must_exist(layout):
    rows = [source("E0001", "INFORMS", "actual"), source("E0003", "SAS", "precursor", "inferido (I1)")]
    write_competency(layout, rows=rows, consenso=(2, 1, 1, 1))
    errors, _ = check(layout)
    assert any("I1 is referenced but not written" in e for e in errors)


def test_subfields_must_exist_in_domain_and_be_justified(layout):
    write_competency(layout, subfields=("analítica cuántica",))
    errors, _ = check(layout)
    assert any("not in domain.md" in e for e in errors)


def test_subfield_justification_by_domain(layout):
    path = write_competency(layout)
    text = path.read_text(encoding="utf-8").replace(
        "- analítica predictiva: explícita [E0001 p. 3].",
        "- analítica predictiva: por domain.md; la pregunta es qué ocurrirá.",
    )
    path.write_text(text, encoding="utf-8")
    assert check(layout) == ([], [])
    path.write_text(text.replace("por domain.md", "porque sí"), encoding="utf-8")
    assert any("needs 'explícita" in e for e in check(layout)[0])


def test_statement_must_match_header_and_sections_must_be_ordered(layout):
    path = write_competency(layout)
    text = path.read_text(encoding="utf-8")
    text = text.replace("Construir modelos predictivos validados, para estimar un resultado.\n\n## Subcampos",
                        "Otra cosa.\n\n## Subcampos")
    path.write_text(text, encoding="utf-8")
    assert any("differs from the Enunciado" in e for e in check(layout)[0])
    write_competency(layout, extra="\n## Opiniones\n\nTexto.\n")
    assert any("unknown sections" in e for e in check(layout)[0])


def test_optional_sections_are_allowed(layout):
    write_competency(layout, extra="\n## Notas de calibración\n\n- Nota.\n\n## Pendientes\n\n- Buscar fuente.\n")
    assert check(layout) == ([], [])


def test_old_domain_version_is_a_warning(layout):
    write_competency(layout)
    layout.domain.write_text(DOMAIN.replace("0.7", "0.8"), encoding="utf-8")
    errors, warnings = check(layout)
    assert errors == [] and len(warnings) == 1


def test_unsupported_format_version_stops_the_scripts(layout):
    layout.format.write_text("Versión 0.4\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        validate_.run(layout, [], fix=False)


def test_next_id_never_reuses_identifiers(layout):
    assert lib.next_id(layout) == "C001"
    write_competency(layout, cid="C007")
    assert lib.next_id(layout) == "C008"


def test_status_lists_pending_documents_and_the_map(layout):
    write_competency(layout)
    record.record(layout, ["E0001"])
    result = status.status(layout)
    pending = [e["id"] for e in result["pending"]]
    assert pending == ["E0002", "E0003", "E0004", "E0005"]
    assert result["next_id"] == "C002"
    assert result["map"][0]["id"] == "C001"
    assert result["pending"][0]["text"] is None


def test_status_flags_documents_mapped_under_an_older_domain(layout):
    write_competency(layout)
    record.record(layout, ["E0001"])
    layout.domain.write_text(DOMAIN.replace("0.7", "0.8"), encoding="utf-8")
    assert [e["id"] for e in status.status(layout)["outdated"]] == ["E0001"]


def test_record_lists_citing_competencies_and_refuses_rejected(layout):
    write_competency(layout)
    rows = record.record(layout, ["E0001", "E0003"])
    assert rows["E0001"]["competencias"] == "C001"
    assert rows["E0003"]["competencias"] == ""
    with pytest.raises(SystemExit):
        record.record(layout, ["E0006"])
