# P505 — SQL intermedio sobre Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P505_scopus_sql_intermedio/`.

### Preguntas analíticas actuales

- ¿Qué autores concentran más documentos sobre proptech?
- ¿Qué fuentes concentran más documentos sobre proptech?

Sobre `data/scopus_proptech.db` y la cadena de búsqueda preservada,
Sus entregables son `authors_by_documents.csv` y `sources_by_documents.csv`.
La implementación incluye notebooks de estudiante y profesor y pruebas.

La práctica diseñada usa consultas SQL para agrupar y ordenar evidencia
bibliográfica. Los entregables hacen observable la respuesta agregada, pero la
procedencia original del extracto no está explicada más allá de los archivos
locales.

### Inventario técnico de implementación

- **Extiende:** agregación SQL del caso Scopus hacia concentraciones por autor
  y fuente.
- **Reutiliza:** base relacional y cadena de búsqueda de P503–P504.

### Relación técnica con actividades anteriores

Repite el dominio de P504 pero añade dos perspectivas de concentración. Sin
P505 se pierde esa extensión de agrupación y ordenamiento; la consulta exacta
debe verificarse en notebook antes de una comparación más fina.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Preguntas y entregables | `submission/questions.json` | explícita | Falta extraer el detalle de la secuencia del notebook. |
| Datos y búsqueda | `data/scopus_proptech.db`, `search_string.txt` | estructural | No documenta licencia/procedencia externa. |
| Capacidades `data.C01`, `data.C02`, `data.C05` | `traceability.yaml` | explícita | Alineación pendiente de auditoría. |

## Auditoría de Analytics

SQL se usa para responder preguntas sobre concentración bibliográfica; no es
un fin disciplinar independiente.
