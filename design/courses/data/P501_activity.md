# P501 — Serving de métricas Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P501_superstore_serving/`.

### Preguntas analíticas actuales

- ¿Qué interfaces permiten responder la evolución mensual de ventas y la
  contribución de cada categoría?

Parte de `data/superstore_orders.csv`, al
grano de línea de orden, y publica tres representaciones: detalle CSV para
exploración, `monthly_sales` y `category_sales` en una base SQLite.

El producto es `submission/sales_serving.db`, acompañado de
`sales_detail.csv`, `serving_manifest.csv` y la pregunta persistente. El
manifiesto hace explícitos el grano, consumidor e intención de cada interfaz.
La actividad ejercita derivación de vistas con distintos consumidores y la
relación entre representación de datos y una pregunta analítica.

La evidencia diseñada son los artefactos de serving y las pruebas. No hay
notebook de estudiante que documente una secuencia de aula invertida.

### Inventario técnico de implementación

- **Reutiliza:** agregación mensual y por categoría sobre líneas de pedido.
- **Introduce:** publicación de una misma fuente en CSV de detalle y tablas
  SQLite con grano, consumidor y propósito documentados.
- **Introduce:** manifiesto de interfaces de datos como artefacto persistente.

### Relación técnica con actividades anteriores

Extiende P500: conserva métricas, pero añade diseño de interfaces para analista
y dashboard. Sin P501 se pierde la habilidad de distinguir representación y
consumidor de datos.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Interfaces y consumidores | `professor/main.py`, `submission/serving_manifest.csv` | explícita | No hay manifiesto de procedencia local. |
| Métricas mensual y por categoría | `professor/main.py`, `submission/sales_serving.db` | explícita | La interacción del estudiante no queda descrita. |
| Capacidades `data.C02`–`data.C05` | `traceability.yaml` | explícita | Requiere auditoría posterior contra la actividad. |

## Auditoría de Analytics

La base SQLite y los CSV sirven a productos de consulta para una pregunta de
negocio; no son un fin de ingeniería de datos por sí mismos.
