# P449 — Monitoreo de costos: costo acumulado frente a presupuesto

## Actividad actual implementada

**Implementación:** `implementation/productos/P449_cost_monitoring/`.

### Preguntas analíticas actuales

- ¿Excede el costo acumulado de operación el presupuesto declarado?

`data/costs.json` contiene el costo de tres ejecuciones (`1.2`, `1.1`, `1.4`) y un presupuesto (`3.5`), sin moneda, periodo ni capacidad asociada. `professor/main.py` (`monitor_cost`) suma con `Decimal` a partir de la representación textual de cada valor y alerta si el total supera estrictamente el presupuesto. `submission/cost_report.json` registra `cost: 3.7`, `budget: 3.5`, `alert: true`. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** operar una capacidad con un límite explícito de costo (docstring); usuario y capacidad no evidenciados.
- **Producto terminal:** reporte de costo acumulado, presupuesto y alerta.
- **Uso y límite:** permite detectar sobrecosto con una regla exacta. No atribuye costo a componentes ni a una capacidad, no proyecta el costo ni define qué hacer ante la alerta.
- **Disciplinas contribuyentes:** gestión de costos de operación al servicio de la sostenibilidad de una capacidad no nombrada.

### Highlights de contribución

- **H01 — Acumula costos por ejecución contra un presupuesto (caso y datos):** el dato es una lista de costos por corrida y un tope global; la comparación es del acumulado, no de cada corrida. Límite: sin unidad, periodo ni vínculo con una capacidad del curso, no hay particularidad del caso que condicione el monitoreo; se registra esa ausencia. Sin este hito, el costo no aparecería como dimensión de operación.
- **H02 — Suma en decimal para que el umbral no dependa del punto flotante:** `Decimal(str(cost))` evita que la suma binaria altere la comparación; con `float`, los costos persistidos suman 3.6999999999999997, y la prueba de profesor exige que `1.25 + 0.75` frente a `2.00` no alerte («alcanzar el presupuesto no es excederlo») y que `1.25 + 0.76` dé exactamente 2.01 y alerte. `tests/test_activity.py` sólo exige el archivo. Sin este hito, el borde del presupuesto sería frágil.

### Inventario técnico de implementación

- **Introduce:** monitoreo de costo acumulado y aritmética `Decimal` para montos.
- **Reutiliza:** comparación con umbral declarado (P439, P442, P445) y persistencia JSON.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Costo acumulado vs. presupuesto | H01 | Suma de corridas; alerta estricta | Sin unidad, periodo ni capacidad. |
| Exactitud monetaria | H02 | `Decimal(str(x))` con bordes probados | Sólo suma; sin atribución por componente. |

### Relación técnica con actividades anteriores

Misma técnica de umbral que P439, P442 y P445, con nuevo objeto (costo) y una novedad técnica distinguible: aritmética decimal para el borde. No consume ejecuciones de P428/P429. Posible solapamiento estructural con P445 (conteo/umbral sobre ejecuciones) que requiere decisión posterior.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Acumulado vs. presupuesto | S01, S02, S03 | `implementation/productos/P449_cost_monitoring/data/costs.json`; `implementation/productos/P449_cost_monitoring/submission/cost_report.json` | No se sabe qué capacidad ni qué periodo. |
| H02 — Suma decimal | S02, S04 | `implementation/productos/P449_cost_monitoring/professor/main.py`: `monitor_cost`; `implementation/productos/P449_cost_monitoring/professor/test_main.py` | La prueba del estudiante no verifica valores. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Costos y presupuesto | `data/costs.json` | Tres corridas; sin unidad. |
| S02 | Monitoreo | `professor/main.py` | Suma decimal; alerta estricta. |
| S03 | Reporte entregado | `submission/cost_report.json` | Sin acción asociada. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: bordes; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** suma costos en decimal, compara con el presupuesto y persiste el reporte.
- **`submission/`:** `cost_report.json`.
- **Pruebas:** las de profesor verifican presupuesto alcanzado sin alerta y excedido con alerta; `test_01` verifica existencia.
- **Trazabilidad:** sólo `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P439/P442/P445:** la práctica de evaluar contra umbral; ningún artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P449 mapea únicamente `productos.C05`, que nombra «costos»; el mapeo se sostiene. Auditoría pregunta 5: sin capacidad asociada al costo, la actividad puede leerse como control de gasto genérico; la contribución técnica más distinguible es la aritmética decimal del borde.
