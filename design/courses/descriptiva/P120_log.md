# Log — P120

## S02.P120.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P120_retail_sales/` (`data/sales.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con `questions.json` y nueve CSV, `tests/conftest.py`, `tests/test_activity.py`); P100–P109 como contexto de secuencia.
- **Trazabilidad revisada:** P120 → `descriptiva.C01`, `C02`, `C03` en `implementation/descriptiva/traceability.yaml`; coherente con la evidencia. C04 y C05 no mapeados ni evidenciados de forma explícita.
- **Highlights añadidos:** H01–H08 (preguntas enlazadas, grano y consistencia, devolución binaria a valor neto, dos tasas, magnitud y tasa en un gráfico, umbral de volumen y matriz, riesgo vs prioridad, persistencia verificada). Highlight obligatorio de caso y datos: H03.
- **Cambios realizados:** creación de `P120_activity.md`; no se modificó la implementación ni se crearon propuestas.
- **Ambigüedades:** procedencia de `sales.csv` no documentada (real o sintética); tasa global de devolución cercana a 0,5 no comentada en el notebook; las pruebas no verifican `questions.json`; la pregunta de medios de pago no fija criterio de «requiere investigación»; diferencias entre categorías de alrededor de un punto se presentan sin incertidumbre.
- **Cambios de IDs:** ninguno (primera asignación).
- **Superficies, contrato y dependencias:** S01–S06 declaradas; contrato separa notebook, diez archivos de `submission/` y pruebas; dependencias demostrables con P103/P104 (patrón de resumen y prueba) y hacia P121/P122 (plantilla y `questions.json`).
- **Auditoría de Analytics:** el producto es un diagnóstico descriptivo de devoluciones por segmento; pandas y Plotly sirven a ese producto. Responde qué, dónde y cuándo con evidencia persistida; usuario y decisión concreta no evidenciados.

## S03.P120.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T02.
- **Señales descartadas relevantes:**
  - métodos de validación «input validation, data type validation, range and constraint validation, and cross-reference validation» (DPSIA/DI, p. 92) — ya cubierta: P102 H01, P124 H02 y P120 H02 (identidad `Quantity × Price = TotalAmount`).
  - *scores* y *rankings* con características deseables (DM-Proximity, p. 75) — ya cubierta: umbrales de volumen y separación entre riesgo y prioridad (P120 H06–H07, P121 H05, P122 H04/H06).

## S03.P120.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta: P120 H02, P121 H02, P122 H01, H05.

## S03.P120.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - brechas de calidad «accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y métodos para evaluarla (CAP-E.3.6.1, 3.6.4, p. 15) — ya cubierta: P120 H02, P121 H02, P122 H01 y H05.

## S03.P120.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - criterios de éxito y línea base del estado actual (p. 11: Task 2.4 «Define primary measures of success»; Task 2.5 «Identify baseline performance of the current state») — marginal: en descriptiva la «línea base» ya aparece como KPI global del período (P120 H04, P121 H03, P122 H02) y como referencia de pares (P125 H02); medidas de éxito de una solución pertenecen a predictiva/prescriptiva.
  - caso de negocio, costos, beneficios y consecuencias indirectas (p. 8: Task 1.5 «Create an initial business case») — fuera de alcance: la evaluación de costo-beneficio de una solución excede la pregunta descriptiva; P122 H04 ya pondera por valor expuesto.
  - documentar y reportar hallazgos de datos (p. 16: Task 3.7 «Identify appropriate elements of a data report») — ya cubierta en lo esencial: P122 H01/H05 (tabla de calidad y cobertura de flete), P120 H02 (grano y consistencia); un «reporte de datos» formal sería una variante.

## S03.P120.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - «Variability, uncertainty, sampling error, and inference» (p. 44) frente a tasas sin intervalos — marginal: el umbral de volumen (P120 H06, P121 H05, P122 H06) ya cumple la función descriptiva; intervalos desplazarían hacia Estadística.

