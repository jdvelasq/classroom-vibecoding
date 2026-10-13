from __future__ import annotations

import json
from dataclasses import asdict

from search_lib import FETCHED, ROOT, Layout, read_index, read_log, read_plan


def plan(layout: Layout) -> dict[str, object]:
    log = read_log(layout)
    fetched = [row for row in log if row["status"] == FETCHED]
    fetched_per_target: dict[str, int] = {}
    for row in fetched:
        fetched_per_target[row["target"]] = fetched_per_target.get(row["target"], 0) + 1
    return {
        "sources": asdict(read_plan(layout)),
        "fetched_urls": sorted({row["url"] for row in fetched}),
        "fetched_per_target": fetched_per_target,
        "queries_already_run": sorted({(row["target"], row["query"]) for row in log}),
        "indexed_titles": sorted({row["title"] for row in read_index(layout)}),
    }


def main() -> int:
    print(json.dumps(plan(Layout(ROOT)), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
