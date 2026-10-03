# P213 — Transición de estados de cliente

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P213_transicion_estados_cliente/`.

### Preguntas analíticas actuales

- ¿Cuál es la probabilidad de que un cliente cambie de estado de compra el próximo mes?
- ¿Qué estado siguiente resulta más probable para cada estado observado?

Construye y evalúa una matriz de transición de Markov con observaciones
cliente-mes, pronósticos de estado, métricas, gráfico y supuestos.

### Inventario técnico de implementación

- **Introduce:** definición auditable de estados activo, latente e inactivo;
  tabulación cruzada y normalización de matriz de transición.
- **Introduce:** modelo de Markov de primer orden, línea base que conserva el
  estado y pronóstico por máxima probabilidad.
- **Verifica y comunica:** contrasta pronósticos con observaciones y persiste
  matriz, muestra evaluada, métricas y supuestos.

### Relación técnica con actividades anteriores

Complementa P212: cambia la duración hasta un evento por transiciones
mensuales entre estados. Sin P213 se pierde una representación probabilística
recurrente de la evolución de clientes.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

El producto estima transiciones, no causas ni intervenciones de retención. La
entrada P213 de `traceability.yaml` mapea `predictiva.C01`–`C04`.
