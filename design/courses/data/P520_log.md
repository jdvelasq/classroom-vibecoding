# Log — P520

## S02.P520.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P520_mapreduce_basico/` (`data/timesheet.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/driver_metrics.csv`, `tests/test_activity.py`); P519 para operadores y datos; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P520 → `data.C01`, `data.C02`, `data.C05`; C01 parcial.
- **Highlights:** añadidos H01 (SQL como especificación), H02 (valor compuesto con contador; caso y datos), H03 (aplicación completa y persistencia).
- **Ambigüedades:** SQL no ejecutado y distinto de la salida (`mean_hours`); el SQL aparece después del mapper, a diferencia de «primero la pregunta y su SQL» de `case-selection.md`; `weeks` cuenta filas sin verificar unicidad conductor-semana; procedencia de datos no documentada.
- **Contraste con `case-selection.md`:** conforme en pregunta, datos y SQL acotado; añade `mean_hours`.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P519; P521 repite la agregación sin consumir el archivo.
- **Auditoría de Analytics:** producto descriptivo por entidad con pregunta explícita; MapReduce como habilitador; sin interpretación de resultados.

## S03.P520.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - BDS-Parallel Programming (p. 59: «Typical parallel programming paradigm such as MapReduce», T2) — ya cubierta en el alcance decidido por `case-selection.md` (modelo de cómputo local al servicio de agregación y unión). La presencia de `ssn` y `location` en `drivers.csv` (S01) frente a DPSIA/DP p. 84 — marginal como cambio de aprendizaje (la pregunta no usa esas columnas); corresponde corregir el dataset distribuido, sin crear contenido.
