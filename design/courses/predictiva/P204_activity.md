# P204 — Clasificación básica numérica

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P204_clasificacion_basica_numerica/`.

### Preguntas analíticas actuales

- ¿Cómo podemos estimar, con fines educativos, la probabilidad de que un caso histórico corresponda a la clase M a partir de mediciones numéricas?

Usa mediciones históricas de cáncer de mama exclusivamente para una práctica
educativa; el notebook prohíbe interpretarlo como diagnóstico. Compara una
logística base con una especificación que incorpora término cuadrático e
interacción, y guarda estimadores, métricas y comparación.

### Inventario técnico de implementación

- **Reutiliza:** división estratificada, escalamiento y regresión logística.
- **Introduce:** ingeniería de características cuadrática e interacción, pipeline y ROC AUC.
- **Introduce:** frontera analítica entre probabilidad educativa y diagnóstico clínico.

### Relación técnica con actividades anteriores

Extiende P201 desde clasificación multiclase a probabilidad binaria y
especificación flexible. Sin P204 se pierde comparación explícita de modelos
probabilísticos sobre entradas numéricas.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook, datos, modelos, métricas, pruebas y `traceability.yaml` sustentan
`predictiva.C01`–`C04`; la restricción de uso clínico es explícita.
