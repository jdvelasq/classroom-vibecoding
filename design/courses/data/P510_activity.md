# P510 — Valoraciones de cursos DataCamp

## Actividad actual implementada

**Implementación:** `implementation/data/P510_datacamp_valoraciones/`.

### Preguntas analíticas actuales

- ¿Qué cursos y tecnologías tienen mayor adopción y mejor valoración para
  priorizar una oferta educativa?

Parte de un volcado SQL local
con dos granos: curso y calificación de usuario a curso. La salida
`course_ratings.csv` agrega número y promedio de calificaciones por curso y
lenguaje de programación.

El notebook de profesor hace visible la carga del volcado, el cambio de grano,
la consulta de agregación y conciliaciones que evitan confundir agregación con
pérdida de calificaciones. La evidencia diseñada es el CSV y las validaciones
de cardinalidad, sumas y rango de calificaciones.

### Inventario técnico de implementación

- **Introduce:** carga de volcado SQL en SQLite y comparación de dos granos:
  curso y calificación individual.
- **Introduce:** `LEFT JOIN`, agregación por curso y conciliaciones de filas,
  suma de calificaciones y rango de promedios.

### Relación técnica con actividades anteriores

Introduce un caso de evaluación de oferta y una conciliación explícita de
agregación. Sin P510 se pierde la práctica de comprobar que resumir no ocultó
registros fuente.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Pregunta, granos y salida | `professor/notebook.ipynb`, `submission/course_ratings.csv` | explícita | No hay manifiesto de procedencia del volcado. |
| Conciliación de agregación | notebook de profesor | explícita | El notebook de estudiante no contiene contenido. |
| Capacidades `data.C01`–`data.C05` | `traceability.yaml` | explícita | Alineación pendiente. |

## Auditoría de Analytics

La consulta y el modelo relacional sirven una decisión de priorización de
oferta educativa; no son el objetivo curricular autónomo.
