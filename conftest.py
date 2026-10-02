"""Aísla los paquetes de actividades durante la auditoría del repositorio."""

import sys

import pytest


@pytest.fixture(autouse=True)
def isolate_activity_packages():
    """Evita que una actividad reutilice los módulos de otra actividad."""
    for prefix in ("professor", "src"):
        for module_name in list(sys.modules):
            if module_name == prefix or module_name.startswith(f"{prefix}."):
                sys.modules.pop(module_name)
