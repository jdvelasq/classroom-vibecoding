# Log — P511

## S01.P511.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Evidencia:** manifiesto, notebooks, entregables, pruebas y trazabilidad.
- **Decisión:** mapa creado; se confirmó integración many-to-one y preservación de grano.

## S02.P511.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P511_superstore_integracion/` (`data/*.csv`, `data/source_manifest.json`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/test_activity.py`); P500–P503 para relaciones.
- **Trazabilidad revisada:** P511 → `data.C01`–`data.C05`; C05 mínima.
- **Highlights:** añadidos H01 (claves contextuales porque `Order ID` no es clave; caso y datos), H02 (uniones `many_to_one` validadas y conservación del grano), H03 (agregación posterior a la integración con detalle y respuesta persistidos).
- **Preservado:** pregunta, cuatro fuentes, claves sustitutas, validación many-to-one, preservación del grano y doble entrega.
- **Corregido:** la descripción previa decía que la pregunta «se parece a P500»; P500 responde evolución mensual, la comparación pertinente es `category_sales` de P501.
- **Añadido:** conteos de filas por tabla; ejemplo de `Order ID` repetido; columnas `Customer ID_x/_y` en la salida; fechas como texto; utilidad negativa visible no interpretada; pruebas de sólo existencia; duplicación con P514.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** el generador de las tablas derivadas no está en la actividad; las claves contextuales impiden contar clientes o productos únicos.
- **Superficies / contrato / dependencias:** S01–S06; recibe caso de P500–P502; habilita datos y práctica para P512, P514, P515.
- **Auditoría de Analytics:** integración al servicio de una descripción trazable; sin riesgo de identidad relevante.

## S03.P511.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Integration (pp. 71–72: «schema mapping», «data mapping», «challenges brought by heterogeneous data sources») — ya cubierta: claves contextuales y validación de cardinalidad (H01, H02).

## S03.P511.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 (merge/join, transform) (p. 5) — ya cubierta por P511 H01–H03; P514/P515 repiten la técnica (duplicación ya registrada por S02).

## S03.P511.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.5.1 «merging/joining data across sources may require business rules» (p. 15) — ya cubierta por P511 H01 (claves contextuales) y H02.

## S03.P511.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - transformaciones y uniones necesarias (p. 15 «CAP-P.3.5.1 Identify the transformations and merge/joins that may be necessary to solve an analytics problem») — ya cubierta: P511 H01–H03.

## S03.P511.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - prohibición de unir dos tablas de hechos y *drill across*; claves foráneas nulas → fila por defecto (pp. 7, 20) — ya cubierta (P511 H02 valida cardinalidad) o marginal (no hay dos hechos en el curso); la falta de validación en P515 es un defecto ya registrado por S02, no una señal nueva de este documento.

## S03.P511.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco autorizado de la NASEM para la formación de pregrado en ciencia de datos. Define la «data acumen» y diez áreas conceptuales (entre ellas gestión y curaduría de datos, flujo de trabajo y reproducibilidad, ética) y pide que la ética atraviese todo el currículo. Respalda expectativas generales, no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «muchos candidatos presentan consultas SQL básicas, pero carecen de la comprensión de modelado de datos avanzado, … normalización vs. desnormalización» (p. 175); «construir modelos lógicos de datos» como pilar crítico para Data Analyst (p. 252). Categoría: ya cubierta. Normalización de multivalor con PK/FK (P503 H02, H04), tabla plana integrada (P511 H01–H03) y hecho–dimensiones que contrasta con la tabla plana (P512 H02) ya ejercen el contraste.
  - «Integración de fuentes» como habilidad del dominio «Data & features» (p. 96; p. 231: «Integración de fuentes (133)»); «integrar fuentes de datos y permitir políticas basadas en evidencia» (p. 291). Categoría: ya cubierta. Integración por claves contextuales con cardinalidad validada (P511 H01–H02) y conciliación del agregado con la fuente (P510 H03).

## S03.P511.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P511.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
