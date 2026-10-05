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

## S03.P100.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Spark, Hadoop, Kafka, procesamiento distribuido (p. 175) y modelado avanzado, índices, sharding (p. 175) — fuera de alcance: ingeniería de datos/bases de datos; P100 ya usa MapReduce sólo como habilitador.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Visualización (Power BI)» con 76,1 % de brecha curricular en IES (pp. 102, 116) y Power BI/Tableau/Looker como herramientas demandadas (p. 176); certificación Power BI 2,19 % (p. 79) — fuera de alcance: señal de herramienta en fuente governmental; la frontera del curso excluye la capacitación en una plataforma BI concreta, no BI como tal y ya produce visualizaciones (P103 H04, P120 H05) y un tablero (P124 H04).
  - analistas Big Data/BI que «migrarán de un rol descriptivo (reportes) a uno predictivo y prescriptivo» (p. 291); ML, MLOps, series de tiempo, pronósticos, backtesting (pp. 96–97, 176) — fuera de alcance: pertenecen a predictiva/prescriptiva/productos de datos.
  - déficit de habilidad para «problemas mal definidos, ambiguos» y trabajo con proyectos del sector productivo (pp. 177, 183, 217, 221) — fuera de alcance como propuesta de taller: recomendación de nivel programa/política; el curso ya prioriza casos trazables (`datalabs/`) y la ausencia de usuario/decisión está registrada en las auditorías S02.
  - muestra no probabilística, «Margen de error: No aplica, dado el carácter no probabilístico, exploratorio y no inferencial del estudio» (p. 323) — marginal: buen ejemplo de declaración de límite de evidencia, pero el curso ya declara fronteras (P123 H01, P125 H06) y no hay caso con datos para enseñarlo distinto.

## S03.P100.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Análisis de Datos» como temática priorizada por demanda laboral (p. 2: «enfocado en las áreas más demandadas por el mercado: datos, programación, ciberseguridad …») — marginal: confirma pertinencia laboral del curso (función governmental), pero no define contenidos, estándar ni herramientas; no cambia lo que el estudiante hace en ningún taller.
  - metodología *learning by doing* con desafíos concretos y simulación de situaciones reales de trabajo (p. 1: «la capacitación se centra en resolver problemas prácticos, fomentando el aprendizaje a través de la experiencia»; «el aula se convierte en un espacio que simula situaciones reales de trabajo») — ya cubierta: los talleres presenciales guiados por casos (P120–P125, P150–P154) ya siguen ese formato; un documento governmental no prescribe pedagogía.
  - metodologías ágiles, colaboración y mentoría (p. 1: «La implementación de metodologías ágiles, la colaboración y el aprendizaje compartido también son elementos esenciales») — fuera de alcance: rasgo del formato bootcamp, sin relación con un producto descriptivo.
  - focalización regional y poblacional (p. 2: «distribución regional que permita adaptar las iniciativas … a las particularidades y demandas específicas de cada área geográfica»; p. 3: lista de grupos focalizados) — fuera de alcance: describe el diseño de la política, no una señal curricular; no hay datos del programa en el documento que permitan construir un caso descriptivo.
  - temáticas de IA, blockchain, nube y ciberseguridad (p. 2) — fuera de alcance: no pertenecen a descriptiva.

## S03.P100.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Analítica descriptiva, analítica predictiva y sesgos algorítmicos» (p. 5) — marginal: mención de tema en un temario ejecutivo, sin contenido; la frontera descripción/predicción ya organiza el curso y el sesgo algorítmico pertenece a predictiva.
  - proyecto final integrador «un caso y un plan de negocios que utiliza la IA» (p. 6) y estudios de caso empresariales (pp. 8–9) — fuera de alcance: formato de programa ejecutivo centrado en estrategia de IA; el curso ya trabaja con casos (P120–P125) y no posee productos de IA.
  - ML supervisado/no supervisado, entrenamiento/validación/prueba, redes neuronales, visión artificial, PLN, robótica (pp. 4–5) — fuera de alcance: predictiva y productos de datos.

## S03.P100.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - gestión de datos «at scale» (p. 1) — fuera de alcance: no justifica ampliar el MapReduce simulado de P100–P101; si acaso, refuerza la auditoría S02 ya registrada de que esas actividades son habilitadoras de ingeniería de datos y no responden la pregunta descriptiva. No genera propuesta nueva.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «principles and practices of managing data at scale, with a focus on use cases in data analysis and machine learning» con «focus on ensuring reliable, scalable operationalization» (p. 1) — fuera de alcance: es la identidad de un curso de ingeniería de datos/productos de datos; Berkeley lo ubica como curso propio posterior a ciencia de datos (prerrequisito «DATA C100 ... or equivalent», p. 1), lo que ilustra (institutional, no prescribe) la frontera que el curso ya declara («no posee ... ingeniería de datos»).

## S03.P100.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado en Data Science (antes Statistics 102). Cubre fundamentos probabilísticos de la inferencia y el ciclo de modelado y decisión, con sus implicaciones humanas, sociales y éticas. Sólo lista temas: no tiene resultados de aprendizaje, casos ni evaluación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - decisión frecuentista y bayesiana, Thompson sampling, control óptimo y Q-learning (p. 1) — fuera de alcance: son decisión secuencial y prescriptiva.
  - modelos jerárquicos bayesianos, árboles de decisión, redes neuronales, ensambles y sistemas de recomendación (p. 1) — fuera de alcance: predictiva y aprendizaje automático.
  - algoritmos de clustering (p. 1) — fuera de alcance aquí: el documento sólo nombra la técnica, sin uso descriptivo concreto. La única detección de grupos del curso (Louvain sobre co-ocurrencias en P123 H05) ya cubre la estructura relacional que el curso necesita.
  - diseño experimental básico (p. 1) — fuera de alcance: el curso describe datos observados y no los diseña.
  - implicaciones humanas, sociales y éticas del ciclo de modelado (p. 1) — ya cubierta en lo descriptivo por P102 H02 (minimización), P108 H01–H05 (riesgo de reidentificación) y P125 H07 (no divulgar salarios individuales). El documento no detalla prácticas que añadir.

## S03.P100.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de 11 semanas, sin codificación, organizado en sesgos de decisión, análisis descriptivo, Big Data, experimentación, predictivo (ML, redes neuronales), prescriptivo y cuestiones ético-jurídicas; casos y tareas de negocio. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - web scraping, API, «¿Qué datos puedes encontrar?», Amazon y APIs (p. 7) — fuera de alcance: adquisición de datos externos; los casos del curso parten de fuentes trazables provistas.
  - «Experimentación: el estándar de oro» (p. 7), análisis predictivo y redes neuronales (pp. 7–8), prescriptivo y árboles de decisión (p. 8) — fuera de alcance: inferencia causal experimental, predictiva y prescriptiva pertenecen a otros cursos; P125 H06 ya fija el límite causal de una descripción.
  - sesgos y trampas en decisiones (p. 7; Módulo 8, p. 8) — marginal: contexto de decisión, sin producto descriptivo nuevo.
  - Big Data y las cuatro V (p. 7) — marginal/fuera de alcance: P100 ya trata volumen como ejercicio de ingeniería; no cambia el producto descriptivo.
  - hacking, amenazas internas, caso TalkTalk (pp. 8, 11) — fuera de alcance: seguridad informática.

