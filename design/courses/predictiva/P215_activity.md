# P215 — Filtrado colaborativo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P215_filtrado_colaborativo/`.

### Preguntas analíticas actuales

- ¿Qué películas debería priorizarse para un usuario a partir de usuarios con patrones de calificación similares?
- ¿Qué vecinos respaldan cada recomendación y qué cobertura logra el método?

Con calificaciones FilmTrust, genera vecinos similares, puntajes predichos,
recomendaciones y un resumen de cobertura.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** prioriza películas para el usuario 272 mediante preferencias de vecinos; no hay decisión de producto real evidenciada.
- **Producto terminal:** vecinos elegibles, puntajes predichos, recomendaciones y cobertura.
- **Uso y límite:** ausencia de calificación no es puntuación baja; no evalúa satisfacción, ranking retenido ni impacto.
- **Disciplinas contribuyentes:** similitud coseno y filtrado colaborativo sirven a una recomendación predictiva.

### Highlights de contribución

- **H01 — Conserva la ausencia como ausencia:** construye matriz usuario×película y centra calificaciones sin convertir faltantes en desaprobación.
- **H02 — Exige respaldo antes de predecir:** filtra vecinos por al menos dos películas comunes y similitud positiva.
- **H03 — Estima una puntuación desde desviaciones ponderadas:** combina preferencias de vecinos y exige dos respaldos para recomendar.
- **H04 — Hace visible cobertura y soporte:** persiste vecinos, recomendaciones y resumen de densidad/cobertura.

### Inventario técnico de implementación

- **Introduce:** consolidación usuario-ítem, medias por usuario y matriz de
  similitud entre usuarios.
- **Introduce:** predicción como desviación ponderada de vecinos y filtro de al
  menos dos vecinos de respaldo.
- **Verifica y comunica:** persiste vecinos, recomendaciones y cobertura de la
  matriz; las pruebas verifican esos artefactos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Matriz dispersa | H01 | Pivot usuario×película y medias | No mide cold start. |
| Vecinos/recomendación | H02–H03 | Similitud coseno, soporte y score | Sólo usuario 272. |
| Cobertura | H04 | CSV de vecinos/recomendaciones/resumen | No hay métrica de ranking retenido. |

### Relación técnica con actividades anteriores

Extiende P214 de asociaciones de canasta a preferencias de usuarios similares.
Sin P215 se pierde el contraste entre recomendar por coocurrencia y recomendar
por afinidad colaborativa, además de la consideración explícita de cobertura.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook; `data/filmtrust_ratings.csv` | Datos/usuario sin contexto operativo. |
| H02 | S02 | Notebook: ratings comunes y similitud | Umbrales fijos. |
| H03 | S02 | Notebook; `submission/recommendations.csv` | Sin evaluación retenida. |
| H04 | S03, S04 | CSV de entrega; pruebas | Tests sólo presencia. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Matriz y faltantes | Datos; notebook | Faltante no es baja calificación. |
| S02 | Vecinos y score | Notebook; recomendaciones | Requiere dos vecinos. |
| S03 | Cobertura | `coverage_summary.csv` | Sin ranking o satisfacción. |
| S04 | Entregas y trazabilidad | `submission/`; tests; YAML | Falta entrada P215. |

### Contrato de evidencia actual

- **Código:** consolida ratings, calcula vecinos, estima puntuaciones y filtra recomendaciones.
- **`submission/`:** conserva cobertura, vecinos y recomendaciones.
- **Pruebas:** comprueban tres CSV.
- **Trazabilidad:** falta entrada P215.

### Dependencias en la secuencia

- **Recibe de P214:** producto de recomendación; cambia reglas por afinidad de usuarios.
- **Habilita para Pyyy:** no hay dependencia posterior demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P215 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad; este mapeo no crea ni infiere
capacidades faltantes.
