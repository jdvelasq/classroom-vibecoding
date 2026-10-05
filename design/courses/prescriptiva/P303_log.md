# Log — P303

## S02.P303.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P303_politicas_y_supervision_humana/` (`data/applications.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, `submission/review_policy.csv`, `submission/policy_contract.json`, `tests/test_activity.py`); relación con P300 y P302.
- **Trazabilidad revisada:** P303 → `prescriptiva.C01`, `C04`; sustentadas.
- **Highlights:** añadidos H01–H04 (precedencia y autoridad; puntaje vs acción; registro versionado; salvaguardas).
- **Ambigüedades:** (1) el volcado muestra sólo cinco de seis solicitudes y la fila A05 de `review_policy.csv` truncada; no se puede confirmar que la rama «recomendar_rechazo» se ejercite (ninguna solicitud visible con documentación completa y monto ≤ 10.000 supera 0,30); (2) umbrales 0,08, 0,30 y 10.000 sólo en código, ausentes del contrato; (3) el notebook importa `main` desde `src/`, vacío; (4) procedencia de las solicitudes y de la probabilidad no documentada.
- **Superficies / contrato / dependencias:** S01–S05; prueba de columnas y campos no vacíos; recibe de P300/P302; práctica retomada en P306.
- **Auditoría de Analytics:** regla prescriptiva por entidad con autoridad humana y escalamiento; faltan validación de umbrales y monitoreo ejecutado. Identidad de Analytics preservada.

## S03.P303.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify steps needed to ensure that a decision-making system is auditable» (PR-On Automation, p. 110). Categoría: ya cubierta por el registro por solicitud con versión, razón y autoridad (H03) y las salvaguardas declaradas (H04).

## S03.P303.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Plan de examen de la certificación CAP-Pro, derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio y del problema analítico, datos, selección de método, desarrollo de modelos, despliegue y gestión del ciclo de vida de la solución) con subtareas evaluables. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Declaring the grain … becomes a binding contract on the design» (p. 5) aplicado al registro de decisiones por solicitud (H03) — marginal: P303 y P306 H08 ya fijan una fila por decisión con versión y razón; nombrar el grano no cambia lo que el estudiante hace.
  - dimensiones tipo 2 con fechas de vigencia (p. 15) para historiar versiones de política («una sola versión; sin historial») — fuera de alcance: es diseño de almacenamiento (Productos de datos / Fundamentos de data), no semántica de la política.

## S03.P303.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de consenso sobre la formación de pregrado en ciencia de datos. Define el *data acumen*, es decir, la capacidad de «make good judgments … and ultimately make good decisions using data» (p. 22), en diez áreas conceptuales, y recomienda integrar la ética en todo el currículo y adoptar un código o juramento profesional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Necesitamos personas que… entiendan el problema de negocio, que puedan traducir preguntas estratégicas en modelos analíticos y que comuniquen resultados de manera efectiva a stakeholders no técnicos» (p. 173); «evaluar trade-offs y tomar decisiones informadas» (p. 177) — ya cubierta: el contrato de política (P300 H03, P302 H04) y las razones de descarte (P302 H01) responden a esa traducción. El intercambio explícito aparece en P307 H02, P309 H04 y P317 H02.

## S03.P303.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - interacción humano–IA con supervisión, criterio y responsabilidad en contextos de alto riesgo (p. 5: «Interacción humano - IA: supervisión, criterio y responsabilidad en contextos de alto riesgo») — ya cubierta: P303 H01–H04 (autoridad por motivo y salvaguardas no negociables), P308 H06 (aprobación obligatoria y anulación con motivo).

## S03.P303.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: describe los fundamentos probabilísticos de la inferencia y «the modeling and decision-making life cycle … including its human, social, and ethical implications». Sólo lista temas; no hay syllabus, casos, productos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa ejecutivo online de 11 semanas sin código: sesgos, descriptiva, big data, experimentación, ML, redes neuronales, dos módulos de prescriptiva (árboles de decisión; sesgos de economía del comportamiento) y ética/legal, con casos y tareas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online sobre historia de la web y la nube, Node.js, contenedores y llaves, DevOps y sus métricas, casos de migración, serverless, empresa ágil y cloud native. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso ejecutivo de 8 semanas sobre estrategia y ecosistema de datos (IA para líderes, plataformas y diseño de bases de datos, modern data stack, nube, Lean DevOps, ética/gobierno de datos). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - falsos positivos/negativos, precisión/*recall* en fraude (p. 9) — fuera de alcance: evaluación de clasificadores (Predictiva); P303 y P305 toman la probabilidad como dada.

