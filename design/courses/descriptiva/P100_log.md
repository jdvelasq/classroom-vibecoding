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
