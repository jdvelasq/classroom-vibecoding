# Log — P121

## S02.P121.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P121_vuelos/` (dos agregados `.csv.gz` en `data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con `questions.json` y seis CSV, `tests/`); P120 como comparación inmediata.
- **Trazabilidad revisada:** P121 → `descriptiva.C01`, `C02`, `C03`; coherente con la evidencia.
- **Highlights añadidos:** H01–H07 (agregados aditivos, conciliación, denominadores, matriz día × hora, segmentos con umbral, serie vs estacionalidad, persistencia verificada). Highlight obligatorio de caso y datos: H01, reforzado por H04 (orientación filas = día, columnas = hora).
- **Cambios realizados:** creación de `P121_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** origen, período completo y transformación de los agregados no documentados (el notebook sólo los llama «reales»); la vista estacional agrupa tres años; el umbral de 25.000 vuelos no tiene justificación persistida; las pruebas no verifican `questions.json`; posible duplicación de secuencia con P120 y P122 (matriz + top N con umbral).
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; dependencia demostrable de P120; salida hacia actividades posteriores no evidenciada como artefacto.
- **Auditoría de Analytics:** diagnóstico descriptivo de concentración de demoras; disciplinas al servicio del producto. Sin declaración explícita de límite causal pese a la pregunta de «reducir».

## S03.P121.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - series de tiempo (estacionariedad, motivos, pronóstico; DM-Time Series, E, p. 80) — el pronóstico está fuera de alcance (predictiva). «Measuring growth over time» ya está cubierta por P121 H06 y por las series de P120/P122/P150.
  - *scores* y *rankings* con características deseables (DM-Proximity, p. 75) — ya cubierta: umbrales de volumen y separación entre riesgo y prioridad (P120 H06–H07, P121 H05, P122 H04/H06).

## S03.P121.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta: P120 H02, P121 H02, P122 H01, H05.

## S03.P121.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - brechas de calidad «accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y métodos para evaluarla (CAP-E.3.6.1, 3.6.4, p. 15) — ya cubierta: P120 H02, P121 H02, P122 H01 y H05.

## S03.P121.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - criterios de éxito y línea base del estado actual (p. 11: Task 2.4 «Define primary measures of success»; Task 2.5 «Identify baseline performance of the current state») — marginal: en descriptiva la «línea base» ya aparece como KPI global del período (P120 H04, P121 H03, P122 H02) y como referencia de pares (P125 H02); medidas de éxito de una solución pertenecen a predictiva/prescriptiva.
  - caso de negocio, costos, beneficios y consecuencias indirectas (p. 8: Task 1.5 «Create an initial business case») — fuera de alcance: la evaluación de costo-beneficio de una solución excede la pregunta descriptiva; P122 H04 ya pondera por valor expuesto.

## S03.P121.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Variability, uncertainty, sampling error, and inference» (p. 44) frente a tasas sin intervalos — marginal: el umbral de volumen (P120 H06, P121 H05, P122 H06) ya cumple la función descriptiva; intervalos desplazarían hacia Estadística.
  - «the pitfalls of misrepresenting data and results» (p. 38) frente a la matriz día × hora sin volumen por celda (H04) — marginal: variante de P120 H05 (magnitud y tasa en un mismo gráfico).
  - «Data consistency checking» (p. 46), «document data quality problems» (p. 37) — ya cubierta (P121 H02 conciliación; P122 H05 cobertura; P153 H03).

## S03.P121.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - rotación «promedio simple ≈ 27,5 %» frente a «ponderada por número de empleados ≈ 29,8 %» (p. 307) — ya cubierta: razón de sumas vs promedio de razones (P121 H03, P153 H02); ejemplo equivalente, no cambia lo que el estudiante hace.

## S03.P121.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P121.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad de datos, representatividad y por qué fallan los modelos» (p. 5) — fuera de alcance/ya cubierta: el encuadre es de entrenamiento de modelos (predictiva); la calidad y el grano antes de agregar ya están en P120 H02, P122 H01 y P121 H02. El folleto no desarrolla método ni caso.

## S03.P121.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclo «from data preparation to exploration, visualization and analysis» (p. 1) — ya cubierta: preparación y calidad (P106 H01–H05, P107 H01–H02), exploración y visualización al servicio de un diagnóstico (P120 H02–H05, P121 H02–H04, P122 H01–H05). La ficha no da detalle que permita contrastar más.

## S03.P121.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - intervalos de confianza, pruebas de permutación y *false discovery rate* (p. 1: «permutation testing, false discovery rate, … confidence intervals») — fuera de alcance: los índices de P120–P122 registran como límite que las tasas por segmento no tienen intervalos ni pruebas de diferencia. Convertir ese límite en inferencia formal (por ejemplo, controlar comparaciones múltiples en un top N de segmentos) mete Estadística inferencial en el curso. Además, el documento no da caso ni profundidad para hacerlo con rigor. Los umbrales de volumen (P120 H06, P121 H05, P122 H06) siguen siendo la salvaguarda descriptiva vigente.
