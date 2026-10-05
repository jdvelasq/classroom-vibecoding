# Log — P106

## S02.P106.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P106_limpieza_pandas/` (`data/ventas.csv`, `professor/main.py`, `professor/diagnostics.py`, `src/main.py`, `submission/ventas.csv`, `tests/`). Comparado con P100–P105.
- **Trazabilidad revisada:** entrada P106 → `descriptiva.C02`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (función por tipo de suciedad; highlight de caso y datos), H02 (canonización con diccionarios y diagnóstico de colisiones), H03 (fechas y regla día/mes), H04 (unidades y escalas), H05 (invariantes de dominio en la prueba).
- **Ambigüedades:** procedencia de `ventas.csv` no documentada y sin fuente limpia ni generador (no hay verdad de referencia); la regla día/mes asume `yyyy-mm-dd` cuando ambos componentes son ≤ 12; peso sin unidad se asume en kg; la prueba no ejecuta `main.py` y no cubre importes ni proveedores canónicos; `diagnostics.py` tiene sus llamadas principales comentadas.
- **Superficies / contrato / dependencias:** S01–S06; habilita P107 (mismo dato, contrato y prueba).
- **Auditoría de Analytics:** producto = capacidad de datos limpia, sin descripción posterior. C02 sustentado en la dimensión de calidad de datos; C05 débil. Domina la preparación de datos como disciplina contribuyente.

## S03.P106.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dimensiones de calidad de datos, entity resolution, limpieza basada en reglas y dependencias funcionales (DG-Data Cleaning, pp. 73–74) — ya cubierta: P106 H01–H05 (función por defecto, canonización con diagnóstico de colisiones, invariantes de dominio) y P107 H01–H03. Nombrar las dimensiones de calidad o formalizar FD/CFD sería marginal (vocabulario, no capacidad nueva).
  - transformación (estandarización, normalización, codificación, unidades; DG-Data Transformation, p. 73) — ya cubierta: P106 H04 lleva magnitudes a una unidad común.

## S03.P106.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» (p. 5) — ya cubierta: P106 H01–H05, P107 H01–H04, P150 H02.

## S03.P106.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limpiar, armonizar, transformar, unir y validar (p. 15: Task 3.5) — ya cubierta: P106 H01–H04, P107 H01–H03, P150 H02 (`validate="many_to_one"`), P121 H02 (conciliación).

## S03.P106.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data preparation, especially data cleansing and data transformation», «Missing and conflicting data» (p. 45) — ya cubierta (P106 H01–H05; P107 H01).
  - «use simple graphics to check data for artifacts, snafus, and inconsistencies» (p. 45) — ya cubierta (P122 H01–H02, histograma con referencia en cero; regla de evidencia visual de `AGENTS.md`).

## S03.P106.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - procesamiento en capas Bronze/Silver/Gold con «validación, normalización y verificación de calidad» (p. 131); reglas de limpieza «tiempos mínimos, duplicados», «control de completitud» (p. 238) — ya cubierta: separación crudo/limpio (P107 H02), limpieza por columna e invariantes (P106 H01, H05).
  - reducción de granularidad mediante «Dominios canónicos» de habilidades y roles (pp. 29, 80–92, 96) — ya cubierta: canonización con diccionarios y diagnóstico de colisiones (P106 H02, P107 H03), normalización de vocabularios (P123 H03).

## S03.P106.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclo «from data preparation to exploration, visualization and analysis» (p. 1) — ya cubierta: preparación y calidad (P106 H01–H05, P107 H01–H02), exploración y visualización al servicio de un diagnóstico (P120 H02–H05, P121 H02–H04, P122 H01–H05). La ficha no da detalle que permita contrastar más.

## S03.P106.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado en Data Science (antes Statistics 102). Cubre fundamentos probabilísticos de la inferencia y el ciclo de modelado y decisión, con sus implicaciones humanas, sociales y éticas. Sólo lista temas: no tiene resultados de aprendizaje, casos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Limpieza de datos» (p. 7) — ya cubierta: P106 H01–H05, P107 H01–H03.

