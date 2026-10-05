# Log — P307

## S02.P307.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P307_decision_informada_por_pronosticos/` (tres archivos de `data/`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, tres CSV de `submission/`, `tests/test_activity.py`); relación con P300, P302 y P304.
- **Trazabilidad revisada:** P307 → `prescriptiva.C01`–`C05`; C01 parcial, C02 sustentada, C03 y C05 no evidenciadas, C04 mínima.
- **Highlights:** añadidos H01–H04 (escenarios y gobierno como datos; valor y quiebre; guardia antes de maximizar; política persistida).
- **Ambigüedades:** (1) la guardia de servicio no cambia la decisión: 110 es también el máximo sin restricción y está en el borde (0,25); (2) `order_comparison.csv` en `submission/` no lo produce el código actual; (3) notebook de dos celdas sin evidencia visual, importando `main` desde `src/` vacío; (4) no hay pronóstico construido: el título «informada por pronósticos» descansa en escenarios dados; (5) trazabilidad a cinco capacidades excede la evidencia; (6) posible duplicación técnica con P300/P302 y solapamiento con P304.
- **Superficies / contrato / dependencias:** S01–S05; pruebas de forma; recibe patrón de P300/P302; no habilita actividades posteriores.
- **Auditoría de Analytics:** auditoría no resuelta para el producto prescriptivo completo: hay acción factible, guardia, dueño, cadencia y gatillo, pero faltan excepción, validación (líneas base, sensibilidad) y monitoreo de resultados.

## S03.P307.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Plan de examen de la certificación CAP-Pro, derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio y del problema analítico, datos, selección de método, desarrollo de modelos, despliegue y gestión del ciclo de vida de la solución) con subtareas evaluables. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cadenas de suministro *just-in-time* que «forecast consumer demand … and optimize production and shipping», con riesgo de escasez de alimentos o medicinas (p. 32). Categoría: ya cubierta. Pedido por escenarios en P307 H01–H03; abastecimiento con guarda de escasez en P316 H01 y H07.

## S03.P307.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de ocho módulos sobre capacidades de IA, aprendizaje automático, NLP, robótica, estrategia, equipos y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: describe los fundamentos probabilísticos de la inferencia y «the modeling and decision-making life cycle … including its human, social, and ethical implications». Sólo lista temas; no hay syllabus, casos, productos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - caso LondonTime «¿Cuántos relojes de moda debe pedir LondonTime antes de que comience la temporada de venta?» (p. 9) — ya cubierta: es el problema de pedido único bajo demanda incierta de P307 (H02–H03).

## S03.P307.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online sobre historia de la web y la nube, Node.js, contenedores y llaves, DevOps y sus métricas, casos de migración, serverless, empresa ágil y cloud native. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso ejecutivo de 8 semanas sobre estrategia y ecosistema de datos (IA para líderes, plataformas y diseño de bases de datos, modern data stack, nube, Lean DevOps, ética/gobierno de datos). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión e inferencia causal, clasificación, deep learning, sistemas de recomendación y redes y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre el proceso de diseño de productos de IA (fundamentos de ML y deep learning, interacción humano–computador, «superminds», modelo de Lawler) con capstone de propuesta de producto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online de estrategia y arquitectura de plataformas digitales y mercados de dos lados (efectos de red, precios, APIs y estándares, gating de calidad, regulación, modelado de dinámica de plataforma). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso corto en línea de MIT: ODE y métodos numéricos, PDE y modelado espacial, mínimos cuadrados y optimización (gradiente, Newton), del ajuste al aprendizaje automático, métodos probabilísticos (Monte Carlo, pronóstico probabilístico, sensibilidad, eventos raros) y tres casos industriales. Sólo lista títulos de módulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un certificado de 6 meses en ingeniería de datos (Python, SQL, ETL/CDC, contenedores, Hadoop/Spark/Airflow, streaming con Kafka/MQTT, nociones de ML, aprendizaje por refuerzo y redes profundas) con proyectos de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de seis meses con cinco partes (fundamentos, optimización, ML, ML avanzado, despliegue), casos de estudio y capstone de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso profesional en línea de MIT: decisiones tempranas de trade-off (Pugh, estudios de trade), modelos de valor con atributos jerárquicos, generación y evaluación de espacios de diseño, y exploración del tradespace (Pareto, sensibilidad, robustez, asignación de tareas entre modelos y personas). Sólo títulos y descripciones semanales; sin contenido técnico. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre prototipado rápido en fabricación (procesos seriales y paralelos, mapeo de atributos de prototipo, costo–valor) con capstone de decisiones de fabricación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos, analítica predictiva, ML, IA) con una clase magistral de «Decision Analytics» que introduce optimización, simulación y análisis de decisiones para analítica prescriptiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto en cinco fases: panorama y modelos de negocio de IA, liderazgo con analítica predictiva e IA generativa/agéntica, innovación, pensamiento de futuros para la decisión estratégica y gobernanza y controles de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses con cinco cursos (ingeniería de datos, Python, estadística, IA/ML, storytelling y visualización), sin contenido prescriptivo explícito. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relato institucional de cuatro talleres participativos con 17 programas de pregrado de la UNAL (p. 7) sobre la noción de currículo, las funciones misionales, las prácticas pedagógicas y las propuestas de armonización. No contiene ningún programa ni curso de analítica, optimización, decisión o simulación, ni resultados de aprendizaje disciplinares. Sus señales son de pedagogía general y de gestión curricular institucional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular». Tiene cuatro ejes: Acuerdo 02/2020 del CESU, resultados de aprendizaje, actualización del PEP y planes de mejoramiento. Distingue tres dimensiones (macro, meso y microcurricular) y cuatro etapas. No contiene contenidos disciplinares ni menciona analítica, decisión u optimización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus de posgrado centrado en el proceso de minería de datos aplicado a datos de salud (preprocesamiento, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, clustering, minería de texto) con proyecto por entregables y survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus introductorio de pregrado centrado en bases de datos (Access, modelado ER, normalización, SQL, MongoDB), BI y visualización/dashboards, con proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa online de 12 semanas (ruta con o sin código) sobre IA generativa, prompts y RAG, agentes con herramientas, memoria, planificación y razonamiento, sistemas multiagente, pruebas/evaluación y protección de soluciones agénticas, con casos prácticos y proyectos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P307.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de curso de bodegas de datos: modelado ER y dimensional (Kimball), dimensiones lentamente cambiantes, tablas de hechos, universos de SAP Business Objects, reportes Web Intelligence y tableros en Tableau. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
