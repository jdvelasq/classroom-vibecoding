"""Records david's decision on one proposal: it leaves tasks.md and enters the log.

Usage (from the repository root):

    python3 .agents/skills/reviewing-tasks/scripts/decide.py <curso>/<Pxxx> <Tnn> \
        --decision aprobada|rechazada --reason "..." [--executor Claude] [--date YYYY-MM-DD] [--write]
    python3 .agents/skills/reviewing-tasks/scripts/decide.py <curso> <Nnn> \
        --decision aprobada|rechazada --reason "..." [--executor Claude] [--date YYYY-MM-DD] [--write]

An activity proposal is recorded as DEC.Pxxx.NN in the activity's log.md;
a course proposal as DEC.<curso>.NN in the course log.md. Either log is
created if it does not exist. The entry keeps the decision, its reason and
the full text of the proposal, so that later audits do not propose it
again. When the last proposal of a tasks file leaves it, the file is
removed. Without --write it prints what it would change.
"""

from __future__ import annotations

import argparse
import datetime as dt

from review_lib import ROOT, Layout, decide, parse_target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("target")
    parser.add_argument("task")
    parser.add_argument("--decision", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--executor", default="Claude")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    layout = Layout(ROOT)
    course, scope = parse_target(args.target)
    changes = decide(layout, course, scope, args.task, args.decision, args.reason,
                     args.executor, args.date)
    for path, text in changes.items():
        verb = "remove" if text is None else "write"
        print(f"{verb if args.write else 'would ' + verb} {layout.shown(path)}")
        if not args.write:
            continue
        if text is None:
            path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
