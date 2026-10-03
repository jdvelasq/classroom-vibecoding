# P209 — SIR adaptativo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P209_sir_adaptativo/`.

### Preguntas analíticas actuales

- ¿Cómo cambia el pronóstico epidemiológico cuando la tasa de infección se adapta a la evidencia temporal?

Extiende el caso de casos diarios con evolución adaptativa, pronósticos, tasa de
infección pronosticada, supuestos y picos de escenario.

### Inventario técnico de implementación

- **Extiende:** SIR básico con tasa de infección adaptativa.
- **Introduce:** comparación entre parámetros fijos y evolución temporal del parámetro.

### Relación técnica con actividades anteriores

Extiende P208; sin P209 se pierde la revisión de un supuesto fijo frente a
evidencia cambiante.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, notebooks, artefactos y pruebas sustentan el mapa. P209 no figura en
`traceability.yaml`; se escala la omisión.
