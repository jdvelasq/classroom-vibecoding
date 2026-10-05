# Log — P411

## S02.P411.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P411_pull_request/` (`HOW_TO_RUN_ME.txt`, `data/repository_template/.gitkeep`, `data/pull_request_case.bundle` como binario, `submission/git_log.txt`, `tests/test_activity.py`); evidencia de P410 y HOW_TO de P415.
- **Trazabilidad revisada:** P411 → `productos.C01`, `productos.C04`. C04 parcial (autorrevisión).
- **Highlights:** añadidos H01 (pull request), H02 (caso y datos: responsable en el contrato del producto), H03 (evidencia divergente del flujo instruido).
- **Ambigüedades:** la evidencia persistida (`merge: add product owner`, `chore: create product card` con hash `4d8becc`) no coincide con lo que produciría la secuencia instruida ni con el hash de P410; uso del `.bundle` no documentado; dependencia de rutas hermanas en la distribución.
- **Superficies / contrato / dependencias:** S01–S04; recibe de P410; habilita P415.
- **Auditoría de Analytics:** resuelta con reservas: gobernanza mínima de la definición del producto mediante práctica GitHub.

## S03.P411.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P411.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
