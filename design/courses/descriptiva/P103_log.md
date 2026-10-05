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

## S03.P103.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P103.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - perfil univariado («data profiling outputs») y visualizaciones comunes con su propósito (CAP-E.3.6.2, 3.6.3, p. 15) — ya cubierta en la secuencia: histograma de P122 H02, mediana/percentiles y caja de P125 H03; la ausencia de distribución en P103 es marginal porque la secuencia la ejerce después.

## S03.P103.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio 17 %, encuadre analítico 15 %, datos 19 %, selección de metodología 15 %, desarrollo de modelos 15 %, despliegue 10 %, ciclo de vida 9 %) con subtareas evaluables. Respalda expectativas profesionales generales, no un syllabus. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
