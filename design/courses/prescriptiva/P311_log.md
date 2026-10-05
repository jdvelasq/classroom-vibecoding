# Log — P311

## S02.P311.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/` (`data/` dos CSV, `professor/main.py`, `professor/notebook.ipynb`, `submission/` dos artefactos, `tests/test_activity.py`; `src/` sólo `.gitkeep`).
- **Trazabilidad revisada:** P311 → `prescriptiva.C03`, `C04`, `C05`. C04/C05 sostenidas (C05 declarativa); C03 parcial.
- **Highlights añadidos:** H01 (tres guardas simultáneas), H02 (meta promedio vs. por escenario; caso/datos), H03 (selección por menor costo y autoridad diferenciada).
- **Ambigüedades:** el nombre «evaluación por simulación» y el rol «prueba de política» de `activity-architecture.md` no corresponden a la implementación, que calcula esperanzas exactas sobre cuatro escenarios. Posible duplicación con P307 (mismo cálculo con otra guarda). Gatillos y límites sin derivación. Sin procedencia. `src/` sin `main.py`.
- **Superficies / contrato / dependencias:** S01–S05; pruebas sólo de existencia; recibe patrón de P307; habilitación no evidenciada.
- **Auditoría de Analytics:** producto = regla diaria de capacidad con servicio, riesgo y presupuesto, autoridad y gatillos. Identidad prescriptiva preservada; aporte metodológico frente a P307 no distinguible.

## S03.P311.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P311.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P311.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
