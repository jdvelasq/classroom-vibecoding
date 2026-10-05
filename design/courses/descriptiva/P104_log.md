# Log — P104

## S02.P104.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P104_drivers_sqlite/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/summary.csv`, `submission/top10_drivers.png`, `temp/db.sqlite`, `tests/`). Comparado con P103 en detalle.
- **Trazabilidad revisada:** entrada P104 → `descriptiva.C02`, `descriptiva.C03`.
- **Highlights añadidos:** H01 (SQL contrastado con pandas en la prueba), H02 (vistas que normalizan nombres con guion; highlight de caso y datos), H03 (función de ventana y CTE), H04 (vista `driver_summary` reutilizable).
- **Ambigüedades:** producto y gráfico casi idénticos a P103 (posible solapamiento a decidir en el curso); la vista `drivers` mantiene `ssn` y `location`; `temp/db.sqlite` está versionado.
- **Superficies / contrato / dependencias:** S01–S06; recibe todo el contrato de P103; habilita la práctica `read_sql_query` usada en P107, P109 y P150–P154, sin artefacto compartido.
- **Auditoría de Analytics:** mismo producto descriptivo que P103; la contribución es de disciplina contribuyente (bases de datos) con verificación cruzada. C02 y C03 sustentados al nivel de P103.

## S03.P104.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - es un cuerpo de conocimiento de computación para pregrados de ciencia de datos, con 11 áreas de conocimiento y competencias de nivel T1/T2/E. Para descriptiva aportan sobre todo AP (presentación y visualización para clientes), DG/DM-Data Preparation (calidad, integración y limpieza, EDA, enmarcar la pregunta), DPSIA (privacidad e integridad) y PR/cap. 6 (comunicar resultados interpretados y sus límites a no especialistas). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P104.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P104.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P104.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de una base relacional y arquitectura de datos (p. 14: CAP-P.3.2.4–3.2.6) — ya cubierta (P104, P151) o fuera de alcance (selección de arquitectura = ingeniería de datos).
