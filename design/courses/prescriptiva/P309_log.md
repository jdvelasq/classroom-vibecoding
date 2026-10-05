# Log — P309

## S02.P309.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P309_covid_hospital_capacity/` (`data/` tres CSV, `professor/main.py`, `professor/notebook.ipynb`, `submission/` seis artefactos, `tests/test_activity.py`; `src/` sólo `.gitkeep`; notebook de estudiante sin celdas).
- **Trazabilidad revisada:** P309 → `prescriptiva.C02`, `C03`, `C04`, `C05`. Sostenidas; C05 sólo declarativa.
- **Highlights añadidos:** H01–H07 (demora acción–efecto; trayectorias completas como unidad; enumeración fecha × tamaño; compromiso D04–D06; riesgo residual; gatillo de escalamiento desde sensibilidad; política en `main.py`).
- **Ambigüedades:** el notebook importa `main` desde `../src`, pero `main.py` está en `professor/` y `src/` está vacío (mismo patrón en P300, P303, P307 y P310–P312). El paso `escalamiento_contingente` repite `activation_day` 5 y `available_day` 9 aunque depende de una revisión diaria posterior. El gatillo 0.30 es la única variante probada; no se calcula umbral de indiferencia. «Probabilidad revisada» no tiene mecanismo de actualización. Sin procedencia de datos.
- **Superficies / contrato / dependencias:** S01–S05; pruebas verifican columnas y acciones, no cálculos; recibe práctica de P307 y P304; habilitación posterior no evidenciada.
- **Auditoría de Analytics:** producto = política de capacidad de dos pasos con autoridad clínica, salvaguardas, cadencia diaria y monitoreo. La evaluación por escenarios sirve a la regla; identidad prescriptiva preservada con los límites registrados.

## S03.P309.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P309.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P309.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
