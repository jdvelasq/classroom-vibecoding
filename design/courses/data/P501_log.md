# Log — P501

## S01.P501.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `professor/main.py`, `data/`, `submission/`, pruebas y
  `traceability.yaml`.
- **Decisión:** se creó el mapa; se dejó como límite la falta de una secuencia
  explícita de trabajo estudiantil.
- **Trazabilidad:** `data.C02`–`data.C05` revisadas.
- **Auditoría:** las interfaces sostienen un producto analítico de consulta.

## S02.P501.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P501_superstore_serving/` (`data/superstore_orders.csv`, `professor/main.py`, `src/main.py`, `submission/sales_detail.csv`, `submission/serving_manifest.csv`, `submission/questions.json`, `submission/sales_serving.db` —binario, descrito desde el código—, `tests/test_activity.py`).
- **Trazabilidad revisada:** P501 → `data.C02`–`data.C05`; `data.C03` sin evidencia.
- **Preservado:** pregunta, tres representaciones, manifiesto con grano/consumidor/propósito, relación de extensión con P500.
- **Corregido / añadido:** se registró que P501 no ejecuta validaciones (P500 sí), que la agregación mensual está duplicada en código y que los consumidores del manifiesto no existen en la implementación; las pruebas sólo comprueban existencia.
- **Highlights añadidos:** H01 (representaciones de grano distinto), H02 (manifiesto de interfaces), H03 (trazabilidad de línea; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** `sales_detail.csv` publica texto mal decodificado (`Accentâ¢`) por la lectura `latin1` de un archivo con BOM UTF-8; `data.C03` mapeada sin evidencia; sin procedencia del CSV; `src/main.py` sin instrucciones.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P500; habilita nombres y granos que P502 cataloga.
- **Auditoría de Analytics:** capacidad de datos para preguntas descriptivas; riesgo moderado de lectura como *serving* de ingeniería de datos.
