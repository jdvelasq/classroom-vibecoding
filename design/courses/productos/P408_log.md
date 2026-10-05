# Log — P408

## S02.P408.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P408_version_control/` (`HOW_TO_RUN_ME.txt`, `data/repository_template/product_card.md`, `data/version_control_case.bundle` como binario, `submission/git_log.txt`, `tests/test_activity.py`); `structure-audit.md`.
- **Trazabilidad revisada:** P408 → `productos.C01`, `productos.C02`. C01 mínimo.
- **Highlights:** añadidos H01 (caso y datos: definición del producto versionada), H02 (ciclo revisar–preparar–confirmar).
- **Ambigüedades:** uso del `.bundle` no documentado (posible fuente de la evidencia persistida); identidad Git fija impide atribuir commits; la evidencia no prueba el contenido del cambio.
- **Superficies / contrato / dependencias:** S01–S05; recibe semántica de P400; habilita P409.
- **Auditoría de Analytics:** resuelta con reservas: anclada a `factory_totals`, pero de contenido Git genérico.

## S03.P408.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P408.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