## S03.P303.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Learn to define an appropriate level of machine involvement in interactions with humans and computers» (p. 7, semana 5) — ya cubierta: P303 H01 enruta cada caso a una autoridad humana y P304 H06 justifica la automatización acotada por latencia; es la capacidad `prescriptiva.C04`.

## S03.P303.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online de estrategia y arquitectura de plataformas digitales y mercados de dos lados (efectos de red, precios, APIs y estándares, gating de calidad, regulación, modelado de dinámica de plataforma). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso corto en línea de MIT: ODE y métodos numéricos, PDE y modelado espacial, mínimos cuadrados y optimización (gradiente, Newton), del ajuste al aprendizaje automático, métodos probabilísticos (Monte Carlo, pronóstico probabilístico, sensibilidad, eventos raros) y tres casos industriales. Sólo lista títulos de módulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un certificado de 6 meses en ingeniería de datos (Python, SQL, ETL/CDC, contenedores, Hadoop/Spark/Airflow, streaming con Kafka/MQTT, nociones de ML, aprendizaje por refuerzo y redes profundas) con proyectos de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de seis meses con cinco partes (fundamentos, optimización, ML, ML avanzado, despliegue), casos de estudio y capstone de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «review of task allocation between models and people in the design process» / «Humans, Methods, and Models» (p. 4) — ya cubierta: autoridad, escalamiento y modo de ejecución proporcional (P303 H01, P304 H06, C04).

## S03.P303.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre prototipado rápido en fabricación (procesos seriales y paralelos, mapeo de atributos de prototipo, costo–valor) con capstone de decisiones de fabricación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos, analítica predictiva, ML, IA) con una clase magistral de «Decision Analytics» que introduce optimización, simulación y análisis de decisiones para analítica prescriptiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - configurar flujos de trabajo y decisiones para ML (p. 16: «Configuring workflows and decisions for machine learning (ML)») — ya cubierta: modo proporcional de ejecución por entidad (P303 H01) y automatización acotada con autoridad sobre parámetros (P304 H06).

## S03.P303.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses con cinco cursos (ingeniería de datos, Python, estadística, IA/ML, storytelling y visualización), sin contenido prescriptivo explícito. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relato institucional de cuatro talleres participativos con 17 programas de pregrado de la UNAL (p. 7) sobre la noción de currículo, las funciones misionales, las prácticas pedagógicas y las propuestas de armonización. No contiene ningún programa ni curso de analítica, optimización, decisión o simulación, ni resultados de aprendizaje disciplinares. Sus señales son de pedagogía general y de gestión curricular institucional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular». Tiene cuatro ejes: Acuerdo 02/2020 del CESU, resultados de aprendizaje, actualización del PEP y planes de mejoramiento. Distingue tres dimensiones (macro, meso y microcurricular) y cuatro etapas. No contiene contenidos disciplinares ni menciona analítica, decisión u optimización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus de posgrado centrado en el proceso de minería de datos aplicado a datos de salud (preprocesamiento, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, clustering, minería de texto) con proyecto por entregables y survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus introductorio de pregrado centrado en bases de datos (Access, modelado ER, normalización, SQL, MongoDB), BI y visualización/dashboards, con proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «sistemas que actúen de manera autónoma, razonen por sí mismos y ejecuten tareas complejas con una supervisión mínima» (p. 3) y agentes «programados para tomar decisiones informadas y resolver problemas complejos de manera autónoma» (p. 12) — ya cubierta/fuera de alcance: el curso ya enseña el modo proporcional de ejecución (automatización acotada con escalamiento en P304 H06; aprobación obligatoria en P308 H06; enrutamiento a autoridad en P303 H01); la autonomía agéntica como tecnología pertenece a otro curso y desplazaría la identidad hacia la herramienta.
  - módulo 03 «Registro de la toma de decisiones para una mayor transparencia», «Evaluación con intervención humana» (p. 13) — ya cubierta: el registro versionado por decisión y la autoridad humana están en P303 H03–H04, P306 H07–H08 y P321 H01–H03; el folleto no aporta método ni forma de evidencia distinta.

