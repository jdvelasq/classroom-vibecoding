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
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - entrenamiento/validación/prueba (p. 5): ya cubierto por la comparación binaria sobre partición estratificada (H04).
  - calidad de datos, representatividad y por qué fallan los modelos (p. 5): no cubierta como capacidad en esta actividad ni en el curso (ningún taller trata representatividad o cambio de distribución entre entrenamiento y uso); no sustentada como propuesta por este documento, que sólo la enuncia en un programa ejecutivo. Señal a contrastar con fuentes *authoritative*.
  - supervisión y responsabilidad en contextos de alto riesgo (p. 5): marginal en esta actividad; H01 delimita expresamente el ejercicio como no diagnóstico y el benchmark no da un contexto clínico, usuario ni evidencia autorizada para convertir ese guardrail en una capacidad nueva.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; se separó «calidad/representatividad», que la entrada daba por cubierta sin que ningún highlight la trate.

## S03.P204.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje supervisado; entrenamiento, validación y prueba (p. 5): ya cubierta (H04: comparación sobre partición estratificada reservada).
  - calidad de datos, representatividad y «por qué fallan los modelos» (p. 5): no cubierta; ningún taller del curso trata representatividad ni cambio de distribución entre entrenamiento y uso. No sustentada como propuesta por este documento (un enunciado en un programa ejecutivo sin método ni caso); señal a contrastar con fuentes *authoritative*.
  - supervisión, criterio y responsabilidad humana en contextos de alto riesgo (p. 5): ya cubierta como límite de uso (H01: probabilidad educativa, no diagnóstico).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P204.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01 (bootstrap pareado de la diferencia entre especificaciones); aporta a N01.
- **Señales descartadas relevantes:**
  - no linealidad en clasificación (T1, pp. 97–98): ningún clasificador del curso es no lineal; se registra en N01.
  - representatividad de los datos («truly representative», PR p. 108; BDS p. 58): fuente *authoritative* que confirma la señal ya registrada; sigue sin una competencia técnica concreta (método, evaluación) que permita anclarla a un taller.

## S03.P204.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - riesgos y sesgo no intencional en el encuadre (Task 2.6, p. 5): ya cubierta como límite de uso no diagnóstico (H01).

## S03.P204.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel inicial detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P204.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel intermedio detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.
