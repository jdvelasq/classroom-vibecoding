# Log — P202

## S01.P202.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se identificó preparación textual como capacidad técnica propia, no clasificación.

## S01.P202.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P202_tokenizacion/`
  (notebook de profesor, matriz, vocabulario, metadatos y pruebas) y P202 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato actual de S01 y se añadieron highlights
  para calidad de abstracts, limpieza fundamentada en evidencia, tratamiento
  diferenciado de conectores y retórica, transformación léxica, vectorización y
  persistencia de la representación.
- **Límite:** la preparación está orientada a inglés y a este corpus; no crea ni
  evalúa un modelo predictivo.
- **Auditoría de Analytics:** el producto es una representación textual
  verificable para análisis posterior; NLP y vectorización contribuyen a ese
  producto sin redefinir la identidad del curso.

## S01.P202.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H06, superficies de corpus/representación/producto,
  contrato de evidencia y dependencia demostrable hacia P203.

## S01.P202.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H06 con superficies actuales; se preserva que el taller prepara representación y no un modelo predictivo.
- **Auditoría de Analytics:** NLP y vectorización sirven a una representación textual verificable.

## S03.P202.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Finding themes in the project description» (p. 7): marginal; agrupa textos, no cambia la preparación auditable de P202.
  - NLP con deep learning (p. 9): fuera de alcance por la misma razón que en P201.

## S03.P202.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - obtención/gestión/calidad de datos para ML y NLP (p. 5): ya cubierta respecto al corpus Scopus (H01–H06); el benchmark no aporta criterio concreto que cambie las reglas auditables de exclusión, limpieza o vectorización.
  - NLP generativo y modelos multimodales (pp. 5–6): fuera de alcance del producto de P202, que prepara abstracts en inglés para análisis posterior; el folleto no aporta corpus, tarea evaluable ni evidencia para reemplazar o extender su representación.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P202.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - procesamiento de lenguaje natural (p. 5) y modelos multimodales (p. 6): fuera de alcance; enunciados sin tarea ni corpus que modifiquen la preparación auditable de H01–H06.
  - obtención y gestión de datos para ML (p. 5): ya cubierta para el corpus (H01–H02: reglas de calidad derivadas de evidencia).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P202.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - extracción y representación de *features* (DM-Data Preparation, T1): ya cubierta para texto (H03–H05).
  - extracción de información (DM, electiva): marginal.

## S03.P202.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - evaluación y documentación de la calidad de datos (Tasks 3.5–3.7, p. 5): ya cubierta (H01–H02, H06: reglas de calidad y metadatos persistidos).

## S03.P202.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel inicial detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P202.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel intermedio detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.
