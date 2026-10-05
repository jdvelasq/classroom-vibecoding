# Log — P210

## S01.P210.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró pronóstico de adopción como producto temporal con fuente explícita.

## S01.P210.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies, contrato y límites del caso temporal; no se modificó implementación.

## S03.P210.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el folleto no trata pronóstico temporal; sin señales relevantes.

## S03.P210.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - simulaciones para predicción (pp. 1, 4): ya cubierta por pronóstico Bass frente a persistencia y evaluación de seis meses (H02–H03); no se aporta nueva comparación o forma de incertidumbre.
  - estrategia/creación de valor de IA (p. 5): fuera de alcance para el pronóstico de matrículas EV; integrarla requeriría otra pregunta analítica y caso organizacional distinto, no una mejora local al producto predictivo terminal.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.
