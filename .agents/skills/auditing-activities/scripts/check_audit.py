"""Validates the model's audit of a course before it is applied.

Usage (from the repository root):

    python3 .agents/skills/auditing-activities/scripts/check_audit.py <audit.json>

The audit names its course. The check confirms that every activity of the
course is described and has a decision, that every outcome and item has one
category, that anchors and proposals point to highlights, surfaces and
proposals that exist, that a point change stays one bounded change, and that
the current traceability.yaml is well formed. It prints warnings and errors
and exits with status 1 when there is an error. It never writes a file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from activity_lib import ROOT, Layout, require_course, require_supported_format
from audit_lib import load_audit, requirements, validate_audit, validate_traceability


def check(layout: Layout, audit_path: Path) -> tuple[list[str], list[str]]:
    require_supported_format(layout)
    audit = load_audit(audit_path)
    course = str(audit.get("curso", ""))
    require_course(layout, course)
    errors, warnings = validate_audit(layout, audit, course)
    targets = {t.id: t for t in requirements(layout, course).targets}
    trace_errors, trace_warnings = validate_traceability(layout, course, targets)
    return errors + trace_errors, warnings + trace_warnings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()
    errors, warnings = check(Layout(ROOT), args.audit)
    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
