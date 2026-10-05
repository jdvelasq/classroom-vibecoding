# Log — P309

## S02.P309.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P309_covid_hospital_capacity/` (`data/` tres CSV, `professor/main.py`, `professor/notebook.ipynb`, `submission/` seis artefactos, `tests/test_activity.py`; `src/` sólo `.gitkeep`; notebook de estudiante sin celdas).
- **Trazabilidad revisada:** P309 → `prescriptiva.C02`, `C03`, `C04`, `C05`. Sostenidas; C05 sólo declarativa.
- **Highlights añadidos:** H01–H07 (demora acción–efecto; trayectorias completas como unidad; enumeración fecha × tamaño; compromiso D04–D06; riesgo residual; gatillo de escalamiento desde sensibilidad; política en `main.py`).
- **Ambigüedades:** el notebook importa `main` desde `../src`, pero `main.py` está en `professor/` y `src/` está vacío (mismo patrón en P300, P303, P307 y P310–P312). El paso `escalamiento_contingente` repite `activation_day` 5 y `available_day` 9 aunque depende de una revisión diaria posterior. El gatillo 0.30 es la única variante probada; no se calcula umbral de indiferencia. «Probabilidad revisada» no tiene mecanismo de actualización. Sin procedencia de datos.
- **Superficies / contrato / dependencias:** S01–S05; pruebas verifican columnas y acciones, no cálculos; recibe práctica de P307 y P304; habilitación posterior no evidenciada.
- **Auditoría de Analytics:** producto = política de capacidad de dos pasos con autoridad clínica, salvaguardas, cadencia diaria y monitoreo. La evaluación por escenarios sirve a la regla; identidad prescriptiva preservada con los límites registrados.
