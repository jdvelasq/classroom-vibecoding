# Log — P304

## S02.P304.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P304_airline_revenue_management/` (tres archivos de `data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, cinco artefactos de `submission/`, `tests/test_activity.py`); relación con P301 y P303.
- **Trazabilidad revisada:** P304 → `prescriptiva.C01`–`C04`; sustentadas; monitoreo declarado (C05) no mapeado.
- **Highlights:** añadidos H01–H07 (capacidad perecedera secuencial; valor marginal; regla por solicitud; consecuencias por escenario; sensibilidad y gatillo; automatización acotada; identidades de conservación).
- **Ambigüedades:** (1) procedencia de los datos no documentada y caso no declarado sintético; (2) valores de R12/R13 y totales esperados por política sólo verificables por aserciones del notebook, no en las cabeceras persistidas inspeccionadas; (3) la variante de sensibilidad cambia la protección a 12 pero no se persiste; (4) la prueba exige sólo dos de cinco artefactos.
- **Superficies / contrato / dependencias:** S01–S06; recibe la regla por entidad de P303; sin artefactos que habiliten actividades posteriores.
- **Auditoría de Analytics:** política prescriptiva operable con entradas observables, acción factible, restricciones, salvaguardas, autoridad, cadencia inmediata y gatillos; falta evidencia de monitoreo ejecutado. Identidad preservada.
