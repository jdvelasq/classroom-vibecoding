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
