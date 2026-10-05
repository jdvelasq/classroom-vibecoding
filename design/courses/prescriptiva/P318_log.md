# Log — P318

## S02.P318.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P318_hydrothermal_planning/` (`data/periods.csv`, `data/hydro.csv`, `data/thermal.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, cinco artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P309, P313, P316, P317 y P319.
- **Trazabilidad revisada:** P318 → `prescriptiva.C02`, `C03`, `C04`, `C05`. C02 y C04 sustentadas; C03 determinista (líneas base y sensibilidad de un parámetro); C05 declarada sin umbrales.
- **Highlights:** añadidos H01–H08. H01 es el highlight obligatorio de caso y datos (filas = períodos ordenados acoplados por el embalse; demanda del período 4 superior a la capacidad térmica). Cifras citadas de `plan_comparison.csv`, cronogramas persistidos y datos; el valor del agua se expresa como producto de datos (10 MWh/hm³ × 90) porque no se persiste en tablas.
- **Ambigüedades:** (1) el cronograma persistido tiene T2 activo en los períodos 1–5 visibles y valor del agua constante, lo que sugiere óptimos alternativos no discutidos; (2) la guarda «no liberar agua que impida cubrir el pico del periodo 4» está escrita para esta instancia y no como regla general; (3) el contrato habla de «despacho diario para los seis periodos» y de «demanda pronosticada», pero los períodos no tienen unidad y el modelo es determinista; (4) regla ingenua, valor del agua y sensibilidad sólo están en el notebook; (5) la prueba no exige `cadence` ni `response_need`; (6) `reservoir_schedule.csv` persiste `-0.0`.
- **Superficies / contrato / dependencias:** S01–S08 declaradas. Recibe de P316 LP continuo y validación sin enumeración. No habilita dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = política de despacho con cadencia, guardas, autoridad, escalamiento y gatillos; LP y duales son evidencia. Auditoría resuelta con límite de guardas específicas de la instancia y monitoreo no cuantificado.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P318.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Markov Decision Processes, «Demonstrate contexts in which MDPs can be useful (e.g., optimization or control problems)» (T2), y Reinforcement Learning (E) (AI, p. 51). Categoría: fuera de alcance. Formalizar MDP o RL convertiría el tramo secuencial en un módulo de IA/IO. La política dependiente del estado ya se ejerce en P304 (H03) y el acoplamiento intertemporal en P318 (H01–H04).

## S03.P318.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