## S03.P106.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso ejecutivo de 8 semanas sobre liderazgo de datos: IA para líderes, marcos de innovación continua de datos, arquitectura TI y SQL, plataformas de datos y diseño de bases, *modern data stack*, nube, ética y gobierno de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python/estadística (pandas, visualización, estadística descriptiva e inferencial), aprendizaje no supervisado (clustering, PCA, clustering espectral y de modularidad), regresión y predicción, clasificación y pruebas de hipótesis, deep learning, sistemas de recomendación y redes/modelos gráficos; con casos de estudio por semana. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «use Regular Expressions, clean a database» (p. 10) — ya cubierta: P106 H01–H04, P107 H01–H03.

## S03.P106.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado en línea de 6 meses (24 módulos en cinco partes: fundamentos de ciencia de datos, optimización, ML, ML avanzado y despliegue) con casos de la facultad de MIT Sloan; orientación dominante a modelado predictivo y prescriptivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño: selección de conceptos (Pugh), estudios de *trade-off*, modelos de valor, generación y evaluación de espacios de diseño, visualización del *tradespace*, frente de Pareto y sensibilidad. Sólo trae títulos de unidades y una descripción breve de cada una. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, termoformado), mapeo de atributos prototipo–producto, decisiones de fabricación y análisis de costo-valor, con un proyecto final sobre una careta facial o un giróscopo satelital. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «access, organize, clean, prepare, transform, and explore data» (p. 7) — ya cubierta: P106 H01–H05, P107 H01–H04.

## S03.P106.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto (asíncrono + 3,5 días presenciales) sobre estrategia, modelos de negocio, IA generativa y agéntica, pensamiento de futuros y gobernanza de IA, con un *capstone* de iniciativa organizacional; requiere 10+ años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Comprender, preparar, y elaborar informes sobre datos, además de limpiar brutos y utilizar SQL para cargar y consultar» (p. 3, p. 5) — ya cubierta: P103–P107.

## S03.P106.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relata cuatro talleres participativos con 17 programas de pregrado de la UNAL sobre currículo, contextos, funciones misionales y prácticas pedagógicas, y recoge propuestas institucionales de armonización (superar el «currículo endogámico», egresados, unificación de conceptos). No contiene ningún programa ni curso de analítica, ningún resultado de aprendizaje disciplinar y ningún contenido de analítica descriptiva o de visualización. Estadística y Administración de Empresas sólo figuran como programas participantes (p. 8: «Economía, Zootecnia, Estadística…»). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular administrativa de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular» (Acuerdo 02 de 2020 del CESU, resultados de aprendizaje, PEP, planes de mejoramiento) en dimensiones macro/meso/microcurricular y cuatro etapas; no contiene contenidos disciplinares. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - «Data Preprocessing» (p. 9), «Apply data preprocessing techniques» (p. 2) — ya cubierta: P106 H01–H05, P107 H01–H03.

## S03.P106.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Sílabo de un curso introductorio de 16 semanas centrado en herramientas (Excel, Access, SQL, MongoDB, SAS, Tableau): modelado ER y normalización, SQL (agregación, joins, subconsultas), NoSQL, sistemas de BI, visualización y tableros, proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.29

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa en línea de 12 semanas, con o sin código, sobre IA generativa, ingeniería de *prompts* y RAG, agentes con herramientas y memoria, planificación y razonamiento, sistemas multiagente, pruebas y evaluación de sistemas agénticos y su protección; casos y proyectos de automatización empresarial. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.30

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad y limpieza de datos: errores, faltantes, falta de consistencia (p. 2: «Problems found in realistic data: errors, missing values, lack of consistency, and techniques for addressing them»; p. 2: «coping with missing and dirty data») — ya cubierta: P106 H01–H05, P107 H01–H03.

