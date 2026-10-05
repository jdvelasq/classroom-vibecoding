# Log — P418

## S02.P418.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P418_container/` (`Dockerfile`, `.dockerignore`, `HOW_TO_RUN_ME.txt`, `requirements.txt`, `data/daily_operations.csv`, `professor/main.py`, `src/main.py`, `submission/factory_report.json`, `tests/test_activity.py`); digests de P412 y P426.
- **Trazabilidad revisada:** P418 → `productos.C02`, `productos.C05`; C05 sin evidencia.
- **Highlights:** añadidos H01 (imagen que fija intérprete, dependencia, datos y código) y H02 (salida por volumen y datos incrustados; caso y datos).
- **Ambigüedades:** no hay evidencia de que `factory_report.json` se haya producido dentro del contenedor; sin prueba del contenedor. El `src/main.py` que copia la imagen es una plantilla sin resolver.
- **Superficies / contrato / dependencias:** S01–S04; recibe de P412; habilita P426 (patrón Dockerfile).
- **Auditoría de Analytics:** no resuelta; introducción a contenedores sobre un indicador trivial.

## S03.P418.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
