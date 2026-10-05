# Log — P152

## S02.P152.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P152_ventas_olap/` (`data/sales_mart.db`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/`); contexto de P150 y P151.
- **Trazabilidad revisada:** P152 → `descriptiva.C01`, `C02`, `C03`, `C05`; `audit-against-design.md` omite C01.
- **Highlights añadidos:** H01 (jerarquías del modelo como rutas; obligatorio de caso y datos), H02 (*roll-up* reconciliado), H03 (*slice* con contraste de medidas: Servicios lidera ventas netas, Oficina unidades, según `north_category_sales.csv`), H04 (*drill-down* encadenado y parametrizado).
- **Ambigüedades:** la región Norte se fija sin criterio; la divergencia de líderes por medida está persistida pero no comentada y el *drill-down* sólo sigue ventas netas; «explican» se usa para una descomposición aditiva; reconciliación por igualdad exacta de flotantes; notebook de estudiante vacío.
- **Superficies, contrato y dependencias:** S01–S05 declaradas; recibe esquema de P151 vía `data/sales_mart.db`; no habilita artefactos posteriores.
- **Auditoría de Analytics:** es la actividad del bloque más próxima a la pregunta descriptiva (qué, dónde, cuándo); falta «para quién» y lectura de la evidencia. OLAP sirve a la descripción, pero sin interpretación persistida puede leerse como ejercicio de consultas BI.

## S02.P152.02

- **Fecha / curso / executor:** 2026-10-04 / `descriptiva` / Claude; **estado:** incremental.
- **Origen:** aclaración del profesor: *business intelligence* es un predecesor que, por su importancia, está contenido en la analítica descriptiva (como la minería de datos en la predictiva).
- **Cambio en la auditoría de Analytics:** la auditoría decía que el producto «puede leerse como ejercicio de consultas BI». Se corrige: la navegación OLAP es BI al servicio de la descripción; el límite que se conserva es la falta de interpretación persistida.
- **Highlights, superficies y dependencias:** sin cambios; no se renumeran IDs.
