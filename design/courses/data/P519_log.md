# Log — P519

## S02.P519.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P519_mapreduce_operators/` (`data/timesheet.csv`, `data/drivers.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/operator_walkthrough.csv`, `tests/test_activity.py`); `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P519 → `data.C02`, `data.C05`; sin vacíos.
- **Highlights:** añadidos H01 (operador genérico vs. regla), H02 (extracto y llave compartida; caso y datos), H03 (unión por clave), H04 (operadores complementarios).
- **Ambigüedades:** `drivers.csv` contiene `ssn` y `location` sin procedencia ni restricción documentadas; `flat_map_pairs` duplica `map_pairs`; `left_outer_join_by_key` no se usa; `union_pairs` con lista vacía y `/ 10` sin significado; `inner_join_by_key` asume clave derecha única.
- **Contraste con `case-selection.md`:** implementado conforme al diseño (operaciones genéricas, extracto pequeño, sin PySpark).
- **Superficies / contrato / dependencias:** S01–S05; habilita P520–P523 por copia literal de funciones y P520–P521 por datos idénticos.
- **Auditoría de Analytics:** taller técnico sin producto propio; aceptable como habilitador sólo por su uso en P520–P521.

## S03.P519.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - BDS-Parallel Programming (p. 59: «Typical parallel programming paradigm such as MapReduce», T2) — ya cubierta en el alcance decidido por `case-selection.md` (modelo de cómputo local al servicio de agregación y unión). La presencia de `ssn` y `location` en `drivers.csv` (S01) frente a DPSIA/DP p. 84 — marginal como cambio de aprendizaje (la pregunta no usa esas columnas); corresponde corregir el dataset distribuido, sin crear contenido.

## S03.P519.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P519.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P519.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
