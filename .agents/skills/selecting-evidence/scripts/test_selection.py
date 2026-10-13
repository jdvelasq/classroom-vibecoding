import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import apply as apply_  # noqa: E402
import evidence_lib as lib  # noqa: E402
import intake  # noqa: E402
import reeval  # noqa: E402

FULL = {"pertinencia": 2, "autoridad": 2, "especificidad": 2, "vigencia": 2, "acceso": 2}


@pytest.fixture
def layout(tmp_path):
    layout = lib.Layout(tmp_path)
    layout.ingest.mkdir(parents=True)
    layout.criteria.write_text("# Criterios\n\nVersión 0.3 (borrador)\n", encoding="utf-8")
    layout.domain.write_text("# Dominio\n\nVersión 0.4 (borrador)\n", encoding="utf-8")
    return layout


def add_doc(layout, name, content=b"%PDF fake", warnings=(), folder=""):
    pdf = layout.ingest / folder / f"{name}.pdf"
    pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf.write_bytes(content)
    header = ["---", f'source: "{layout.shown(pdf)}"', "pages: 3"]
    if warnings:
        header.append("warnings:")
        header += [f'  - "{w}"' for w in warnings]
    pdf.with_suffix(".md").write_text("\n".join(header + ["---", "# Body"]), encoding="utf-8")
    return pdf


def judgment(layout, pdf, **overrides):
    base = {
        "pdf": layout.shown(pdf),
        "title": pdf.stem,
        "issuer": "Issuer",
        "year": 2024,
        "scores": dict(FULL),
        "material_warnings": False,
        "category": "authoritative",
        "role": "actual",
        "rationale": "test",
    }
    base.update(overrides)
    return base


@pytest.mark.parametrize(
    "source, scores, expected",
    [
        ("david", {"pertinencia": 0, "autoridad": None, "especificidad": None, "vigencia": None, "acceso": 0}, "reject"),
        ("david", dict(FULL, autoridad=1, especificidad=1, vigencia=1), "accept"),
        ("david", dict(FULL, pertinencia=1, acceso=0), "accept"),
        ("agent", dict(FULL, autoridad=1, especificidad=1, vigencia=1), "accept"),
        ("agent", dict(FULL, autoridad=1, especificidad=1, vigencia=1, acceso=1), "reject"),
        ("agent", dict(FULL, especificidad=0), "reject"),
    ],
)
def test_decision_rule_always_decides(source, scores, expected):
    assert lib.decide(source, scores) == expected


def test_intake_creates_index_and_lists_pending(layout):
    add_doc(layout, "a", warnings=["páginas con poco texto: [1]"])
    add_doc(layout, "b", content=b"other", folder="agent")
    manifest = intake.intake(layout)
    assert layout.index.read_text(encoding="utf-8").startswith("id,sha256,file,title")
    by_name = {Path(p["pdf"]).name: p for p in manifest["pending"]}
    assert by_name["a.pdf"]["source"] == "david"
    assert by_name["a.pdf"]["conversion_warnings"] == ["páginas con poco texto: [1]"]
    assert by_name["b.pdf"]["source"] == "agent"


def test_intake_ignores_hidden_and_non_pdf_files(layout):
    (layout.ingest / ".gitkeep").write_text("", encoding="utf-8")
    (layout.ingest / ".DS_Store").write_bytes(b"x")
    (layout.ingest / ".hidden.pdf").write_bytes(b"x")
    (layout.ingest / "notes.txt").write_text("x", encoding="utf-8")
    assert intake.intake(layout)["pending"] == []


def test_accept_and_reject_are_filed_and_warnings_do_not_block(layout):
    accepted = add_doc(layout, "accepted", content=b"1")
    rejected = add_doc(layout, "rejected", content=b"2")
    warned = add_doc(layout, "warned", content=b"3")
    outcomes = apply_.apply(
        layout,
        [
            judgment(layout, accepted),
            judgment(layout, rejected, scores=dict(FULL, pertinencia=0), category=None, role=None),
            judgment(layout, warned, material_warnings=True, doubts="scanned pages"),
        ],
    )
    assert [o["decision"] for o in outcomes] == ["accept", "reject", "accept"]
    assert (layout.evidence / "pdf/authoritative/accepted.pdf").exists()
    moved_md = layout.evidence / "md/authoritative/accepted.md"
    assert 'source: "01-evidence/pdf/authoritative/accepted.pdf"' in moved_md.read_text(encoding="utf-8")
    assert (layout.rejected / "rejected.pdf").exists() and (layout.rejected / "rejected.md").exists()
    assert list(layout.ingest.glob("*.pdf")) == []
    assert 'doubts: "scanned pages"' in (layout.decisions / "E0003.yaml").read_text(encoding="utf-8")
    with layout.index.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert [(r["id"], r["decision"]) for r in rows] == [("E0001", "accept"), ("E0002", "reject"), ("E0003", "accept")]
    assert "criteria_version: \"0.3\"" in (layout.decisions / "E0001.yaml").read_text(encoding="utf-8")


