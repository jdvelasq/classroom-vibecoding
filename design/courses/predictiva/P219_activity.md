# P219 — Hiperparámetros

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P219_hiperparametros/`.

### Preguntas analíticas actuales

- ¿Qué combinación de `alpha` y `l1_ratio` de ElasticNet ofrece mejor evidencia predictiva para calidad de vino?
- ¿Cómo se contrasta una exploración manual con `GridSearchCV` sin usar los datos de prueba para escoger el modelo?

Entrena y compara modelos ElasticNet sobre calidad de vino; conserva el mejor
estimador serializado.

### Inventario técnico de implementación

- **Introduce:** partición entrenamiento/prueba, ElasticNet y métricas MSE, MAE
  y R².
- **Introduce:** exploración manual de `alpha` y `l1_ratio`, y búsqueda
  sistemática con `GridSearchCV`.
- **Verifica y comunica:** carga el estimador persistido y comprueba que la
  elección por validación no es inferior en MAE al estimador comparado.

### Relación técnica con actividades anteriores

Extiende P200 y P221 desde entrenar un modelo a seleccionar sus parámetros con
evidencia. Sin P219 se pierde la práctica de separar ajuste de hiperparámetros y
evaluación final.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P219 en `implementation/predictiva/traceability.yaml`.
La actividad conserva un estimador, pero necesita revisar su relación explícita
con la pregunta de calidad antes de ser aprobada curricularmente.
