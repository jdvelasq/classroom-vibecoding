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
