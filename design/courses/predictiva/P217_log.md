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

## S03.P217.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - supervisión humana, privacidad y gobernanza (pp. 5–6): no sustentada; el documento no fija requisito de servicio, y H03 ya delimita monitoreo y procedencia como fuera del taller.
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P217.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - transición de un modelo a producción (T2, p. 97): ya cubierta parcialmente (H01–H03); el documento no fija prácticas que añadir.

## S03.P217.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - requisitos de una solución desplegada (Task 6.4, p. 7): ya cubierta parcialmente (H01: contrato de entrada).
  - seguimiento del desempeño, recalibración y efectos secundarios en el tiempo (Domain VII, p. 7): no cubierta; según `AGENTS.md`, hacer observable y mantenible una capacidad analítica es propio de la línea de productos de datos, por lo que no se propone en Predictiva.

## S03.P217.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel inicial detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.