## S03.P100.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - contenedores, orquestación, Kubernetes, *serverless*, AWS Lambda, *cloud native* (pp. 13–15) — fuera de alcance: infraestructura y productos de datos.
  - casos de transformación organizacional y bucle OODA (pp. 14–15) — fuera de alcance: estrategia tecnológica, sin producto descriptivo.

## S03.P100.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso ejecutivo de 8 semanas sobre liderazgo de datos: IA para líderes, marcos de innovación continua de datos, arquitectura TI y SQL, plataformas de datos y diseño de bases, *modern data stack*, nube, ética y gobierno de datos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Effective business decisions depend on precise forecasting» (p. 6) — fuera de alcance: predictiva.
  - *modern data stack*, ingesta, nube, DevOps Lean, ChatGPT y *no-code* (pp. 7, 14–15) — fuera de alcance: plataformas e ingeniería; estrategia organizacional sin producto descriptivo.

## S03.P100.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python/estadística (pandas, visualización, estadística descriptiva e inferencial), aprendizaje no supervisado (clustering, PCA, clustering espectral y de modularidad), regresión y predicción, clasificación y pruebas de hipótesis, deep learning, sistemas de recomendación y redes/modelos gráficos; con casos de estudio por semana. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - regresión, regularización, árboles, clasificación, SVM, deep learning, sistemas de recomendación, filtros de Kalman, modelos gráficos (pp. 8–11) — fuera de alcance: predictiva y productos de datos.
  - portafolio de «3 real-life projects and 50+ case studies» (p. 4) — marginal: formato de programa; el curso ya organiza talleres por casos (P120–P125).

## S03.P100.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Implement the Lawler Model for defining an AI problem» y resumen ejecutivo de un producto de IA (p. 6, p. 7) — fuera de alcance: definición de problemas para productos de IA (curso de productos de datos); el encuadre de preguntas descriptivas se trata con fuentes más pertinentes (INFORMS, `dataops-03`).
  - algoritmos de ML supervisado, no supervisado y semisupervisado, deep learning, GANs, GPT-3, impacto social de los medios sintéticos (pp. 3, 6–7) — fuera de alcance: predictiva, IA y productos de datos.

## S03.P100.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «How can we Model a Platform?», «Modeling Network Effects» (p. 15) — fuera de alcance: modelado de dinámicas (predictiva/simulación).
  - precios de plataforma, APIs y estándares, gating de calidad, antimonopolio, *roadmap* de funcionalidades (pp. 7–8, 14–15) — fuera de alcance: estrategia de producto y productos de datos, sin pregunta descriptiva.

## S03.P100.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - modelado y simulación con EDO/EDP, métodos de Euler, implícitos y de orden superior, sistemas lineales y no lineales (p. 1: «Ordinary Differential Equations (ODEs)», «Partial Differential Equations (PDEs)») — fuera de alcance: computación científica, sin relación con la pregunta descriptiva.
  - optimización y modelado a partir de datos (p. 2: «Least Squares Problems», «Gradient Descent», «Parameter Estimation and Nonlinear Least Squares») — fuera de alcance: pertenece a predictiva/prescriptiva.
  - regresión, regularización, regresión logística y ajuste de modelos (p. 2: «Regularization», «Logistic Regression», «Assessing Model Fit») — fuera de alcance: predictiva.
  - simulación Monte Carlo, pronóstico probabilístico, sensibilidad y eventos raros (p. 2: «Monte Carlo Simulation», «Probabilistic Forecasting», «Simulating Rare Events») — fuera de alcance: predictiva/prescriptiva. Tampoco hay contenido que respalde la incertidumbre descriptiva que falta en P120–P122.
  - estudios de caso evaluados (p. 2: «Aurora Flight Sciences», «Schlumberger», «BASF») — marginal: sólo nombra los casos, sin contenido; P120–P125 ya organizan el curso por casos.

## S03.P100.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Hadoop, «Platforms for Handling Big Data», DASK para «simulate parallel processing across distributed machines» (pp. 6, 9, 11) — fuera de alcance: confirma que MapReduce y el paralelismo son materia de ingeniería de datos; no justifica ampliar P100/P101 (su auditoría ya registra la identidad no resuelta).
- **Señales de alcance de curso** (registradas sólo en este log):
  - CDC, Debezium, contenedores, streaming (Kafka, MQTT, ThingsBoard), aplicaciones web en Java/Node (pp. 8–11) — fuera de alcance: ingeniería de datos y productos de datos.
  - regresión lineal, Naïve Bayes, k-means, aprendizaje por refuerzo, redes profundas (pp. 8, 11–12) — fuera de alcance: predictiva.
  - «Learn data visualization», D3 (pp. 8, 11) — marginal: herramienta de visualización alternativa; la visualización ya está cubierta (P103 H04, P120 H05).

## S03.P100.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado en línea de 6 meses (24 módulos en cinco partes: fundamentos de ciencia de datos, optimización, ML, ML avanzado y despliegue) con casos de la facultad de MIT Sloan; orientación dominante a modelado predictivo y prescriptivo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - clustering (Módulo 4, p. 7) — fuera de alcance: segmentación no supervisada como técnica de ML sin caso descriptivo en el documento.
  - regresión, CART, *ensembles*, redes neuronales, NLP, filtrado colaborativo, optimización lineal, despliegue (pp. 7–9) — fuera de alcance: predictiva, prescriptiva y productos de datos.

## S03.P100.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño: selección de conceptos (Pugh), estudios de *trade-off*, modelos de valor, generación y evaluación de espacios de diseño, visualización del *tradespace*, frente de Pareto y sensibilidad. Sólo trae títulos de unidades y una descripción breve de cada una. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - selección de conceptos sin modelo (Pugh) y estructura de un estudio de *trade-off* (p. 1: «quantitative methods that do not require a model, such as the Pugh method … overview of how to structure a trade study») — fuera de alcance: son métodos para elegir entre alternativas de diseño, es decir, decisión y prescripción, no descripción de lo que ocurre.
  - generación combinatoria y muestreo de espacios de diseño, y evaluación por valor, costo y desempeño (p. 3: «design decisions are combinatorially paired and sampled to generate a design space») — fuera de alcance: no hay caso ni datos observados que describir; el objeto es un espacio de alternativas construido.
  - sensibilidad, robustez y representación de la incertidumbre de un diseño (p. 4: «define what sensitivity means for a design … how uncertainty can be captured and represented») — fuera de alcance: es robustez de una decisión (prescriptiva). La incertidumbre de una descripción no aparece en este documento como señal.
  - pre-evaluación y post-evaluación para medir la línea base del estudiante (p. 1: «take a Pre-Assessment to get a baseline of your understanding»; p. 4: «Post-Assessment») — fuera de alcance: es una práctica institucional de evaluación del programa. La evaluación de los talleres está fijada por el contrato con `pytest` de `AGENTS.md`, y esta señal no cambia lo que el estudiante hace en ningún Pxxx.

## S03.P100.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, termoformado), mapeo de atributos prototipo–producto, decisiones de fabricación y análisis de costo-valor, con un proyecto final sobre una careta facial o un giróscopo satelital. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Assess data gathered from concept prototypes to make smart decisions on developing your desired product» (p. 5) y «Participants will assess the data results for the different processes used» (p. 8) — fuera de alcance: evaluación de pruebas de ingeniería de fabricación; el documento no contiene datos, preguntas ni métodos de descripción analítica.
  - desarrollar una hipótesis para un producto deseado y probar un prototipo virtual (Módulo 6, p. 7); análisis de costo y valor (Módulo 7, p. 7) — fuera de alcance: diseño de producto físico y decisión económica; no corresponde a descriptiva ni a otro curso de la línea de Analytics más allá de una analogía genérica con prototipos.
  - procesos de fabricación seriales y paralelos, DFM, cálculo de masa y momento de inercia (pp. 6–7) — fuera de alcance: ingeniería mecánica; sin relación con el curso.

