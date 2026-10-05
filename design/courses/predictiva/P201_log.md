# Log — P201

## S01.P201.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró incertidumbre y análisis de errores como aporte distinto de P200.

## S01.P201.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:**
  `implementation/predictiva/P201_clasificacion_basica_imagenes/` (notebook de
  profesor, `submission/metrics.json`, estimador y pruebas) y P201 en
  `implementation/predictiva/traceability.yaml`.
- **Corrección:** se sustituyó la ruta errónea del mapa anterior por
  `P201_clasificacion_basica_imagenes`.
- **Decisión:** se aplicó el contrato actual de S01 y se añadieron highlights
  para representación imagen–vector, estratificación multiclase, clasificación
  probabilística, matriz de confusión, inspección visual por caso y persistencia.
- **Límite:** `predict_proba` no equivale a probabilidades calibradas; la
  implementación no evalúa calibración ni define un contexto organizacional.
- **Auditoría de Analytics:** el producto permanece como clasificación y revisión
  de su evidencia; la regresión logística sirve ese producto y no organiza la
  actividad como una introducción general a ML.

## S01.P201.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se asignaron IDs H01–H06 y se añadieron superficies, contrato y
  dependencias para anclar futuras mejoras en representación, probabilidad o
  evaluación sin inventar cambios curriculares.

## S01.P201.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H06 con superficies observables. No se modificó la implementación ni se introdujeron mejoras.
- **Auditoría de Analytics:** la representación de imagen y la logística sirven a la predicción multiclase evaluada.

## S03.P201.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - deep learning, retropropagación y transfer learning para imágenes (p. 9): fuera de alcance; el folleto no aporta caso ni datos y exigiría una contribución propia no sustentada por este documento.
  - perceptrón y SVM (p. 9): marginal; otro clasificador para el mismo producto de P201.

## S03.P201.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje profundo y CNN para visión (p. 5): marginal; P201 ya permite hacer predicciones multiclase y revisar errores/probabilidades (H03–H05), y una arquitectura adicional con load_digits no cambia la pregunta ni el producto terminal.
  - interacción humano–IA, supervisión y responsabilidad de alto riesgo (p. 5): marginal para el clasificador educativo de dígitos, que no tiene usuario ni decisión organizacional; el texto no plantea un riesgo o contexto concreto que añadir a la revisión de incertidumbre existente.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P201.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - redes neuronales convolucionales y visión artificial (p. 5): fuera de alcance; enunciado sin caso, datos ni evaluación, y una CNN sobre `load_digits` no cambiaría el producto de H03–H05.
  - interacción humano–IA en contextos de alto riesgo (p. 5): no aplica; el caso educativo de dígitos no tiene usuario ni decisión.
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.
