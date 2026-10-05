# Log — P100

## S02.P100.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial (no existían `P100_activity.md` ni `P100_log.md`).
- **Rutas inspeccionadas:** `implementation/descriptiva/P100_mapreduce_word_count/` (`data/file1.txt`–`file4.txt`, `professor/main.py`, `src/main.py`, `submission/part-00000`, `submission/_SUCCESS`, `tests/test_activity.py`, `tests/conftest.py`); `temp/` omitido por ser generado. No hay notebook ni `DESCRIPTION.md`.
- **Trazabilidad revisada:** entrada P100 de `implementation/descriptiva/traceability.yaml` → `descriptiva.C02`.
- **Highlights añadidos:** H01 (etapas map/shuffle/reduce), H02 (unidad textual y normalización; highlight de caso y datos), H03 (volumen simulado por replicación), H04 (convenciones de salida Hadoop), H05 (conteos esperados en pruebas). No inferibles: pregunta, usuario o uso analítico del conteo.
- **Ambigüedades:** procedencia de los cuatro textos no documentada; el contenido de `submission/part-00000` no es visible en el digest, por lo que los conteos citados provienen de las aserciones de prueba; no hay instrucciones para el estudiante.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; las pruebas aceptan cualquier conteo correcto sin exigir map/reduce; habilita P101 (mismo flujo y contrato).
- **Auditoría de Analytics:** producto = capacidad de datos (tabla de frecuencias) dominada por una destreza de disciplina contribuyente (MapReduce). El mapeo a C02 es habilitador, no evidencia de exploración antes de concluir. Identidad no resuelta a nivel de actividad.

## S03.P100.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - MapReduce como paradigma paralelo (BDS-Parallel Programming, T2, p. 59) y problemas de escala (BDS-Problems of Scale, p. 56) — fuera de alcance: la fuente lo sitúa en sistemas de *big data* (ingeniería de datos), lo que confirma la auditoría S02 (identidad no resuelta), no una mejora descriptiva.
  - procesamiento de texto (bag-of-words, word-count, TF-IDF, n-gramas, *stop words*, *stemming*; DG-Working with Various Types of Data, p. 71) — marginal: P100 H02 ya fija la unidad textual por reglas de normalización y P123 H02–H03 normaliza vocabularios. Añadir TF-IDF o lematización sería otra técnica para lo mismo.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «It is important for data science education to incorporate real data used in an appropriate context» (p. 30) — marginal: refuerza una preferencia que AGENTS.md ya establece. Su efecto concreto (calendario sintético uniforme en P150–P154, S01) es un defecto conocido de S02 que requiere decisión de caso y datos de curso, no una mejora local derivada de este documento.
  - comunicación oral/escrita/electrónica a audiencias diversas, informes de situación para gerencia (PR-Communication, pp. 105–106); «Knowing the audience» (AP, p. 44); identificar los asuntos analíticos desde las preocupaciones del cliente (cap. 6, p. 39) — se concreta en las candidatas P120/P152. Extenderlo a todos los talleres sería repetir la misma mejora. La falta de usuario o decisión en P120–P154 es un hallazgo transversal de S02 que corresponde a una decisión de curso.
  - AP-User-centred design, Interaction design, Interface design (T2/E; pp. 46–48: prototipado, estándares de interfaz, GUI, animación, accesibilidad) — fuera de alcance: pertenece a productos de datos o HCI y desplazaría la identidad descriptiva.
  - sesgo y representatividad de muestras (PR-Ethical, p. 108: «Need for data, including samples of data, to be truly representative»; DM-Data Preparation, p. 76: «concerns around potential bias in data»; cap. 6, p. 39) — marginal: la frontera de población ya está declarada en P123 (H01, cadena de búsqueda) y P124 (datos no operativos). Ningún caso actual tiene un sesgo de muestreo demostrable que enseñar con rigor.
  - *clustering*, clasificación, regresión, reglas de asociación (Apriori), ML, IA (DM pp. 77–80; ML; AI) — fuera de alcance: predictiva u otros cursos. Las reglas de asociación no tienen caso descriptivo ni datos en el curso actual.
  - seguridad, criptografía, protocolos, análisis para seguridad (DPSIA/DS, DPSIA/AS, pp. 86–94) — fuera de alcance.