## S03.P100.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Describing a corpus of documents with a term–document matrix» (p. 13) — ya cubierta: P100 H02 (unidad textual), P123 H02–H04 (conteo de campos multivaluados y co-ocurrencia ítem × ítem).
- **Señales de alcance de curso** (registradas sólo en este log):
  - segmentación con K-Means y clustering jerárquico (p. 13), inferencia, pruebas de hipótesis y A/B testing (p. 6, p. 14), regresión, clasificación, series de tiempo, optimización y simulación (pp. 5–14) — fuera de alcance: predictiva, prescriptiva o contenido de Estadística; el catálogo no aporta caso ni datos para un uso descriptivo.
  - EDA y gráficos estadísticos como primer paso de un proceso de modelado (p. 8) — marginal: el curso ya ejerce exploración al servicio de la descripción (P103, P120–P122, P125); aquí aparece como antesala del modelado.

## S03.P100.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto (asíncrono + 3,5 días presenciales) sobre estrategia, modelos de negocio, IA generativa y agéntica, pensamiento de futuros y gobernanza de IA, con un *capstone* de iniciativa organizacional; requiere 10+ años de experiencia. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Creating a culture of data excellence» (p. 16) y «Data excellence» (p. 5) — marginal: título de sesión sin contenido operativo; la calidad de datos antes de concluir ya está en P120 H02, P121 H02, P122 H01/H05 y P153 H03.
  - «Evaluate AI opportunities and risks across business functions using structured analytical frameworks» (p. 7) y «Analyze key trade-offs in AI adoption, including considerations of cost, control, speed, and risk» (p. 7) — fuera de alcance: evaluación estratégica de inversiones en IA para alta dirección; no es una pregunta descriptiva ni tiene caso/datos en el documento.
  - escenarios, prospectiva y «Decision-making under uncertainty» (p. 5; p. 17: «How to lead and make decisions through increasingly uncertain times») — fuera de alcance: pertenece a prescriptiva/estrategia; el curso describe con evidencia observada.
  - analítica predictiva y ML en flujos de decisión (p. 16: «How leaders create conditions for effective integration of predictive analytics»; «Configuring workflows and decisions for machine learning») — fuera de alcance: predictiva y productos de datos.
  - *capstone* orientado a implementación de una iniciativa de IA (p. 17) — fuera de alcance: formato ejecutivo de transformación organizacional, sin relación con un producto descriptivo.

## S03.P100.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado en línea de diez meses en español con cinco cursos de ocho semanas: Data Engineering, Ciencia de Datos con Python, Estadística para la Ciencia de Datos, IA y Machine Learning, y Storytelling y Visualización de Datos Estratégicos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Definir casos de negocio (coste-beneficio) a partir del análisis… para dar recomendaciones justificadas sobre una acción» (p. 8) — fuera de alcance: recomendación de acción es del curso prescriptivo; P125 ya marca el límite de sus «alternativas».
  - paralelismo, persistencia de modelos como API, reducción de dimensiones, clasificación, regresión, aprendizaje supervisado y no supervisado (pp. 6–7) — fuera de alcance: ingeniería de datos, predictiva y productos de datos.

## S03.P100.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relata cuatro talleres participativos con 17 programas de pregrado de la UNAL sobre currículo, contextos, funciones misionales y prácticas pedagógicas, y recoge propuestas institucionales de armonización (superar el «currículo endogámico», egresados, unificación de conceptos). No contiene ningún programa ni curso de analítica, ningún resultado de aprendizaje disciplinar y ningún contenido de analítica descriptiva o de visualización. Estadística y Administración de Empresas sólo figuran como programas participantes (p. 8: «Economía, Zootecnia, Estadística…»). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - evaluación centrada en la resolución de problemas y en el «saber hacer» (p. 82: «la evaluación debería adoptar una orientación sobre el seguimiento del "saber hacer"»; p. 69: «Enfocada en la resolución de problemas») — ya cubierta: los casos P120–P125 se organizan alrededor de preguntas con producto persistido y pruebas que lo recomputan (P120 H01/H08, P125 H06). El documento es una percepción institucional genérica y no cambia lo que el estudiante hace en ningún taller.
  - autoevaluación y coevaluación (p. 82: «dos componentes hasta ahora dejados de lado en los mecanismos de evaluación: autoevaluación y coevaluación») — fuera de alcance: AGENTS.md fija `pytest` sobre `submission/` como contrato de evaluación de los talleres Pxxx. Es una práctica de gestión del curso, no una contribución de un taller, y la fuente sólo la ilustra.
  - seguimiento del avance en proyectos que exceden el marco temporal del curso (p. 82: «seguimiento a diferentes porcentajes de su avance») — marginal: los talleres son guiados y se cierran en sesión, y la señal no tiene ancla en HNN/SNN.
  - equilibrio teoría/práctica y conexión con problemas del contexto (pp. 76–77: «un equilibrio entre los componentes teóricos y los prácticos… predomina el primero»; «enfocar fines y contenidos en la resolución de problemas») — ya cubierta: el curso es taller práctico con casos de dominio (P120 devoluciones, P121 vuelos, P122 cadena de suministro, P125 salarios).
  - métodos de estudio grupales y trabajo cooperativo (p. 79: «se resaltó el éxito de los métodos de estudio grupales») — marginal: es una estrategia de aula sin efecto sobre el producto analítico de ningún Pxxx.
  - recursos innovadores, «uso de metadatos para la investigación a través de ejercicios de modelación» (p. 79) — marginal: la mención es vaga y no tiene caso ni datos. La exploración de metadatos bibliográficos ya existe en P123 (H01–H04).
  - contenidos transversales de igualdad de género y diversidad (p. 77; p. 98: «tenemos formas únicas de evaluar») — fuera de alcance: es un propósito institucional transversal, no una capacidad descriptiva. La sensibilidad de comparar grupos ya está tratada en P125 (H02, H07).
  - objetivos medibles e indicadores para el seguimiento de la armonización (p. 110: «indicadores que permitan un adecuado seguimiento… ausencia de objetivos medibles») — marginal: se refiere a la gestión del programa, no a un KPI que el estudiante construya. La definición de un KPI como contrato ya está en P153 (H01–H03).
  - vínculo con egresados y mercado laboral para actualizar el perfil de egreso (pp. 106–107) — fuera de alcance: es pertinencia institucional del programa, no contenido de taller.

