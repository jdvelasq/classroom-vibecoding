# Log — P212

## S01.P212.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró Kaplan–Meier por contrato, incluida la censura, como
  producto predictivo de tiempo hasta abandono y no como política de retención.

## S01.P212.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies, contrato y límites de uso; no se modificó implementación.

## S03.P212.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el folleto no trata tiempo hasta evento; sin señales relevantes.

## S03.P212.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización y gestión de riesgos (p. 2): marginal; P212 ya estima permanencia por contrato (H02–H03), pero trasladarlo a una oferta personalizada requeriría datos de intervención/resultado y una pregunta causal que el benchmark no suministra; la propuesta no altera ese límite.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P212.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización y gestión de riesgos (p. 2): fuera de alcance; elegir una oferta de retención está fuera del producto (H04).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P212.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sin competencias específicas de tiempo hasta evento.

## S03.P212.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - frontera entre producto analítico y decisión (Domain II): ya cubierta (H04).

## S03.P212.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel inicial detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P212.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel intermedio detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P212.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el informe define áreas de conocimiento a nivel de programa (fundamentos, datos, modelado, flujo de trabajo, comunicación, ética); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P212.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - la demanda laboral (Tabla 35, p. 97) no lista una habilidad específica de esta actividad distinta de las ya cubiertas. Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.

## S03.P212.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un proyecto de inversión pública de bootcamps (159 horas) en ejes temáticos genéricos (análisis de datos, IA, programación, nube, blockchain; pp. 1–3); no contiene contenidos, prácticas ni competencias que contrastar con esta actividad.

## S03.P212.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo de un curso de ingeniería de datos (p. 1): ciclo de vida de gestión de datos a escala; sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P212.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo (p. 1) con temas de inferencia y decisión; para esta actividad no añade una señal distinta de las ya registradas.
