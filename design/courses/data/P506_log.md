# Log — P506

## S01.P506.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`.
- **Estado:** inicial; se inspeccionaron datos, notebooks, entregables, pruebas
  y `traceability.yaml`.
- **Decisión:** se creó descripción conservadora y se registró como límite la
  falta de extracción granular de la consulta.
- **Trazabilidad:** `data.C01`–`data.C03`, `data.C05` revisadas.

## S02.P506.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P506_scopus_sql_avanzado/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`); contraste con `implementation/data/P505_scopus_sql_intermedio/submission/authors_by_documents.csv`.
- **Trazabilidad revisada:** P506 → `data.C01`, `data.C02`, `data.C03`, `data.C05`; C03 sin evidencia explícita.
- **Preservado:** pregunta, entregable, condición temporal de continuidad y relación con P504–P505.
- **Completado:** se extrajo la consulta (dos CTE, `COUNT(DISTINCT publication_year)`, umbral `>= 3`) pendiente en la pasada previa; pruebas sólo de existencia; notebook del estudiante sin celdas.
- **Highlights añadidos:** H01 (CTE encadenadas), H02 (continuidad como años activos; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** umbral de 3 años y corte 2020 sin justificación; 2026 posiblemente incompleto; `data.C03` mapeada sin evidencia.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P503–P505; habilita P507 (CTE y periodo).
- **Auditoría de Analytics:** operacionalización con propósito analítico; riesgo moderado por encuadre de temario SQL.

## S03.P506.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PDA (p. 112: «Write appropriate database queries») y DM-IR (p. 82) — ya cubierta: secuencia SQL sobre el corpus. La desambiguación de autores (DG-Data Cleaning, p. 73: «entity resolution») es marginal para P506: identidad por ID Scopus ya decidida en P503 H03.

## S03.P506.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P506.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P506.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - derivar necesidades de datos de la pregunta (p. 13 «CAP-P.3.1.1 Identify an appropriate sequencing and prioritization of data needed, including sources»; p. 10 «CAP-P.2.2.1 Identify why analytics element(s) would be classified as an input, output, both, or neither») — ya cubierta: P500 H02, P503 (entidades desde la pregunta), P506 H02, P517 H02 (contrato mínimo derivado de la pregunta).

## S03.P506.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
