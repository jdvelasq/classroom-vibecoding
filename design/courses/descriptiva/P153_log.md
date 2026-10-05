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
