# Log — P425

## S02.P425.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P425_api_contract/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/score_examples.json`, `tests/test_activity.py`); digests de P400, P423, P426 y búsqueda de «risk» en P430–P455.
- **Trazabilidad revisada:** P425 → `productos.C02`, `C04`, `C05`; C05 sin evidencia; C01 evidenciada pero no mapeada.
- **Highlights:** añadidos H01 (contrato con errores explicables), H02 (ejemplos ejecutados) y H03 (regla de umbral sin procedencia; caso y datos).
- **Ambigüedades:** umbral 4500 sin origen; las cuatro filas de `daily_operations.csv` serían `low`. La validación admite negativos y booleanos. `tests/test_activity.py` no verifica contenido. Vocabulario «factory risk» recurrente en P430–P452 sin artefacto común.
- **Superficies / contrato / dependencias:** S01–S05; recibe: ninguna; habilita P426 (lógica copiada).
- **Auditoría de Analytics:** parcialmente resuelta; mecanismo de la línea sobre una regla arbitraria.

## S03.P425.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM (p. 122: «Not checking input») — ya cubierta: P425 H01 contrato con errores explicables.

## S03.P425.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
