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

## S03.P501.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PR-Communication (p. 106: «Produce a technical document for colleagues to guide technical development») — ya cubierta: manifiesto de interfaces (H02). El texto mal decodificado (H03) se resuelve por la candidata P500.

## S03.P501.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P501.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
