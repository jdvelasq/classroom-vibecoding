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

## S03.P221.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - razones y métodos para reducir *features* (T2, p. 98): ya cubierta (H01–H02).
  - representatividad de los datos («truly representative», PR p. 108; BDS p. 58): fuente *authoritative* que confirma la señal ya registrada; sigue sin una competencia técnica concreta (método, evaluación) que permita anclarla a un taller.

## S03.P221.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - impulsores (*drivers*) del resultado y su relación con la salida (Task 2.2, p. 5): ya cubierta (H01–H02: selección integrada).
