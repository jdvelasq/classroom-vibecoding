# Log — P151

## S02.P151.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P151_ventas_mart/` (`data/`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/`); contexto de P104, P107, P109 y P150.
- **Trazabilidad revisada:** P151 → `descriptiva.C01`, `C02`, `C03`, `C05`; `audit-against-design.md` omite C01.
- **Highlights añadidos:** H01 (hecho y dimensiones desde grano línea, `dim_date` sin calendario completo; obligatorio de caso y datos), H02 (claves sin pérdida de hechos), H03 (mart persistido con integridad referencial), H04 (consulta en estrella).
- **Ambigüedades:** `data/sales_mart.db`, accesible al estudiante, equivale al mart que la actividad pide construir; fórmula de `net_sales` algebraicamente distinta de P150; generador idéntico (mismo hash) en P150–P154; notebook de estudiante vacío; respuesta sin lectura.
- **Superficies, contrato y dependencias:** S01–S05 declaradas; P152–P154 leen `data/sales_mart.db`, no `submission/sales_mart.db`: la dependencia es de esquema/lógica, no de artefacto.
- **Auditoría de Analytics:** el producto observable es una capacidad de datos (mart); el modelado dimensional organiza la actividad. Tensión con la frontera del curso («no posee ingeniería de datos»); no resuelta.

## S02.P151.02

- **Fecha / curso / executor:** 2026-10-04 / `descriptiva` / Claude; **estado:** incremental.
- **Origen:** aclaración del profesor: *business intelligence* es un predecesor que, por su importancia, está contenido en la analítica descriptiva (como la minería de datos en la predictiva).
- **Cambio en la auditoría de Analytics:** la auditoría oponía el mart a la frontera «no posee ingeniería de datos». Se corrige: el modelado dimensional es práctica de BI, parte de la analítica descriptiva; se conservan como límites la respuesta sin interpretar y el peso de la construcción en el notebook.
- **Highlights, superficies y dependencias:** sin cambios; no se renumeran IDs.

## S03.P151.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - integridad lógica «Entity integrity, referential integrity, domain integrity» (DPSIA/DI, p. 90); integración de fuentes y *data warehouse* (DG-Data Integration, p. 71) — ya cubierta: P150 H02, P151 H02–H03, P153 H03.

## S03.P151.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P151.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de un conjunto normalizado y fuentes de datos (CAP-E.3.2.3, 3.2.6, p. 14) — ya cubierta: P150 H01, P151 H01.

## S03.P151.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de una base relacional y arquitectura de datos (p. 14: CAP-P.3.2.4–3.2.6) — ya cubierta (P104, P151) o fuera de alcance (selección de arquitectura = ingeniería de datos).

## S03.P151.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Marco de consenso para la formación de pregrado en ciencia de datos: define «data acumen» como capacidad de juzgar, usar herramientas con responsabilidad y decidir con datos, y lista diez áreas conceptuales, con la ética transversal y una práctica repetida del ciclo completo con preguntas mal planteadas y datos «sucios». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P151.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «SQL avanzado», «Integración de fuentes», «Python aplicado», «Excel avanzado» en el dominio «Data & features» (p. 96); SQL 11,11 % de requerimiento (p. 79) — ya cubierta: SQL con vistas, ventanas y CTE (P104 H02–H04), UDF y capa cruda/limpia (P107 H02), consultas en estrella (P151 H04); integración de fuentes en P150 H01–H02.
  - Spark, Hadoop, Kafka, procesamiento distribuido (p. 175) y modelado avanzado, índices, sharding (p. 175) — fuera de alcance: ingeniería de datos/bases de datos; P100 ya usa MapReduce sólo como habilitador.

## S03.P151.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P151.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
