# P215 — Filtrado colaborativo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P215_filtrado_colaborativo/`.

### Preguntas analíticas actuales

- ¿Qué películas debería priorizarse para un usuario a partir de usuarios con patrones de calificación similares?
- ¿Qué vecinos respaldan cada recomendación y qué cobertura logra el método?

Con calificaciones FilmTrust, genera vecinos similares, puntajes predichos,
recomendaciones y un resumen de cobertura.

### Inventario técnico de implementación

- **Introduce:** consolidación usuario-ítem, medias por usuario y matriz de
  similitud entre usuarios.
- **Introduce:** predicción como desviación ponderada de vecinos y filtro de al
  menos dos vecinos de respaldo.
- **Verifica y comunica:** persiste vecinos, recomendaciones y cobertura de la
  matriz; las pruebas verifican esos artefactos.

### Relación técnica con actividades anteriores

Extiende P214 de asociaciones de canasta a preferencias de usuarios similares.
Sin P215 se pierde el contraste entre recomendar por coocurrencia y recomendar
por afinidad colaborativa, además de la consideración explícita de cobertura.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P215 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad; este mapeo no crea ni infiere
capacidades faltantes.
