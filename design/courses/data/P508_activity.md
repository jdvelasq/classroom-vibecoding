# P508 — Entrega de Scopus con SQLAlchemy

## Actividad actual implementada

**Implementación:** `implementation/data/P508_scopus_sqlalchemy/`.

### Preguntas analíticas actuales

- ¿Qué fuentes concentran documentos de proptech publicados desde 2020?

Usa la base Scopus local y entrega `recent_sources.csv` y
`scopus_delivery.db`. Notebooks de estudiante y profesor, cadena de búsqueda y
pruebas acompañan el caso.

La evidencia implementada conecta una consulta bibliográfica con un artefacto
de entrega en SQLite. Permite observar una respuesta agregada y una forma de
publicarla; la secuencia y el uso específico de SQLAlchemy requieren inspección
granular de notebooks antes de una afirmación más fuerte.

### Inventario técnico de implementación

- **Extiende:** consulta de fuentes recientes mediante una entrega SQLite.
- **Introduce:** artefacto de delivery `scopus_delivery.db` además del CSV de
  respuesta; el uso específico de SQLAlchemy no está confirmado aún.

### Relación técnica con actividades anteriores

Extiende P504–P507 al empaquetar una respuesta para entrega. Sin P508 se pierde
la transición visible de consulta a artefacto de consumo.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Pregunta, CSV y base de entrega | `submission/questions.json`, `submission/` | explícita | No se infiere la API usada. |
| Datos y búsqueda | `data/` | estructural | Procedencia externa no narrada. |
| Capacidades `data.C01`, `data.C02`, `data.C04`, `data.C05` | `traceability.yaml` | explícita | Alineación pendiente. |

## Auditoría de Analytics

La capa de entrega opera una respuesta a una pregunta bibliográfica; no
convierte la actividad en ingeniería de software independiente.
