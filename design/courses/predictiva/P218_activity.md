# P218 — Despliegue mediante API

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P218_deployment_api/`.

### Preguntas analíticas actuales

- ¿Cómo puede otro proceso solicitar una predicción de precio de vivienda mediante HTTP?
- ¿Qué contrato y validaciones debe cumplir la solicitud antes de usar el modelo?

Expone un predictor serializado mediante FastAPI, con endpoint de salud,
contrato Pydantic y un cliente que consume `/predict`.

### Inventario técnico de implementación

- **Introduce:** FastAPI, endpoints GET/POST, serialización JSON y consumidor
  HTTP con `requests`.
- **Introduce:** `BaseModel` de Pydantic y restricciones de dominio para las
  siete características de vivienda.
- **Reutiliza:** modelo de precio y la transformación a `DataFrame` de P217,
  pero sustituye interfaz manual por un contrato interoperable.

### Relación técnica con actividades anteriores

Extiende P217 para que una capacidad predictiva pueda ser invocada por software
en lugar de una persona. Sin P218 se pierde el contrato verificable entre un
modelo y un consumidor programático.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Es un producto de datos con disponibilidad y validación de entrada. No existe
entrada P218 en `implementation/predictiva/traceability.yaml`; debe revisarse
antes de aprobar la actividad.
