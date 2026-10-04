# P220 — Pipelines

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P220_pipelines/`.

### Preguntas analíticas actuales

- ¿Cómo se conserva el procesamiento de texto junto con un clasificador de frases?
- ¿Cómo se busca una configuración reproducible sin separar vectorización, transformación TF–IDF y modelo?

Empaqueta clasificación de frases en un `Pipeline` de `CountVectorizer`,
`TfidfTransformer` y regresión logística, con búsqueda de parámetros y
estimador persistido.

### Inventario técnico de implementación

- **Introduce:** `Pipeline` de transformación y estimador, persistencia con
  `pickle` y predicción desde el objeto recuperado.
- **Extiende:** clasificación textual de P203 mediante TF–IDF y
  `GridSearchCV` con `balanced_accuracy`.
- **Verifica y comunica:** contrasta precisión y exactitud balanceada de
  entrenamiento/prueba y evita guardar un estimador peor que el actual.

### Relación técnica con actividades anteriores

Reutiliza texto y clasificación de P202–P203, pero concentra el aprendizaje en
la reproducibilidad del flujo completo. Sin P220 se pierde la garantía de que
transformación y modelo viajan juntos al usarlo después.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P220 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad.
