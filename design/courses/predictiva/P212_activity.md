# P212 — Tiempo hasta abandono

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P212_tiempo_hasta_abandono/`.

### Preguntas analíticas actuales

- ¿Cuánto tiempo es esperable que permanezca un cliente?
- ¿Cómo difiere la permanencia estimada por tipo de contrato?

Con datos de abandono de clientes de telecomunicaciones, estima curvas de
supervivencia, retención por contrato, supuestos y una visualización.

### Inventario técnico de implementación

- **Introduce:** estimación Kaplan–Meier, conjunto en riesgo, eventos y censura.
- **Introduce:** curvas de supervivencia segmentadas y cálculo de retención a un
  horizonte.
- **Verifica y comunica:** exporta curvas, gráfico, retención y supuestos; las
  pruebas comprueban la evidencia persistente.

### Relación técnica con actividades anteriores

Extiende los pronósticos puntuales de P210–P211 hacia tiempo hasta evento e
incorpora censura. Sin P212 se pierde la distinción entre predecir una etiqueta
y estimar permanencia durante un horizonte.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

La actividad responde a una pregunta predictiva de permanencia; elegir una
oferta de retención es una decisión prescriptiva fuera de su alcance. La entrada
P212 de `traceability.yaml` mapea `predictiva.C01`–`C04`.
