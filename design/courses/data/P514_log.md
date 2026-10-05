# Log — P514

## S01.P514.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró ETL por etapas como diferencia técnica frente a P511.

## S02.P514.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P514_superstore_etl/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/test_activity.py`); P511 y P513 para relaciones; P515 para contraste.
- **Trazabilidad revisada:** P514 → `data.C01`–`data.C05`.
- **Highlights:** añadidos H01 (integración organizada en `extract`/`transform`/`publish`), H02 (reporte de filas por etapa con granos distintos; caso y datos).
- **Preservado:** pregunta, etapas raw/staging/curated, joins validados heredados, reporte de etapas y relación de extensión con P511.
- **Corregido:** «introduce publicación de datos curados» se precisa: staging y curated son el mismo DataFrame escrito dos veces, sin transformación entre ellas; el detalle publicado es igual al de P511.
- **Añadido:** raw = 5926 como suma de cuatro granos; estado constante; respuesta más gruesa que la de P511; posible duplicación con P511; interfaz del estudiante en `src/main.py`.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** duplicación de producto con P511 y de pregunta con P515, pendiente de decisión de curso.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P511; habilita la forma de reporte y la pregunta para P515.
- **Auditoría de Analytics:** no resuelta; lo nuevo es la organización ETL y el producto no cambia respecto de P511.

## S03.P514.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Transformation (p. 73: «Data Transformation pipeline») y SDM (p. 120: «Data lifecycle») — sin respaldo para el contraste ETL/ELT: el documento no lo trata; no aporta argumento a la auditoría pendiente.

## S03.P514.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 (merge/join, transform) (p. 5) — ya cubierta por P511 H01–H03; P514/P515 repiten la técnica (duplicación ya registrada por S02).

## S03.P514.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - transformaciones y uniones necesarias (p. 15 «CAP-P.3.5.1 Identify the transformations and merge/joins that may be necessary to solve an analytics problem») — ya cubierta: P511 H01–H03.
