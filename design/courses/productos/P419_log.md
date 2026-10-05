# Log — P419

## S02.P419.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P419_random_seed/` (`professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/sample.json`, `tests/test_activity.py`, `data/`); digest de P420.
- **Trazabilidad revisada:** P419 → `productos.C02`, `productos.C05`; ambas débiles.
- **Highlights:** añadidos H01 (semilla registrada con la muestra, generador local) y H02 (ausencia de caso registrada como límite).
- **Ambigüedades:** `data/` vacía; las etiquetas `factory-3` y `factory-4` no existen en el dataset del curso. Sin `HOW_TO_RUN_ME.txt`. La prueba no verifica sensibilidad a la semilla.
- **Superficies / contrato / dependencias:** S01–S04; recibe: ninguna; habilita P420 (práctica de semilla 123).
- **Auditoría de Analytics:** no resuelta; mecanismo de programación sin capacidad analítica.

## S03.P419.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PDA-Numerical Computing (p. 119: «Allow reproducibility in data analysis with non-deterministic algorithms») — ya cubierta: P419 H01.
