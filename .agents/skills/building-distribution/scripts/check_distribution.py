"""Checks that 06-distribution/ holds only what a student should receive.

Usage (from the repository root):

    python3 .agents/skills/building-distribution/scripts/check_distribution.py [--collect]

For every course and activity of COURSE_ACTIVITIES it checks that the copy
exists, has no instructor files at its root, keeps professor/, submission/
and temp/ empty but for .gitkeep, carries no local artifacts, and that an
activity-level requirements.txt only names packages of the root
requirements.txt. With --collect it also runs pytest test discovery in each
course, which must never fail because of the distribution layout.

Conditions the repository cannot show yet, such as a GitHub Actions grading
workflow or a requirements.txt at the root of each course, are reported as
not verified, not as errors. It never writes a file.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys

from build_distribution import (
    COURSE_ACTIVITIES,
    DISTRIBUTION_DIR,
    EMPTY_DIRECTORIES,
    INSTRUCTOR_FILE_NAMES,
    LOCAL_DIRECTORY_NAMES,
    LOCAL_FILE_NAMES,
    ROOT,
)

# pytest exits with 5 when it collects no tests, which a course of
# laboratories without tests may legitimately do.
NO_TESTS_COLLECTED = 5


def package_names(path) -> set[str]:
    names = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line and not line.startswith("-"):
            names.add(re.split(r"[\s<>=!~\[;]", line, maxsplit=1)[0].lower().replace("_", "-"))
    return names


def check_activity(activity_dir, root_packages: set[str]) -> list[str]:
    shown = activity_dir.relative_to(ROOT).as_posix()
    errors = []
    for name in INSTRUCTOR_FILE_NAMES:
        if (activity_dir / name).exists():
            errors.append(f"{shown}: the instructor file {name} was distributed")
    for name in EMPTY_DIRECTORIES:
        leftover = sorted(p.name for p in (activity_dir / name).glob("*") if p.name != ".gitkeep")
        if leftover:
            errors.append(f"{shown}/{name}/ is not empty: {', '.join(leftover)}")
    for path in activity_dir.rglob("*"):
        if path.name in LOCAL_DIRECTORY_NAMES or path.name in LOCAL_FILE_NAMES:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: local artifact")
    local_requirements = activity_dir / "requirements.txt"
    if local_requirements.exists():
        extra = sorted(package_names(local_requirements) - root_packages)
        if extra:
            errors.append(f"{shown}/requirements.txt names packages outside the root requirements.txt: {', '.join(extra)}")
    return errors


def collect(course_dir) -> str | None:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"],
        cwd=course_dir, capture_output=True, text=True,
    )
    if result.returncode in (0, NO_TESTS_COLLECTED):
        return None
    tail = "\n".join((result.stdout + result.stderr).strip().splitlines()[-5:])
    return f"{course_dir.relative_to(ROOT).as_posix()}: pytest discovery failed\n{tail}"


def check(run_collection: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    unverified: list[str] = []
    root_packages = package_names(ROOT / "requirements.txt")
    for course_id, activity_paths in COURSE_ACTIVITIES.items():
        course_dir = DISTRIBUTION_DIR / course_id
        if not course_dir.is_dir():
            errors.append(f"06-distribution/{course_id}/ does not exist; build the distribution first")
            continue
        for activity_path in activity_paths:
            activity_dir = course_dir / activity_path.split("/")[-1]
            if not activity_dir.is_dir():
                errors.append(f"{activity_dir.relative_to(ROOT).as_posix()} is missing")
                continue
            errors += check_activity(activity_dir, root_packages)
        if not list((course_dir / ".github" / "workflows").glob("*.y*ml")):
            unverified.append(f"06-distribution/{course_id}/ has no GitHub Actions grading workflow")
        if not (course_dir / "requirements.txt").exists():
            unverified.append(f"06-distribution/{course_id}/ has no requirements.txt taken from the root one")
        if run_collection:
            problem = collect(course_dir)
            if problem:
                errors.append(problem)
    return errors, unverified


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--collect", action="store_true")
    args = parser.parse_args()
    errors, unverified = check(args.collect)
    for item in unverified:
        print(f"not verified: {item}")
    for error in errors:
        print(f"error: {error}")
    print(f"{len(errors)} errors, {len(unverified)} not verified")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
