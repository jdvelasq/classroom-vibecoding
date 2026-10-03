# P502 — Linaje de datos Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P502_superstore_linaje/`.

### Preguntas analíticas actuales

- ¿Cuál es el linaje desde Superstore hasta las interfaces que responden ventas
  mensuales y ventas por categoría?

El material de profesor construye tres
artefactos: catálogo de datos, catálogo de columnas y `lineage.csv`. Describe
el grano de cada representación y las transformaciones desde la fuente de
líneas de pedido hacia detalle, métricas mensuales y agregados por categoría.

El producto entregable es el conjunto de catálogos y linaje en `submission/`.
La práctica hace observable documentación de origen, grano, consumidores y
transformaciones; no evidencia una implementación de pipeline ejecutable por
parte del estudiante.

### Inventario técnico de implementación

- **Reutiliza:** artefactos Superstore de detalle, métricas y categorías.
- **Introduce:** catálogo de datasets, catálogo de columnas y tabla de linaje
  con transformaciones entre representaciones.
- **Introduce:** documentación explícita de grano y consumidor por dataset.

### Relación técnica con actividades anteriores

Extiende P501: describe el recorrido entre fuente e interfaces. Sin P502 se
pierde la evidencia de linaje que permite auditar las métricas publicadas.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Pregunta y producto de linaje | `professor/main.py`, `submission/questions.json` | explícita | Los catálogos son construidos por el profesor. |
| Granos y transformaciones | `submission/data_catalog.csv`, `lineage.csv` | explícita | No hay manifiesto de procedencia para el CSV de entrada. |
| Capacidades `data.C03`–`data.C05` | `traceability.yaml` | explícita | Revisión de alineación pendiente. |

## Auditoría de Analytics

La actividad documenta cómo datos e interfaces sostienen preguntas de ventas;
catálogo y linaje son habilitadores de evidencia analítica, no contenido de
gobierno de datos aislado.