## S03.P303.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de curso de bodegas de datos: modelado ER y dimensional (Kimball), dimensiones lentamente cambiantes, tablas de hechos, universos de SAP Business Objects, reportes Web Intelligence y tableros en Tableau. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 5. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - una lista de títulos de métodos y herramientas de un programa de business analytics, sin descripciones, objetivos ni evaluación: recolección de datos, A/B testing, correlación y causalidad, pronóstico, regresión, «Simulation Toolkit» (Analysis ToolPak, Solver), visualización, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - temario de un programa ejecutivo de Business Analytics. Tiene un módulo de orientación y nueve módulos, en secuencia descriptiva → predictiva → prescriptiva → aplicación, cada uno con un título y una frase de resultado. Los módulos 4, 5, 7 y 8 tocan optimización, simulación y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «2026 — Agentic AI… agentes inteligentes… ejecutan de forma autónoma procesos completos» y la pregunta de cierre «Si una máquina puede analizar, recomendar, decidir y ejecutar… ¿qué queda para nosotros?» (pp. 60, 63) — ya cubierta: la autoridad humana proporcional (automatizar, recomendar con aprobación o escalar) es C04 y se ejerce en P303 H01, P304 H06 y P308 H06; la pregunta motiva el curso pero no añade capacidad.

## S03.P303.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Las decisiones son influenciadas por factores emocionales, situaciones y culturales y siguen siendo basadas en experiencia e intuición» (p. 2); «Se continúan tomando decisiones basadas en hipótesis o criterios» (p. 6) — ya cubierta: la regla explícita con precedencias, razón y versión (P303 H01–H03) y el contrato de política (P300 H03) responden a ese diagnóstico. La fuente no propone ningún mecanismo adicional.
  - mito «El modelo es sabio y omnisciente» (pp. 3–6) — ya cubierta: la autoridad humana, el escalamiento y la anulación con motivo están en P303 H01–H02, P308 H06 y P306 H07 (banda de revisión). La tasa de anulación como señal de revisión está en P308 H07.

## S03.P303.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre estrategia de datos (diagnóstico, brechas, objetivos, iniciativas, gobierno, uso responsable, caso de valor, priorización, hoja de ruta y evaluación), ilustrada con un caso de mantenimiento predictivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - recorrido histórico de metodologías (KDD, CRISP-DM, ASUM-DM, TDSP, INFORMS, CRISP-ML(Q)) y ciclo de vida completo de una solución analítica, ilustrado con un caso de abandono de clientes que pasa de predicción a decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: diapositivas de un curso de DataOps que trasladan Lean (TPS, Lean Software/Product Development, desperdicios, value stream mapping, teoría de restricciones, 5 porqués) al ciclo de vida de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación docente sobre gestión de proyectos: cascada frente a Agile, Scrum, XP, Kanban, escalamiento (Disciplined Agile, Scrum of Scrums, SAFe), manifiesto DataOps y prácticas ágiles para iniciativas de analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación docente que define DataOps como combinación de analítica, *lean*, *agile* y DevOps, con pasos de implementación (pruebas, versionado, ambientes, contenedores, parametrización), MLOps, ciclo de vida de ciencia de datos y la plantilla de *epic hypothesis*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación organizacional: silos entre equipos de datos, coordinación relacional, flujo de desarrollo y pruebas (ramas, tests de datos y de código), cuellos de botella con Kanban, priorización de mejoras por «oportunidad», trampas del CDO y etapas de madurez de la analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre DataOps aplicado a ciencia de datos y ML: deuda técnica, pruebas automáticas, ambientes, orquestación, contenedores, arquitectura de datos y prácticas ágiles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.44

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre calidad de datos en DataOps: pruebas automáticas en cada etapa del pipeline (entradas, lógica de negocio, salidas), severidad con acción asociada (detener, investigar, informar), pruebas de balance por ubicación, balance histórico y control estadístico de procesos, y la separación entre pipeline de valor (datos variables) y de innovación (código variable). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.45

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data product owner … Responsable por el éxito del producto de datos y represéntale al usuario» y «Stakeholder: Usuario» (pp. 5–6) — ya cubierta/marginal: la autoridad y el dueño de la decisión ya son campos obligatorios del contrato (P300 H03, P303 H01); el documento habla del dueño de un producto de datos, no de la autoridad sobre una acción.

## S03.P303.46

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - gobierno: «establishment of criteria that avoid arbitrary thresholds in variable selection» (p. 20) — marginal: la frase se refiere a selección de variables en modelado, no a umbrales de decisión; aunque los logs S02 registran umbrales no derivados (P303 0,08/0,30/10.000; P311 gatillos; P315 40/60 min; P320 0,10), esta fuente no aporta un método para derivarlos y P312 H02 ya enseña a anclar un umbral en el punto de indiferencia.

