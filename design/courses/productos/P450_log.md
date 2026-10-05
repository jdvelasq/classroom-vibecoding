# Log — P450

## S02.P450.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P450_human_review/` (`data/recommendation.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/review.json`, `tests/test_activity.py`); `P425_api_contract/professor/main.py`, `P430_idempotency/professor/main.py`, `P432_duckdb_transformation/data/daily_operations.csv`.
- **Trazabilidad revisada:** P450 → `productos.C04`, `productos.C05`.
- **Highlights:** añadidos H01 (recomendación accionable, caso y datos), H02 (autorización explícita).
- **Ambigüedades:** el riesgo `high` de la fábrica 2 (P430, P450–P452) no se deriva de la regla de P425 aplicada al insumo del curso, que daría `low`; revisor, fecha y motivo no se registran.
- **Superficies / contrato / dependencias:** S01–S05; contenido repetido de P430 sin dependencia de artefacto.
- **Auditoría de Analytics:** resuelta con límite; revisión humana sobre un indicador cuyo origen no se evidencia.

## S03.P450.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P450.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Tasks 6.3 y 1.6 sobre «sponsor agreement and stakeholder alignment» (p. 4, 7) — ya cubierta: la autorización humana explícita es P450 H02. La aprobación de un patrocinador como ritual organizacional queda fuera de alcance.

## S03.P450.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify a potential ethical analytics risk» (p. 22, CAP-E.6.1.2) — marginal: reconocimiento genérico; la salvaguarda operativa ya está en la revisión humana (P450 H01–H02).

## S03.P450.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Tasks 6.1–6.3 validación de negocio, «business validation report» y acuerdo del patrocinador antes de desplegar (pp. 22–23) — fuera de alcance en su núcleo (juzgar si la solución resuelve el problema de negocio es responsabilidad del curso de origen: Predictiva/Prescriptiva); la parte operable ya está en la compuerta técnica (P403 H02) y la autorización humana explícita (P450 H02).

## S03.P450.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P450.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Marco de pregrado que define la «data acumen» (diez áreas conceptuales) y recomienda que la ética y la reproducibilidad atraviesen el currículo; trata el flujo de trabajo y la gestión de datos como competencias generales, no la operación de productos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P450.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Estudio de política pública que cuantifica la brecha de talento TI en Colombia y la pertinencia de la oferta educativa. Para Productos de datos su valor es de pertinencia laboral: escasez de perfiles DevOps/SRE/MLOps y una brecha formativa en prácticas de producción (CI/CD real, rollback, secretos, monitoreo de deriva, seguridad). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P450.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P450.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Interacción humano - IA: supervisión, criterio y responsabilidad en contextos de alto riesgo» (p. 5) — ya cubierta: P450 separa recomendación y acción autorizada y autoriza sólo ante aprobación explícita (H01, H02); el folleto no aporta práctica concreta.

## S03.P450.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de 4 unidades (cruzado con COMPSCI C187) sobre gestión de datos a escala para análisis y ML, con énfasis en una operacionalización confiable. Sólo incluye la descripción, los prerrequisitos y datos administrativos; no trae temario, prácticas ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P450.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «modeling and decision-making life cycle… including its human, social, and ethical implications» (p. 1). Categoría: **ya cubierta**. El curso trata la revisión humana (P450 H01–H02) y la retroalimentación del consumidor (P451 H01–H02). La ficha no aporta un mecanismo operativo concreto que cambie lo que el estudiante hace.
