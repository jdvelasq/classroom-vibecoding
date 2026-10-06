# P214 — Transición de estados de cliente

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P213_transicion_estados_cliente/`.

### Preguntas analíticas actuales

- ¿Cuál es la probabilidad de que un cliente cambie de estado de compra el próximo mes?
- ¿Qué estado siguiente resulta más probable para cada estado observado?

Construye y evalúa una matriz de transición de Markov con observaciones
cliente-mes, pronósticos de estado, métricas, gráfico y supuestos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima el estado de compra siguiente; no establece acción de retención.
- **Producto terminal:** matriz de transición, pronósticos por cliente-mes y comparación contra persistencia.
- **Uso y límite:** estados se derivan de compras observadas; la matriz no prueba causas ni autoriza campañas.
- **Disciplinas contribuyentes:** cadenas de Markov y evaluación temporal sirven al producto predictivo.

### Highlights de contribución

- **H01 — Hace auditable el estado de cliente:** define activo, latente e inactivo desde compras consecutivas antes de estimar transiciones.
- **H02 — Reserva transiciones completas:** aparta los últimos tres meses y estima la matriz sólo con historial previo.
- **H03 — Lee una matriz como pronóstico probabilístico:** filas=estado actual, columnas=estado siguiente; compara la clase más probable con persistencia.
- **H04 — Persiste matriz, muestra de pronósticos, métricas, gráfico y supuestos:** separa predicción de una intervención comercial.

### Inventario técnico de implementación

- **Introduce:** definición auditable de estados activo, latente e inactivo;
  tabulación cruzada y normalización de matriz de transición.
- **Introduce:** modelo de Markov de primer orden, línea base que conserva el
  estado y pronóstico por máxima probabilidad.
- **Verifica y comunica:** contrasta pronósticos con observaciones y persiste
  matriz, muestra evaluada, métricas y supuestos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Estados cliente-mes | H01 | Definición observable de tres estados | No demuestra intención del cliente. |
| Matriz temporal | H02–H03 | Markov de primer orden y baseline persistente | Sólo tres transiciones retenidas. |
| Evidencia persistida | H04 | Matriz, pronósticos, métricas, PNG, supuestos | Tests sólo presencia. |

### Relación técnica con actividades anteriores

Complementa P213: cambia la duración hasta un evento por transiciones
mensuales entre estados. Sin P214 se pierde una representación probabilística
recurrente de la evolución de clientes.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook; `customer_month_states.csv.gz` | Estados son definición didáctica. |
| H02 | S02 | Notebook: últimos tres meses | Horizonte pequeño. |
| H03 | S02, S03 | Notebook; transición/forecast/metrics CSV | No causalidad ni política. |
| H04 | S04 | `submission/`; pruebas | Tests no validan cálculos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Estados y tiempo | Datos; notebook | Diciembre parcial se excluye. |
| S02 | Matriz/selección | Notebook; matriz CSV | Filas deben sumar uno. |
| S03 | Baseline/evaluación | Métricas y pronósticos | Sin incertidumbre. |
| S04 | Entrega/límite | Supuestos; pruebas | No hay política de retención. |

### Contrato de evidencia actual

- **Código:** deriva matriz de Markov, evalúa contra persistencia y grafica.
- **`submission/`:** conserva matriz, pronósticos, métricas, PNG y supuestos.
- **Pruebas:** exigen archivos, no valores.
- **Trazabilidad:** P214 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de P213:** temporalidad de cliente y límite entre predicción/intervención.
- **Habilita para P215–P216:** comparación de productos de recomendación, sin dependencia de código demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

El producto estima transiciones, no causas ni intervenciones de retención. La
entrada P214 de `traceability.yaml` mapea `predictiva.C01`–`C04`.
