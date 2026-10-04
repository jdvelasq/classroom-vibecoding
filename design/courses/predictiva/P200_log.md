# Log — P200

## S01.P200.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se mapearon preparación, regresión, comparación y artefactos persistentes.

## S01.P200.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P200_regresion_basica/`
  (notebook de profesor, datos, `submission/` y pruebas) y la entrada P200 de
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights que separan contribuciones observables:
  tipado y tratamiento de entradas, aislamiento entrenamiento/prueba,
  especificaciones lineales, MLP, comparación fuera de muestra y persistencia
  conjunta de transformadores y modelos. No se modificó la implementación ni
  se añadieron mejoras pendientes.

## S01.P200.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se precisaron dos highlights: `OneHotEncoder` como método para
  representar categorías nominales, y el contraste aislado entre regresión
  lineal y MLP usando sólo `Horsepower`. La comparación persistida sustenta MSE
  de prueba 22.03 y 15.60, respectivamente.

## S01.P200.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P200_regresion_basica/`
  (notebook de profesor, `submission/model_comparison.csv` y pruebas) y P200
  en `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato reescrito de S01: cada highlight quedó
  contrastado contra una ruta y con su límite de inferencia. Se confirmó la
  granularidad de semántica categórica, preprocesamiento sin filtración,
  especificaciones lineales, contraste de MLP de una entrada y persistencia.
- **Auditoría de Analytics:** el producto permanece como estimación verificable
  de MPG; preprocesamiento, regresión y MLP contribuyen a ese producto y no
  reorganizan la actividad como un curso introductorio de ML.
