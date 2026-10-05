# Log — P415

## S02.P415.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P415_github_actions/` (`HOW_TO_RUN_ME.txt`, `data/repository_template/` con `quality.yml`, `src/main.py`, `tests/test_environment_report.py`, `requirements.txt`, datos; `submission/git_log.txt`; `tests/test_activity.py`); digests de P411, P412 y P416.
- **Trazabilidad revisada:** P415 → `productos.C02`, `productos.C05`; C05 indirecto.
- **Highlights:** añadidos H01 (fusión condicionada a check remoto) y H02 (continuidad del repositorio y la prueba; caso y datos con ausencia de particularidad del dato declarada).
- **Ambigüedades:** el digest muestra sólo la cabecera de `quality.yml`; los pasos del flujo se describen desde `HOW_TO_RUN_ME.txt`. El log persistido no demuestra que el check fuera verde. La equivalencia de la prueba con P412 se infiere de nombre y propósito.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P411 (repositorio) y P412 (prueba); habilita P416 (copia de `temp/github_actions_case`).
- **Auditoría de Analytics:** no resuelta; lectura como capacitación en GitHub Actions sobre un indicador trivial.

## S03.P415.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P415.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P415.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
