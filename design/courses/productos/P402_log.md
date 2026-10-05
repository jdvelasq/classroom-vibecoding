# Log — P402

## S02.P402.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P402_data_testing_pytest_pandas/` (`data/*.csv`, `professor/main.py`, `professor/notebook.ipynb`, `professor/test_main.py`, `src/main.py`, `submission/validation_report.json`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P402 → `productos.C02`, `productos.C05`. No mapea `productos.C03`, aunque la actividad lo evidencia directamente; C05 sin evidencia.
- **Highlights:** añadidos H01 (contrato), H02 (caso y datos: llave derivada de la granularidad máquina-día), H03 (reporte persistido), H04 (pruebas de aceptación y rechazo).
- **Ambigüedades:** el reporte persistido proviene de `main.py`, no del notebook (faltan `rows`, `contract_columns`, `business_key`); mensajes de llave duplicada distintos entre ambos; procedencia del extracto no documentada; el notebook del profesor permanece aunque la modalidad del estudiante es Python.
- **Superficies / contrato / dependencias:** S01–S06; evaluación sólo por existencia; habilita P405 (subconjunto del extracto).
- **Auditoría de Analytics:** resuelta con reservas: compuerta de insumos con usuario declarado; falta conexión con el indicador protegido y la acción ante rechazo.

## S03.P402.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).
  - DG-Data Cleaning (p. 73: calidad como adecuación al uso; reglas FD/CFD; p. 74: «Write rules for data cleaning according to the requirement of applications») y DPSIA/DI (p. 92: «input validation, data type validation, range and constraint validation, and cross-reference validation») — ya cubierta: P402 H01–H02 convierte expectativas operativas en contrato con llave de negocio; P441 H01 separa inválidos con motivo.

## S03.P402.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Dominio III, Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» y 3.6 «Assess data quality» (p. 5) — ya cubierta: contrato y compuerta de aceptación (P402 H01–H04), conciliación (P440 H01–H02), cuarentena (P441 H01). La limpieza en sí pertenece a Fundamentos o Descriptiva.

## S03.P402.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dimensiones de calidad «accuracy, completeness, consistency, timeliness, validity, uniqueness» (p. 15, CAP-E.3.6.1) — ya cubierta: contrato de datos (P402 H01), frescura (P439 H01), observabilidad integrada (P442 H02).

## S03.P402.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.6.6.1 «Identify causes of incorrect data in production systems» (p. 23) — ya cubierta: contrato de datos (P402), compatibilidad de entradas (P404), registros tardíos (P437), frescura (P439), conciliación (P440), cuarentena (P441), observabilidad integrada (P442).
  - CAP-P.3.6.1 dimensiones de calidad «missing data, accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» (p. 15) — ya cubierta en su uso operativo (contrato de seis reglas P402 H01, frescura P439 H01, señales integradas P442); el perfilado exploratorio es de Descriptiva.

## S03.P402.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el grano como «binding contract on the design» y no mezclar granos (p. 5) — ya cubierta: P402 H02 (llave derivada del grano máquina-día) y P443 H01 (cambio de grano que el linaje explica).
  - nulos en claves foráneas sustituidos por fila «unknown» (p. 7) y atributos nulos como «Unknown»/«Not Applicable» (p. 11) — fuera de alcance: reglas de diseño del modelo dimensional; la validación de completitud del insumo ya es P402 H01.