## S03.P100.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular administrativa de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular» (Acuerdo 02 de 2020 del CESU, resultados de aprendizaje, PEP, planes de mejoramiento) en dimensiones macro/meso/microcurricular y cuatro etapas; no contiene contenidos disciplinares. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - resultados de aprendizaje como «declaraciones expresas de lo que se espera que un estudiante conozca y demuestre» (p. 2) — fuera de alcance: decisión de nivel de programa; el curso ya expresa capacidades C01–C05 en `traceability.yaml`, y S03 no redefine resultados de programa.
  - dimensión «Microcurricular: compete a las didácticas y procesos de evaluación de los aprendizajes» (p. 2) — marginal: no prescribe método; el formato de taller guiado y la evaluación con `pytest` ya son decisiones vigentes.
  - etapa 4, «diseñar los mecanismos de monitoreo y evaluación» de los resultados de aprendizaje (p. 3) — fuera de alcance: proceso de gestión curricular, no contenido de un taller.
  - atender «las exigencias y necesidades del medio, la actualidad de las áreas de conocimiento» (p. 3) — marginal: principio general sin señal técnica o pedagógica que ancle a un Pxxx; la familia institutional ilustra, no impone.

## S03.P100.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Sílabo de un curso de minería de datos aplicada a salud (textos de Albright–Winston y Han–Kamber): preprocesamiento, exploración, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, *clustering* y atípicos, minería de texto; proyecto por entregables (propuesta, reporte de recolección, reporte de preparación, informe final) y artículo de revisión. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Mining Frequent Patterns, Associations, and Correlations», «Classification and Prediction», «Clustering and Outlier Analysis», regresión, minería de texto (p. 9) — fuera de alcance: la minería de datos es predecesora contenida en la predictiva; el análisis de atípicos como técnica de minería no cabe en un Pxxx sin desplazar su identidad.
  - «Create business intelligence for healthcare through data analytics» (p. 3) — ya cubierta en general por P150–P154; el dominio de salud no aporta capacidad distinta.
  - formular hipótesis en la exploración (p. 6) — marginal: sin producto ni método asociado.
  - artículo de revisión de literatura, póster, foros (pp. 6–8) — fuera de alcance: formatos de evaluación ajenos al contrato `Pxxx`/`pytest`.

## S03.P100.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Sílabo de un curso introductorio de 16 semanas centrado en herramientas (Excel, Access, SQL, MongoDB, SAS, Tableau): modelado ER y normalización, SQL (agregación, joins, subconsultas), NoSQL, sistemas de BI, visualización y tableros, proyecto final en equipo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - normalización y formas normales, diagramas de dependencias (p. 5) — fuera de alcance: diseño de bases de datos (disciplina contribuyente).
  - «Tell compelling stories with data», «Present data-driven insights using data visualization and dashboards» (p. 1) — marginal desde este documento: enunciado de objetivo sin método; la ausencia de lectura persistida ya está registrada en las auditorías (p. ej., P152 H03, P154 S04).
  - NoSQL/MongoDB y su framework de agregación (pp. 6–7); capacitación en Excel, Access, SAS, Tableau (p. 1) — fuera de alcance: plataformas concretas y bases no relacionales.
  - proyecto final que identifica problema, recolecta, limpia, analiza y modela (pp. 2–3) — fuera de alcance como formato: el curso evalúa con talleres `Pxxx` y `pytest`; los «models» exceden la línea descriptiva.

## S03.P100.29

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa en línea de 12 semanas, con o sin código, sobre IA generativa, ingeniería de *prompts* y RAG, agentes con herramientas y memoria, planificación y razonamiento, sistemas multiagente, pruebas y evaluación de sistemas agénticos y su protección; casos y proyectos de automatización empresarial. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - RAG, *embeddings*, almacén vectorial (p. 11); agentes con LangChain, herramientas, memoria y MCP, planificación y razonamiento (p. 12); sistemas multiagente, pruebas unitarias/de integración, métricas de latencia y robustez (p. 13); IA multimodal (p. 14) — fuera de alcance: construcción de productos de IA (productos de datos), no descripción.
  - casos y proyectos (agente de análisis de investigación financiera, chatbots, procesamiento documental) (pp. 14–16) — fuera de alcance: automatización de procesos con agentes; el «análisis de datos y generación de insights» automatizado (p. 14) no aporta método descriptivo.
  - resultados de aprendizaje en marketing, ventas y operaciones (p. 6) — marginal: enunciados generales sin contenido descriptivo.

## S03.P100.30

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - herramientas de línea de comandos para ordenar, contar, agregar y unir (p. 2) — ya cubierta: P100 H01 reproduce el patrón contar/ordenar/agregar; cambiar de herramienta sería marginal.
- **Señales de alcance de curso** (registradas sólo en este log):
  - regresión, clasificación (árboles, Naive Bayes, SVM), SVD/PCA y clustering (k-means, jerárquico, k-center) (p. 2) — fuera de alcance: predictiva o modelado no supervisado propio de otras disciplinas contribuyentes.
  - Bloom filters, sketches y estructuras para escalar a big data y flujos (p. 2–3) — fuera de alcance: ingeniería de datos / productos de datos.
  - casos de uso de analítica en empresas (Google, Facebook, Netflix) y proyecto final como 35 % de la evaluación (pp. 2, 4) — marginal: contexto motivacional; la evaluación del curso se rige por `pytest` sobre talleres (AGENTS.md) y la ficha no aporta un criterio de evaluación transferible.

## S03.P100.31

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de métodos y herramientas de un programa de *business analytics*, sin descripciones: recolección de datos (encuestas, NPS, pasiva, medios), A/B testing, correlación y causalidad, pronóstico (suavizamiento exponencial, tendencia y estacionalidad, estadística descriptiva, nuevo producto), regresión, *simulation toolkit* (Analysis ToolPak, Solver), visualización e interpretación de datos, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Data Visualization and Interpretation» y «Descriptive Statistics» (p. 1) — ya cubierta: visualización en P103/P120–P125 y estadísticos robustos en P125 H03. El rótulo no especifica ninguna práctica nueva.
  - «Data Collection Methods: Surveys, Net Promoter Score (NPS), and Self-Reports; Passive Data Collection; Media Data Collection» (p. 1) — fuera de alcance: el curso describe datos existentes y no diseña su recolección, y no hay caso de encuestas en el curso. NPS como KPI sería una variante de los KPI ya trabajados (P120, P124, P153): marginal.
  - «A/B Testing» (p. 1) — fuera de alcance: es inferencia experimental o causal, no descripción, y no hay caso ni datos.
  - «Forecasting» (objetivo/subjetivo, «Exponential Smoothing», «New Product») y «Regression Analysis» (p. 1) — fuera de alcance: pertenecen a analítica predictiva.
  - «Simulation Toolkit: Analysis ToolPak, Solver Optimization Tool», «Optimization Models», «Decision Trees» (p. 1) — fuera de alcance: son analítica prescriptiva o predictiva y herramientas de hoja de cálculo. Una señal de herramienta institucional no basta para imponer un tema.

