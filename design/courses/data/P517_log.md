# Log — P517

## S02.P517.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P517_vermont_contratos/` (`data/vermont.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/contract_report.csv`, `tests/test_activity.py`); P516 para relaciones; P513–P515 para contraste de estados.
- **Trazabilidad revisada:** P517 → `data.C01`, `data.C03`, `data.C04`, `data.C05`; coherente; C02 no mapeada y no ejercitada.
- **Highlights:** H01 (acción de alcance distinta de rechazo; caso y datos), H02 (contrato mínimo de seis columnas e identidad VT/50), H03 (clasificación `BREAKING`/`SCOPE`/`COMPATIBLE`/`NONE`), H04 (lotes perturbados que ejercitan cada rama).
- **Ambigüedades:** los lotes son perturbaciones simuladas del mismo archivo, no entregas reales; `source_release="2017"` es una columna inventada, no procedencia; la fila `optional_column` del reporte no es visible en la evidencia inspeccionada (el código implica `PASS`/`COMPATIBLE`/`ACCEPT`); columnas no requeridas eliminadas se clasifican `NONE`; sólo se registra la primera regla violada; `FILTER_ZIPCODE_0` no se aplica.
- **Superficies / contrato / dependencias:** S01–S06; recibe datos y reglas de P516; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** el contrato protege una pregunta analítica concreta; la práctica de Data Engineering queda subordinada. Límite: simulación y acción no materializada.

## S03.P517.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Cleaning (p. 74: «Write rules for data cleaning according to the requirement of applications and data semantics») — ya cubierta: contrato mínimo derivado de la pregunta (H02, H03).

## S03.P517.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - Task 3.1 «Identify and prioritize data needs» (p. 5) — ya cubierta (P500 H02, P517 H02).

## S03.P517.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - CAP-E.3.1.1 «Identify data needs, sources, and acquisition sequence» (p. 13) — ya cubierta por P500 H02 y P517 H02.
  - CAP-E.3.7.1 y 3.8.1 (p. 16) — ya cubierta por P516 H01 (alcance que cambia la pregunta) y P517 H01; la parte no cubierta va a las candidatas.

## S03.P517.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P517.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P517.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco autorizado de la NASEM para la formación de pregrado en ciencia de datos. Define la «data acumen» y diez áreas conceptuales (entre ellas gestión y curaduría de datos, flujo de trabajo y reproducibilidad, ética) y pide que la ética atraviese todo el currículo. Respalda expectativas generales, no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P517.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad: aplicación de reglas de limpieza (tiempos mínimos, duplicados), control de completitud, consistencia de escalas» (p. 238); «Trazabilidad y gobernanza: separación clara entre evidencia empírica … y supuestos de negocio» (p. 41). Categoría: ya cubierta. Controles de calidad ejecutables (P500 H04), reglas nombradas con dimensión y conteo (P516 H02), contrato y decisiones persistidas (P517 H02–H04).

## S03.P517.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P517.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P517.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.
