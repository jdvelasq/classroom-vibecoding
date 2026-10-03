# P507 — SQL analítico sobre Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P507_scopus_sql_analitico/`.

### Preguntas analíticas actuales

- ¿Qué palabras clave están entre las diez más frecuentes por año desde 2020?

Usa la base Scopus local y entrega
`submission/top_keywords_by_year.csv`. Preserva `search_string.txt`, notebooks
de estudiante y profesor y pruebas.

La práctica diseñada combina una condición temporal con conteos por año y
palabra clave para producir una respuesta reproducible. El resultado muestra
la evidencia esperada, pero no basta por sí solo para afirmar qué construcciones
SQL específicas domina el estudiante.

### Inventario técnico de implementación

- **Extiende:** agregación temporal por año y ranking de palabras clave dentro
  de cada período.
- **Reutiliza:** corpus y base relacional de la secuencia Scopus.

### Relación técnica con actividades anteriores

Añade una dimensión textual y ranking temporal. Sin P507 se pierde esa forma de
descripción anual; el detalle SQL sigue pendiente de validación granular.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Pregunta y respuesta anual | `submission/questions.json`, `top_keywords_by_year.csv` | explícita | Consulta detallada pendiente de lectura. |
| Datos de búsqueda | `scopus_proptech.db`, `search_string.txt` | estructural | Sin procedencia externa explícita. |
| Capacidades `data.C01`–`data.C03`, `data.C05` | `traceability.yaml` | explícita | Alineación pendiente. |

## Auditoría de Analytics

La actividad produce una descripción temporal del corpus; las técnicas de
consulta son medios para ese producto analítico.
