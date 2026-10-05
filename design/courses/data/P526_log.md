# Log — P526

## S02.P526.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P526_eventos/` (`data/events.csv.gz` como binario, `professor/main.py`, `src/main.py`, `submission/event_replay.csv`, `submission/session_conversion.csv`, `submission/event_summary.csv`, `tests/test_activity.py`); P519–P522 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P526 → `data.C01`–`data.C05`; coherente.
- **Highlights:** añadidos H01 (tiempo de evento vs. llegada; caso y datos), H02 (desorden simulado determinista), H03 (conversión e ingreso por sesión).
- **Ambigüedades:** tardanza construida (28 = 14 bloques × 2); métricas por sesión invariantes al orden, por lo que no se muestra la confusión que la pregunta menciona; tasa 0.5 sobre 16 sesiones sin criterio de muestra; `revenue > 0` como conversión; identificadores de usuario copiados a `submission/` sin restricción documentada; procedencia sólo en `case-selection.md`; sin notebook de profesor.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P519–P520 y P522; habilita: no evidenciada.
- **Auditoría de Analytics:** producto analítico claro (métrica de conversión); procesamiento de eventos como habilitador; la amenaza analítica no se demuestra.

## S03.P526.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - PDA-Numerical Computing (p. 119: «Allow reproducibility in data analysis with non-deterministic algorithms») — ya cubierta: simulación determinista y declarada (H02). DM-Time Series Data (p. 80, E) — fuera de alcance.

## S03.P526.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P526.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P526.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - derivar necesidades de datos de la pregunta (p. 13 «CAP-P.3.1.1 Identify an appropriate sequencing and prioritization of data needed, including sources»; p. 10 «CAP-P.2.2.1 Identify why analytics element(s) would be classified as an input, output, both, or neither») — ya cubierta: P500 H02, P503 (entidades desde la pregunta), P506 H02, P517 H02 (contrato mínimo derivado de la pregunta).

## S03.P526.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - hechos y dimensiones de llegada tardía (pp. 20, 23) — ya cubierta/marginal: P526 H01 separa tiempo de evento y orden de llegada; la búsqueda de claves vigentes de Kimball presupone SCD tipo 2, fuera de alcance.

## S03.P526.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - `user_id` y `user_session` copiados a `submission/` desde una muestra privada (privacidad, p. 45) — marginal como señal de este documento: `user_session` es la llave del grano y la restricción de uso es un requisito de cumplimiento de `AGENTS.md`. Se escala como higiene junto con la candidata P519, sin proponer un cambio de aprendizaje.

## S03.P526.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - «muestra voluntaria (no probabilística)» como limitación declarada (p. 238). Categoría: marginal. La falta de criterio de muestra (P526 S01) y de pertinencia del corpus (auditoría P503) ya está registrada por S02; aquí sólo se recoge dentro de la candidata de P526.

## S03.P526.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P526.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P526.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de 4 unidades, cruzado con COMPSCI C187, que cubre la gestión de datos a escala a lo largo del ciclo de vida, con requisitos previos de programación (CS 61B o equivalente) y de un curso de ciencia de datos de nivel superior (DATA C100 o equivalente); no detalla temario, datos, herramientas ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P526.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P526.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «RGPD (Reglamento General de Protección de Datos)», «Privacidad y anonimización» (p. 8); caso TalkTalk sobre protección de datos de clientes (p. 11) — marginal: S02 ya registra `ssn` en `drivers.csv` (P519, P521) y `user_id`/`user_session` copiados en `event_replay.csv` (P526) como defectos de distribución/sensibilidad; P521 ya proyecta sólo `name` del maestro. La corrección (retirar o seudonimizar identificadores, documentar restricciones) es higiene de datos que no requiere este benchmark, y un bullet de temario ejecutivo no basta para crear un contenido de privacidad propio.
