# P215 — Recomendación mediante Apriori

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P214_recomendacion_apriori/`.

### Preguntas analíticas actuales

- Dada una canasta parcial con fruta tropical y yogur, ¿qué producto es probable que complete esa misma canasta?
- ¿La confianza de la regla se sostiene en transacciones no usadas para encontrarla?

Usa canastas de compras para generar itemsets frecuentes, reglas de asociación,
recomendaciones y validación sobre un segmento retenido.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima qué ítem puede completar una canasta parcial; no hay decisión comercial ni usuario operativo definidos.
- **Producto terminal:** reglas, recomendaciones y confianza evaluada en canastas retenidas.
- **Uso y límite:** asociación condicional no demuestra que recomendar produzca una compra adicional.
- **Disciplinas contribuyentes:** minería de reglas sirve a una predicción condicional de Analytics.

### Highlights de contribución

- **H01 — Conserva la unidad transaccional:** cada fila se recupera como canasta completa de longitud variable; así soporte y coocurrencia no se reducen a columnas fijas.
- **H02 — Separa descubrimiento y comprobación:** reserva el 20% de canastas antes de construir itemsets y reglas.
- **H03 — Distingue frecuencia de señal condicional:** usa soporte, confianza y lift para recomendar consecuentes de `{tropical fruit, yogurt}`.
- **H04 — Verifica la misma confianza fuera del entrenamiento y persiste reglas, recomendaciones y métricas.**

### Inventario técnico de implementación

- **Introduce:** Apriori, itemsets de pares y ternas, soporte, confianza y lift.
- **Introduce:** evaluación de confianza en canastas retenidas y métricas de la
  brecha de confianza.
- **Verifica y comunica:** exporta distribución de canasta, reglas, itemsets,
  recomendaciones, métricas y supuestos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Canastas variables | H01 | CSV gzip y recuperación de transacciones | No hay contexto comercial documentado. |
| Regla retenida | H02–H04 | Apriori, soporte/confianza/lift y held-out confidence | Asociación no es efecto comercial. |

### Relación técnica con actividades anteriores

P215 cambia el pronóstico por cliente o período por una predicción condicional
dentro de una transacción. Sin P215 se pierde la relación entre patrón de
coocurrencia, evidencia retenida y recomendación de ítem.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook; `groceries_baskets.csv.gz` | Procedencia no documentada. |
| H02 | S02 | Notebook: split 80/20 | Segmento retenido no es aleatorio explícitamente. |
| H03 | S02 | Notebook; reglas/recomendaciones CSV | Lift no prueba causalidad. |
| H04 | S03, S04 | Métricas/entregas; pruebas | Tests sólo comprueban archivos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Canastas/dataset | Datos; notebook | Unidad es transacción completa. |
| S02 | Apriori/reglas | Notebook; reglas | No convertir asociación en intervención. |
| S03 | Validación/producto | Métricas/recomendaciones | Confianza retenida, no uplift. |
| S04 | Entregas/pruebas | `submission/`; tests | Presencia de archivos. |

### Contrato de evidencia actual

- **Código:** explora canastas, divide, descubre reglas y contrasta confianza retenida.
- **`submission/`:** conserva itemsets, reglas, recomendaciones, métricas y figuras.
- **Pruebas:** verifican artefactos, no cálculos.
- **Trazabilidad:** P215 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de P214:** predicción condicionada y evaluación retenida, sin código común.
- **Habilita para P216:** contraste entre coocurrencia de ítems y afinidad colaborativa.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Una asociación no demuestra que recomendar cause una compra adicional. La
entrada P215 de `traceability.yaml` mapea `predictiva.C01`–`C04`.
