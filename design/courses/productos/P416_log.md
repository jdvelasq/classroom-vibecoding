# Log — P416

## S02.P416.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P416_github_actions_nox/` (`HOW_TO_RUN_ME.txt`, `data/repository_template/` con `tests.yml`, `noxfile.py`, `src/main.py`, `tests/test_report.py`, `requirements.txt`, datos; `submission/git_log.txt`; `tests/test_activity.py`); digests de P414, P415 y búsqueda de reutilización en P417–P455.
- **Trazabilidad revisada:** P416 → `productos.C02`, `productos.C05`; C05 sin evidencia propia.
- **Highlights:** añadidos H01 (paridad local/CI mediante una sesión Nox) y H02 (retiro versionado de la verificación de P415; caso y datos sin particularidad del dato).
- **Ambigüedades:** P416 es composición de P414 y P415 (posible solapamiento). Pasos del flujo descritos sólo en `HOW_TO_RUN_ME.txt`. La cadena de repositorio P408–P416 termina aquí sin consumidor posterior.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P414 y P415; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; capacitación en CI sobre un indicador trivial.

## S03.P416.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