## S03.P100.32

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de un módulo de orientación y nueve módulos con una línea de descripción cada uno, organizados por la tríada descriptiva (M1–M2), predictiva (M3–M6) y prescriptiva (M4, M7–M8), más aplicación en el negocio (M9). No incluye contenidos detallados, datos, evaluación ni resultados de aprendizaje. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Module 1: Descriptive Analytics: Gathering Insights — Identify effective methods for collecting data on customer behavior and use it to make better decisions for your business» (p. 1) — fuera de alcance: diseñar la recolección de datos (instrumentos, encuestas, experimentos) no tiene caso ni datos en el curso, y AGENTS.md privilegia datasets existentes y trazables. La señal es una sola línea de una fuente institucional, insuficiente para imponer un tema. La parte de «usar los datos para decidir» ya la cubren las preguntas de priorización de P120–P122 y P125 (P120 H01/H07, P125 H04).
  - «Module 2: Descriptive Analytics: Describing and Forecasting Future Events — use historical data such as trends and consumption patterns to estimate forecasts for the future» (p. 1) — fuera de alcance en su parte de pronóstico: pertenece a predictiva según AGENTS.md («qué resultado futuro… con qué incertidumbre»). Wharton traza la frontera de otro modo, y como evidencia institucional eso no impone identidad. La descripción de tendencias y patrones históricos ya está cubierta: series mensuales en P120 H05, P121 H06 (serie nacional frente a patrón por mes del año), P150 H04 y P152 H02.
  - «Module 5: … Interpret and visualize the results of simulation models to evaluate complex business decisions in uncertain settings» (p. 1) — fuera de alcance: visualizar resultados de simulación para evaluar decisiones bajo incertidumbre corresponde a predictiva o prescriptiva.
  - módulos 3, 4, 6, 7 y 8 (predicción del desempeño de empleados, optimización, árboles de decisión, «prescriptions») (p. 1) — fuera de alcance: son de predictiva y prescriptiva.
  - «Module 9: Application of Analytics for Business — Explain important components of different use cases of analytics in business and create a plan to put data to work in your organization» (p. 1) — marginal: un plan organizacional de adopción de analítica no es un producto descriptivo. La conexión de la pregunta con un contexto de uso ya está en el contrato `questions.json` (P120 H01) y en la pregunta de publicación de P153.

## S03.P100.33

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - algoritmo MapReduce, shuffle & sort y jobs encadenados en HDFS (pp. 28–31: «Los problemas complejos se resuelven mediante la ejecución secuencial o en paralelo de múltiples jobs de MapReduce»; «El almacenamiento intermedio en HDFS … introducen una sobrecarga») — ya cubierta: P100 H01/H04 y P101 H02 implementan exactamente map/shuffle/reduce y convenciones de salida; encadenar jobs o Spark/Hive/Pig (pp. 38, 50, 51) sería ingeniería de datos, fuera de alcance.
  - las cinco V (p. 28: «Veracidad (Precisión?) – Valor (Utilidad?)») — marginal: vocabulario; el volumen artificial de P100 ya está reconocido como límite (H03).
- **Señales de alcance de curso** (registradas sólo en este log):
  - tipología descriptiva / diagnóstica / predictiva / prescriptiva (p. 37: «Analítica Descriptiva — Análisis de la situación actual para la toma de decisiones operativas»; «Analítica Diagnóstica — … identificar las causas y factores que explican por qué se observó un resultado») — fuera de alcance como propuesta: es un encuadre conceptual; la frontera descripción/causa ya está persistida y probada en P125 H06, y la diagnóstica causal desplazaría la identidad descriptiva del curso.
  - «La analítica transforma datos en conocimiento para apoyar mejores decisiones» (p. 2) y «Business Analytics no elimina la incertidumbre. La convierte en una decisión informada» (p. 4) — marginal: refuerzo retórico de la pregunta→decisión ya presente como contrato `questions.json` (P120 H01) y priorización (P120 H07, P125 H04); no cambia lo que el estudiante hace.
  - KDD/CRISP-DM (pp. 16, 21), ML estadístico, ensembles, gradient boosting, deep learning (pp. 9, 19, 25, 48, 52), MLOps (p. 55), producto de datos y DataOps (pp. 44, 53–54), cloud (pp. 26–27) — fuera de alcance: pertenecen a predictiva o productos de datos; la idea de «tests sobre los datos en cada paso» (p. 54) ya está en P150–P154 (aserciones de grano y reconciliación) y P153 H03.
  - analítica por dominio (p. 61: «People / HR Analytics … Marketing Analytics … Inventory Analytics») — ya cubierta: P120 (retail), P121 (operaciones), P122 (cadena de suministro), P124 (marketing), P125 (personas/compensación).

## S03.P100.34

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diapositivas de un módulo DataOps que enumeran problemas organizacionales de la analítica (objetivos cambiantes, silos, mala calidad, desconfianza en los datos), mitos y brechas de conocimiento (alfabetización de datos, liderazgo) y falta de soporte (objetivos poco claros, acceso a datos, paso a producción). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Data Literacy es la habilidad de leer tablas y grafos, entenderlos para concluir correctamente y saber cuando se está potencialmente desinformado» (p. 6) — ya cubierta en parte / marginal por sí sola: los límites de lectura ya aparecen en P121 H04 (matriz día × hora como patrón agregado), P122 H03 (proporción a tiempo vs demora promedio) y P125 H06 (límite causal persistido). Si se aprueba la candidata de lectura persistida en P152 (documento `mintic-fedesoft-talento-digital-2025-2030`), esta página puede añadirse como fuente de contexto; literature-derived no la prescribe.
  - «No se deben buscar insights interesantes o responder preguntas interesantes sin un objetivo claro» y «La falta de objetivos claros puede llevar a responder preguntas de negocio de bajo valor» (p. 8); «Datos, conocimientos, decisiones y acciones no son sinónimos» (p. 8) — ya registrada: la ausencia de usuario/decisión en P120–P154 está documentada en las auditorías S02 (pregunta de auditoría 1); la diapositiva es perspectiva organizacional, no un mecanismo enseñable que cambie un taller concreto.
  - «Se sigue CRISP-DM y modelos de cascada», «Fatiga por procesos manuales», «Se ignoran los beneficios de la automatización» (pp. 2, 8) — fuera de alcance: crítica metodológica/organizacional (DataOps) propia de productos de datos; contexto histórico, no prescripción vigente.

## S03.P100.35

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Material de clase (serie DataOps) que define estrategia de datos y su cadena objetivos → diagnóstico → valor → brechas → objetivos de datos → iniciativas → gobierno/arquitectura/uso responsable → caso de valor y priorización → hoja de ruta → ejecución → evaluación, con un caso de mantenimiento predictivo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - creación de valor (mejorar, enriquecer, ofrecer información) (p. 10), análisis de brechas y su plantilla (pp. 11–12), objetivos estratégicos de datos (p. 14), iniciativas (p. 15), caso de valor con VPN/ROI (p. 19), priorización de portafolio (p. 20), hoja de ruta (p. 21), ejecución y evaluación de la estrategia (pp. 22–23) — fuera de alcance: estrategia y gestión de datos a nivel organizacional; no hay producto descriptivo ni caso con datos para enseñarlo con rigor en un taller.

## S03.P100.36

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación docente que recorre la evolución KDD → CRISP-DM → … → MAISTRO y las dimensiones de un proyecto de analítica (problema de negocio, problema analítico, datos, preparación, diseño, evaluación, operación, mejora continua, gobernanza) con un caso de abandono de clientes que transita de una pregunta descriptiva a una solución prescriptiva. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - procedencia y condiciones de uso no documentadas en P120, P121, P122, P124, P150–P154 (p. 13) — ya registrada: es un requisito de `AGENTS.md` («Case and dataset provenance») señalado en cada S02; este documento lo refuerza pero no aporta un argumento distinto por taller. Sólo se propone para P123, donde el defecto toca directamente la pregunta temporal.
  - tipología descriptiva/predictiva/prescriptiva con «¿Qué ocurrió? ¿Quiénes abandonaron?» y métodos EDA, segmentación, visualización, minería de procesos (p. 16) — ya cubierta en identidad del curso; minería de procesos: fuera de alcance (sin caso ni datos de eventos en el curso).
  - diseño de modelos, evaluación con datos no usados, despliegue, adopción, monitoreo de deriva, recalibración (pp. 17–26) — fuera de alcance: predictiva, prescriptiva y productos de datos.

