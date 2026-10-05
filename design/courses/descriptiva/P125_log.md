# Log — P125

## S02.P125.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P125_salarios/` (`data/salarios.csv`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con cinco archivos, `tests/`); P103/P104, P108/P109 y P120–P124 como comparación.
- **Trazabilidad revisada:** P125 → `descriptiva.C01`–`C05`; coherente. Es la única evidencia persistida y probada de C04 en P120–P125.
- **Highlights añadidos:** H01–H07 (población sintética de mecanismo conocido, pares comparables, estadísticos robustos, señalamiento con doble criterio, decil superior, límite causal persistido, agregados sin divulgación). Highlight obligatorio de caso y datos: H01.
- **Cambios realizados:** creación de `P125_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** el notebook no declara que los datos son sintéticos; las áreas señaladas coinciden con los ajustes negativos del generador sin que el taller lo use para discutir C04; la mediana de pares incluye al individuo y no se reporta el tamaño de los grupos; umbrales −5 %, 50 % y P90 sin justificación; la respuesta «No» a la segunda pregunta demuestra posibilidad, no igualdad de acceso; `technical_high_salary` no se persiste; las alternativas de texto fijo rozan lo prescriptivo; la redacción de la primera pregunta difiere ligeramente entre `questions.json` y la celda del notebook; carpeta `.pytest_cache/` presente.
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S05 declaradas; dependencias demostrables de P103/P104 y P120–P122 (prácticas), conceptual con P108/P109; salida no evidenciada.
- **Auditoría de Analytics:** diagnóstico de brechas con frontera causal explícita; responde qué ocurre, dónde y con qué evidencia. Las disciplinas contribuyentes sirven al producto.

## S03.P125.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - tipos de medida nominal/ordinal/intervalo/razón (DM-Proximity, p. 76) — marginal: la elección de mediana y percentiles ya está justificada en P125 H03.

## S03.P125.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 5.6 «Document and communicate model findings, including assumptions, limitations, and constraints» (p. 6) — ya cubierta en su forma descriptiva: P125 H06; extenderlo a otros talleres no se sostiene con esta señal genérica.

## S03.P125.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - perfil univariado («data profiling outputs») y visualizaciones comunes con su propósito (CAP-E.3.6.2, 3.6.3, p. 15) — ya cubierta en la secuencia: histograma de P122 H02, mediana/percentiles y caja de P125 H03; la ausencia de distribución en P103 es marginal porque la secuencia la ejerce después.
  - interpretación correcta de la salida de un modelo descriptivo/diagnóstico (CAP-E.5.3.1, p. 20) — ya cubierta: P125 H06 (respuesta con límite).

## S03.P125.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - criterios de éxito y línea base del estado actual (p. 11: Task 2.4 «Define primary measures of success»; Task 2.5 «Identify baseline performance of the current state») — marginal: en descriptiva la «línea base» ya aparece como KPI global del período (P120 H04, P121 H03, P122 H02) y como referencia de pares (P125 H02); medidas de éxito de una solución pertenecen a predictiva/prescriptiva.
  - caso de negocio, costos, beneficios y consecuencias indirectas (p. 8: Task 1.5 «Create an initial business case») — fuera de alcance: la evaluación de costo-beneficio de una solución excede la pregunta descriptiva; P122 H04 ya pondera por valor expuesto.

## S03.P125.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - confusión y causalidad (p. 44) — ya cubierta (H06); la candidata P120 sólo adelanta el patrón.

## S03.P125.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «uso de datos anonimizados y agregados», cortes territoriales sólo «cuando hay masa crítica» y categoría NB «sólo descriptivamente» (p. 238); Privacy Engineer «PII» (p. 335); protección de datos personales (pp. 183, 203) — ya cubierta: minimización y anonimización con riesgo medido (P102 H02, P108 H01–H05), persistir sólo agregados con tamaño mínimo (P125 H04, H07).
  - mediana como «indicador más robusto», percentiles P25/P50/P75/P90 y bandas (p. 263) — ya cubierta: P125 H03 y H05.
  - bandas «puntuales» (BI 6,8–6,8 M) leídas como «perfiles bien tipificados» (pp. 290, 310) con sólo 42 observaciones en 6 cargos (p. 302) — marginal: contraejemplo útil de interpretar dispersión nula sin mirar tamaño de celda, pero P125 H04 ya exige tamaño mínimo antes de señalar; no aporta caso/datos reutilizables (microdatos no disponibles).

## S03.P125.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P125.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Implementación responsable de la IA: tolerancia al riesgo, supervisión y gobernanza» (p. 5) — fuera de alcance: gobernanza organizacional de IA; la dimensión responsable de datos ya está en P108 H01–H06 y P125 H07.

## S03.P125.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de pregrado de 4 unidades, con prerrequisitos de programación y de un curso de ciencia de datos (DATA C100 o equivalente), sobre gestión de datos a escala para análisis y machine learning a lo largo de todo el ciclo de vida, con foco en operacionalización confiable y escalable. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P125.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - inferencia causal (p. 1: «causal inference») — ya cubierta en lo que toca a descriptiva: P125 H06 persiste y verifica el límite «no identifica su causa / no prueba que … cause». La estimación causal en sí queda fuera de alcance.

## S03.P125.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Estadísticas descriptivas», «Distribuciones normales y no normales» (p. 7) — ya cubierta: histograma con referencia en cero (P122 H02), mediana/percentiles y caja (P125 H03).

## S03.P125.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P125.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Ethics – AI Bias and Fairness» (p. 15) — fuera de alcance: sesgo de modelos de IA (predictiva); la dimensión de no divulgación individual ya está en P108 y P125 H07.

## S03.P125.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - casos «Predicting Wages» y «Gender Wage Gap» con regresión para inferencia causal (p. 8) — fuera de alcance: P125 compara contra pares por construcción (H02) y declara explícitamente que la brecha no identifica causa (H06); la regresión causal pertenece a otro curso y contradiría ese límite.

## S03.P125.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P125.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P125.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P125.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado de 6 meses en ingeniería de datos: Python/pandas, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, NiFi, Kafka, DASK, seguridad web, ML y aprendizaje por refuerzo; portafolio GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
