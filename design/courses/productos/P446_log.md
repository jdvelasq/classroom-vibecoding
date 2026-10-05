# Log — P446

## S02.P446.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P446_runbook/` (`RUNBOOK.md`, `data/incident.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/freshness_alert_runbook.md`, `tests/test_activity.py`); contexto de P439, P442, P447.
- **Trazabilidad revisada:** P446 → `productos.C04`, `productos.C05`.
- **Highlights:** añadidos H01 (salvaguarda de publicación, caso y datos con límite), H02 (síntoma y rechazo).
- **Ambigüedades:** `data/incident.json` no se lee; numeración `incident-002` antes de `incident-001` en P447; el reporte protegido no se nombra; posible solapamiento con P447.
- **Superficies / contrato / dependencias:** S01–S05; dependencia sólo conceptual con P439.
- **Auditoría de Analytics:** resuelta con límite; salvaguarda sobre publicación de un reporte no identificado.

## S03.P446.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P446.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P446.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify the types of documentation needed for various analytics methodologies» (p. 25, CAP-E.7.6.1) — ya cubierta: runbook (P446 H01–H02), ficha de catálogo (P454 H01), contrato documentado con respuestas ejecutadas (P425 H02).

## S03.P446.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.6.4.2 documentación del modelo y del reporte «so that the analytics solutions can be reused if the business circumstances should change» (p. 23); Task 7.6 y CAP-P.7.6.1 «Identify the types of documentation needed for various audiences» (p. 25) — ya cubierta: ficha operacional (P454 H01–H02), runbook para quien atiende (P446 H01–H02), contrato documentado con respuestas ejecutadas para el consumidor (P425 H02).

## S03.P446.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
