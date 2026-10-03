# P515 — ELT Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P515_superstore_elt/`.

### Preguntas analíticas actuales

- ¿Qué segmentos y regiones concentran las ventas y la utilidad?

Carga cuatro fuentes como tablas raw en SQLite, crea una tabla curada mediante
SQL y entrega `superstore_elt.db`, respuesta agregada y `elt_report.csv`.

### Inventario técnico de implementación

- **Introduce:** carga raw y transformación ELT dentro de SQLite.
- **Extiende:** integración Superstore mediante `CREATE TABLE AS SELECT`.
- **Introduce:** medición de filas raw y curated en reporte de ejecución.

### Relación técnica con actividades anteriores

Contrasta con P514: misma pregunta, distinta ubicación de la transformación.
Sin P515 se pierde el contraste técnico ETL versus ELT.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

Manifiesto, código de profesor, entregables, pruebas y trazabilidad
`data.C01`–`data.C05` respaldan el mapa.

## Auditoría de Analytics

SQLite es el medio para producir evidencia comercial, no el objetivo autónomo.
