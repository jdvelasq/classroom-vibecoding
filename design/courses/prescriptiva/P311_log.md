# Log — P311

## S02.P311.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/` (`data/` dos CSV, `professor/main.py`, `professor/notebook.ipynb`, `submission/` dos artefactos, `tests/test_activity.py`; `src/` sólo `.gitkeep`).
- **Trazabilidad revisada:** P311 → `prescriptiva.C03`, `C04`, `C05`. C04/C05 sostenidas (C05 declarativa); C03 parcial.
- **Highlights añadidos:** H01 (tres guardas simultáneas), H02 (meta promedio vs. por escenario; caso/datos), H03 (selección por menor costo y autoridad diferenciada).
- **Ambigüedades:** el nombre «evaluación por simulación» y el rol «prueba de política» de `activity-architecture.md` no corresponden a la implementación, que calcula esperanzas exactas sobre cuatro escenarios. Posible duplicación con P307 (mismo cálculo con otra guarda). Gatillos y límites sin derivación. Sin procedencia. `src/` sin `main.py`.
- **Superficies / contrato / dependencias:** S01–S05; pruebas sólo de existencia; recibe patrón de P307; habilitación no evidenciada.
- **Auditoría de Analytics:** producto = regla diaria de capacidad con servicio, riesgo y presupuesto, autoridad y gatillos. Identidad prescriptiva preservada; aporte metodológico frente a P307 no distinguible.
