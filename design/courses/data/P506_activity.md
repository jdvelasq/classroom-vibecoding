# P506 — SQL avanzado sobre Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P506_scopus_sql_avanzado/`.

### Preguntas analíticas actuales

- ¿Qué autores muestran producción sostenida sobre proptech desde 2020?

Usa `scopus_proptech.db` y entrega
`submission/sustained_authors.csv`. Los notebooks de profesor y estudiante y
las pruebas forman parte del caso.

La evidencia diseñada es una respuesta tabular que requiere definir una
condición temporal de continuidad sobre autores. La actividad ejercita SQL en
función de una pregunta analítica longitudinal; el detalle de la consulta se
debe verificar en las celdas de notebook antes de atribuir técnicas concretas.

### Inventario técnico de implementación

- **Extiende:** consultas Scopus con un criterio de producción sostenida desde
  2020.
- **Reutiliza:** base relacional, búsqueda y salidas CSV de la secuencia SQL.

### Relación técnica con actividades anteriores

Añade una condición longitudinal al patrón de concentración de P504–P505. Sin
P506 se pierde el tratamiento explícito de continuidad temporal en el caso.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Pregunta y entrega | `submission/questions.json`, `sustained_authors.csv` | explícita | Consulta concreta sin extraer. |
| Datos | `data/scopus_proptech.db`, `search_string.txt` | estructural | Procedencia externa no narrada. |
| Capacidades `data.C01`–`data.C03`, `data.C05` | `traceability.yaml` | explícita | Alineación pendiente. |

## Auditoría de Analytics

El criterio de producción sostenida se usa para producir evidencia temporal
sobre un dominio; SQL cumple una función habilitadora.
