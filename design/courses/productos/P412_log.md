# Log — P412

## S02.P412.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P412_repro_environment/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `data/daily_operations.csv`, `professor/main.py`, `src/main.py`, `submission/environment_report.json`, `tests/test_activity.py`, `tests/test_environment_report.py`); `structure-audit.md`; P400 para comparación.
- **Trazabilidad revisada:** P412 → `productos.C02`, `productos.C05`. C05 débil.
- **Highlights:** añadidos H01 (ambiente aislado), H02 (procedencia de ejecución), H03 (prueba de regresión), H04 (caso y datos: indicador fijo de referencia y contrato de salida inestable).
- **Ambigüedades:** `requirements.txt` local no registrado como excepción en `structure-audit.md` y compatibilidad con la raíz no verificable; Python 3.9.6 en la evidencia sin versión de referencia del repositorio; docstrings descriptivos frente a la regla de claridad de `AGENTS.md`; columna `total_units_produced` frente a `total_units` de P400; la prueba sobrescribe `submission/`.
- **Superficies / contrato / dependencias:** S01–S07; recibe de P400; habilita P413–P414.
- **Auditoría de Analytics:** resuelta con reservas: reproducibilidad de un indicador real del curso, pero trivial.

## S03.P412.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).

## S03.P412.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
