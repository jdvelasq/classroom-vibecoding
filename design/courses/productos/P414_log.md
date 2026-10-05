# Log — P414

## S02.P414.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P414_nox/` (`HOW_TO_RUN_ME.txt`, `noxfile.py`, `requirements.txt`, `data/daily_operations.csv`, `professor/main.py`, `src/main.py`, `submission/report.json`, `tests/test_activity.py`, `tests/test_report.py`); digests de P400, P412, P413 y P416 para relaciones.
- **Trazabilidad revisada:** P414 → `productos.C02`, `productos.C05`; C05 sin evidencia propia.
- **Highlights:** añadidos H01 (sesión Nox que encapsula ambiente y prueba) y H02 (resultado exacto como criterio; caso y datos, con la trivialidad del dato declarada como límite).
- **Ambigüedades:** `tests/test_report.py` ejecuta la plantilla `src/main.py`, que lanza `NotImplementedError`; en la distribución esa prueba falla hasta que el estudiante resuelva. No hay evidencia persistida de que la sesión Nox se ejecutara. Solapamiento P412–P414 sobre el mismo indicador y prueba.
- **Superficies / contrato / dependencias:** S01–S04 declaradas; recibe de P400/P412/P413; habilita P416 (plantilla con `noxfile.py` y `src/main.py` del mismo tamaño).
- **Auditoría de Analytics:** no resuelta; lectura posible como capacitación en herramienta. El indicador no tiene usuario ni decisión dentro del taller.

## S03.P414.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
