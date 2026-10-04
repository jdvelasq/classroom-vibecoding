# Log — P204

## S01.P204.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registraron ingeniería de variables, AUC y límite clínico como aportes propios.

## S01.P204.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P204_clasificacion_basica_numerica/`
  (notebook de profesor, modelos, métricas, comparación y pruebas) y P204 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights para el límite educativo, logística
  binaria, términos flexibles, tensión AUC–exactitud y persistencia de las dos
  especificaciones.
- **Límite:** se mantuvo explícita la prohibición de leer el ejercicio como
  diagnóstico clínico o como evaluación de calibración y equidad.

## S01.P204.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió la particularidad del dataset —212 casos M, 357 B y
  muchas mediciones— para justificar la selección didáctica de dos entradas y
  reforzar el límite de no diagnóstico.

## S01.P204.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05 y las superficies, contrato y dependencias
  que anclan cualquier mejora futura sin alterar el límite clínico educativo.

## S01.P204.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió índice externo y vínculo H01–H05 con superficies actuales; se mantuvo el límite de no diagnóstico y no se alteró implementación.
- **Auditoría de Analytics:** clasificación y evaluación sirven a una estimación binaria pedagógicamente limitada.

## S03.P204.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios; aporta a N01 (árboles y ensambles).
- **Señales descartadas relevantes:**
  - regresión logística y probit; caso Challenger (p. 9): marginal; variación de caso con el mismo método de H02.
  - pruebas de hipótesis Neyman–Pearson y p-values (p. 9): fuera de alcance; estadística inferencial, no producto predictivo.

## S03.P204.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - entrenamiento/validación/prueba y calidad/representatividad de datos (p. 5): ya cubiertos por la comparación binaria evaluada (H01–H05); no corrige defecto demostrado ni añade contraste sustantivo al caso.
  - supervisión y responsabilidad en contextos de alto riesgo (p. 5): marginal en esta actividad; H01 delimita expresamente el ejercicio como no diagnóstico y el benchmark no da un contexto clínico, usuario ni evidencia autorizada para convertir ese guardrail en una capacidad nueva.