## S03.P120.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Formular preguntas correctas ... interpretar métricas y KPIs» (p. 219); Índice de Rotación definido con variables, numerador y promedio de planta (pp. 305–306) — ya cubierta: pregunta enlazada a evidencia (P120 H01) y KPI como contrato con numerador/denominador (P153 H01).
  - demanda de «customer analytics», «analítica de clientes», «Perfil híbrido: marketing + analítica» (pp. 162–163) — ya cubierta: casos de marketing (P124) y retail (P120); otro dominio sería variación de caso.

## S03.P120.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad de datos, representatividad y por qué fallan los modelos» (p. 5) — fuera de alcance/ya cubierta: el encuadre es de entrenamiento de modelos (predictiva); la calidad y el grano antes de agregar ya están en P120 H02, P122 H01 y P121 H02. El folleto no desarrolla método ni caso.

## S03.P120.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclo «from data preparation to exploration, visualization and analysis» (p. 1) — ya cubierta: preparación y calidad (P106 H01–H05, P107 H01–H02), exploración y visualización al servicio de un diagnóstico (P120 H02–H05, P121 H02–H04, P122 H01–H05). La ficha no da detalle que permita contrastar más.

## S03.P120.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - intervalos de confianza, pruebas de permutación y *false discovery rate* (p. 1: «permutation testing, false discovery rate, … confidence intervals») — fuera de alcance: los índices de P120–P122 registran como límite que las tasas por segmento no tienen intervalos ni pruebas de diferencia. Convertir ese límite en inferencia formal (por ejemplo, controlar comparaciones múltiples en un top N de segmentos) mete Estadística inferencial en el curso. Además, el documento no da caso ni profundidad para hacerlo con rigor. Los umbrales de volumen (P120 H06, P121 H05, P122 H06) siguen siendo la salvaguarda descriptiva vigente.

## S03.P120.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** propone T03.
- **Señales descartadas relevantes:**
  - nota de integración: revisiones previas (`national-academies-data-science-for-undergraduates-2018`, `berkeley-data-c102-data-inference-and-decisions`, `mit-data-science-and-machine-learning`) descartaron intervalos para P120 como marginales o fuera de alcance; este documento sitúa el intervalo dentro del módulo de análisis descriptivo y T03 lo limita a leer cada tasa contra la tasa base (con `ibm-spss-modeler-applications-guide` después), no a inferencia formal.

## S03.P120.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso ejecutivo de 8 semanas sobre liderazgo de datos: IA para líderes, marcos de innovación continua de datos, arquitectura TI y SQL, plataformas de datos y diseño de bases, *modern data stack*, nube, ética y gobierno de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - semanas 1–2 «Python for Data Science – Numpy – Pandas – Data Visualization», «Descriptive Statistics», caso «Fitness product customer footfall analysis» (p. 6) — ya cubierta: P103 H01–H04 (pandas, agregación, ranking visual), P120–P122 (resúmenes por segmento, series, matrices) y P125 H03 (mediana y percentiles).
  - «Inferential Statistics» (p. 6) e «Hypothesis Testing: … p-values: Confidence» (p. 9) — fuera de alcance como propuesta: P120 H06 y P121 H05 registran la falta de intervalos como límite, pero introducir inferencia formal desplazaría el foco hacia Estadística; el documento institucional no aporta un caso que lo ancle al producto descriptivo.
  - «Recommendations and Ranking – Using Population Averages – Using Population Comparisons and Ranking» (p. 10) — ya cubierta en su parte descriptiva (rankings por valor y tasa con umbral en P120 H06–H07); la recomendación personalizada es producto de datos.

## S03.P120.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado de 6 meses en ingeniería de datos: Python/pandas, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, NiFi, Kafka, DASK, seguridad web, ML y aprendizaje por refuerzo; portafolio GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Analyzing and translating technical results into actionable insights for executives» (p. 7); «communicate results that are clear and meaningful to stakeholders» (p. 11) — ya cubierta en lo que toca a descripción: P120 H07 (prioridad frente a riesgo), P125 H06 (respuesta con límite); el folleto no describe cómo se evalúa esa comunicación, por lo que no aporta un mecanismo concreto (institutional ilustra, no impone).
  - «Correlation» (Módulo 3, p. 7) — marginal: técnica aislada sin caso descriptivo asociado en el documento; las relaciones entre dimensiones ya se describen con matrices de segmentos (P120 H06, P121 H04, P122 H06).

