# P217 — Despliegue en aplicación web

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P217_deployment_web_app/`.

### Preguntas analíticas actuales

- ¿Cómo se entrega una predicción de precio de vivienda a un usuario mediante una interfaz web?
- ¿Cómo se transforma y valida la entrada del formulario antes de invocar un modelo ya entrenado?

Publica un predictor serializado de precio de vivienda en Flask, con formulario,
transformación de variables y manejo de entradas inválidas.

### Inventario técnico de implementación

- **Introduce:** aplicación Flask, rutas GET/POST, plantilla HTML y lectura de
  campos de formulario.
- **Introduce:** contrato local de siete características, conversión de tipos y
  ensamblaje de una fila `DataFrame` antes de `predict`.
- **Verifica:** trata errores de valores y entrega el archivo fuente como
  evidencia persistente; la prueba comprueba su presencia.

### Relación técnica con actividades anteriores

Reutiliza un modelo ya entrenado para convertir una predicción en capacidad
utilizable. Sin P217 se pierde la transición desde evaluación de modelos hacia
una interfaz para un usuario, aunque el entrenamiento queda fuera de esta
actividad.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Es un producto de datos: la predicción queda disponible a un usuario. No existe
entrada P217 en `implementation/predictiva/traceability.yaml`; debe revisarse
antes de aprobar la actividad.
