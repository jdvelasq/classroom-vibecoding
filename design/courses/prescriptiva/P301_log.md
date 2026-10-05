# Log — P301

## S02.P301.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P301_air_france_447/` (`data/search_cells.csv`, `data/search_rounds.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, los cuatro artefactos de `submission/`, `tests/test_activity.py`); contexto en `activity-architecture.md`.
- **Trazabilidad revisada:** P301 → `prescriptiva.C01`; sustentada como contraste (decisión no recurrente).
- **Highlights:** añadidos H01–H06 (frontera excepcional/recurrente; cobertura vs éxito; actualización tras fracaso; repetir vs reasignar; verificación interna; persistencia del protocolo).
- **Ambigüedades:** (1) el nombre AF447 y el mapa titulado «escenario pedagógico AF447» podrían leerse como reconstrucción histórica; el notebook lo niega explícitamente; (2) sólo se observaron cinco filas de `search_cells.csv` en el volcado, aunque las aserciones fijan 25 celdas; (3) autoridad y escalamiento no se ejercen ni registran; (4) el supuesto de efectividad constante al repetir una celda está declarado pero no discutido como límite del plan.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; prueba de existencia de cuatro artefactos; recibe de P300 el formato de frontera de decisión; no habilita artefactos posteriores.
- **Auditoría de Analytics:** el producto es deliberadamente un protocolo excepcional, coherente con el diseño; no debe contarse como política recurrente gobernada. La teoría de búsqueda contribuye sin organizar el taller.

## S03.P301.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Bayesian networks para problemas diagnósticos y la inferencia (AI-Probability-based, p. 51). Categoría: ya cubierta como actualización bayesiana tras un fracaso (H03–H04). Las redes bayesianas como formalismo son fuera de alcance: llevarían el taller hacia IA y no hacia la política.

## S03.P301.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - problema no susceptible de solución analítica (p. 8: CAP-P.1.3.2) — marginal: P301 H01 ya ejerce una frontera de alcance (plan excepcional frente a política recurrente); no cambia lo que el estudiante hace.
  - línea base del estado actual (p. 12: CAP-P.2.5.1 «Identify current baseline performance») — ya cubierta: comparación contra reglas ingenuas con igual capacidad (P301 H02, P305 H02, P308 H02–H03, P313 H05, P318 H02).

## S03.P301.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de consenso sobre la formación de pregrado en ciencia de datos. Define el *data acumen*, es decir, la capacidad de «make good judgments … and ultimately make good decisions using data» (p. 22), en diez áreas conceptuales, y recomienda integrar la ética en todo el currículo y adoptar un código o juramento profesional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de ocho módulos sobre capacidades de IA, aprendizaje automático, NLP, robótica, estrategia, equipos y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «frequentist and Bayesian decision-making» (p. 1) — ya cubierta: P301 actualiza creencias tras un fracaso (H03–H04) y P322 valora una medición por su efecto en la acción (H01–H02). Un tema listado en un catálogo no muestra qué falta en esos talleres.

