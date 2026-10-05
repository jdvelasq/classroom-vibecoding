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
