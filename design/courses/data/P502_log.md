# Log — P502

## S01.P502.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `professor/main.py`, `submission/`, pruebas y
  `traceability.yaml`.
- **Decisión:** se creó el mapa de catálogos y linaje; se registró que los
  productos presentes son generados por material de profesor.
- **Trazabilidad:** `data.C03`–`data.C05` revisadas.
- **Auditoría:** el producto sigue una pregunta de negocio y preserva
  Analytics como identidad.

## S02.P502.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P502_superstore_linaje/` (`data/superstore_orders.csv`, `professor/main.py`, `src/main.py`, `submission/data_catalog.csv`, `submission/column_catalog.csv`, `submission/lineage.csv`, `submission/questions.json`, `tests/test_activity.py`); contraste con `implementation/data/P501_superstore_serving/submission/serving_manifest.csv`.
- **Trazabilidad revisada:** P502 → `data.C03`, `data.C04`, `data.C05`; C03 parcial, C05 débil.
- **Preservado:** pregunta, tres artefactos de documentación, grano y consumidor por dataset, y la constatación previa de que no hay pipeline ejecutable.
- **Corregido:** la descripción previa decía que P502 «reutiliza artefactos Superstore»; el código no lee el CSV ni los archivos de P501: catálogo y linaje son literales escritos a mano.
- **Highlights añadidos:** H01 (catálogo de datasets), H02 (roles de columnas), H03 (cambio de grano en el linaje; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** `data/superstore_orders.csv` presente sin uso; ubicación `submission` remite a P501; consumidor «Privado» sin explicación (¿restricción de uso?); catálogo de columnas parcial; linaje no verificable contra el código.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P501 nombres y granos; no habilita una actividad posterior de forma demostrable.
- **Auditoría de Analytics:** documentación que sirve a la auditabilidad de métricas; riesgo de documentación formal desconectada de los datos.

## S03.P502.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DI-Methods (p. 91: «Understand how to use the integrity models in multiple data ownership domains to ensure provenance») — ya cubierta en lo pertinente: linaje con cambio de grano (H03); el resto es seguridad.

## S03.P502.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.4.3 «lineage, traceability, and version control of data» (p. 15) — ya cubierta por P502 H03 y P503 H01; versionado de datos como práctica es marginal.
  - CAP-E.3.2.2 roles de gobierno (owner, steward, custodian) (p. 14) — marginal: vocabulario organizacional sin caso; el consumidor «Privado» de P502 es un defecto de S02, no una señal de este documento.

## S03.P502.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - linaje y trazabilidad (p. 15 «CAP-P.3.4.3 Identify the purpose of lineage, traceability, and version control of data») — ya cubierta: P502 H03 (cambio de grano por paso de linaje), P503 H01 (consulta preservada).
