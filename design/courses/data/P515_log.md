# Log — P515

## S01.P515.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se confirmó contraste ELT con P514 y se preservó la pregunta común.

## S02.P515.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P515_superstore_elt/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/test_activity.py`); P511, P512 y P514 para relaciones.
- **Trazabilidad revisada:** no existe entrada P515 en `implementation/data/traceability.yaml`; escalada.
- **Highlights:** añadidos H01 (transformación en el motor tras cargar raw), H02 (uniones SQL por claves contextuales homónimas sin validación de cardinalidad; caso y datos), H03 (capas raw y curada en un mismo artefacto).
- **Preservado:** pregunta común con P514, carga raw, CTAS en SQLite, reporte de filas y contraste ETL/ELT.
- **Corregido:** la descripción previa afirmaba trazabilidad `data.C01`–`data.C05`; la entrada no existe. Se precisa que la tabla curada selecciona sólo cuatro columnas de contexto.
- **Añadido:** ausencia de validación de cardinalidad en SQL; coincidencia con P514 salvo precisión flotante, no verificada por código; estado constante; capas raw dentro de la entrega; interfaz del estudiante en `src/main.py`.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** falta de entrada de trazabilidad; duplicación de pregunta y respuesta con P514.
- **Superficies / contrato / dependencias:** S01–S06 (S06 = trazabilidad ausente); recibe de P511, P512, P514; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** no resuelta; la contribución se reduce a un contraste técnico de Data Engineering.

## S03.P515.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Transformation (p. 73: «Data Transformation pipeline») y SDM (p. 120: «Data lifecycle») — sin respaldo para el contraste ETL/ELT: el documento no lo trata; no aporta argumento a la auditoría pendiente.

## S03.P515.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 (merge/join, transform) (p. 5) — ya cubierta por P511 H01–H03; P514/P515 repiten la técnica (duplicación ya registrada por S02).

## S03.P515.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
