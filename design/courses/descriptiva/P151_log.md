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
