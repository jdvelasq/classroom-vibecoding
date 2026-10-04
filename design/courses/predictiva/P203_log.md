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
