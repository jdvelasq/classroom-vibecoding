# Log — P521

## S02.P521.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P521_mapreduce_avanzado/` (`data/timesheet.csv`, `data/drivers.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/driver_activity.csv`, `tests/test_activity.py`); P519–P520 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P521 → `data.C01`, `data.C02`, `data.C05`; sin vacíos formales.
- **Highlights:** añadidos H01 (reducir al grano del maestro antes de unir; caso y datos), H02 (unión con regla explícita), H03 (ranking por millas).
- **Ambigüedades:** «mayor actividad» = millas; con horas el orden cambia (conductor 14 vs. 33 en archivos persistidos); `wage-plan` y `certified` ignorados; SQL comentado no ejecutado y con columnas distintas de la salida; agregación de P520 repetida sin leer su salida; unión con nombres ya mostrada en P519 (posible duplicación); `ssn` en datos.
- **Contraste con `case-selection.md`:** conforme (unión, agregación y orden sencillo).
- **Superficies / contrato / dependencias:** S01–S05; recibe de P519–P520; habilita: no evidenciada.
- **Auditoría de Analytics:** ranking descriptivo con pregunta explícita; riesgo de identidad bajo; incremento técnico pequeño.

## S03.P521.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - BDS-Parallel Programming (p. 59: «Typical parallel programming paradigm such as MapReduce», T2) — ya cubierta en el alcance decidido por `case-selection.md` (modelo de cómputo local al servicio de agregación y unión). La presencia de `ssn` y `location` en `drivers.csv` (S01) frente a DPSIA/DP p. 84 — marginal como cambio de aprendizaje (la pregunta no usa esas columnas); corresponde corregir el dataset distribuido, sin crear contenido.
