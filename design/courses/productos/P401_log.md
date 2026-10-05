# Log — P401

## S02.P401.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P401_code_testing_pytest/` (`data/drivers.csv`, `data/timesheet.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/certified_driver_totals.csv`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P401 → `productos.C02`, `productos.C05`. C05 sin evidencia.
- **Highlights:** añadidos H01 (precondición de columnas), H02 (prueba `pytest`), H03 (caso y datos: dos granularidades y atributos sensibles).
- **Ambigüedades:** `drivers.csv` contiene `ssn` y `location` sin documentación de procedencia ni de restricciones de uso; el producto publica `name`. La rama `ValueError` no se prueba. Conteos de filas tomados del número de líneas del digest.
- **Superficies / contrato / dependencias:** S01–S06; evaluación sólo por existencia; recibe la práctica de P400; no habilita una actividad posterior de forma demostrable.
- **Auditoría de Analytics:** no resuelta. Posible duplicación con P400 (misma estructura, distinto marco de pruebas); se lee como entrenamiento en herramienta.

## S03.P401.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DP (p. 84: «Demonstrate awareness about data sensitiveness when data is processed as an input») frente a `ssn`/`location` en `drivers.csv` con exclusión no declarada (H03) — marginal: una aserción de que la salida no propaga `ssn` sería coherente con probar la transformación, pero la práctica de privacidad tiene su lugar en P453; incrustarla en P401 añadiría una segunda contribución a un taller de `pytest`. Si P401 se rediseña, puede retomarse como precondición declarada.
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).

## S03.P401.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P401.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - datos sensibles y uso restringido (p. 13, CAP-E.3.1.2; p. 14, CAP-E.3.3.1) — ya cubierta: P453 H01–H02 (enmascaramiento); el `ssn` de P401 ya es límite registrado por S02.

## S03.P401.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Temario del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con tareas y subtareas evaluables (pesos: Deployment 10 %, Lifecycle Management 9 %). Sólo los dominios VI–VII y algunas subtareas de III (linaje, gobierno, calidad) tocan la operación de capacidades. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
