"""Fetches the pages chosen by the agent into 01-evidence/ingest/agent/.

The candidates file is a JSON list, one object per page:

    [
      {
        "source": "platforms",          # or "universities"
        "target": "DataCamp",           # a platform or university of sources.md
        "query": "data analyst career track",
        "url": "https://www.datacamp.com/tracks/data-analyst-with-python",
        "title": "Data Analyst with Python"
      }
    ]

Candidates are processed in order, so the agent lists the best page first.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Callable

import requests

from search_lib import (
    FETCHED,
    PLATFORMS,
    ROOT,
    UNIVERSITIES,
    Layout,
    Plan,
    agent_inbox,
    append_log,
    read_index,
    read_log,
    read_plan,
    sha256,
    slug,
    today,
)

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
]
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) classroom-vibecoding evidence search"

Fetcher = Callable[[str, Path], None]


def chrome() -> str:
    for candidate in [os.environ.get("CHROME_BIN", "")] + CHROME_CANDIDATES:
        if candidate and (Path(candidate).exists() or shutil.which(candidate)):
            return candidate
    raise SystemExit("No Chrome or Chromium found; set CHROME_BIN.")


def fetch_url(url: str, out: Path) -> None:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=60)
    response.raise_for_status()
    if "pdf" in response.headers.get("Content-Type", "") or response.content.startswith(b"%PDF"):
        out.write_bytes(response.content)
        return
    # Chrome's default header and footer are kept on purpose: they stamp the
    # URL and the access date on every page, so the PDF carries its own
    # provenance. The price is that two prints of one page never share a
    # hash, which is why the log also deduplicates by URL.
    subprocess.run(
        [chrome(), "--headless=new", "--disable-gpu", f"--print-to-pdf={out}", url],
        check=True,
        capture_output=True,
        timeout=120,
    )
    if not out.exists() or out.stat().st_size == 0:
        raise RuntimeError("Chrome produced no PDF")


def limit_reason(plan: Plan, candidate: dict[str, str], run: Counter) -> str | None:
    source, target = candidate["source"], candidate["target"]
    if source == PLATFORMS:
        if target not in plan.platforms:
            return f"{target} is not an agent platform in sources.md"
        if run[target] >= plan.per_platform_limit:
            return "over-limit"
    elif source == UNIVERSITIES:
        if not any(target in group for group in plan.universities.values()):
            return f"{target} is not a university in sources.md"
        if run[target] >= plan.per_university_limit or run[UNIVERSITIES] >= plan.universities_run_limit:
            return "over-limit"
    else:
        return f"unknown source {source}"
    return None


def unique_path(folder: Path, stem: str) -> Path:
    path = folder / f"{stem}.pdf"
    n = 2
    while path.exists():
        path = folder / f"{stem}-{n}.pdf"
        n += 1
    return path


def fetch(layout: Layout, candidates: list[dict[str, str]], fetcher: Fetcher = fetch_url) -> list[dict[str, str]]:
    plan = read_plan(layout)
    log = read_log(layout)
    fetched_urls = {row["url"] for row in log if row["status"] == FETCHED}
    known_hashes = {row["sha256"] for row in read_index(layout)}
    known_hashes |= {row["sha256"] for row in log if row["status"] == FETCHED}
    inbox = agent_inbox(layout)
    inbox.mkdir(parents=True, exist_ok=True)
    known_hashes |= {sha256(p) for p in layout.ingest.rglob("*.pdf")}

    run: Counter = Counter()
    rows = []
    for candidate in candidates:
        row = {
            "date": today(),
            "source": candidate["source"],
            "target": candidate["target"],
            "query": candidate.get("query", ""),
            "url": candidate["url"],
            "file": "",
            "sha256": "",
        }
        reason = limit_reason(plan, candidate, run)
        if reason:
            rows.append({**row, "status": reason})
            continue
        if candidate["url"] in fetched_urls:
            rows.append({**row, "status": "duplicate-url"})
            continue

        stem = slug(candidate["target"], 30) + "-" + slug(candidate.get("title") or candidate["url"])
        with tempfile.TemporaryDirectory() as tmp:
            downloaded = Path(tmp) / "page.pdf"
            try:
                fetcher(candidate["url"], downloaded)
            except Exception as error:  # noqa: BLE001 - every failure is logged, none stops the run
                rows.append({**row, "status": f"failed: {type(error).__name__}"})
                continue
            digest = sha256(downloaded)
            if digest in known_hashes:
                rows.append({**row, "sha256": digest, "status": "duplicate-hash"})
                continue
            out = unique_path(inbox, stem)
            shutil.move(str(downloaded), out)

        known_hashes.add(digest)
        fetched_urls.add(candidate["url"])
        run[candidate["target"]] += 1
        if candidate["source"] == UNIVERSITIES:
            run[UNIVERSITIES] += 1
        rows.append({**row, "file": layout.shown(out), "sha256": digest, "status": FETCHED})

    append_log(layout, rows)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("candidates", type=Path)
    args = parser.parse_args()
    candidates = json.loads(args.candidates.read_text(encoding="utf-8"))
    rows = fetch(Layout(ROOT), candidates)
    json.dump(rows, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
