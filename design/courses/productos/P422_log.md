# Log — P422

## S02.P422.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P422_model_monitoring/` (`data/reference.csv`, `data/production.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/monitoring_report.json`, `tests/test_activity.py`, `requirements.txt`); digests de P404, P420, P423.
- **Trazabilidad revisada:** P422 → `productos.C02`, `C03`, `C05`; C03 y C05 sustentados.
- **Highlights:** añadidos H01 (señal de deriva por variable), H02 (desplazamiento concentrado en un caso construido; caso y datos) y H03 (exclusión de la etiqueta).
- **Ambigüedades:** procedencia de `production.csv` no documentada (filas repetidas, enteros en `alcohol`). No se carga modelo pese al nombre. Las pruebas usan `quality` como variable, que `main()` excluye. Solapamiento conceptual con P404. Sin `HOW_TO_RUN_ME.txt`.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P420 (dominio) y P404 (patrón); habilita: no evidenciada.
- **Auditoría de Analytics:** parcialmente resuelta; vigila insumos sin usuario ni modelo.

## S03.P422.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ML-General (p. 97: «Explain how to efficiently transition a model into production») — ya cubierta: seguimiento, registro, monitoreo y reversión.

## S03.P422.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 7.1 «Track analytics solution performance» (p. 7) — ya cubierta: monitoreo de entradas (P422 H01) y de desempeño (P423 H01). La única brecha material, el origen del umbral, queda en la candidata P423.

## S03.P422.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify the metrics that monitor analytics solution performance» (p. 24, CAP-E.7.1.1) — ya cubierta: P422 H01 (señal por variable de entrada), P423 H01–H02 (desempeño observado frente a mínimo), P445 H01–H02 (disponibilidad frente a meta).

## S03.P422.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Temario del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con tareas y subtareas evaluables (pesos: Deployment 10 %, Lifecycle Management 9 %). Sólo los dominios VI–VII y algunas subtareas de III (linaje, gobierno, calidad) tocan la operación de capacidades. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
