# Log — P216

## S01.P216.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se documentó la secuencia de nueve notebooks como una comparación
  explícita de familias temporales y se registró la ausencia de trazabilidad P216.

## S01.P216.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadieron hitos de aprendizaje para hacer auditable la
  progresión desde inspección temporal hasta evaluación fuera del período de
  especificación; no se añadieron técnicas ni cambios a la implementación.

## S01.P216.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se sustituyeron los hitos generales por los once aspectos
  verificables de la secuencia implementada, incluida la importación de
  funciones, ACF/PACF, escalamiento, reconstrucción de diferencias, *stacking*,
  combinación y persistencia acumulativa de pronósticos y métricas.

## S01.P216.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H13, incluyendo la particularidad temporal del
  dataset, y se añadieron superficies de cambio, contrato de evidencia y
  dependencias comprobadas/no comprobadas para análisis posterior de benchmarks.

## S01.P216.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se declaró producto, índice externo y vínculo H01–H13 con superficies actuales. Se preservaron la implementación y la ausencia de trazabilidad P216.
- **Auditoría de Analytics:** regresión, MLP y análisis temporal sirven a pronósticos comparables; no justifican asignación operativa de mano de obra.

## S03.P216.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el folleto no trata series de tiempo; sin señales relevantes.

## S03.P216.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - entrenamiento/validación/prueba y simulaciones para predicción (pp. 4–5): ya cubiertas por evaluación cronológica de 24 meses (H01, H13) y comparación de familias (H04–H11); no aporta señal material para el pronóstico de mano de obra de Sutter.
  - estrategia empresarial y transformación organizacional (pp. 5–6): fuera de alcance de la pregunta sobre pronóstico mensual; convertirla en plan de asignación de personal sería otra contribución, sin organización usuaria, objetivo o restricciones evidenciadas.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P216.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - redes neuronales recurrentes (RNNs) (p. 5): marginal; enunciado sin detalle, y P216 ya contrasta MLP sobre rezagos con familias clásicas (H06–H11).
  - aprendizaje supervisado; entrenamiento, validación y prueba (p. 5): ya cubierta (H01, H13: evaluación cronológica de 24 meses).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P216.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - series de tiempo: estacionariedad, transformación y pronóstico (DM-Time Series, electiva): ya cubierta (H03, H08, H13).
  - RNN y LSTM (ML-Deep Learning, T2): marginal; no son competencia núcleo y P216 ya contrasta MLP con familias clásicas.

## S03.P216.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - integración de varios modelos (Task 5.5, p. 6): ya cubierta (H09, H11: apilamiento y combinación).

## S03.P216.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel inicial detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.
