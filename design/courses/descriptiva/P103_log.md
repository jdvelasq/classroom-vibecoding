# Log — P103

## S02.P103.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P103_drivers_pandas/` (`data/drivers.csv`, `data/timesheet.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/summary.csv`, `submission/top10_drivers.png`, `tests/`). Comparado con P100–P102.
- **Trazabilidad revisada:** entrada P103 → `descriptiva.C02`, `descriptiva.C03`.
- **Highlights añadidos:** H01 (reconciliación de granularidades conductor-semana / conductor; highlight de caso y datos), H02 (comparación con la media propia vía `transform`), H03 (resumen recalculado por la prueba), H04 (ranking visual persistido).
- **Ambigüedades:** preguntas sólo implícitas en comentarios; el comentario «por año» no se verifica en los datos; no se comprueba que todos los conductores tengan las mismas semanas, lo que condiciona la lectura del ranking de totales; notebook de estudiante vacío.
- **Superficies / contrato / dependencias:** S01–S06; recibe `drivers.csv` de P102; habilita P104 (mismo contrato) y P105 (código comentado).
- **Auditoría de Analytics:** primer producto descriptivo reconocible (resumen y ranking), sin usuario, decisión ni interpretación. C02 y C03 sustentados en nivel básico.

## S03.P103.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - es un cuerpo de conocimiento de computación para pregrados de ciencia de datos, con 11 áreas de conocimiento y competencias de nivel T1/T2/E. Para descriptiva aportan sobre todo AP (presentación y visualización para clientes), DG/DM-Data Preparation (calidad, integración y limpieza, EDA, enmarcar la pregunta), DPSIA (privacidad e integridad) y PR/cap. 6 (comunicar resultados interpretados y sus límites a no especialistas). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
