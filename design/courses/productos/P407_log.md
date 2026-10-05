# Log — P407

## S02.P407.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P407_config_file/` (`CONFIG.json`, `ESTIMATOR.pkl` y `data/*/sentences.csv.gz` como binarios, `professor/main.py`, `src/main.py`, `submission/metrics.json`, `tests/test_activity.py`); comparación con P406.
- **Trazabilidad revisada:** P407 → `productos.C02`, `productos.C03`, `productos.C05`. C03 y C05 sin evidencia nueva.
- **Highlights:** añadidos H01 (configuración por archivo validada), H02 (caso y datos: caso repetido de P406 como límite).
- **Ambigüedades:** posible duplicación con P406; sin `HOW_TO_RUN_ME.txt` para el estudiante (P406 sí lo tiene); `metrics.json` idéntico al de P406, por lo que la evaluación no distingue el mecanismo.
- **Superficies / contrato / dependencias:** S01–S06; recibe todo el caso de P406.
- **Auditoría de Analytics:** no resuelta: práctica de configuración sin capacidad analítica identificada.

## S03.P407.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
