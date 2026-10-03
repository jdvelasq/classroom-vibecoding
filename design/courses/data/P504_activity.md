# P504 — SQL básico sobre Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P504_scopus_sql_basico/`.

### Preguntas analíticas actuales

- ¿Qué documentos de proptech se publicaron desde 2020?
- ¿Qué tipos de documento componen el resultado de la búsqueda?

Usa la base
`data/scopus_proptech.db` y preserva la cadena de búsqueda. Las entregas son
`documents_recent.csv` y `documents_by_type.csv`.

La evidencia disponible muestra práctica de consulta SQL para filtrar y
agregar un corpus bibliográfico; los notebooks de profesor y estudiante son
parte de la implementación. Las pruebas y entregables hacen observable el
resultado de las consultas, no el dominio general de SQL fuera de este caso.

### Inventario técnico de implementación

- **Introduce:** consultas SQL de filtrado temporal, conteo y agrupación sobre
  la base relacional Scopus.
- **Reutiliza:** cadena de búsqueda y base construida en P503.

### Relación técnica con actividades anteriores

Extiende P503 al ejercitar consultas sobre su representación relacional. Sin
P504 se pierde el primer uso explícito de SQL para responder preguntas del caso.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Preguntas y archivos de respuesta | `submission/questions.json` | explícita | Falta inventario detallado de consultas del notebook. |
| Fuente bibliográfica y búsqueda | `data/scopus_proptech.db`, `search_string.txt` | estructural | La procedencia original no está narrada localmente. |
| Capacidades `data.C02`, `data.C05` | `traceability.yaml` | explícita | Revisión de alineación pendiente. |

## Auditoría de Analytics

SQL sirve para producir evidencia sobre producción bibliográfica; la actividad
se orienta a preguntas y entregables analíticos, no a un temario de SQL.