## S03.P303.47

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Regla de segmentos interpretables con exclusión explícita, «these segments capture almost 8,000 records with zero hits between them, so it makes sense to exclude them from future offers» (p. 124), y segmentos personalizados «based on your own business rules» (p. 135) — marginal: una regla por segmentos con exclusiones es otra forma de la regla con precedencias de P303 (H01) y de la banda de revisión de P306 (H07); cambiaría la técnica de minería, no lo que el estudiante hace con la política.
  - Elegir el corte según el costo de los errores, «What constitutes a "desirable" gain depends on the cost of Type I and Type II errors» y el corte 0,248 para el 30 % superior (pp. 303–304) — ya cubierta en el curso: el corte derivado del valor/costo está en P304 (H02–H03, costo de oportunidad) y P306 (H03); P303 tiene como contribución el enrutamiento por autoridad y su límite S02 (umbrales sin justificación) no tiene datos de resultados con los que evaluar errores. Una señal de herramienta no basta para cambiar su caso.

## S03.P303.48

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reglas aplicadas automáticamente a nuevos registros y actualización con criterio humano (p. 40: «Updating the rulesets is not an automatic process because cluster creation requires human input») — ya cubierta: P303 H01/H04 (autoridad humana por motivo) y P304 H06 (automatización acotada con autoridad sobre parámetros).

## S03.P303.49

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Manual de inicio de la herramienta KNIME: instalación, nodos y puertos, un flujo de ejemplo con K-Means, vistas del entorno, preferencias, importación/exportación y metanodos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.50

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Churn Analysis. Create reports showing customers at risk of canceling their service» (p. 1). Categoría: fuera de alcance. Es un producto descriptivo o predictivo (reporte de riesgo). La política que usa el riesgo como insumo ya está en P303 H02 y P306 H02.

## S03.P303.51

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - scoring en tiempo real dentro de una transacción: «a sales representative could run a model that predicts the likelihood of fraud within the context of an online sales transaction» (p. 20); operadores SQL `PREDICTION_PROBABILITY` para desplegar modelos (pp. 29, 34). Fuera de alcance: desplegar e integrar en aplicaciones es tarea de Productos de datos. Lo prescriptivo, la automatización acotada por latencia con autoridad humana sobre parámetros, ya está en P304 (H06).
  - PREDICT elige el umbral que maximiza la exactitud promedio por clase (p. 42), y la exactitud engaña con clases desbalanceadas y priors (p. 59). Fuera de alcance: son calibración y evaluación del clasificador (Predictiva). El umbral por exactitud es justo el criterio que la candidata de P303 reemplaza por costos.

## S03.P303.52

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/perceptual-edge-dashboard-design-requirements-questionnaire.md` (`source_sha256`: b2fda9a2366e49604d91b330424c4fdf5d9ee294068f4c8b998f1a188fb30a6c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.53

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` (`source_sha256`: 5d936194154a3c8774fd7df35e28c7a427fb9d4348130b86ae9c6ec58946548f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: taller práctico de BI empresarial en Power BI: diseño extensible, versionado y DevOps de archivos, gobierno y certificación de datasets, Power Query, modelado dimensional, DAX/medidas, refresco incremental, pipelines de despliegue. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.54

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-data-mining.md` (`source_sha256`: 6396a7c9e3efce998f0bbb9907cacb228244737c80bdebcdae17ce913b7f6ce9).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - decisiones estratégicas (humanas) frente a operativas automáticas (p. 4: «Las decisiones operativas son automáticas – como las calificaciones de crédito … – y no requieren de la intervención humana») — ya cubierta, y el curso la trata con más matiz: P303 H01–H04 enruta cada solicitud de crédito a una autoridad humana y declara «no se automatiza la decisión crediticia»; la afirmación del documento no corrige ningún defecto del taller.

## S03.P303.55

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-forecasting.md` (`source_sha256`: 7cabe87e23ff9469d7b4b9e17582dd694b8ac329ed0975bf9a26e3dcb26b5569).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Colección de artículos técnicos sobre construcción y evaluación de pronósticos con software SAS; el uso de pronósticos para decisiones aparece sólo como motivación (pp. 7, 13, 37, 100). **No contiene** secciones sustantivas de inventario, demand planning, FVA ni planeación por escenarios: los white papers de Chase y Gilliland son extractos de 2–3 páginas y sus secciones de FVA (pp. 160, 166) sólo figuran en el índice. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P303.56

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-stat.md` (`source_sha256`: 2977c390790a2e7206c4e754753b180908bbc6165dba6d6b29031a0c9e190ca7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Manual de referencia de la sintaxis y los detalles de PROC REG: regresión lineal por mínimos cuadrados, nueve métodos de selección de modelos, diagnósticos de colinealidad, influencia y heterocedasticidad, pruebas lineales y de falta de ajuste, ridge y puntuación de datos nuevos. Es estimación estadística y predictiva; no trata decisiones, acciones ni políticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