## S03.P100.37

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas docentes que trasladan Lean (Toyota Production System, Lean Software y Lean Product Development) a la analítica vista como sistema de producción y de desarrollo de producto: desperdicios en analytics, *value stream mapping*, entrega rápida, teoría de restricciones, análisis de causa raíz (5 porqués, árbol de realidad actual) y capas del ciclo de vida del dato (DataOps). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - análisis de causa raíz con 5 porqués y árbol de realidad actual (p. 10) — fuera de alcance: herramienta de mejora de procesos organizacionales; aplicado a hallazgos descriptivos, empujaría a explicaciones causales que el curso no posee (cf. límite causal de P125 H06).
  - control estadístico de procesos, colas, teoría de restricciones, *value stream mapping*, versionado, orquestación, cómputo distribuido (pp. 7–9, 12) — fuera de alcance: DataOps, ingeniería de datos y productos de datos.

## S03.P100.38

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre gestión de proyectos: cascada frente a Agile (manifiesto, Scrum, XP, Kanban), escalamiento (Scrum of Scrums, SAFe, DAD), manifiesto y principios DataOps, ciclo de vida analítico y prácticas ágiles para épicas de productos de datos. Perspectiva organizacional/metodológica. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - principios DataOps «Make it reproducible», «Analytics is code», «Quality is paramount», «Reuse» (p. 10) — ya cubierta en lo que toca al curso: pruebas que recomputan los productos desde `data/` (P103 H03, P120 H08, P121 H07), funciones reutilizables (P101 H02, P123 H07) y compuerta de calidad (P153 H03). El resto (orquestación, ambientes desechables, *cycle times*) es productos de datos.
  - ciclo de vida analítico con *business understanding*, adquisición, exploración y preparación de datos (p. 11) — ya cubierta/fuera de alcance: exploración y preparación están en P106–P107, P120–P122; *feature engineering*, entrenamiento, despliegue y monitoreo pertenecen a predictiva y productos de datos.
  - Scrum, XP, Kanban, SAFe, Scrum of Scrums, *epic hypothesis statement*, MVP (pp. 2–9, 12–14) — fuera de alcance: gestión ágil de proyectos/productos; no cambia lo que el estudiante aprende en ningún taller descriptivo ni tiene caso para enseñarse con rigor en el curso.

## S03.P100.39

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas que definen DataOps como combinación de analítica, *lean thinking*, Agile y DevOps; recorren cascada, lean, Agile, DevOps, siete pasos de implementación (pruebas de datos y lógica, control de versiones, ramas, ambientes, contenedores, parametrización, «sin miedo ni heroísmo»), diferencias DevOps/DataOps, cadena de suministro de datos, MLOps, ciclo de vida de ciencia de datos y *epic hypothesis statement*. Perspectiva metodológica/organizacional orientada a productos de datos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - control de versiones, ramas, múltiples ambientes, contenedores Docker, CI/CD, orquestación y monitoreo (pp. 6–17) — fuera de alcance: ingeniería de software y productos de datos.
  - MLOps, *data science lifecycle*, *model serving* (pp. 20, 23) — fuera de alcance: predictiva y productos de datos.

## S03.P100.40

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación (diapositivas) sobre DataOps desde la perspectiva directiva. Trata los silos entre equipos (TI, ingeniería de datos, ciencia de datos, visualización, gobierno), la coordinación relacional, el flujo de desarrollo con ramas y pruebas, la eliminación de cuellos de botella con Kanban, la priorización por oportunidad, las «trampas» del CDO y las etapas de madurez de la analítica. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - priorización de resultados deseados mediante entrevistas, con puntuación de importancia y satisfacción en escala 1–10 (p. 7: «Oportunidad = Importancia + max(0, Importancia - Satisfacción)») — fuera de alcance: es una técnica de gestión del portafolio de mejoras de un equipo de datos. Sirve para formular necesidades de los usuarios, pero no describe un fenómeno con evidencia y no tiene caso ni datos en el curso. La formulación de preguntas ya está representada en P109 H01 y en el contrato `questions.json` de P120 H01.
  - ramas de desarrollo, pruebas de integración, *pre-release*, *merge* y *release* (p. 5) y ambientes de desarrollo distintos de producción (p. 4) — fuera de alcance: es ingeniería y operación de productos de datos.
  - silos, coordinación relacional, Kanban, cuellos de botella y teoría de restricciones (pp. 2–4, 6) — fuera de alcance: son gestión organizacional de equipos de datos.
  - trampas del CDO (defensa de los datos, valor diferido, proyectos largos en cascada) y etapas de madurez (Data Desert → Boutique → Waterfall → DataOps Analytics) (pp. 9, 11) — fuera de alcance: es contexto histórico y organizacional, sin consecuencia sobre lo que el estudiante hace en un taller descriptivo.

## S03.P100.41

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre DataOps aplicado a ML e ingeniería de datos: programación tradicional vs ML, deuda técnica, arquitectura canónica y arquitectura DataOps (Airflow, Jenkins, Docker, Git…), *design thinking*, *agile data warehousing*, data lake/DW/marts, esquemas para análisis, reutilización de código y fallas típicas de proyectos de analítica. Perspectiva organizacional/metodológica orientada a productos de datos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - *design thinking* para problemas mal definidos (p. 7: «Ganar entendimiento del problema consultado expertos, observando y empatizando») — fuera de alcance: metodología de diseño de productos; no tiene caso ni datos en el documento.
  - deuda técnica de ML, orquestación, ambientes, CI/CD, contenedores, herramientas de plataforma (pp. 2–8, 11) — fuera de alcance: predictiva, ingeniería de datos y productos de datos.

## S03.P100.42

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diapositivas sobre DataOps aplicado a la calidad de datos: pruebas automáticas en cada etapa del pipeline analítico (acceso, transformación, modelado, visualización, reportería), distinción entre *value pipeline* e *innovation pipeline*, ejemplos de pruebas de entradas, lógica de negocio y salidas, niveles de severidad y pruebas de balance (de ubicación, histórico, control estadístico de procesos). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Analytics es código», *value pipeline* frente a *innovation pipeline*, ambientes idénticos a producción y liberación de código (p. 3) — fuera de alcance: operación de pipelines en producción, que es del curso de productos de datos.
  - tipos de pruebas de software (unitarias, de integración, funcionales, de regresión, de desempeño, de humo) y «Cada vez que algo falla se agrega una nueva prueba» (p. 2) — fuera de alcance como contenido: el curso ya usa `pytest` sólo para verificar participación (convención de los talleres), y enseñar tipología de pruebas desplaza la identidad hacia ingeniería de software.
  - control estadístico de procesos y pruebas de balance temporal con notificación automática (p. 5: «Se monitorea cada aspecto del proceso constantemente buscando patrones anómalos») — fuera de alcance: monitoreo continuo de un producto en operación (productos de datos).

