# Log — P441

## S02.P441.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P441_data_quarantine/` (`data/records.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/quarantine.json`, `tests/test_activity.py`); P402 y P440 para relación.
- **Trazabilidad revisada:** P441 → `productos.C02`, `productos.C03`, `productos.C05`; C02 débil.
- **Highlights:** añadidos H01 (cuarentena con motivo), H02 (caso como límite).
- **Ambigüedades:** una sola regla; válidos y cuarentena en el mismo archivo; sin reingreso; `amount` genérico desconectado del caso de fábricas; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe práctica de P402; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): patrón genérico de data engineering.

## S03.P441.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Cleaning (p. 73: calidad como adecuación al uso; reglas FD/CFD; p. 74: «Write rules for data cleaning according to the requirement of applications») y DPSIA/DI (p. 92: «input validation, data type validation, range and constraint validation, and cross-reference validation») — ya cubierta: P402 H01–H02 convierte expectativas operativas en contrato con llave de negocio; P441 H01 separa inválidos con motivo.

## S03.P441.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Dominio III, Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» y 3.6 «Assess data quality» (p. 5) — ya cubierta: contrato y compuerta de aceptación (P402 H01–H04), conciliación (P440 H01–H02), cuarentena (P441 H01). La limpieza en sí pertenece a Fundamentos o Descriptiva.

## S03.P441.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P441.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.6.6.1 «Identify causes of incorrect data in production systems» (p. 23) — ya cubierta: contrato de datos (P402), compatibilidad de entradas (P404), registros tardíos (P437), frescura (P439), conciliación (P440), cuarentena (P441), observabilidad integrada (P442).

## S03.P441.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - dimensiones tardías con fila provisional «unknown» que luego se sobrescribe con tipo 1 (p. 23: «special dimension rows are created with the unresolved natural keys as attributes … updated with type 1 overwrites») — fuera de alcance: alternativa de diseño físico a la cuarentena que exige un esquema estrella; el contraste «publicar con contexto desconocido frente a retener» sería interesante pero no hay caso ni datos en el curso que lo sostengan con rigor.

## S03.P441.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Missing and conflicting data» y «Data preparation, especially data cleansing» (p. 45); en los roles de almacenamiento, «document data quality problems» (p. 37) — ya cubierta: contrato de datos (P402 H01, H03) y cuarentena con motivo (P441 H01).
