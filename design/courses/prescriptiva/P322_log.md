# Log — P322

## S02.P322.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/` (`data/decision_scenarios.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, tres artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P310 y P311.
- **Trazabilidad revisada:** P322 → `prescriptiva.C01`, `C03`, `C04`, `C05`. Sustentadas; C03 sin sensibilidad.
- **Highlights:** añadidos H01–H03. H01 es el highlight obligatorio de caso y datos (estado desfavorable más probable y con pérdida grande). Valores 10.000 y 31.300 de `information_value.csv` (verificados con los datos: 0,45 × 120.000 − 0,55 × 80.000 = 10.000; 0,45 × 0,85 × 120.000 − 0,55 × 0,15 × 80.000 − 8.000 = 31.300).
- **Ambigüedades:** (1) la razón persistida de «lanzar ahora» dice que expone a «una pérdida esperada», pero su valor esperado es +10.000; la conclusión (medir antes es mejor) se sostiene por la comparación, no por esa razón; (2) decisiones y razones están escritas en el código y no dependen de los valores calculados; (3) precisión simétrica y sin valor de información perfecta; (4) el notebook presencial sólo llama a `main()`; (5) la prueba sólo verifica presencia de archivos.
- **Superficies / contrato / dependencias:** S01–S05 declaradas. Recibe de P310/P311 la práctica de escenarios con probabilidad.
- **Auditoría de Analytics:** producto terminal = política de medición con regla por resultado, guardas, autoridad y gatillos. Auditoría resuelta, con el defecto de la razón persistida.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P322.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Infer the value to an organization of undertaking a particular investigation», «Argue the case for what data an organization should routinely gather» y «Evaluate the costs associated with the automation of a particular activity» (PR-Economic, p. 106). Categoría: ya cubierta por el valor de medir antes de actuar y las guardas de costo y precisión de la medición (H01–H03).

## S03.P322.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P322.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