## S03.P301.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa ejecutivo online de 11 semanas sin código: sesgos, descriptiva, big data, experimentación, ML, redes neuronales, dos módulos de prescriptiva (árboles de decisión; sesgos de economía del comportamiento) y ética/legal, con casos y tareas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online sobre historia de la web y la nube, Node.js, contenedores y llaves, DevOps y sus métricas, casos de migración, serverless, empresa ágil y cloud native. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso ejecutivo de 8 semanas sobre estrategia y ecosistema de datos (IA para líderes, plataformas y diseño de bases de datos, modern data stack, nube, Lean DevOps, ética/gobierno de datos). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión e inferencia causal, clasificación, deep learning, sistemas de recomendación y redes y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre el proceso de diseño de productos de IA (fundamentos de ML y deep learning, interacción humano–computador, «superminds», modelo de Lawler) con capstone de propuesta de producto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online de estrategia y arquitectura de plataformas digitales y mercados de dos lados (efectos de red, precios, APIs y estándares, gating de calidad, regulación, modelado de dinámica de plataforma). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso corto en línea de MIT: ODE y métodos numéricos, PDE y modelado espacial, mínimos cuadrados y optimización (gradiente, Newton), del ajuste al aprendizaje automático, métodos probabilísticos (Monte Carlo, pronóstico probabilístico, sensibilidad, eventos raros) y tres casos industriales. Sólo lista títulos de módulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un certificado de 6 meses en ingeniería de datos (Python, SQL, ETL/CDC, contenedores, Hadoop/Spark/Airflow, streaming con Kafka/MQTT, nociones de ML, aprendizaje por refuerzo y redes profundas) con proyectos de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de seis meses con cinco partes (fundamentos, optimización, ML, ML avanzado, despliegue), casos de estudio y capstone de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso profesional en línea de MIT: decisiones tempranas de trade-off (Pugh, estudios de trade), modelos de valor con atributos jerárquicos, generación y evaluación de espacios de diseño, y exploración del tradespace (Pareto, sensibilidad, robustez, asignación de tareas entre modelos y personas). Sólo títulos y descripciones semanales; sin contenido técnico. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre prototipado rápido en fabricación (procesos seriales y paralelos, mapeo de atributos de prototipo, costo–valor) con capstone de decisiones de fabricación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos, analítica predictiva, ML, IA) con una clase magistral de «Decision Analytics» que introduce optimización, simulación y análisis de decisiones para analítica prescriptiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto en cinco fases: panorama y modelos de negocio de IA, liderazgo con analítica predictiva e IA generativa/agéntica, innovación, pensamiento de futuros para la decisión estratégica y gobernanza y controles de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses con cinco cursos (ingeniería de datos, Python, estadística, IA/ML, storytelling y visualización), sin contenido prescriptivo explícito. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relato institucional de cuatro talleres participativos con 17 programas de pregrado de la UNAL (p. 7) sobre la noción de currículo, las funciones misionales, las prácticas pedagógicas y las propuestas de armonización. No contiene ningún programa ni curso de analítica, optimización, decisión o simulación, ni resultados de aprendizaje disciplinares. Sus señales son de pedagogía general y de gestión curricular institucional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular». Tiene cuatro ejes: Acuerdo 02/2020 del CESU, resultados de aprendizaje, actualización del PEP y planes de mejoramiento. Distingue tres dimensiones (macro, meso y microcurricular) y cuatro etapas. No contiene contenidos disciplinares ni menciona analítica, decisión u optimización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus de posgrado centrado en el proceso de minería de datos aplicado a datos de salud (preprocesamiento, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, clustering, minería de texto) con proyecto por entregables y survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus introductorio de pregrado centrado en bases de datos (Access, modelado ER, normalización, SQL, MongoDB), BI y visualización/dashboards, con proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa online de 12 semanas (ruta con o sin código) sobre IA generativa, prompts y RAG, agentes con herramientas, memoria, planificación y razonamiento, sistemas multiagente, pruebas/evaluación y protección de soluciones agénticas, con casos prácticos y proyectos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de curso de bodegas de datos: modelado ER y dimensional (Kimball), dimensiones lentamente cambiantes, tablas de hechos, universos de SAP Business Objects, reportes Web Intelligence y tableros en Tableau. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 5. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - una lista de títulos de métodos y herramientas de un programa de business analytics, sin descripciones, objetivos ni evaluación: recolección de datos, A/B testing, correlación y causalidad, pronóstico, regresión, «Simulation Toolkit» (Analysis ToolPak, Solver), visualización, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Módulo 8 (p. 1: «Determine the most favorable outcome for a business decision using decision trees in conjunction with optimization and simulation»). Categoría: **marginal**. La estructura de decisión secuencial bajo incertidumbre, que es lo que modela un árbol (medir → señal → actuar), ya la ejerce P322 (H01–H02, valor de la información muestral con regla condicionada a la señal), y P301 actualiza creencias tras un resultado (H03–H04). Integrar el árbol con optimización y simulación sería una técnica adicional sin un producto de política distinto. `AGENTS.md` advierte que un árbol de decisión aislado no basta como producto terminal. Las carencias de P322 (sin valor de la información perfecta ni sensibilidad) ya están en su log S02, y el temario no las justifica de forma independiente.

## S03.P301.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: conferencia histórica en diapositivas que recorre 50 años de hitos (RDBMS, SQL, DW/ETL, BI, minería, CRISP-DM, data science, big data, producto de datos, DataOps/MLOps, modelos fundacionales, IA agéntica) bajo la tesis «la analítica transforma datos en conocimiento para apoyar mejores decisiones». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 10. Lectura: completa (pp. 2–9 en texto). Las pp. 1 y 10 tienen poco texto: sólo repiten el título, que funciona como portada y cierre. No se pudieron renderizar porque el PDF no existe en `/mnt/user-data/uploads/classroom-vibecoding/design/benchmarks-pdf/literature-derived/`. Por su posición y su título no parecen tener contenido sustantivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre estrategia de datos (diagnóstico, brechas, objetivos, iniciativas, gobierno, uso responsable, caso de valor, priorización, hoja de ruta y evaluación), ilustrada con un caso de mantenimiento predictivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - recorrido histórico de metodologías (KDD, CRISP-DM, ASUM-DM, TDSP, INFORMS, CRISP-ML(Q)) y ciclo de vida completo de una solución analítica, ilustrado con un caso de abandono de clientes que pasa de predicción a decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: diapositivas de un curso de DataOps que trasladan Lean (TPS, Lean Software/Product Development, desperdicios, value stream mapping, teoría de restricciones, 5 porqués) al ciclo de vida de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación docente sobre gestión de proyectos: cascada frente a Agile, Scrum, XP, Kanban, escalamiento (Disciplined Agile, Scrum of Scrums, SAFe), manifiesto DataOps y prácticas ágiles para iniciativas de analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación docente que define DataOps como combinación de analítica, *lean*, *agile* y DevOps, con pasos de implementación (pruebas, versionado, ambientes, contenedores, parametrización), MLOps, ciclo de vida de ciencia de datos y la plantilla de *epic hypothesis*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación organizacional: silos entre equipos de datos, coordinación relacional, flujo de desarrollo y pruebas (ramas, tests de datos y de código), cuellos de botella con Kanban, priorización de mejoras por «oportunidad», trampas del CDO y etapas de madurez de la analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
