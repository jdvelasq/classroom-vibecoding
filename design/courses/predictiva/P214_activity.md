# P214 — Recomendación mediante Apriori

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P214_recomendacion_apriori/`.

### Preguntas analíticas actuales

- Dada una canasta parcial con fruta tropical y yogur, ¿qué producto es probable que complete esa misma canasta?
- ¿La confianza de la regla se sostiene en transacciones no usadas para encontrarla?

Usa canastas de compras para generar itemsets frecuentes, reglas de asociación,
recomendaciones y validación sobre un segmento retenido.

### Inventario técnico de implementación

- **Introduce:** Apriori, itemsets de pares y ternas, soporte, confianza y lift.
- **Introduce:** evaluación de confianza en canastas retenidas y métricas de la
  brecha de confianza.
- **Verifica y comunica:** exporta distribución de canasta, reglas, itemsets,
  recomendaciones, métricas y supuestos.

### Relación técnica con actividades anteriores

P214 cambia el pronóstico por cliente o período por una predicción condicional
dentro de una transacción. Sin P214 se pierde la relación entre patrón de
coocurrencia, evidencia retenida y recomendación de ítem.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Una asociación no demuestra que recomendar cause una compra adicional. La
entrada P214 de `traceability.yaml` mapea `predictiva.C01`–`C04`.
