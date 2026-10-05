# Log — P305

## S02.P305.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P305_tax_inspections/` (`data/taxpayers.csv`, `data/audit_capacity.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, seis artefactos de `submission/`, `tests/test_activity.py`); relación con P303–P304.
- **Trazabilidad revisada:** P305 → `prescriptiva.C01`, `C02`, `C04`; sustentadas; sensibilidad (C03) no mapeada.
- **Highlights:** añadidos H01–H06 (valor por acción indivisible; reglas con igual capacidad; cartera exacta verificada; explicación de exclusiones; composición no anidada; recomendación supervisada).
- **Ambigüedades:** (1) la política se ilustra en una sola semana: la recurrencia es declarativa; (2) el contrato no contiene métricas de monitoreo ni umbrales para «desviación sostenida»; (3) equidad, debido proceso y disuasión se nombran como límites pero no se modelan; (4) celda de verificación duplicada en el notebook; (5) la prueba sólo verifica existencia.
- **Superficies / contrato / dependencias:** S01–S06; recibe registro y contrato de P303–P304; P306 retoma el contraste ranking/optimizador.
- **Auditoría de Analytics:** el riesgo señalado en el diseño (terminar en una solución matemática) está mitigado por el contrato y el registro pendiente de supervisor; el monitoreo de resultados sigue siendo declarativo.
