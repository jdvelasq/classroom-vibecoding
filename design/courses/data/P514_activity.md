# P514 — ETL Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P514_superstore_etl/`.

### Preguntas analíticas actuales

- ¿Qué segmentos y regiones concentran las ventas y la utilidad?

Extrae cuatro fuentes Superstore, las integra, publica detalle curado y una
respuesta agregada, y genera `pipeline_report.csv` con estados raw, staging y
curated.

### Inventario técnico de implementación

- **Introduce:** etapas ETL explícitas y publicación de datos curados.
- **Reutiliza/extiende:** joins validados y preservación de línea de orden.
- **Introduce:** reporte de filas y estado por etapa.

### Relación técnica con actividades anteriores

Extiende P511 con una secuencia ETL observable. Sin P514 se pierde la práctica
de organizar, reportar y publicar transformaciones por etapas.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

Manifiesto, `professor/main.py`, entregables, pruebas y `traceability.yaml`
(`data.C01`–`data.C05`) sustentan el mapa.

## Auditoría de Analytics

ETL habilita la respuesta comercial; no sustituye el producto analítico.
