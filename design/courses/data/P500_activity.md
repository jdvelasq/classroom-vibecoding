# P500 — Métricas mensuales de Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P500_superstore_metricas/`.

### Preguntas analíticas actuales

- ¿Cómo evolucionan mensualmente las ventas, la utilidad, el número de órdenes
  y el valor promedio por orden?

Usa
`data/superstore_orders.csv`, con una fila por producto dentro de una orden.
El material de profesor explicita el formato de entrada, interpreta la fecha y
verifica unicidad de `Order ID` + `Product Name`, descuento y valores faltantes
de `Product Base Margin` antes de agregar por mes.

El producto persistente es `submission/monthly_sales_metrics.csv`; además,
`metric_contract.json` documenta grano, fórmulas y controles de calidad. La
actividad ejercita lectura tabular, interpretación temporal, agregación,
conteo distinto y definición reproducible de métricas. Python ejecuta la
definición, pero el contrato declara que las métricas no dependen de la
herramienta.

La evidencia diseñada son los dos artefactos de `submission/` y sus pruebas.
La actividad está diseñada para observar la formulación y construcción de
métricas, no para demostrar logro estudiantil fuera de esos artefactos.

### Inventario técnico de implementación

- **Introduce:** lectura CSV con delimitador, codificación, decimal y fecha
  explícitos; definición de grano y validaciones de unicidad/dominio.
- **Introduce:** agrupación mensual, `nunique` de órdenes y métrica derivada
  de valor promedio por orden.
- **Introduce:** contrato JSON de métricas y reconciliación previa a la salida.

### Relación técnica con actividades anteriores

Es la primera actividad `P5xx` del curso. Si se elimina, se pierde la base de
grano, contrato de métrica y controles que las actividades Superstore posteriores
reutilizan.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Pregunta y entrega mensual | `professor/main.py`, `submission/questions.json` | explícita | No hay notebook de estudiante. |
| Grano y controles | `professor/main.py`, `submission/metric_contract.json` | explícita | La procedencia externa no está documentada en un manifiesto local. |
| Capacidades `data.C01`–`data.C05` | `traceability.yaml` | explícita | Deben revisarse frente a la evidencia de la actividad. |

## Auditoría de Analytics

El producto es una explicación temporal basada en métricas reproducibles para
una pregunta de desempeño comercial. Pandas sirve a ese producto; la actividad
no se organiza como un curso de programación o estadística aislado.
