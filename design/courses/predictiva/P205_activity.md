# P205 — Priorización con probabilidades

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P205_priorizacion_con_probabilidades/`.

### Preguntas analíticas actuales

- ¿Qué tan confiables son las probabilidades de default estimadas?
- ¿Cómo cambia el comportamiento al variar el umbral de clasificación?

Usa una simulación didáctica de predicciones fuera de muestra; publica resumen
de calibración, tradeoffs de umbral y revisión por grupo. El material aclara que
los costos ilustran consecuencias de error, no una política crediticia real.

### Inventario técnico de implementación

- **Introduce:** bandas de calibración y comparación entre probabilidad media y frecuencia observada.
- **Introduce:** barrido de umbrales, costos de falsos positivos/negativos y revisión por grupo.
- **Introduce:** separación entre salida predictiva y política de decisión.

### Relación técnica con actividades anteriores

Extiende P204: usa probabilidades para evaluar calibración y punto operativo,
sin diseñar una política prescriptiva. Sin P205 se pierde la lectura crítica de
probabilidades antes de priorizar.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook, CSV de entrada, tres entregables, pruebas y `traceability.yaml`
sustentan `predictiva.C01`, `C04` y `C05`. La simulación limita inferencias
sobre crédito real.
