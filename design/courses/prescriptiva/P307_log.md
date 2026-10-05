# Log — P307

## S02.P307.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P307_decision_informada_por_pronosticos/` (tres archivos de `data/`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, tres CSV de `submission/`, `tests/test_activity.py`); relación con P300, P302 y P304.
- **Trazabilidad revisada:** P307 → `prescriptiva.C01`–`C05`; C01 parcial, C02 sustentada, C03 y C05 no evidenciadas, C04 mínima.
- **Highlights:** añadidos H01–H04 (escenarios y gobierno como datos; valor y quiebre; guardia antes de maximizar; política persistida).
- **Ambigüedades:** (1) la guardia de servicio no cambia la decisión: 110 es también el máximo sin restricción y está en el borde (0,25); (2) `order_comparison.csv` en `submission/` no lo produce el código actual; (3) notebook de dos celdas sin evidencia visual, importando `main` desde `src/` vacío; (4) no hay pronóstico construido: el título «informada por pronósticos» descansa en escenarios dados; (5) trazabilidad a cinco capacidades excede la evidencia; (6) posible duplicación técnica con P300/P302 y solapamiento con P304.
- **Superficies / contrato / dependencias:** S01–S05; pruebas de forma; recibe patrón de P300/P302; no habilita actividades posteriores.
- **Auditoría de Analytics:** auditoría no resuelta para el producto prescriptivo completo: hay acción factible, guardia, dueño, cadencia y gatillo, pero faltan excepción, validación (líneas base, sensibilidad) y monitoreo de resultados.

## S03.P307.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
