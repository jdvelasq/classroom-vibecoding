# Log — P315

## S02.P315.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P315_wildfire_resource_positioning/` (`data/` tres CSV, `professor/notebook.ipynb`, `submission/` siete artefactos, `tests/test_activity.py`; notebook de estudiante sin celdas).
- **Trazabilidad revisada:** P315 → `prescriptiva.C02`, `C03`, `C04`, `C05`. C02/C04 sostenidas; C03 limitada a sensibilidad de recursos; C05 declarativa sobre salidas del modelo.
- **Highlights añadidos:** H01–H05 (tiempo esperado ponderado desde geografía; heurísticas vs. interacción espacial; modelo p-mediana verificado; conjuntos no anidados; reasignación por etapa y monitoreo con umbral).
- **Ambigüedades:** riesgo estático sin escenarios pese a la etapa «validación bajo incertidumbre» de la arquitectura; umbrales 40/60 min no derivados; el monitoreo compara recomputaciones del modelo, no tiempos observados; reasignación no calculada; comparación de heurísticas no persistida. Posible duplicación de plantilla con P305 y P308.
- **Superficies / contrato / dependencias:** S01–S05; las pruebas verifican estructura y coherencia línea base ≤ umbral, no optimalidad; recibe patrón de P305/P308; habilitación no evidenciada.
- **Auditoría de Analytics:** producto = política de posicionamiento con reasignación gobernada, autoridad y monitoreo; la localización óptima contribuye. Identidad preservada; validación bajo incertidumbre ausente.

## S03.P315.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Algorithms for combinatorial optimization problems», «Use common algorithms … (e.g., Branch and Bound algorithms)», max-flow, «Heuristic optimization techniques» y «Implement Dynamic Programming solutions» (PDA-Algorithms, pp. 115–116). Categoría: ya cubierta en el uso (mochila P305 H03, asignación P308 H04, localización P315 H03, flujo LP P316 H05, heurísticas como línea base P316 H03). Implementar B&B o DP es fuera de alcance: `s05-diseno-prescriptiva.md` excluye la implementación de solvers.
