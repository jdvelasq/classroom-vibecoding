# Log — P213

## S01.P213.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se distinguió explícitamente la matriz de Markov predictiva de
  una política prescriptiva de contacto o retención.

## S01.P213.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies, contrato y límites de uso; no se modificó implementación.

## S03.P213.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Hidden Markov Models (p. 10–11): marginal; extiende la cadena de Markov de H03 con estados ocultos sin una capacidad predictiva distinguible para este caso.

## S03.P213.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización del cliente y toma de decisiones con IA (pp. 2, 5): fuera de alcance para la pregunta de transición de estado siguiente; pasar de estimar estado a elegir contacto/retención sería otra contribución, sin evidencia de intervención ni regla de decisión en P213.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.
