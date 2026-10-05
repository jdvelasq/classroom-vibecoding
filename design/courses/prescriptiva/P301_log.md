# Log — P301

## S02.P301.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P301_air_france_447/` (`data/search_cells.csv`, `data/search_rounds.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, los cuatro artefactos de `submission/`, `tests/test_activity.py`); contexto en `activity-architecture.md`.
- **Trazabilidad revisada:** P301 → `prescriptiva.C01`; sustentada como contraste (decisión no recurrente).
- **Highlights:** añadidos H01–H06 (frontera excepcional/recurrente; cobertura vs éxito; actualización tras fracaso; repetir vs reasignar; verificación interna; persistencia del protocolo).
- **Ambigüedades:** (1) el nombre AF447 y el mapa titulado «escenario pedagógico AF447» podrían leerse como reconstrucción histórica; el notebook lo niega explícitamente; (2) sólo se observaron cinco filas de `search_cells.csv` en el volcado, aunque las aserciones fijan 25 celdas; (3) autoridad y escalamiento no se ejercen ni registran; (4) el supuesto de efectividad constante al repetir una celda está declarado pero no discutido como límite del plan.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; prueba de existencia de cuatro artefactos; recibe de P300 el formato de frontera de decisión; no habilita artefactos posteriores.
- **Auditoría de Analytics:** el producto es deliberadamente un protocolo excepcional, coherente con el diseño; no debe contarse como política recurrente gobernada. La teoría de búsqueda contribuye sin organizar el taller.
