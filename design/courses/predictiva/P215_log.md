# Log — P215

## S01.P215.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se documentó el cambio de asociación Apriori a vecinos de
  usuarios y se registró como pendiente la ausencia de trazabilidad formal.

## S01.P215.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `Codex`; **estado:** incremental.
- **Decisión:** se añadieron producto, highlights, anclas, superficies y contrato de evidencia; se dejó visible que faltantes no son malas calificaciones y que no hay evaluación retenida de ranking.
- **Trazabilidad:** continúa ausente la entrada P215; no se infirieron capacidades aprobadas.

## S03.P215.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** propone T01 (contraste con línea base en calificaciones retenidas).
- **Señales descartadas relevantes:**
  - filtrado colaborativo ítem–ítem (p. 10): marginal; variante del mismo método.
  - side-information, active learning y retos de sistema (p. 10): fuera de alcance; sin caso ni datos que los sustenten.

## S03.P215.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización de experiencia del cliente (p. 2): aporta contexto, no una propuesta separada; la brecha material de P215 sigue siendo que aún no permite juzgar si sus recomendaciones superan una referencia en calificaciones no vistas (H03–H04, S03), que ya atiende T01.
  - IA generativa y agentes (p. 6): fuera de alcance; P215 predice calificación con preferencias colaborativas y no hay tarea, datos ni criterio de evaluación del folleto para sustituir o añadir otro producto.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; el resultado era «propone T01», pero T01 la propuso la revisión del documento de MIT y este documento no le aporta evidencia; se revirtió además la edición de OpenWork en `P215_tasks.md` (fuente de Berkeley y campo «Interacciones»).

## S03.P215.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización de la experiencia del cliente (p. 2): contexto genérico de recomendación; no aporta evidencia a T01 (propuesta por la revisión del documento de MIT), por lo que no se añade a sus fuentes.
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P215.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - filtrado colaborativo (T2, p. 101): ya cubierta (H02–H03).
  - evaluación contra línea base y separación entrenamiento/prueba en recomendadores (pp. 96, 101): se añade como fuente de T01.

## S03.P215.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - línea base del estado actual (Task 2.5, p. 5): se añade como fuente de T01.

## S03.P215.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - línea base del estado actual (Task 2.5, p. 11): se añade como fuente de T01.

## S03.P215.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - línea base del estado actual (CAP-P.2.5.1, p. 11): se añade como fuente de T01.

## S03.P215.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el informe define áreas de conocimiento a nivel de programa (fundamentos, datos, modelado, flujo de trabajo, comunicación, ética); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P215.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Modelos recomendación» demandados (Tabla 35, p. 97): ya cubierta; no aporta evidencia a T01.
  - Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.

## S03.P215.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un proyecto de inversión pública de bootcamps (159 horas) en ejes temáticos genéricos (análisis de datos, IA, programación, nube, blockchain; pp. 1–3); no contiene contenidos, prácticas ni competencias que contrastar con esta actividad.

## S03.P215.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo de un curso de ingeniería de datos (p. 1): ciclo de vida de gestión de datos a escala; sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P215.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sistemas de recomendación (p. 1): ya cubierta; no aporta evidencia a T01.
