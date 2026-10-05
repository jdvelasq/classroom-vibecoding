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
