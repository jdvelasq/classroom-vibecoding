# Log — P103

## S02.P103.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P103_drivers_pandas/` (`data/drivers.csv`, `data/timesheet.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/summary.csv`, `submission/top10_drivers.png`, `tests/`). Comparado con P100–P102.
- **Trazabilidad revisada:** entrada P103 → `descriptiva.C02`, `descriptiva.C03`.
- **Highlights añadidos:** H01 (reconciliación de granularidades conductor-semana / conductor; highlight de caso y datos), H02 (comparación con la media propia vía `transform`), H03 (resumen recalculado por la prueba), H04 (ranking visual persistido).
- **Ambigüedades:** preguntas sólo implícitas en comentarios; el comentario «por año» no se verifica en los datos; no se comprueba que todos los conductores tengan las mismas semanas, lo que condiciona la lectura del ranking de totales; notebook de estudiante vacío.
- **Superficies / contrato / dependencias:** S01–S06; recibe `drivers.csv` de P102; habilita P104 (mismo contrato) y P105 (código comentado).
- **Auditoría de Analytics:** primer producto descriptivo reconocible (resumen y ranking), sin usuario, decisión ni interpretación. C02 y C03 sustentados en nivel básico.
