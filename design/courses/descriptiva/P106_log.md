# Log — P106

## S02.P106.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P106_limpieza_pandas/` (`data/ventas.csv`, `professor/main.py`, `professor/diagnostics.py`, `src/main.py`, `submission/ventas.csv`, `tests/`). Comparado con P100–P105.
- **Trazabilidad revisada:** entrada P106 → `descriptiva.C02`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (función por tipo de suciedad; highlight de caso y datos), H02 (canonización con diccionarios y diagnóstico de colisiones), H03 (fechas y regla día/mes), H04 (unidades y escalas), H05 (invariantes de dominio en la prueba).
- **Ambigüedades:** procedencia de `ventas.csv` no documentada y sin fuente limpia ni generador (no hay verdad de referencia); la regla día/mes asume `yyyy-mm-dd` cuando ambos componentes son ≤ 12; peso sin unidad se asume en kg; la prueba no ejecuta `main.py` y no cubre importes ni proveedores canónicos; `diagnostics.py` tiene sus llamadas principales comentadas.
- **Superficies / contrato / dependencias:** S01–S06; habilita P107 (mismo dato, contrato y prueba).
- **Auditoría de Analytics:** producto = capacidad de datos limpia, sin descripción posterior. C02 sustentado en la dimensión de calidad de datos; C05 débil. Domina la preparación de datos como disciplina contribuyente.

## S03.P106.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dimensiones de calidad de datos, entity resolution, limpieza basada en reglas y dependencias funcionales (DG-Data Cleaning, pp. 73–74) — ya cubierta: P106 H01–H05 (función por defecto, canonización con diagnóstico de colisiones, invariantes de dominio) y P107 H01–H03. Nombrar las dimensiones de calidad o formalizar FD/CFD sería marginal (vocabulario, no capacidad nueva).
  - transformación (estandarización, normalización, codificación, unidades; DG-Data Transformation, p. 73) — ya cubierta: P106 H04 lleva magnitudes a una unidad común.

## S03.P106.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» (p. 5) — ya cubierta: P106 H01–H05, P107 H01–H04, P150 H02.

## S03.P106.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limpiar, armonizar, transformar, unir y validar (p. 15: Task 3.5) — ya cubierta: P106 H01–H04, P107 H01–H03, P150 H02 (`validate="many_to_one"`), P121 H02 (conciliación).

## S03.P106.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data preparation, especially data cleansing and data transformation», «Missing and conflicting data» (p. 45) — ya cubierta (P106 H01–H05; P107 H01).
  - «use simple graphics to check data for artifacts, snafus, and inconsistencies» (p. 45) — ya cubierta (P122 H01–H02, histograma con referencia en cero; regla de evidencia visual de `AGENTS.md`).

## S03.P106.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - procesamiento en capas Bronze/Silver/Gold con «validación, normalización y verificación de calidad» (p. 131); reglas de limpieza «tiempos mínimos, duplicados», «control de completitud» (p. 238) — ya cubierta: separación crudo/limpio (P107 H02), limpieza por columna e invariantes (P106 H01, H05).
  - reducción de granularidad mediante «Dominios canónicos» de habilidades y roles (pp. 29, 80–92, 96) — ya cubierta: canonización con diccionarios y diagnóstico de colisiones (P106 H02, P107 H03), normalización de vocabularios (P123 H03).

## S03.P106.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
