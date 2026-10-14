import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_distribution  # noqa: E402


def make_activity(root):
    activity = root / "06-distribution" / "demo" / "P100_demo"
    for name in ("professor/.gitkeep", "submission/.gitkeep", "temp/.gitkeep", "tests/test_activity.py"):
        (activity / name).parent.mkdir(parents=True, exist_ok=True)
        (activity / name).write_text("", encoding="utf-8")
    return activity


def test_a_clean_activity_has_no_errors(tmp_path, monkeypatch):
    monkeypatch.setattr(check_distribution, "ROOT", tmp_path)
    assert check_distribution.check_activity(make_activity(tmp_path), {"pandas"}) == []


def test_instructor_material_and_foreign_packages_are_errors(tmp_path, monkeypatch):
    monkeypatch.setattr(check_distribution, "ROOT", tmp_path)
    activity = make_activity(tmp_path)
    (activity / "activity.md").write_text("x", encoding="utf-8")
    (activity / "professor" / "notebook.ipynb").write_text("x", encoding="utf-8")
    (activity / "requirements.txt").write_text("pandas<3\nnox==2024.4.15  # sesión\n", encoding="utf-8")
    errors = check_distribution.check_activity(activity, {"pandas"})
    assert any("instructor file activity.md" in e for e in errors)
    assert any("professor/ is not empty: notebook.ipynb" in e for e in errors)
    assert any("outside the root requirements.txt: nox" in e for e in errors)
