# P203 — Clasificación básica de texto

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P203_clasificacion_basica_texto/`.

### Preguntas analíticas actuales

- ¿Cómo podemos anticipar si una frase de una noticia financiera comunica una señal positiva, negativa o neutral?

Usa frases financieras etiquetadas, reserva una muestra estratificada, construye
una matriz documento–término con `CountVectorizer` y ajusta regresión logística.
Entrega clasificador, vectorizador y métricas de prueba.

### Inventario técnico de implementación

- **Reutiliza:** representación textual introducida en P202, ahora mediante un vectorizador entrenado sólo en train.
- **Introduce:** clasificación multiclase de texto, accuracy balanceada, macro F1 y matriz de confusión.
- **Introduce:** serialización de modelo, vectorizador y métricas.

### Relación técnica con actividades anteriores

Extiende P202: transforma preparación textual en producto predictivo. Sin P203
se pierde la conexión entre vocabulario, clasificación y evaluación por clase.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook, datos, artefactos, pruebas y `traceability.yaml` sustentan
`predictiva.C01`, `C02` y `C04`. El producto es una estimación de sentimiento,
no una decisión financiera automatizada.
