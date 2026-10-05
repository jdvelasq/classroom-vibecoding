# Log — P153

## S02.P153.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P153_ventas_kpis/` (`data/sales_mart.db`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` con cinco archivos, `tests/`); contexto de P120, P121, P122, P124 y P150–P152.
- **Trazabilidad revisada:** P153 → `descriptiva.C01`, `C02`, `C03`, `C05`; `audit-against-design.md` omite C01.
- **Highlights añadidos:** H01 (KPI como contrato), H02 (tasa ponderada como ratio de sumas sobre `discount_pct` por línea; obligatorio de caso y datos), H03 (calidad como compuerta de publicación), H04 (linaje).
- **Ambigüedades:** ningún valor de KPI se calcula; las reglas cubren integridad del hecho pero no «problemas de definición» que la pregunta menciona; la rama `BLOQUEADO` nunca se ejercita sobre datos íntegros por construcción; «Gerencia comercial» es sólo etiqueta de propietario; «segmento» en el linaje no se define; prueba de linaje débil (longitud > 8); gráfico sobre booleanos; notebook de estudiante vacío.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; P154 no consume el catálogo y publica `orders`, ausente de él.
- **Auditoría de Analytics:** producto = gobierno de métricas; fortalece C01/C05 pero no describe lo que ocurre. Se lee como práctica de BI/gobierno de datos.

## S02.P153.02

- **Fecha / curso / executor:** 2026-10-04 / `descriptiva` / Claude; **estado:** incremental.
- **Origen:** aclaración del profesor: *business intelligence* es un predecesor que, por su importancia, está contenido en la analítica descriptiva (como la minería de datos en la predictiva).
- **Cambio en la auditoría de Analytics:** la auditoría decía que la actividad «se lee como práctica de BI/gobierno de datos». Se corrige: el gobierno de métricas es BI y forma parte de la analítica descriptiva; se conserva como límite que las reglas no ejercitan el bloqueo.
- **Highlights, superficies y dependencias:** sin cambios; no se renumeran IDs.

## S03.P153.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - integridad lógica «Entity integrity, referential integrity, domain integrity» (DPSIA/DI, p. 90); integración de fuentes y *data warehouse* (DG-Data Integration, p. 71) — ya cubierta: P150 H02, P151 H02–H03, P153 H03.
  - procedencia de datos (DPSIA/DI, p. 91: «Data provenance assurance») y auditabilidad de sistemas de decisión (PR-On Automation, p. 111) — ya cubierta en lo descriptivo por el linaje de P153 H04. Lo demás es fuera de alcance (seguridad y automatización).

## S03.P153.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - linaje, trazabilidad y control de versiones de los datos (CAP-E.3.4.3, p. 15) — ya cubierta: P153 H04.

## S03.P153.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio 17 %, encuadre analítico 15 %, datos 19 %, selección de metodología 15 %, desarrollo de modelos 15 %, despliegue 10 %, ciclo de vida 9 %) con subtareas evaluables. Respalda expectativas profesionales generales, no un syllabus. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