## S03.P100.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - caso de negocio, selección de stack, modelos, despliegue y ciclo de vida (Tasks 1.5, 4.3–4.4, dominios V–VII, pp. 4–7) — fuera de alcance: gestión de proyectos, predictiva, prescriptiva y productos de datos.

## S03.P100.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - roles de gobierno de datos (owner, steward, custodian) (CAP-E.3.2.2, p. 14) — marginal: P153 ya declara propietario del KPI; los roles de custodia no cambian lo que el estudiante produce.
  - línea base del estado actual de las medidas de éxito (CAP-E.2.5.1, p. 12) — marginal: medir el estado actual es lo que ya hacen los KPI globales de P120–P122 y P124; no hay caso con medida de éxito de un proyecto contra la cual comparar.
  - caso de negocio con beneficios y costos (Task 1.5, p. 8), selección de stack (Task 4.4, p. 18), modelos predictivos y prescriptivos, despliegue y ciclo de vida (dominios V–VII, pp. 19–25) — fuera de alcance: gestión de proyecto, predictiva, prescriptiva y productos de datos.

## S03.P100.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio 17 %, encuadre analítico 15 %, datos 19 %, selección de metodología 15 %, desarrollo de modelos 15 %, despliegue 10 %, ciclo de vida 9 %) con subtareas evaluables. Respalda expectativas profesionales generales, no un syllabus. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - actualizar el enunciado del problema a partir de hallazgos de datos (p. 16: CAP-P.3.8.1 «appropriate changes to an analytic problem statement based on multiple observed data findings») — marginal: P122 H05 ya restringe la comparación de flete según la cobertura observada; no hay caso adicional que lo ejercite de forma distinta.
  - selección de métodos descriptivos/diagnósticos vs predictivos vs prescriptivos (p. 17: CAP-P.4.1.2–4.1.4) — fuera de alcance como propuesta de taller: es criterio de diseño curricular entre cursos.
  - debilidades de un modelo en hoja de cálculo y selección de stack tecnológico (p. 18: CAP-P.4.4.1–4.4.2) — marginal: el curso ya contrasta herramientas para el mismo producto (P103/P104, P106/P107, P108/P109).
  - desarrollo, validación cruzada, calibración y despliegue de modelos; seguimiento del ciclo de vida (pp. 19–25: Domains V–VII) — fuera de alcance: predictiva, prescriptiva y productos de datos.

## S03.P100.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «processing text into data that can be analyzed» (p. 43) — ya cubierta (P100 H02, P123 H02–H03).
- **Señales de alcance de curso** (registradas sólo en este log):
  - áreas de *data acumen* (p. 41: «Data description and visualization», «Workflow and reproducibility», «Communication and teamwork»…) — ya cubierta en conjunto por C01–C05 de `traceability.yaml`; la familia authoritative respalda expectativas generales, no un syllabus.
  - «Ability to understand client needs» (p. 48) y roles de *business analysis* «assembling and presenting data to inform a decision-making process» (p. 38) — marginal: la ausencia de usuario/decisión ya es límite registrado en casi todas las Pxxx; el documento no aporta un mecanismo distinto para cerrarla.
  - fundamentos matemáticos y computacionales (pp. 41–43), «Data Modeling and Assessment» con *machine learning*, *deep learning* y *model assessment* (p. 46), «making inferences and predictions» en el ciclo (p. 40) — fuera de alcance: predictiva/otros cursos.
  - «Source code (version) control systems» y «Collaboration» (p. 47) — marginal: la distribución por repositorio y GitHub Actions ya las ejercita fuera del contenido del taller.
  - «Record retention policies» (p. 45) y código de ética/juramento (pp. 50–51, 138) — fuera de alcance: sin caso ni producto descriptivo que los ejercite con rigor; la dimensión responsable ya está en P102, P108, P109, P125 H07.
  - pasos de evaluación de Jordan, «Create challenge questions and exercises» (p. 89) — marginal: orientación general de evaluación; el contrato `pytest` de participación es una decisión ya tomada.
