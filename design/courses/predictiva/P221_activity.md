# P221 — Selección de variables para regresión

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P221_selection_inputs_regresion/`.

### Preguntas analíticas actuales

- ¿Qué subconjunto de características mejora la predicción de MPG de un automóvil?
- ¿Cómo se selecciona el número de entradas sin separar esa selección del modelo?

Parte de Auto MPG y entrena una regresión lineal con `SelectKBest` y
`f_regression` dentro de un pipeline evaluado.

### Inventario técnico de implementación

- **Introduce:** `SelectKBest`, prueba `f_regression` y búsqueda de cantidad de
  variables en `GridSearchCV`.
- **Reutiliza:** manejo de categoría de origen, partición y regresión de P200.
- **Verifica y comunica:** compara MSE, MAE y R²; preserva el estimador elegido
  como artefacto de entrega.

### Relación técnica con actividades anteriores

Profundiza P200 al tratar explícitamente qué información entra al modelo, y
P220 al encapsular la transformación junto con el estimador. Sin P221 se pierde
la competencia de justificar una regresión con selección reproducible de inputs.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P221 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad.
