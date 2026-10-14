from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
PROFESSOR_DIR = ACTIVITY_DIR / "professor"
IS_PROFESSOR = any(
    (path / ".PROFESSOR").exists() for path in ACTIVITY_DIR.parents
) and (PROFESSOR_DIR / "client.py").is_file()
CODE_DIR = PROFESSOR_DIR if IS_PROFESSOR else ACTIVITY_DIR / "src"


def test_01():
    client_file = CODE_DIR / "client.py"
    server_file = CODE_DIR / "server.py"

    assert client_file.is_file()
    assert client_file.read_text(encoding="utf-8").strip()
    assert server_file.is_file()
    assert server_file.read_text(encoding="utf-8").strip()
