# P202 — Tokenización

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P202_tokenizacion/`.

### Preguntas analíticas actuales

- ¿Cómo preparamos los abstracts de Scopus para identificar términos distintivos sin que textos vacíos, fórmulas retóricas y avisos de copyright distorsionen la representación?

Procesa abstracts comprimidos, excluye ausencias y textos breves, elimina avisos
editoriales y preserva abstracts tokenizados, vocabulario y matriz documento–término.

### Inventario técnico de implementación

- **Introduce:** limpieza textual basada en evidencia, expresiones regulares y normalización.
- **Introduce:** representación documento–término y artefactos matriciales persistentes.

### Relación técnica con actividades anteriores

Introduce preparación de texto necesaria para P203; no es aún un clasificador.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook, datos, matriz y vocabulario en `submission/`, pruebas y
`traceability.yaml` sustentan `predictiva.C02`.
