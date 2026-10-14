"""Prints, as JSON, the open proposals of an activity or a course, in the order they are discussed.

Usage (from the repository root):

    python3 .agents/skills/reviewing-tasks/scripts/pending.py <curso>/<Pxxx>
    python3 .agents/skills/reviewing-tasks/scripts/pending.py <curso>

`<curso>/<Pxxx>` lists the open proposals of one activity's tasks.md;
`<curso>` lists those of the course tasks.md. `next` is the proposal to
discuss now, with its full text; the rest are listed by id and title only,
so that one proposal is discussed at a time. It reads only.
"""

from __future__ import annotations

import argparse
import json

from review_lib import ROOT, Layout, parse_target, proposals


def pending(layout: Layout, target: str) -> dict[str, object]:
    course, scope = parse_target(target)
    found = proposals(layout, course, scope)
    first = found[0] if found else None
    return {
        "target": target,
        "open": len(found),
        "next": None if first is None else {
            "scope": first.scope,
            "id": first.id,
            "title": first.title,
            "state": first.state,
            "tasks": layout.shown(first.tasks),
            "log": layout.shown(first.log),
            "text": first.text,
        },
        "queue": [{"scope": p.scope, "id": p.id, "title": p.title} for p in found[1:]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("target")
    args = parser.parse_args()
    print(json.dumps(pending(Layout(ROOT), args.target), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
