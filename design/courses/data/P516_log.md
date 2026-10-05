# Log — P516

## S01.P516.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró el alcance de `zipcode=0` como límite crítico.

## S02.P516.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P516_vermont_calidad/` (`data/vermont.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/quality_report.csv`, `tests/test_activity.py`); P500, P510, P511 para relaciones; P517 para dependencia.
- **Trazabilidad revisada:** P516 → `data.C01`, `data.C03`, `data.C04`; coherente.
- **Highlights:** añadidos H01 (granos mezclados por total estatal; caso y datos), H02 (calidad como reglas con dimensión y conteo), H03 (clave compuesta y dominio como unidad de análisis).
- **Preservado:** pregunta, cinco reglas, clave (`zipcode`, `agi_stub`), `zipcode = 0` como riesgo de alcance.
- **Corregido:** la descripción previa hablaba de «perfilado»; el notebook evalúa reglas sobre 5 de 147 columnas, no perfila el extracto.
- **Añadido:** 1476 × 147; ausencia de procedencia, año y diccionario; defecto de estado (sólo la regla de alcance puede no ser `PASS`); diagnóstico sin conjunto filtrado; prueba de sólo existencia.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** la interpretación de `zipcode = 0` se apoya sólo en un comentario.
- **Superficies / contrato / dependencias:** S01–S05; habilita datos y reglas para P517.
- **Auditoría de Analytics:** diagnóstico de aptitud para una pregunta; sin riesgo de identidad relevante.

## S03.P516.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Cleaning (pp. 73–74: «The dimensions of data quality»; «Various forms for data quality rules such as functional dependencies (FD)…»; «suitable for its intended use») — ya cubierta: reglas nombradas por dimensión (H02), clave compuesta y dominio (H03), aptitud para la pregunta (H01). La falta de diccionario y procedencia (S01) es marginal desde este documento (CCF p. 66: «Files: data, metadata» es genérico).

## S03.P516.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T02.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta por P516 H02–H03.

## S03.P516.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - CAP-E.3.6.1 «accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y 3.6.4 métodos de evaluación (p. 15) — ya cubierta por P516 H02; atípicos se integran en la candidata de perfil.
  - CAP-E.3.7.1 y 3.8.1 (p. 16) — ya cubierta por P516 H01 (alcance que cambia la pregunta) y P517 H01; la parte no cubierta va a las candidatas.

## S03.P516.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limitaciones a partir de atributos, contexto y metadatos (p. 14 «CAP-P.3.2.1 Identify data limitations and constraints based on data attributes, data context, and metadata, and propose appropriate course of actions») — ya cubierta en lo esencial por H01–H03; la verificación de metadatos se propone desde CRISP-DM.
  - perfilado multivariado (p. 15 «CAP-P.3.6.2 Identify patterns and characteristics of a multivariate dataset from data profiling outputs») — marginal: perfilar las 147 columnas contradice el contrato mínimo derivado de la pregunta (P517 H02); el perfilado exploratorio es de Descriptiva.

## S03.P516.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - esquema de eventos de error y dimensión de auditoría (pp. 23–24) — ya cubierta por P516 H02 (reglas con dimensión y conteo) y P514 H02 (reporte por etapa); como esquema dimensional del *back room* es fuera de alcance.

## S03.P516.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «use simple graphics to check data for artifacts, snafus, and inconsistencies» y «Data consistency checking» (pp. 45–46) — marginal: `AGENTS.md` ya exige celdas de evidencia visual y las reglas nombradas de P516 (H02) son el mecanismo de consistencia. Extender a las 147 columnas sin diccionario no tiene caso riguroso.

## S03.P516.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad: aplicación de reglas de limpieza (tiempos mínimos, duplicados), control de completitud, consistencia de escalas» (p. 238); «Trazabilidad y gobernanza: separación clara entre evidencia empírica … y supuestos de negocio» (p. 41). Categoría: ya cubierta. Controles de calidad ejecutables (P500 H04), reglas nombradas con dimensión y conteo (P516 H02), contrato y decisiones persistidas (P517 H02–H04).