## S03.P120.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - modelos de valor con atributos organizados en jerarquías «for evaluation and summation» (p. 2) — fuera de alcance: agregar atributos ponderados en una función de valor convierte la priorización descriptiva en una regla de decisión (prescriptiva). Además está ya cubierta en su forma descriptiva: P120 H07 separa el criterio de riesgo del de prioridad y P125 H04 exige un doble criterio con umbrales explícitos sin fundirlos en un puntaje.

## S03.P120.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, termoformado), mapeo de atributos prototipo–producto, decisiones de fabricación y análisis de costo-valor, con un proyecto final sobre una careta facial o un giróscopo satelital. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo comercial de cursos cortos presenciales (3–5 días): Data Science para profesionales (visualización/dashboards con Power BI o Tableau), Data Science para principiantes e intermedios (R/Python, SQL, regresión, ML), programa de analítica avanzada y predictiva, *masterclasses* para directivos y *fast tracks* temáticos (texto, regresión, clasificación, clustering y redes). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto (asíncrono + 3,5 días presenciales) sobre estrategia, modelos de negocio, IA generativa y agéntica, pensamiento de futuros y gobernanza de IA, con un *capstone* de iniciativa organizacional; requiere 10+ años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Contar una historia con los puntos claves para fundamentar las decisiones empresariales mediante informes, cuadros de mando, historias e infografías» y «Anticipar y gestionar las preguntas de los diversos públicos y audiencias» (p. 8) — marginal desde este documento: la falta de interpretación escrita en varios talleres ya está registrada en S02 y el patrón de conclusiones con límite existe en P125 H06; un folleto institucional no describe un mecanismo evaluable que justifique cambiar un taller concreto.

## S03.P120.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relata cuatro talleres participativos con 17 programas de pregrado de la UNAL sobre currículo, contextos, funciones misionales y prácticas pedagógicas, y recoge propuestas institucionales de armonización (superar el «currículo endogámico», egresados, unificación de conceptos). No contiene ningún programa ni curso de analítica, ningún resultado de aprendizaje disciplinar y ningún contenido de analítica descriptiva o de visualización. Estadística y Administración de Empresas sólo figuran como programas participantes (p. 8: «Economía, Zootecnia, Estadística…»). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular administrativa de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular» (Acuerdo 02 de 2020 del CESU, resultados de aprendizaje, PEP, planes de mejoramiento) en dimensiones macro/meso/microcurricular y cuatro etapas; no contiene contenidos disciplinares. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Probability and Uncertainty» (p. 9) — respaldo débil a la candidata P120 de incertidumbre de tasas (`cambridge-business-analytics`): tema semanal de un curso de minería, sin indicación de su uso descriptivo.

## S03.P120.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - tipos de variables y de gráficos, «Charting Considerations», «Heat Maps», «Interactive» (p. 7) — ya cubierta: ranking legible (P103 H04), magnitud y tasa en un gráfico y matrices (P120 H05–H06, P121 H04), tablero filtrable (P124 H04).

## S03.P120.29

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa en línea de 12 semanas, con o sin código, sobre IA generativa, ingeniería de *prompts* y RAG, agentes con herramientas y memoria, planificación y razonamiento, sistemas multiagente, pruebas y evaluación de sistemas agénticos y su protección; casos y proyectos de automatización empresarial. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.30

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - distribuciones, varianza, colas y pruebas de significancia (p. 2: «Hypothesis testing for determining the significance of an observation») — fuera de alcance: P120–P125 usan umbrales de volumen (P120 H06, P121 H05, P125 H04) y estadísticos robustos (P125 H03) al servicio del diagnóstico; introducir inferencia formal convertiría los talleres en práctica de Estadística y la ficha institucional no lo impone.

## S03.P120.31

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Correlation and Causation» (p. 1) — ya cubierta: P125 H06 persiste y verifica el límite causal junto a cada respuesta. Que P120–P122 no declaren ese límite ya está registrado por S02 y se trata en la candidata P120 del documento ACM. Al ser un simple rótulo institucional, esta señal no añade argumento propio.

