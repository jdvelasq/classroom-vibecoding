import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fetch as fetch_  # noqa: E402
import plan as plan_  # noqa: E402
import search_lib as lib  # noqa: E402

REAL_SOURCES = lib.ROOT / "01-evidence" / "sources.md"


@pytest.fixture
def layout(tmp_path):
    layout = lib.Layout(tmp_path)
    layout.ingest.mkdir(parents=True)
    (layout.evidence / "sources.md").write_text(REAL_SOURCES.read_text(encoding="utf-8"), encoding="utf-8")
    return layout


def fake_fetcher(content_by_url):
    def fetcher(url, out):
        if url not in content_by_url:
            raise ConnectionError(url)
        out.write_bytes(content_by_url[url])

    return fetcher


def candidate(target, url, source=lib.PLATFORMS):
    return {"source": source, "target": target, "query": "q", "url": url, "title": url.rsplit("/", 1)[-1]}


def test_plan_reads_the_approved_sources(layout):
    plan = lib.read_plan(layout)
    assert plan.platforms == ["Coursera", "DataCamp", "edX", "Udemy"]
    assert plan.manual_platforms == ["Pluralsight"]
    assert (plan.per_platform_limit, plan.per_university_limit, plan.universities_run_limit) == (3, 2, 10)
    assert plan.platform_category == "professional-learning"
    assert plan.university_category == "institutional"
    assert "Carnegie Mellon University" in plan.universities["Referentes internacionales"]
    assert set(plan.terms) == {"Campo", "Subcampos", "Tendencia emergente", "Precursores"}


def test_plan_refuses_an_unreviewed_sources_version(layout):
    path = layout.evidence / "sources.md"
    path.write_text(path.read_text(encoding="utf-8").replace("Versión 0.3", "Versión 0.4"), encoding="utf-8")
    with pytest.raises(SystemExit):
        lib.read_plan(layout)


def test_fetch_writes_pdfs_to_the_agent_inbox_and_logs_them(layout):
    rows = fetch_.fetch(layout, [candidate("DataCamp", "https://x/a")], fake_fetcher({"https://x/a": b"%PDF a"}))
    assert rows[0]["status"] == lib.FETCHED
    assert (layout.root / rows[0]["file"]).parent == lib.agent_inbox(layout)
    with lib.log_path(layout).open(newline="", encoding="utf-8") as f:
        logged = list(csv.DictReader(f))
    assert logged[0]["url"] == "https://x/a" and logged[0]["query"] == "q"


def test_fetch_deduplicates_by_url_across_runs(layout):
    fetcher = fake_fetcher({"https://x/a": b"%PDF a"})
    fetch_.fetch(layout, [candidate("DataCamp", "https://x/a")], fetcher)
    rows = fetch_.fetch(layout, [candidate("DataCamp", "https://x/a")], fetcher)
    assert rows[0]["status"] == "duplicate-url"


def test_fetch_deduplicates_by_hash_against_the_index(layout):
    pdf = layout.root / "known.pdf"
    pdf.write_bytes(b"%PDF known")
    with layout.index.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "sha256"])
        writer.writeheader()
        writer.writerow({"id": "E0001", "sha256": fetch_.sha256(pdf)})
    rows = fetch_.fetch(layout, [candidate("edX", "https://x/b")], fake_fetcher({"https://x/b": b"%PDF known"}))
    assert rows[0]["status"] == "duplicate-hash"
    assert not list(lib.agent_inbox(layout).glob("*.pdf"))


def test_fetch_applies_the_per_platform_limit(layout):
    urls = [f"https://x/{i}" for i in range(4)]
    rows = fetch_.fetch(
        layout,
        [candidate("Coursera", u) for u in urls],
        fake_fetcher({u: f"%PDF {u}".encode() for u in urls}),
    )
    assert [r["status"] for r in rows] == [lib.FETCHED] * 3 + ["over-limit"]


def test_fetch_applies_the_university_limits(layout):
    urls = [f"https://u/{i}" for i in range(3)]
    rows = fetch_.fetch(
        layout,
        [candidate("University of Warwick", u, lib.UNIVERSITIES) for u in urls],
        fake_fetcher({u: f"%PDF {u}".encode() for u in urls}),
    )
    assert [r["status"] for r in rows] == [lib.FETCHED] * 2 + ["over-limit"]


def test_fetch_rejects_targets_outside_sources_and_manual_platforms(layout):
    rows = fetch_.fetch(
        layout,
        [candidate("Pluralsight", "https://p/1"), candidate("Unknown U", "https://u/1", lib.UNIVERSITIES)],
        fake_fetcher({}),
    )
    assert all("not" in r["status"] for r in rows)


def test_fetch_logs_failures_without_stopping(layout):
    rows = fetch_.fetch(
        layout,
        [candidate("edX", "https://x/missing"), candidate("edX", "https://x/ok")],
        fake_fetcher({"https://x/ok": b"%PDF ok"}),
    )
    assert rows[0]["status"].startswith("failed")
    assert rows[1]["status"] == lib.FETCHED


def test_plan_reports_what_was_already_fetched(layout):
    fetch_.fetch(layout, [candidate("edX", "https://x/a")], fake_fetcher({"https://x/a": b"%PDF a"}))
    report = plan_.plan(layout)
    assert report["fetched_urls"] == ["https://x/a"]
    assert report["fetched_per_target"] == {"edX": 1}