## S03.P100.43

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Artifactos no reproducibles» y «El código y la data crecen independientemente» como problemas típicos (p. 2) — marginal: la reproducibilidad del curso ya está asegurada por las pruebas que recomputan los productos desde `data/` (P103 H03, P120 H08). Versionar datos frente a código es materia de productos de datos.
- **Señales de alcance de curso** (registradas sólo en este log):
  - el rol de analista de datos o BI tiene como responsabilidades «Consulta, Limpieza, Exploración, Interpretación, Visualizaciones, Tablas, Reportes» y como habilidad «Entendimiento y análisis de datos que influencian las decisiones» (p. 5) — ya cubierta: consulta (P104, P151–P152), limpieza (P106–P107), exploración y tablas (P103, P120–P122), visualización (P103 H04, P120 H05) y reporte filtrable (P124). La «interpretación» es la debilidad conocida de varios talleres (sin lectura persistida en P150–P154), pero un perfil de cargo no aporta el método ni el caso para corregirla, y la familia sólo da contexto organizacional.
  - estructuras de equipo por función, por dominio, centralizadas o descentralizadas, sus cuellos de botella y la falta de *ownership* (pp. 2–4, 8) — fuera de alcance: es diseño organizacional, sin capacidad que el estudiante ejerza en un taller descriptivo.
  - perfiles de habilidad (I, T, Pi, M, E) y equipos «altamente productivos» (p. 7) — fuera de alcance: es contexto de gestión de talento, no una capacidad del curso.

## S03.P100.44

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - transformaciones de texto (tokenización, stemming, lematización, stopwords, p. 16) — marginal: P100 H02 ya fija la unidad textual como decisión; añadir lematización sería otra técnica para el mismo objetivo.
- **Señales de alcance de curso** (registradas sólo en este log):
  - alcance del proyecto con objetivos traducidos a criterios medibles, interesados y criterios de éxito (p. 13–14: «business objectives must be translated into measurable technical goals»; «defining success criteria») — marginal aquí: refuerza el hallazgo ya registrado en las auditorías S02 (falta usuario/decisión en casi todos los Pxxx), pero el documento no aporta un mecanismo didáctico nuevo frente a `questions.json` (P120 H01) y es literatura de gestión de proyectos, no prescripción curricular.
  - las ocho dimensiones como ciclo de proyecto (pp. 12–13, Fig. 2) y prácticas ágiles (Sprint 0, retrospectivas, p. 14 y p. 22) — fuera de alcance: gestión de proyectos analíticos; no es el producto descriptivo del curso.
  - diseño/modelado, evaluación con AUC/F1, operación, monitoreo de deriva, MLOps (§4.4, §4.5, §4.7, §4.8) — fuera de alcance: predictiva y productos de datos.

## S03.P100.45

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de ejemplos de una herramienta de minería de datos orientada a modelos predictivos (CRISP-DM); los capítulos de auditoría de datos, gráficos exploratorios, listas de decisión por segmentos y canasta de mercado son los únicos con contenido descriptivo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - metodología CRISP-DM para organizar proyectos (p. 20: «organize projects according to the Cross-Industry Standard Process for Data Mining») — fuera de alcance: marco de minería orientado a modelado; el curso se organiza por pregunta descriptiva y producto.
  - preparación automática de datos ADP (p. 63: «make your data ready for data mining quickly and easily, without needing to have prior knowledge of the statistical concepts involved»; p. 68: precisión de 10,6 % a 78,8 %) — fuera de alcance: preparación al servicio de la precisión predictiva y opaca para el estudiante, lo contrario de las decisiones explícitas de P106/P107.
  - pronóstico de series con intervalos de confianza, suavizamiento exponencial y ARIMA (pp. 165–168, 184) — fuera de alcance: pertenece a predictiva.
  - modelado causal temporal de KPI y análisis de causa raíz de atípicos (pp. 339–346) — fuera de alcance: inferencia causal y predicción; contradice el límite asociación/causalidad que sostiene P125 H06.
  - perfilamiento de grupos con reglas C5.0, árboles y modelos de respuesta (pp. 94, 325–326, 111–129) — fuera de alcance: modelos predictivos/clasificación.
  - medidas de utilidad de campaña con costos fijos y variables (p. 130: «Profit Margin = Frequency * Revenue per respondent - Cover * Variable cost») — fuera de alcance: evaluación económica de acciones (prescriptiva).

## S03.P100.46

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Guía de la metodología CRISP-DM en la herramienta SPSS Modeler: tareas, preguntas de control y reportes por fase, ilustrados con un caso de *web mining* de un e-retailer. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - formular y revisar hipótesis en la exploración (p. 20); «What additional questions have your results raised?» (p. 35); reporte final según audiencia y plan de difusión de hallazgos (pp. 39, 41) — marginal desde este documento: la falta de lectura persistida ya está registrada en auditorías (P152 H03, P154 S04) y no se sostiene por una guía de herramienta.
  - introducción: proyectos donde «your work will focus on data exploration and visualization» y modelado es menos relevante (p. 7) — contexto que respalda la identidad descriptiva; sin propuesta.
  - plan de proyecto, inventario de recursos, riesgos, costo/beneficio (pp. 11–15), modelado y diseño de pruebas (pp. 29–33), evaluación de modelos (pp. 35–37), despliegue y monitoreo (pp. 39–42) — fuera de alcance: gestión de proyectos, predictiva y productos de datos.

## S03.P100.47

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Guía de inicio de la herramienta KNIME (versión 2.x): instalación, nodos, puertos, configuración/ejecución, vistas, hiliting, preferencias, importación/exportación y meta nodos; incluye un flujo de ejemplo (lector de archivos → K-Means → color → tabla y dispersión sobre Iris). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - flujo visual de nodos configurables y ejecutables (p. 3: «A workflow is built by dragging nodes from the Node Repository onto the Workflow Editor and connecting them») — fuera de alcance: herramienta low-code alternativa; cambiar de herramienta no cambia lo que el estudiante aprende y el curso no es capacitación en plataformas. Una señal professional-learning no basta para imponer un tema.
  - ejemplo con K-Means sobre Iris (p. 5: «we read in data from an ASCII file, assign color to it, cluster the data») — fuera de alcance: modelado de agrupamiento sin pregunta descriptiva ni caso; pertenece a otro curso y el dataset es didáctico genérico.

## S03.P100.48

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Text Analysis. Analyze feedback to find common themes and trends» (p. 1) — ya cubierta en su versión descriptiva (P123 H04–H05 co-ocurrencia y comunidades; P100 H02 tokenización).
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Churn Analysis», «Forecasting», «Campaign Analysis. … targeting the people most likely to respond» (p. 1), lift y profit charts «to compare and contrast the quality of your models» (p. 2), DMX «A prediction against a data mining model is simply a join» (p. 2), algoritmos (árboles, Naïve Bayes, redes neuronales; p. 2) — fuera de alcance: predictiva.
  - «Market Basket Analysis. Determine items sold together» y «Market Analysis. Define market segments by automatically grouping like customers» (p. 1) — fuera de alcance: minería no supervisada sin caso preparado; señal de herramienta que por sí sola no impone tema.
  - «fine-grained role-based security» (p. 2) — marginal: rasgo de plataforma sin capacidad descriptiva asociada.