## S03.P120.32

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de un módulo de orientación y nueve módulos con una línea de descripción cada uno, organizados por la tríada descriptiva (M1–M2), predictiva (M3–M6) y prescriptiva (M4, M7–M8), más aplicación en el negocio (M9). No incluye contenidos detallados, datos, evaluación ni resultados de aprendizaje. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.33

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Una transacción representa una operación. La historia revela el comportamiento» (p. 13: «¿Con qué frecuencia viene? … ¿Cuánto valor genera a lo largo del tiempo?») — marginal: sugiere un perfil histórico de cliente (frecuencia/valor), pero P120 ya rankea clientes (`top_customers.csv`) y P103 H01 agrega registros a entidad; el documento no aporta método ni datos para un análisis RFM y, como señal histórica de una diapositiva, no justifica una actividad.

## S03.P120.34

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Se confunde el éxito del modelo con su máxima precisión», «El modelo es sabio y omnisciente», «No hay un producto mínimo viable», llevar modelos a producción, «laptop analytics», fricción con TI (pp. 3–5, 9) — fuera de alcance: modelos y operacionalización pertenecen a predictiva y productos de datos.

## S03.P120.35

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diagnóstico de «Contexto y prioridades» y «Decisiones y resultados» (p. 8) — marginal desde este documento: refuerza la falta de usuario/decisión en P120 ya tratada por la candidata de framing derivada de `informs-cap-essentials-blueprint`; en este material es contexto organizacional, no práctica de taller.

## S03.P120.36

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - evaluar calidad por exactitud, completitud, consistencia, actualidad, validez, relevancia y unicidad (p. 13) — ya cubierta: P120 H02, P121 H02, P122 H01 y H05.

## S03.P120.37

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desperdicios «Problema equivocado», características que «No ayudan al usuario a tomar decisiones» (p. 6) y «Preguntas de bajo valor para responder» (p. 10) — marginal aquí: refuerza en lo conceptual la necesidad de conectar preguntas con decisiones, tratada como candidata P120 a partir de `dataops-03-methodologies` e INFORMS; este documento no aporta un mecanismo propio.

## S03.P120.38

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Working analytics over comprehensive documentation» y «Continually satisfy your consumer» (p. 10) — marginal: principios de equipo, sin método aplicable a un taller descriptivo; la orientación al usuario se trata en la candidata P120 de `informs-cap-pro-blueprint`.

## S03.P120.39

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - *epic hypothesis statement* con «For [customers] … Measured by [metrics]» (p. 25) — fuera de alcance: plantilla de priorización de iniciativas de producto con beneficio y requerimientos no funcionales; la declaración de destinatario/decisión de una pregunta descriptiva se trata en la candidata P120 de `informs-cap-pro-blueprint`, sin necesidad de este formato.

## S03.P120.40

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación (diapositivas) sobre DataOps desde la perspectiva directiva. Trata los silos entre equipos (TI, ingeniería de datos, ciencia de datos, visualización, gobierno), la coordinación relacional, el flujo de desarrollo con ramas y pruebas, la eliminación de cuellos de botella con Kanban, la priorización por oportunidad, las «trampas» del CDO y las etapas de madurez de la analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.41

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Los usuarios tienen conocimiento de negocio pero saben poco sobre que pueden hacer los datos por ellos» y «Obtenga retroalimentación de los usuarios» (p. 12) — marginal: refuerzo organizacional; la declaración de destinatario/decisión se trata en la candidata P120 de `informs-cap-pro-blueprint`.

## S03.P120.42

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - verificar las entradas antes de transformar y detectar los problemas lo antes posible (p. 4: «Los tests deben incluirse en cada etapa del pipeline») — ya cubierta: grano y consistencia aritmética antes de agregar en P120 H02, y grano y faltantes en P122 H01.