def test_exact_duplicate_leaves_inbox(layout):
    first = add_doc(layout, "first", content=b"same")
    apply_.apply(layout, [judgment(layout, first)])
    add_doc(layout, "copy", content=b"same")
    manifest = intake.intake(layout)
    assert manifest["pending"] == []
    assert manifest["duplicates"][0]["duplicate_of"] == "E0001"
    assert (layout.rejected / "duplicates" / "copy.pdf").exists()


def test_title_and_issuer_match(layout):
    old = add_doc(layout, "old", content=b"old")
    apply_.apply(layout, [judgment(layout, old, title="Framework", year=2020)])
    new = add_doc(layout, "new", content=b"new")
    same = add_doc(layout, "same", content=b"same-year")
    outcomes = apply_.apply(
        layout,
        [
            judgment(layout, new, title="FRAMEWORK", year=2024),
            judgment(layout, same, title="Framework", year=2020),
        ],
    )
    assert outcomes[0]["decision"] == "accept"
    assert "previous_edition: \"E0001\"" in (layout.decisions / "E0002.yaml").read_text(encoding="utf-8")
    assert outcomes[1]["decision"] == "reject"
    assert 'duplicate_of: "E0001"' in (layout.decisions / "E0003.yaml").read_text(encoding="utf-8")


def test_unsupported_criteria_version_stops(layout):
    layout.criteria.write_text("Versión 9.9\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        apply_.apply(layout, [])


def test_dry_run_moves_nothing(layout):
    pdf = add_doc(layout, "doc")
    apply_.apply(layout, [judgment(layout, pdf)], dry_run=True)
    assert pdf.exists()
    assert lib.read_index(layout) == []


def test_domain_change_restores_and_reevaluates(layout):
    kept = add_doc(layout, "kept", content=b"kept")
    dropped = add_doc(layout, "dropped", content=b"dropped")
    apply_.apply(
        layout,
        [
            judgment(layout, kept),
            judgment(layout, dropped, scores=dict(FULL, pertinencia=0), category=None, role=None),
        ],
    )
    assert reeval.outdated(layout)["rejected_for_pertinence"] == []

    layout.domain.write_text("Versión 0.5\n", encoding="utf-8")
    pending = reeval.outdated(layout)
    assert [e["id"] for e in pending["rejected_for_pertinence"]] == ["E0002"]
    assert [e["id"] for e in pending["accepted"]] == ["E0001"]

    restored = reeval.restore(layout, "E0002")
    assert restored == layout.ingest / "dropped.pdf"
    assert 'source: "01-evidence/ingest/dropped.pdf"' in restored.with_suffix(".md").read_text(encoding="utf-8")
    assert [r["id"] for r in lib.read_index(layout)] == ["E0001"]
    assert intake.intake(layout)["duplicates"] == []

    apply_.apply(layout, [judgment(layout, restored)])
    decision = lib.read_decision(layout.decisions / "E0003.yaml")
    assert decision["reevaluates"] == "E0002"
    assert decision["domain_version"] == "0.5"
    assert (layout.decisions / "superseded" / "E0002.yaml").exists()


def test_regulation_copy_is_reported_not_judged(layout):
    layout.regulations.mkdir(parents=True)
    (layout.regulations / "cesu.pdf").write_bytes(b"norm")
    add_doc(layout, "cesu-copy", content=b"norm")
    manifest = intake.intake(layout)
    assert manifest["pending"] == [] and manifest["duplicates"] == []
    assert manifest["regulations"][0]["regulation"] == "00-regulations/pdf/cesu.pdf"
    assert not (layout.ingest / "cesu-copy.pdf").exists()
