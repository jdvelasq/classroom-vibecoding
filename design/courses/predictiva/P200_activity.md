# P200 — Regresión básica

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P200_regresion_basica/`.

### Preguntas analíticas actuales

- ¿Cómo podemos predecir el consumo de combustible (MPG) de un automóvil a partir de sus características técnicas?

Usa `auto_mpg.csv`; elimina nulos, trata `Origin` como categoría y reserva una
muestra reproducible. Compara regresión lineal con especificaciones de mayor
flexibilidad y guarda modelos, preprocesadores y comparación de desempeño.

### Inventario técnico de implementación

- **Introduce:** partición train/test, escalamiento, codificación categórica y regresión lineal.
- **Introduce:** MSE, visualización de predicción y comparación de modelos.

### Relación técnica con actividades anteriores

Primera actividad predictiva; establece la separación entre preparación,
ajuste y evaluación.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook de profesor, datos, modelos de `submission/`, pruebas y
`traceability.yaml` sustentan `predictiva.C01`–`C04`. El producto es una
estimación de MPG; sklearn sirve al producto de Analytics.
