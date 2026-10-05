# Log — P217

## S01.P217.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se identificó como producto de datos orientado a uso, no como
  una nueva actividad de entrenamiento; se registró la trazabilidad ausente.

## S01.P217.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `Codex`; **estado:** incremental.
- **Decisión:** se añadieron producto, highlights, anclas, superficies y contrato de evidencia; se registró que la prueba sólo exige código no vacío.
- **Trazabilidad:** continúa ausente la entrada P217.

## S03.P217.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el folleto no trata despliegue; sin señales relevantes.

## S03.P217.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - interacción humano–IA, supervisión y responsabilidad (p. 5): ya parcialmente cubierta por la entrega a una persona y manejo de errores (H01–H03), pero el folleto no concreta qué persona decide ni cuál es el uso autorizado del precio; no permite completar esos vacíos con rigor ni añade una mejora ejecutable al contrato de interfaz existente.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.
