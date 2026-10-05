# Log — P518

## S02.P518.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P518_github_api/` (`data/github_issues_page_1.json`, `professor/main.py`, `src/main.py`, `submission/api_ingestion_report.csv`, `submission/github_issues.parquet` sólo como binario, `tests/test_activity.py`); P513 para contraste del reporte de ingestión.
- **Trazabilidad revisada:** P518 → `data.C01`–`data.C05`; `data.C01` sin evidencia (no hay pregunta), a escalar.
- **Highlights:** añadidos H01 (falla y reintento), H02 (proyección JSON y marca de pull requests; caso y datos), H03 (llave única y reporte). No inferible: proporción de pull requests y contenido del Parquet.
- **Ambigüedades:** procedencia y fecha de captura del JSON sin documentar; `pages_requested` y `status` constantes; el reporte no se escribe en el camino de falla; no hay notebook de profesor; la prueba acepta cualquier archivo.
- **Superficies / contrato / dependencias:** S01–S07 declaradas; contrato separado entre código, `submission/`, prueba y trazabilidad; recibe práctica de P513; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; el taller se lee como ingestión de APIs (Data Engineering) sin producto ni pregunta analítica.

## S03.P518.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CCF-The Web (p. 67: «Data are frequently obtained via web applications»), PDA (p. 114: «Utility of APIs; when to look for one») y DG-Data Acquisition (p. 70: «Pull-based and push-based approaches») — ya cubierta en lo técnico (H01–H03); el vacío de pregunta analítica no se resuelve con este documento. DM-Mining Web Data (p. 81: scraping, T2) — fuera de alcance.

## S03.P518.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «ensuring proper data transport across systems» (p. 5) — fuera de alcance/marginal: transporte entre sistemas es práctica de ingeniería; P513 y P518 ya tienen la auditoría de identidad no resuelta.

## S03.P518.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P518.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P518.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P518.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «scraping data from websites, processing text into data» (p. 43) — marginal o fuera de alcance: P518 ya cubre la obtención desde una fuente externa estructurada; el texto como dato pertenece a otros cursos.
