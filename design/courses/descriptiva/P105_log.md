# Log — P105

## S02.P105.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P105_drivers_chatgpt/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/`). Comparado con P103–P104.
- **Trazabilidad revisada:** entrada P105 → `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (*prompts* emparejados con código P103), H02 (estructura del dataset trasladada al *prompt*; highlight de caso y datos), H03 (salvaguarda «No inventes datos»). No inferibles: respuestas del asistente, verificación de resultados o producto persistido.
- **Ambigüedades:** el notebook no ejecuta nada y `submission/` está vacío; la prueba sólo exige una celda; se propone compartir `drivers.csv` completo (con `ssn` y `location`) con el asistente, en tensión con la minimización de P102; tercera repetición de la misma pregunta (P103–P105).
- **Superficies / contrato / dependencias:** S01–S05; recibe de P103; no habilita dependencias demostrables.
- **Auditoría de Analytics:** producto = especificación en lenguaje natural, no descripción. Mapeo a C02, C03 y C05 sin artefacto que lo sustente; requiere revisión. Centrada en una herramienta contribuyente.

## S03.P105.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - es un cuerpo de conocimiento de computación para pregrados de ciencia de datos, con 11 áreas de conocimiento y competencias de nivel T1/T2/E. Para descriptiva aportan sobre todo AP (presentación y visualización para clientes), DG/DM-Data Preparation (calidad, integración y limpieza, EDA, enmarcar la pregunta), DPSIA (privacidad e integridad) y PR/cap. 6 (comunicar resultados interpretados y sus límites a no especialistas). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P105.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P105.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