## S03.P106.31

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de métodos y herramientas de un programa de *business analytics*, sin descripciones: recolección de datos (encuestas, NPS, pasiva, medios), A/B testing, correlación y causalidad, pronóstico (suavizamiento exponencial, tendencia y estacionalidad, estadística descriptiva, nuevo producto), regresión, *simulation toolkit* (Analysis ToolPak, Solver), visualización e interpretación de datos, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.32

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de un módulo de orientación y nueve módulos con una línea de descripción cada uno, organizados por la tríada descriptiva (M1–M2), predictiva (M3–M6) y prescriptiva (M4, M7–M8), más aplicación en el negocio (M9). No incluye contenidos detallados, datos, evaluación ni resultados de aprendizaje. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.33

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ETL como corrección de errores, eliminación de duplicados y unificación de formatos (p. 12: «corrigiendo errores, eliminando duplicados y unificando formatos») — ya cubierta: P106 H01–H04 y P107 H01–H03; la deduplicación no aparece como señal con caso propio en el documento.

## S03.P106.34

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «La poca calidad de los datos sigue siendo un desafío serio», «Existencia de errores en los datos», «Malos datos arruinan buenos reportes», «Falta de confianza en los datos» (p. 2) — ya cubierta: limpieza e invariantes (P106 H01–H05, P107 H01–H04) y calidad como compuerta de publicación (P153 H03).

## S03.P106.35

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Material de clase (serie DataOps) que define estrategia de datos y su cadena objetivos → diagnóstico → valor → brechas → objetivos de datos → iniciativas → gobierno/arquitectura/uso responsable → caso de valor y priorización → hoja de ruta → ejecución → evaluación, con un caso de mantenimiento predictivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.36

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limpiar duplicados, faltantes, inconsistencias y atípicos; «Validar los datos preparados» (p. 15) — ya cubierta: P106 H01–H05, P107 H01–H03.

## S03.P106.37

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Los datos no son testeados completamente» y «no hay suficientes pruebas que garanticen que los datos defectuosos no entren en las pipelines» como causa raíz de ciclos lentos (p. 10) — ya cubierta en lo que toca al curso: P106 H05 y P107 H04 verifican invariantes de dominio del archivo limpio, P153 H03 condiciona la publicación a reglas de calidad. Las brechas de esas pruebas (no cubren importes, proveedores ni fechas válidas) ya están registradas en S02; la señal se refiere a pipelines en producción (productos de datos).

## S03.P106.38

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre gestión de proyectos: cascada frente a Agile (manifiesto, Scrum, XP, Kanban), escalamiento (Scrum of Scrums, SAFe, DAD), manifiesto y principios DataOps, ciclo de vida analítico y prácticas ágiles para épicas de productos de datos. Perspectiva organizacional/metodológica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.39

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - pruebas de lógica de negocio y conformidad de campos (p. 4) — ya cubierta: invariantes de dominio de P106 H05 y contrato compartido de P107 H04 (las debilidades de esas pruebas ya están registradas en sus actividades; el documento no aporta argumento nuevo).

## S03.P106.40

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación (diapositivas) sobre DataOps desde la perspectiva directiva. Trata los silos entre equipos (TI, ingeniería de datos, ciencia de datos, visualización, gobierno), la coordinación relacional, el flujo de desarrollo con ramas y pruebas, la eliminación de cuellos de botella con Kanban, la priorización por oportunidad, las «trampas» del CDO y las etapas de madurez de la analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.41

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre DataOps aplicado a ML e ingeniería de datos: programación tradicional vs ML, deuda técnica, arquitectura canónica y arquitectura DataOps (Airflow, Jenkins, Docker, Git…), *design thinking*, *agile data warehousing*, data lake/DW/marts, esquemas para análisis, reutilización de código y fallas típicas de proyectos de analítica. Perspectiva organizacional/metodológica orientada a productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P106.42

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - pruebas de entrada sobre formato de fechas, tipo y rango de campos (p. 4) — ya cubierta: patrón de fechas y descuentos en [0, 1] en P106 H05 (y P107 H04), y tipos y no negatividad en P124 H02.
