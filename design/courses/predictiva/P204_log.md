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

## S03.P204.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - variabilidad, incertidumbre y error de muestreo (p. 44): se añade como fuente de T01.

## S03.P204.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - la demanda laboral (Tabla 35, p. 97) no lista una habilidad específica de esta actividad distinta de las ya cubiertas. Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.

## S03.P204.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un proyecto de inversión pública de bootcamps (159 horas) en ejes temáticos genéricos (análisis de datos, IA, programación, nube, blockchain; pp. 1–3); no contiene contenidos, prácticas ni competencias que contrastar con esta actividad.

## S03.P204.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo de un curso de ingeniería de datos (p. 1): ciclo de vida de gestión de datos a escala; sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P204.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** refuerza T01; aporta a N01.
- **Señales descartadas relevantes:**
  - pruebas de permutación e intervalos de confianza (p. 1): se añade como fuente de T01.

## S03.P204.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - máquinas de soporte vectorial (p. 8): marginal; otro clasificador para el mismo producto.

## S03.P204.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de computación en la nube y DevOps (temario, pp. 12–14: web, Node.js, contenedores, PKI, métricas DevOps, casos de migración); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P204.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso ejecutivo de liderazgo de datos (temario, pp. 13–14: IA para líderes, marcos de innovación, SQL y arquitectura, plataformas de datos, nube, ética y gobierno); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P204.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de diseño de productos de IA (módulos, pp. 4–5: proceso de diseño, panorama de algoritmos de ML y deep learning, interacción humano–máquina, organizaciones «superminds», GANs); no detalla prácticas de modelado o evaluación que contrastar con esta actividad.

## S03.P204.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de estrategia de plataformas digitales y mercados de dos lados (temario, pp. 13–15: efectos de red, precios, arquitectura, gobierno de calidad); sin contenidos de modelado predictivo.

## S03.P204.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de modelado y simulación (ODE, PDE, optimización); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P204.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado de ingeniería de datos (módulos, pp. 10–11: Python, SQL, contenedores, CDC, almacenes de datos, procesamiento distribuido); para esta actividad no añade señales.

## S03.P204.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - clasificación con árboles (módulo 14, p. 8): se registra en N01.

## S03.P204.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de ingeniería de sistemas orientada al valor (semanas 1–4: modelos de valor, generación y evaluación de alternativas, exploración de *tradespace* bajo incertidumbre); es contenido de decisión multicriterio, propio de Prescriptiva; sin señales para esta actividad.
