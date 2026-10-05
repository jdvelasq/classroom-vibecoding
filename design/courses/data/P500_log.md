# Log — P500

## S01.P500.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `professor/main.py`, `data/superstore_orders.csv`,
  `submission/`, `tests/test_activity.py`, `traceability.yaml`.
- **Decisión:** se creó el mapa de la actividad implementada y se registró la
  falta de un manifiesto local de procedencia.
- **Trazabilidad:** se revisaron `data.C01` a `data.C05`.
- **Auditoría:** producto analítico de métricas comerciales preserva identidad
  de Analytics.

## S02.P500.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P500_superstore_metricas/` (`data/superstore_orders.csv`, `professor/main.py`, `src/main.py`, `submission/metric_contract.json`, `submission/monthly_sales_metrics.csv`, `submission/questions.json`, `tests/test_activity.py`); contraste con `implementation/data/P501_superstore_serving/submission/sales_detail.csv` y la lectura de `implementation/data/P513_superstore_batch/`.
- **Trazabilidad revisada:** P500 → `data.C01`–`data.C05`; las cinco tienen evidencia.
- **Preservado:** pregunta, grano línea-de-orden, contrato de métrica, frontera de herramienta y auditoría de producto descriptivo.
- **Corregido:** la descripción previa afirmaba que el código «verifica» los faltantes de `Product Base Margin` y hacía una «reconciliación previa a la salida»: los faltantes son texto fijo del contrato y no hay reconciliación, sólo aserciones. Se precisó que `submission/` contiene tres artefactos y que las pruebas sólo comprueban existencia.
- **Highlights añadidos:** H01 (convención regional de lectura), H02 (fórmulas derivadas del grano; highlight obligatorio de caso y datos), H03 (métricas independientes de herramienta), H04 (compuerta de calidad). IDs nuevos; no existían highlights previos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** `encoding="latin1"` sobre un archivo con BOM UTF-8 (indicado por el prefijo `ï»¿` eliminado): el contrato persiste una codificación incorrecta y los textos no ASCII se decodifican mal (visible en P501); P513 usa `utf-8-sig`. La no unicidad de `Row ID` se afirma sin comprobarse. Sin procedencia del CSV. `src/main.py` sin instrucciones.
- **Superficies / contrato / dependencias:** S01–S07 declaradas; contrato separado entre código, `submission/`, prueba de existencia y trazabilidad; habilita a P501 (misma lectura y agregación) y el patrón `questions.json`.
- **Auditoría de Analytics:** producto descriptivo mensual con métricas auditables; pandas es habilitador. Riesgo de identidad bajo.

## S03.P500.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
- **Señales de alcance de curso** (registradas sólo en este log):
  - DG-Data Acquisition (p. 70: «minimize the deviation between the collected data and the real objects»; disposición de equilibrio exactitud/eficiencia) — marginal: el curso ya deriva requisitos desde preguntas (P500 H02, P517 H02); no aporta una capacidad nueva.
  - PR-Economic Considerations (p. 107: «Argue the case for what data an organization should routinely gather; design a related data collection process») — marginal: variante de `data.C01` ya ejercida (P500, P516, P517); el costo/valor de datos no tiene caso en el curso.
  - DG-Data Privacy and Security (p. 74: GDPR, Privacy Shield, HIPAA, GLBA, leyes estatales de EE. UU.) y PR-Legal Considerations e Intellectual Property (pp. 109–110) — fuera de alcance: detalle jurídico de otras jurisdicciones; a lo sumo una mención del marco local en la documentación de la candidata P526.
  - DPSIA/DP-Cryptography, Communication Protocols, Data Security (pp. 84–89) y Analysis for Security (pp. 92–94) — fuera de alcance: seguridad informática y ML para seguridad, no habilitación de datos para un propósito analítico.
  - CCF-Storage, Operating System, Networks, Compilers (pp. 64–68) — fuera de alcance: fundamentos de sistemas sin efecto sobre las capacidades `data.C01`–`C05`.
  - PDA-Programming (p. 114: «Manipulate data from selected sources (e.g., databases, spreadsheets, text documents, XML) utilizing appropriate techniques (e.g., database queries, API calls, regular expressions)») y cap. 6 (p. 38: «basic education in computing (programming, databases, use of the Internet)») — ya cubierta: CSV (P500), volcado SQL (P510), base relacional (P503), API/JSON (P518), Parquet (P524).
  - SDM (p. 121: «Execute a basic Data (Science) Lifecycle on a simple data product»; SDM-Software Testing) — marginal: las pruebas de participación son una decisión explícita de `AGENTS.md`, no un defecto que el benchmark corrija.
  - DM-Data Preparation, ingeniería de variables (p. 76: «feature extraction and representation; feature selection and feature generation») y DM-Information Extraction (p. 77, E) — fuera de alcance: pertenecen a los cursos predictivos o a procesamiento de texto avanzado.

## S03.P500.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.1 «Identify and prioritize data needs» (p. 5) — ya cubierta (P500 H02, P517 H02).
- **Señales de alcance de curso** (registradas sólo en este log):
  - Task 3.3 «Create a data management plan» (p. 5) — marginal: los manifiestos y contratos (P500 H03, P501 H02, P511 manifiesto, P517) ya cubren lo pertinente; un plan formal sería gestión de proyecto.
  - dominios I–II y IV–VII (pp. 4–7) — fuera de alcance (P001 y cursos de línea).

## S03.P500.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.1.1 «Identify data needs, sources, and acquisition sequence» (p. 13) — ya cubierta por P500 H02 y P517 H02.
  - CAP-E.4.4.1 características del *stack* (bases, nube, *open source*) (p. 18) — ya cubierta por la frontera de herramientas (P500 H03, P508 H01); profundizar sería identidad de herramienta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - CAP-E.3.6.3 visualizaciones comunes (p. 15) y dominios I–II, IV–VII (pp. 7–12, 17–25) — fuera de alcance: encuadre, métodos, modelos, despliegue y ciclo de vida pertenecen a P001 y a los cursos de línea.
