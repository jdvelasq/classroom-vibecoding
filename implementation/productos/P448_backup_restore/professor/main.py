"""Respalda y restaura un artefacto de operación mínimo."""

import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE = ROOT_DIR / "data" / "registry.json"
BACKUP = ROOT_DIR / "submission" / "registry.backup.json"
RESTORED = ROOT_DIR / "submission" / "registry.restored.json"


def backup_and_restore(source=SOURCE, backup=BACKUP, restored=RESTORED):
    """La restauración comprobable hace que el respaldo sea más que una copia olvidada."""

    shutil.copy2(source, backup)
    shutil.copy2(backup, restored)
    return json.loads(restored.read_text())


if __name__ == "__main__":
    backup_and_restore()
