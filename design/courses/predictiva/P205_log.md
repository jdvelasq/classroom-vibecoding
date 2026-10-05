# Log — P205

## S01.P205.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se delimitó calibración/priorización como análisis predictivo, no política crediticia.

## S01.P205.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:**
  `implementation/predictiva/P205_priorizacion_con_probabilidades/` (notebook,
  entrada simulada, tres tablas y pruebas) y P205 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato actual de S01 y se añadieron highlights
  para calibración, consecuencias de umbral, frontera con política, revisión
  por grupo y persistencia; se incorporó la naturaleza simulada del dataset y
  los tamaños desiguales de sus dos grupos.
- **Auditoría de Analytics:** el producto es evidencia predictiva previa a una
  priorización; no define una política prescriptiva real.

## S01.P205.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05 y se documentaron superficies, contrato de
  evidencia y dependencia comprobada con P204; no se inventó una dependencia
  técnica con los talleres posteriores.

## S01.P205.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H05 con superficies existentes. Se preservó el límite entre evidencia predictiva simulada y política crediticia.
- **Auditoría de Analytics:** calibración y umbrales sirven a evidencia previa, no a una política prescriptiva real.

## S03.P205.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - falsos positivos/negativos y precision/recall (p. 9): ya cubierta (H02: conteos y costos por umbral).

## S03.P205.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - supervisión y criterio humano, tolerancia al riesgo, gobernanza (pp. 5–6): ya expresan el límite que H03 traza entre probabilidad/umbral y política, pero no cambian materialmente la capacidad de P205 para revisar probabilidades simuladas; tampoco justifican crear una política con datos ficticios. Se conserva la identidad Predictiva, no se convierte la actividad en Prescriptiva.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P205.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sesgos algorítmicos (p. 5): ya cubierta en la medida que el caso permite (H04: revisión por grupo simulado, sin inferir equidad).
  - supervisión humana, tolerancia al riesgo y gobernanza (pp. 5–6): ya cubierta como frontera entre umbral y política (H03).
  - gestión de riesgos como capacidad de IA (p. 2): ya cubierta (H02: consecuencias de umbrales con costos).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P205.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sensibilidad, especificidad y costo de errores (T1, p. 97): ya cubierta (H02).

## S03.P205.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - medidas de éxito ligadas a la decisión e identificación de riesgos (Tasks 2.4, 2.6, pp. 4–5): ya cubierta (H02–H03: costos de error y frontera con política).

## S03.P205.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sesgo más probable de un modelo predictivo y causa de resultados sesgados o no éticos (Tasks 2.6, 5.3, pp. 12, 20): ya cubierta en la medida que el caso lo permite (H04: revisión por grupo simulado).

## S03.P205.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - causa de resultados sesgados o no éticos de un modelo predictivo (CAP-P.5.3.5, p. 20): ya cubierta en la medida que el caso lo permite (H04).

## S03.P205.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - capacidad de detectar sesgo algorítmico (p. 52): ya cubierta en la medida que el caso lo permite (H04).

## S03.P205.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calibración de modelos» y «Analítica de riesgos» demandadas (Tabla 35, p. 97): ya cubierta (H01–H02).
  - Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.
