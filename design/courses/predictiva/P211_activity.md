# P211 — Pronóstico de congestión de servicio

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P211_pronostico_congestion_servicio/`.

### Preguntas analíticas actuales

- ¿Cómo puede anticiparse la congestión de un servicio a partir de volumen de llamadas y velocidad de respuesta?

Usa series de una línea 800 y publica pronóstico de congestión, gráfico,
métricas y supuestos.

### Inventario técnico de implementación

- **Extiende:** pronóstico temporal hacia un servicio operativo con variables de demanda y respuesta.
- **Introduce:** producto de congestión para anticipar presión de servicio.

### Relación técnica con actividades anteriores

Reutiliza pronóstico de P210 pero cambia de adopción a capacidad de servicio.
Sin P211 se pierde la conexión entre pronóstico y una señal operativa.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, fuente, notebooks, pronóstico, métricas, supuestos y pruebas sustentan
`predictiva.C01`–`C04`.