## S03.P100.49

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - extracción de términos y asociaciones entre palabras en texto (pp. 140–141) — ya cubierta: P100 H02 (unidad textual) y P123 H02–H04 (palabras clave y co-ocurrencia); la normalización se recoge en la candidata P123.
- **Señales de alcance de curso** (registradas sólo en este log):
  - clustering como segmentación exploratoria y su evaluación por centroides y reglas (pp. 63–64, 99–100: «How do you know if the clusters can reliably be used for business decision making?») — fuera de alcance: segmentación por modelos no supervisados trae la lógica de ML y no hay caso descriptivo en el documento; las comunidades de P123 H05 ya cubren agrupamiento descriptivo en su contexto.
  - detección de anomalías por clasificación de una clase (pp. 61–62) e importancia de atributos/EXPLAIN y PROFILE (pp. 38–43, 69–70) — fuera de alcance: modelos supervisados o de puntuación (predictiva).
  - clasificación, regresión, matriz de confusión, lift de clasificación, ROC, costos, división entrenamiento/prueba, puntuación y despliegue (pp. 20, 23, 41–43, Part II–III) — fuera de alcance: predictiva y productos de datos.
  - normalización min-max/z-score, binning automático, winsorización y recorte como preparación embebida en modelos (pp. 127–133) — fuera de alcance: preparación al servicio de algoritmos; la parte descriptiva (juicio de dominio sobre atípicos) se recoge en la candidata P106.

## S03.P100.50

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-data-mining.md` (`source_sha256`: 6396a7c9e3efce998f0bbb9907cacb228244737c80bdebcdae17ce913b7f6ce9).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - procesamiento distribuido en memoria y Hadoop (pp. 10–11) — marginal: promoción de infraestructura; P100 ya enseña el patrón MapReduce y sus límites (H01, H03).
- **Señales de alcance de curso** (registradas sólo en este log):
  - segmentación por clustering, reglas de asociación (canasta de mercado), analítica de texto como insumo de modelos (p. 5, p. 7) — fuera de alcance: técnicas de modelado no supervisado/predictivo presentadas como herramientas; el documento no aporta un caso descriptivo ni datos, y una señal professional-learning no basta para imponer el tema.
  - muestreo representativo y partición entrenamiento/prueba, sobreajuste, torneos de modelos, código de calificación, implementación y monitoreo (pp. 7–12) — fuera de alcance: predictiva y productos de datos.

## S03.P100.51

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-forecasting.md` (`source_sha256`: 7cabe87e23ff9469d7b4b9e17582dd694b8ac329ed0975bf9a26e3dcb26b5569).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el orden temporal se pierde en un sistema de archivos distribuido y hay que reordenar antes de analizar (p. 14: «sorting on a particular file system is not possible. This is particularly problematic for time series analysis») — marginal: P100 H01 ya hace visible el ordenamiento como *shuffle*. La infraestructura distribuida no es materia del curso.
- **Señales de alcance de curso** (registradas sólo en este log):
  - identificar series cortas e intermitentes (p. 88: «short series … intermittent time series (for example, a series that contains a large number of zero values)») — fuera de alcance: su propósito declarado es elegir métodos de pronóstico (predictiva).
  - SSA, descubrimiento de motivos, similitud con DTW y extracción de características (pp. 42–51) — fuera de alcance: técnicas de reducción de dimensión para aprendizaje automático, sin caso descriptivo en el curso.
  - simulaciones *rolling*, comparación de modelos, escenarios *what-if*, control charts del error, FVA, ML y redes neuronales (pp. 99–102, 153–154, 166–168, 77–82) — fuera de alcance: pertenecen a predictiva (evaluación de pronósticos) o a prescriptiva y productos de datos (escenarios y monitoreo).

## S03.P100.52

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-stat.md` (`source_sha256`: 2977c390790a2e7206c4e754753b180908bbc6165dba6d6b29031a0c9e190ca7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Manual de referencia de PROC REG: ajuste por mínimos cuadrados, nueve métodos de selección de variables, pruebas de hipótesis, colinealidad, residuos e influencia, y gráficos de diagnóstico de ODS Graphics. Ejemplos: salarios de béisbol, predicción de aptitud aeróbica, peso por estatura y edad, variables cualitativas, ridge y falta de ajuste. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - ajuste de regresión lineal y polinómica con lectura de ANOVA, R², valores *p* y ecuación ajustada (pp. 6–7, 10–11, 16–17: «R-square of 0.77 indicates that Height accounts for 77% of the variation in Weight») — fuera de alcance: modelar y explicar varianza le corresponde a predictiva y a Estadística; sería meter capacitación en Estadística dentro de descriptiva.
  - nueve métodos de selección de variables (FORWARD, BACKWARD, STEPWISE, MAXR, RSQUARE, CP…) con criterios AIC/BIC/Cp (pp. 5, 160–178) — fuera de alcance: construcción de modelos predictivos («The goal is to develop an equation to predict fitness», p. 160).
  - advertencia de que los estadísticos quedan sesgados tras seleccionar el modelo, y de que hace falta teoría sustantiva (p. 93: «no statistical method can be relied on to identify the "true" model»; p. 178: «the p-values for the parameter estimates are not valid») — fuera de alcance: es un guardrail de inferencia tras la selección. El curso no hace selección de modelos.
  - residuos estudentizados > 2 como atípicos, leverage > 2p/n y Cook's D como influencia (pp. 11, 107, 146–147: «Studentized residuals … can be used to identify outlying or extreme observations») — fuera de alcance: los atípicos se definen respecto de un modelo ajustado. Para describir atípicos en descriptiva haría falta exploración de distribuciones, no diagnóstico de regresión, y el documento no ofrece esa variante.
  - paneles de diagnóstico (Q-Q, histograma y box plot de residuos, observado frente a predicho, gráfico RF, residuos frente a regresor con loess) (pp. 9, 13–15, 149, 153) — fuera de alcance: son evidencia visual sobre la adecuación del modelo, no sobre el fenómeno descrito. El principio de «evidencia visual antes de decidir» ya lo exige `AGENTS.md` para todos los notebooks.
  - una observación muy influyente (Pete Rose) domina el ajuste y se excluye para reajustar (pp. 147–148: «Pete Rose is the highly influential observation. You might obtain a better fit … if you omit his statistics») — fuera de alcance como técnica. Como idea («pocos casos pueden dominar un resumen») ya está cubierta por los umbrales de volumen de P120 H06, P121 H05 y P122 H06, y por el doble criterio de P125 H04.
  - colinealidad, VIF y regresión ridge (pp. 190–193), y prueba de falta de ajuste con réplicas (pp. 194–195) — fuera de alcance: estimación estadística y diseño experimental.

## S03.P100.53

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - técnicas oficiales de modelado dimensional de Kimball (hechos, dimensiones de calendario, dimensiones de cambio lento, dimensiones conformadas, jerarquías). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - tablas de fotos periódicas y medidas semiaditivas (pp. 7–8), tablas de hechos sin medidas (p. 8), dimensiones conformadas, matriz de bus y *drill-across* (pp. 13–14), tablas puente (p. 21) — fuera de alcance por caso: el curso tiene un solo proceso transaccional (ventas); la no aditividad sí entra en P154 T01.

## S03.P100.54

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sílabo de un curso de posgrado de data warehousing y BI (modelado ER y dimensional de Kimball, SAP BusinessObjects y Tableau). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - universos de SAP BusinessObjects, *loops*, *chasm traps* y *fan traps*, IDT y Web Intelligence (pp. 3–4) — fuera de alcance: plataforma concreta; el doble conteo que ilustran las trampas *fan/chasm* se trata como no aditividad en P154 T01.
  - seguridad por fila (p. 4) — fuera de alcance: productos de datos.
  - tablas de fotos (*snapshot*) y hechos sin medidas (p. 3) — fuera de alcance por caso (un solo proceso transaccional).
