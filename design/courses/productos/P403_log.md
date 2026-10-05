# Log — P403

## S02.P403.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P403_model_testing_pytest/` (`ESTIMATOR.pkl` como binario, `data/model_test_set.csv`, `professor/main.py`, `professor/notebook.ipynb`, `professor/test_main.py`, `src/main.py`, `submission/model_test_report.json`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P403 → `productos.C02`, `productos.C03`, `productos.C05`. C03 sostenido; C05 indirecto.
- **Highlights:** añadidos H01 (artefacto congelado), H02 (compuerta de umbrales), H03 (familias de pruebas en notebook), H04 (caso y datos: clase asimétrica y objetivo sin semántica).
- **Ambigüedades:** significado de `target` y procedencia de modelo y datos no documentados (los nombres de variables coinciden con los del conjunto Breast Cancer Wisconsin, sin que la implementación lo declare); umbrales sin justificación; reporte persistido de `main.py` distinto del notebook; las pruebas de interfaz y reproducibilidad no están en `pytest`.
- **Superficies / contrato / dependencias:** S01–S06; habilita P404 (mismo artefacto y filas).
- **Auditoría de Analytics:** resuelta con reservas: habilitación de un modelo, sin usuario ni semántica del producto.

## S03.P403.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).

## S03.P403.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P403.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Perform business validation of the analytics solution» y secciones del «business validation report» (p. 22, CAP-E.6.1.1, 6.2.1) — fuera de alcance en su sentido pleno: la validación de negocio del método pertenece a los cursos de origen (el curso «no vuelve a … predecir ni prescribir»); la compuerta operativa de habilitación ya es P403 H02.
  - «Identify a potential ethical analytics risk» (p. 22, CAP-E.6.1.2) — marginal: reconocimiento genérico; la salvaguarda operativa ya está en la revisión humana (P450 H01–H02).
