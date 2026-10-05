# Log — P426

## S02.P426.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P426_api_container/` (`Dockerfile`, `.dockerignore`, `HOW_TO_RUN_ME.txt`, `requirements.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/score_response.json`, `tests/test_activity.py`); digests de P418, P425; `structure-audit.md` (manifiesto local).
- **Trazabilidad revisada:** P426 → `productos.C02`, `C04`, `C05`; C05 sin evidencia.
- **Highlights:** añadidos H01 (servicio en contenedor frente al lote de P418) y H02 (borde 4500 y estrictez de tipo; caso y datos con regla sin procedencia).
- **Ambigüedades:** el docstring afirma que el contenedor entrega la misma decisión, pero las pruebas no ejecutan el contenedor. Lógica duplicada de P425. La plantilla `src/main.py` no expone el `app` que espera el `CMD` del `Dockerfile`, y las instrucciones no lo indican.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P425 y P418; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; despliegue con herramienta sobre regla arbitraria.

## S03.P426.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P426.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P426.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
