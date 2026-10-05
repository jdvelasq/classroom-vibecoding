# Log — P427

## S02.P427.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P427_secret_config/` (`HOW_TO_RUN_ME.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/secret_config_report.json`, `tests/test_activity.py`, `data/`); digests de P406, P407, P425, P426, P452.
- **Trazabilidad revisada:** P427 → `productos.C02`, `C04`, `C05`; C04 y C05 sólo en el mecanismo.
- **Highlights:** añadidos H01 (credencial separada de código y evidencia) y H02 (falla explicable; caso y datos ausentes como límite).
- **Ambigüedades:** la clave no se usa para nada; no se conecta con la API de P425–P426 ni con P452. Ninguna prueba verifica que el valor no aparezca en el reporte.
- **Superficies / contrato / dependencias:** S01–S04; recibe prácticas de P406–P407; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; práctica genérica de software.

## S03.P427.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
