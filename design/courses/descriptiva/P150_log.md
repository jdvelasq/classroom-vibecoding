# Log — P150

## S02.P150.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P150_ventas_tabla/` (`data/` con tres CSV y `sales_mart.db`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/`); contexto de P103, P106, P107, P120 y P122.
- **Trazabilidad revisada:** P150 → `descriptiva.C01`, `C02`, `C03`, `C05` en `implementation/descriptiva/traceability.yaml`; `audit-against-design.md` lista sólo C02, C03, C05 para P150–P154.
- **Highlights añadidos:** H01 (medida que exige integrar fuentes normalizadas; obligatorio de caso y datos), H02 (grano protegido), H03 (descomposición bruto/descuento/neto), H04 (tabla y respuesta persistidas).
- **Ambigüedades:** datos sintéticos (`generate_data.py`, semilla fija, «para los talleres de BI») sin declaración de procedencia al estudiante; el calendario es determinista (una fecha por pedido, casi 20 pedidos por mes, verificado reproduciendo el generador), por lo que la serie mensual no admite lectura estacional; `data/sales_mart.db` presente pero no usado; notebook de estudiante vacío y sin `DESCRIPTION.md`; sin celdas markdown ni conclusión.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; pruebas recalculan la transformación completa; P151 no consume `sales_analytics.csv` (dependencia de artefacto no evidenciada).
- **Auditoría de Analytics:** producto = tabla descriptiva integrada; la integración contribuye, pero sin usuario, decisión ni lectura la actividad se acerca a preparación de datos. Pregunta 5 no resuelta para el bloque P150–P154.

## S02.P150.02

- **Fecha / curso / executor:** 2026-10-04 / `descriptiva` / Claude; **estado:** incremental.
- **Origen:** aclaración del profesor: *business intelligence* es un predecesor que, por su importancia, está contenido en la analítica descriptiva (como la minería de datos en la predictiva).
- **Cambio en la auditoría de Analytics:** la auditoría trataba la integración del bloque P150–P154 como preparación de datos y dejaba la pregunta 5 no resuelta para el bloque. Se corrige: BI forma parte de la analítica descriptiva; el límite que se conserva es la falta de usuario y de lectura persistida.
- **Highlights, superficies y dependencias:** sin cambios; no se renumeran IDs.

## S03.P150.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - integridad lógica «Entity integrity, referential integrity, domain integrity» (DPSIA/DI, p. 90); integración de fuentes y *data warehouse* (DG-Data Integration, p. 71) — ya cubierta: P150 H02, P151 H02–H03, P153 H03.

## S03.P150.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» (p. 5) — ya cubierta: P106 H01–H05, P107 H01–H04, P150 H02.

## S03.P150.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de un conjunto normalizado y fuentes de datos (CAP-E.3.2.3, 3.2.6, p. 14) — ya cubierta: P150 H01, P151 H01.

## S03.P150.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limpiar, armonizar, transformar, unir y validar (p. 15: Task 3.5) — ya cubierta: P106 H01–H04, P107 H01–H03, P150 H02 (`validate="many_to_one"`), P121 H02 (conciliación).

## S03.P150.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - Marco de consenso para la formación de pregrado en ciencia de datos: define «data acumen» como capacidad de juzgar, usar herramientas con responsabilidad y decidir con datos, y lista diez áreas conceptuales, con la ética transversal y una práctica repetida del ciclo completo con preguntas mal planteadas y datos «sucios». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