## S03.P120.43

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Láminas sobre cómo organizar equipos de datos: estructuras típicas (equipos pequeños, Big Data Ops, Hybrid, Large Scale), equipos por función o por dominio, roles del grupo central y de soporte con sus responsabilidades, habilidades y herramientas, perfiles en T, Pi y M, y estructuras centralizada y descentralizada. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.44

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - exploración con «descriptive reports that characterize distributions, anomalies, correlations» y evaluación de calidad por completitud, exactitud, oportunidad, consistencia y representatividad (p. 15) — ya cubierta: P120 H02 (grano y consistencia), P121 H02 (conciliación), P122 H01 (tabla de calidad) y H05 (cobertura de flete).
  - «criteria that avoid arbitrary thresholds in variable selection» (p. 20) — marginal: se refiere a selección de variables en modelos; los umbrales de volumen sin justificación de P120 H06, P121 H05 y P122 H06 son un límite ya registrado en S02, y esta frase no aporta un método para justificarlos.

## S03.P120.45

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** refuerza T03.
- **Señales descartadas relevantes:**
  - distribución de una variable con superposición de una segunda variable y diagrama de dispersión con color por categoría (pp. 85–87) — ya cubierta: P120 H05 codifica magnitud y tasa en un mismo gráfico; P103 H04 ranking visual.
  - gráfico de red (*web graph*) de asociaciones entre categorías (pp. 87–88) — marginal: la matriz categoría × canal de P120 H06 ya representa el cruce de dos variables categóricas.
  - derivar una medida (razón Na/K, p. 89; incremento porcentual de ingreso, p. 224) antes de explorar — ya cubierta: P120 H03 (bruto/devuelto/neto) y P150 H03 derivan medidas antes de agregar.
  - tamaño mínimo de segmento (p. 122: «Increase the minimum segment size to 1,000»; p. 125: 500) — ya cubierta: umbrales de volumen en P120 H06, P121 H05 y P122 H06.

## S03.P120.46

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - objetivos de negocio, criterios de éxito y supuestos («Specify all business questions as precisely as possible», p. 10; «Are there data quality assumptions?», «How does the project sponsor… expect to view the results?», p. 12) — marginal desde este documento: refuerza la candidata de framing de P120 de `informs-cap-essentials-blueprint`; como guía de herramienta no aporta un argumento distinto.
  - «Is there enough data to draw generalizable conclusions…?» (p. 17) — ya cubierta: umbrales de volumen (P120 H06, P121 H05, P122 H06).

## S03.P120.47

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - inspeccionar resultados intermedios en cada salida (p. 18: «Open Out-port View … you can inspect the data») y vistas enlazadas con hiliting (p. 10: «The propagation of the hilite status works for all views») — marginal: la inspección visual de evidencia intermedia ya es norma del curso (AGENTS.md, celdas de evidencia visual) y P124 H04 ofrece una vista filtrable; la selección enlazada es una prestación de herramienta.

## S03.P120.48

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data Exploration. … Compare the differences between high profit and low profit customers» (p. 1) — ya cubierta (comparación por segmentos en P120 H06–H07; cola alta en P125 H05).

## S03.P120.49

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - construir una tabla de casos con un registro por caso y agregar datos transaccionales al nivel del caso (p. 17: «single-record case data presentation»; p. 127: «it must be aggregated to the case level») — ya cubierta: P103 H01, P120 H02, P150 H01–H02.
  - formular bien la pregunta antes de analizar (p. 18: «you must learn how to ask the right questions») y comprender la fase de exploración y calidad (p. 19: «identify data quality problems and to scan for patterns») — ya cubierta: P120 H01 (`questions.json`), P122 H01, P106.

## S03.P120.50

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-data-mining.md` (`source_sha256`: 6396a7c9e3efce998f0bbb9907cacb228244737c80bdebcdae17ce913b7f6ce9).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - White paper comercial de SAS (2015) que presenta el ciclo de vida analítico (pregunta → preparación → exploración → modelado → implementación → evaluación) como marco para vender Enterprise Miner, Factory Miner y Decision Manager; foco declarado en minería de datos predictiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P120.51

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-forecasting.md` (`source_sha256`: 7cabe87e23ff9469d7b4b9e17582dd694b8ac329ed0975bf9a26e3dcb26b5569).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calendario de eventos recurrentes como repositorio aparte (pp. 96–97: pulso, cambio de nivel, rampa) — fuera de alcance: es insumo de modelos de pronóstico. Para describir, P120 ya contrasta días laborales y fines de semana.
