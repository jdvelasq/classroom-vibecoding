# Log — P221

## S01.P221.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se clasificó como extensión técnica de P200, no como repetición:
  añade selección de variables dentro de la evaluación reproducible.

## S01.P221.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies y ausencia de trazabilidad; no se modificó implementación.

## S03.P221.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - predicción con datos de alta dimensión y validación cruzada (p. 8): ya cubierta (H01–H02).

## S03.P221.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad de datos, representatividad y por qué fallan los modelos (p. 5): no cubierta como capacidad en esta actividad ni en el curso (ningún taller trata representatividad o cambio de distribución entre entrenamiento y uso); no sustentada como propuesta por este documento, que sólo la enuncia en un programa ejecutivo. Señal a contrastar con fuentes *authoritative*.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; la selección integrada (H01–H02) no trata representatividad; se reformuló como señal no cubierta y no sustentada.

## S03.P221.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje supervisado; entrenamiento, validación y prueba (p. 5): ya cubierta (H02: búsqueda de k por validación cruzada).
  - calidad de datos, representatividad y «por qué fallan los modelos» (p. 5): no cubierta; ningún taller del curso trata representatividad ni cambio de distribución entre entrenamiento y uso. No sustentada como propuesta por este documento (un enunciado en un programa ejecutivo sin método ni caso); señal a contrastar con fuentes *authoritative*.
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.
