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

## S03.P521.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P521.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P521.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P521.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
