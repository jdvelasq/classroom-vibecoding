# Log — P203

## S01.P203.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se confirmó que P203 reutiliza preparación textual pero agrega evaluación multiclase y persistencia.

## S01.P203.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P203_clasificacion_basica_texto/`
  (notebook de profesor, métricas, modelo, vectorizador y pruebas) y P203 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato actual de S01: se documentaron highlights
  para vectorizador ajustado en entrenamiento, clasificación textual multiclase,
  evaluación sensible a clases y revisión persistida por frase.
- **Límite:** las probabilidades no se calibran y las señales textuales no
  constituyen una decisión financiera.

## S01.P203.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se precisó el highlight de evaluación con la distribución real
  de etiquetas (1,391 neutrales, 570 positivas y 303 negativas), para vincular
  el desbalance del dataset con exactitud balanceada y F1 macro.

## S01.P203.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05, superficies de caso/vectorización/evaluación,
  contrato de evidencia y dependencias demostrables con P202 y P220.

## S01.P203.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H05 con superficies existentes, sin modificar implementación ni aceptar cambios.
- **Auditoría de Analytics:** vectorización y logística sirven a predicción textual multiclase evaluada.

## S03.P203.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - precision/recall y F1 en clasificación binaria (p. 9): ya cubierta (H04 usa F1 macro y exactitud balanceada).
  - detección de spam (p. 9): marginal; otro caso de clasificación de texto con el mismo método.

## S03.P203.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje supervisado y entrenamiento/validación/prueba (p. 5): ya cubiertos por H01–H04, incluyendo vocabulario aprendido sólo en entrenamiento y métricas sensibles al desbalance; no cambia materialmente el producto de estimación de sentimiento.
  - sesgo algorítmico (p. 5): marginal para el caso de sentimiento de frases sin decisión financiera; el benchmark no identifica sesgo concreto ni proporciona grupos/etiquetas para una evaluación adicional rigurosa.
  - NLP generativo (pp. 5–6): fuera de alcance de la pregunta clasificatoria actual; no se aporta caso/dataset ni criterio de evaluación para justificar desplazar la clasificación de sentimiento.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P203.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje supervisado; entrenamiento, validación y prueba (p. 5): ya cubierta (H01, H03: vocabulario aprendido sólo en entrenamiento y partición estratificada).
  - sesgos algorítmicos (p. 5): no sustentada para este caso; el documento no define grupos ni criterio, y las frases no tienen atributos de grupo.
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P203.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - métricas macro y micro, precision/recall/F1 (T1–T2, pp. 97–98): ya cubierta (H04).
  - Naive Bayes como clasificador probabilístico (DM-Classification, T1): marginal; otro algoritmo para el mismo producto de H02.

## S03.P203.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - encuadre del problema de negocio, *stakeholders* y medida de éxito (Domain I–II, pp. 4–5): S02 registra que esta actividad no tiene usuario ni decisión evidenciados; el hábito se propone en P200 (T01) y extenderlo aquí sería una propuesta por actividad, a decidir después de discutir P200 T01.

## S03.P203.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel inicial detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P203.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel intermedio detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.
