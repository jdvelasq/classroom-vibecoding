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

## S03.P502.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P502.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Arquitecto de Datos que define «un data warehouse corporativo, algunos data marts» hasta «lagos de datos, arquitecturas híbridas …, gobernanza, linaje, seguridad» (p. 290); Líder de BD que participa en «arquitectura de datos y gobierno de información» (p. 286). Categoría: ya cubierta / fuera de alcance. Mart mínimo (P512 H02–H03) y linaje con cambio de grano (P502 H03) ya existen; lagos y gobierno corporativo son arquitectura empresarial, excluida.

## S03.P502.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.
