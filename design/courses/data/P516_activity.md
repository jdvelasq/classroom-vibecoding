# P516 — Calidad de datos tributarios Vermont

## Actividad actual implementada

**Implementación:** `implementation/data/P516_vermont_calidad/`.

### Preguntas analíticas actuales

- ¿Puede este extracto tributario usarse para analizar ingresos por código postal sin confundir agregados estatales?

Usa `vermont.csv` y publica `quality_report.csv` con reglas de completitud,
dominio, unicidad, no negatividad y alcance; código postal 0 representa total
estatal y exige revisión.

### Inventario técnico de implementación

- **Introduce:** perfilado de calidad y reglas expresadas como hallazgos.
- **Introduce:** clave `(zipcode, agi_stub)` y tratamiento explícito de total
  estatal como riesgo de alcance.

### Relación técnica con actividades anteriores

Introduce calidad como condición de uso analítico, no como transformación de
Superstore. Sin P516 se pierde la capacidad de decidir si un extracto es apto.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

Notebook, CSV, prueba y `traceability.yaml` (`data.C01`, `data.C03`, `data.C04`)
sustentan el mapa.

## Auditoría de Analytics

Las reglas deciden si se puede responder una pregunta de ingresos; calidad
sirve a evidencia analítica.
