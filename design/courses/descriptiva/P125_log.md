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
