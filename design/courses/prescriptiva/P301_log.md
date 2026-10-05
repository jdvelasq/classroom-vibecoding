# Log — P301

## S02.P301.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P301_air_france_447/` (`data/search_cells.csv`, `data/search_rounds.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, los cuatro artefactos de `submission/`, `tests/test_activity.py`); contexto en `activity-architecture.md`.
- **Trazabilidad revisada:** P301 → `prescriptiva.C01`; sustentada como contraste (decisión no recurrente).
- **Highlights:** añadidos H01–H06 (frontera excepcional/recurrente; cobertura vs éxito; actualización tras fracaso; repetir vs reasignar; verificación interna; persistencia del protocolo).
- **Ambigüedades:** (1) el nombre AF447 y el mapa titulado «escenario pedagógico AF447» podrían leerse como reconstrucción histórica; el notebook lo niega explícitamente; (2) sólo se observaron cinco filas de `search_cells.csv` en el volcado, aunque las aserciones fijan 25 celdas; (3) autoridad y escalamiento no se ejercen ni registran; (4) el supuesto de efectividad constante al repetir una celda está declarado pero no discutido como límite del plan.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; prueba de existencia de cuatro artefactos; recibe de P300 el formato de frontera de decisión; no habilita artefactos posteriores.
- **Auditoría de Analytics:** el producto es deliberadamente un protocolo excepcional, coherente con el diseño; no debe contarse como política recurrente gobernada. La teoría de búsqueda contribuye sin organizar el taller.

## S03.P301.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Bayesian networks para problemas diagnósticos y la inferencia (AI-Probability-based, p. 51). Categoría: ya cubierta como actualización bayesiana tras un fracaso (H03–H04). Las redes bayesianas como formalismo son fuera de alcance: llevarían el taller hacia IA y no hacia la política.

## S03.P301.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
