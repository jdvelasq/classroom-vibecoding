# P512 — Warehouse Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P512_superstore_warehouse/`.

### Preguntas analíticas actuales

- ¿Cómo se organizan ventas y utilidad por fecha, cliente, producto y geografía sin perder el grano de línea de orden?

La actividad usa las cuatro fuentes Superstore y publica `superstore_mart.db`.
El notebook construye dimensiones de fecha, cliente y producto, y una tabla de
hechos de líneas de orden para consultas temporales por categoría.

### Inventario técnico de implementación

- **Introduce:** modelo dimensional con hecho y dimensiones en SQLite.
- **Extiende:** derivación temporal, claves y unión de dimensiones sin perder
  el grano de línea.
- **Introduce:** consulta SQL sobre mart para métricas por tiempo y categoría.

### Relación técnica con actividades anteriores

Extiende P511: pasa de integración puntual a una representación dimensional.
Sin P512 se pierde la organización de datos para análisis repetible.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

El manifiesto, notebook de profesor, base SQLite y `traceability.yaml`
(`data.C01`–`data.C05`) sustentan el mapa. No se atribuye logro estudiantil.

## Auditoría de Analytics

El mart sirve análisis de ventas y utilidad; el modelado es funcional al
producto analítico.
