# Log — P419

## S02.P419.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P419_random_seed/` (`professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/sample.json`, `tests/test_activity.py`, `data/`); digest de P420.
- **Trazabilidad revisada:** P419 → `productos.C02`, `productos.C05`; ambas débiles.
- **Highlights:** añadidos H01 (semilla registrada con la muestra, generador local) y H02 (ausencia de caso registrada como límite).
- **Ambigüedades:** `data/` vacía; las etiquetas `factory-3` y `factory-4` no existen en el dataset del curso. Sin `HOW_TO_RUN_ME.txt`. La prueba no verifica sensibilidad a la semilla.
- **Superficies / contrato / dependencias:** S01–S04; recibe: ninguna; habilita P420 (práctica de semilla 123).
- **Auditoría de Analytics:** no resuelta; mecanismo de programación sin capacidad analítica.
