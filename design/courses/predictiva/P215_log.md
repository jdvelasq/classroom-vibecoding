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
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** propone T01; el contexto de personalización del folleto refuerza el encuadre, sin cambiar su contenido ni añadir nueva capacidad a lo ya propuesto.
- **Señales descartadas relevantes:**
  - personalización de experiencia del cliente (p. 2): aporta contexto, no una propuesta separada; la brecha material de P215 sigue siendo que aún no permite juzgar si sus recomendaciones superan una referencia en calificaciones no vistas (H03–H04, S03), que ya atiende T01.
  - IA generativa y agentes (p. 6): fuera de alcance; P215 predice calificación con preferencias colaborativas y no hay tarea, datos ni criterio de evaluación del folleto para sustituir o añadir otro producto.
