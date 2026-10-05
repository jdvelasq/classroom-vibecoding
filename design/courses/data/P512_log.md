# Log — P512

## S01.P512.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registraron hecho, dimensiones y preservación de grano como aporte técnico distinto de P511.

## S02.P512.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P512_superstore_warehouse/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/superstore_mart.db`, `tests/test_activity.py`); P500, P501, P503, P505–P507 y P511 para relaciones.
- **Trazabilidad revisada:** P512 → `data.C01`–`data.C05`; C01 limitada a una pregunta de organización.
- **Highlights:** añadidos H01 (dimensión de fecha desde texto `d/m/yy`; caso y datos), H02 (hecho a grano línea separado de dimensiones), H03 (mart persistido y consulta en estrella).
- **Preservado:** pregunta, modelo dimensional en SQLite, preservación del grano, consulta temporal por categoría, relación de extensión con P511.
- **Corregido:** la descripción previa decía que el mart organiza por «geografía»; no hay dimensión geográfica, está dentro de `dim_customer`. Se precisa que el resultado de la consulta no se persiste y que `orders` no entra al mart (no hay `Order ID`).
- **Añadido:** `dim_date` sin calendario completo y con clave por orden de aparición; ausencia de PK/FK; imposibilidad de reconstruir `order_count` de P500; prueba de sólo existencia.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** si la omisión de `orders` en el mart es deliberada.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P511 y P505–P507; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** capacidad de datos descriptiva; riesgo de lectura como taller de modelado dimensional por pregunta de organización y consulta no entregada.
