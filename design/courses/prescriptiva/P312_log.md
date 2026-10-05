# Log — P312

## S02.P312.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P312_sensibilidad_y_tradespace/` (`data/service_options.csv`, `professor/main.py`, `professor/notebook.ipynb`, `submission/` tres artefactos, `tests/test_activity.py`; `src/` sólo `.gitkeep`).
- **Trazabilidad revisada:** P312 → `prescriptiva.C03`, `C05`. Sostenidas; hay evidencia de `C04` no mapeada.
- **Highlights añadidos:** H01 (sensibilidad que localiza el cambio de decisión), H02 (umbral de equilibrio como gatillo), H03 (opción no seleccionada; caso/datos con límite).
- **Ambigüedades:** «tradespace» con un solo criterio; salvaguarda menciona un intervalo de incertidumbre que no se calcula; `REVIEW_RETENTION_GAIN` definida y no usada; presupuesto igual al costo de P2; multiplicador común a todas las opciones. Sin procedencia. `src/` sin `main.py`.
- **Superficies / contrato / dependencias:** S01–S04; pruebas sólo de existencia; recibe forma del registro de P311; habilitación no evidenciada.
- **Auditoría de Analytics:** producto = regla mensual con umbral de revisión, autoridad y monitoreo; el análisis de sensibilidad contribuye. Identidad preservada con límites registrados.

## S03.P312.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P312.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P312.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P312.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - supuestos implícitos y cómo verificarlos (p. 11: CAP-P.2.3.1–2.3.2) — ya cubierta: P312 H02 convierte el supuesto crítico en umbral de revisión; P309 H06 deriva el gatillo de una sensibilidad.
