# P201 — Clasificación básica de imágenes

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P201_clasificacion_basica_imagenes/`.

### Preguntas analíticas actuales

- ¿Cómo podemos clasificar imágenes de dígitos escritos a mano y revisar la incertidumbre de cada predicción?

Usa `sklearn.datasets.load_digits`, transforma matrices de píxeles en vectores,
reserva datos estratificados y ajusta regresión logística. Entrega estimador y
métricas; visualiza ejemplos, probabilidades y matriz de confusión.

### Inventario técnico de implementación

- **Introduce:** representación de imagen como vector de features y clasificación multiclase.
- **Introduce:** `predict_proba`, accuracy, matriz de confusión e inspección visual de errores.

### Relación técnica con actividades anteriores

Extiende P200 de predicción continua a clasificación probabilística y análisis
de incertidumbre por observación.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook, estimador, métricas, pruebas y `traceability.yaml` sustentan
`predictiva.C01`–`C04`; no hay caso organizacional explícito más allá de la
clasificación educativa de dígitos.
