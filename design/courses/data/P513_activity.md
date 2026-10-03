# P513 — Ingestión batch Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P513_superstore_batch/`.

### Preguntas analíticas actuales

- No se localizó una pregunta analítica persistente; la evidencia implementada se centra en la ingestión de dos lotes trimestrales.

Los CSV de Superstore se separan por trimestre y el material de profesor los
convierte a Parquet en una zona raw, produciendo `ingestion_report.csv`.

### Inventario técnico de implementación

- **Introduce:** descubrimiento ordenado de lotes, lectura con contrato de
  formato y escritura Parquet de zona raw.
- **Introduce:** reporte de filas, estado y ruta por lote.

### Relación técnica con actividades anteriores

Introduce una práctica de ingestión batch que no aparece en P511–P512. Sin
P513 se pierde evidencia de manejo de entregas múltiples y reporte operativo.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

`source_manifest.json`, `professor/main.py`, reporte y pruebas sustentan el
mapa. `traceability.yaml` asigna `data.C02`–`data.C05`; falta una pregunta
analítica explícita que conecte la ingestión con un producto de Analytics.

## Auditoría de Analytics

La identidad permanece incompleta hasta explicitar qué análisis habilita la
ingestión; se registra como límite, no se inventa.
