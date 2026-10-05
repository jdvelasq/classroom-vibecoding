# Log — P123

## S02.P123.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P123_scopus/` (`data/scopus.csv.gz`, `data/search_string.txt`, `professor/main.py` y `s01`–`s20`, `src/main.py`, `submission/` con dieciséis archivos, `tests/`); P100, P101 y P106 como antecedentes técnicos.
- **Trazabilidad revisada:** P123 → `descriptiva.C01`, `C02`, `C03`, `C05`; coherente, con C05 apoyada en productos persistentes y procedencia parcial.
- **Highlights añadidos:** H01–H08 (consulta persistida, campos multivaluados, normalización, co-ocurrencia, comunidades y red, serie anual completa, pipeline, pruebas). Highlight obligatorio de caso y datos: H02 (documento con listas «;»), con H04 declarando filas/columnas de la matriz.
- **Cambios realizados:** creación de `P123_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** sin notebook de profesor ni de estudiante (`notebooks/` sólo `.gitkeep`); fecha y tamaño de extracción no documentados; dependencia de red en ejecución (GeoJSON); países fuera del GeoJSON se descartan sin registro; reemplazos de palabras clave por subcadena; ruido temático residual en comunidades; la tercera pregunta apunta sólo a `keywords_frequency.csv`; la pregunta de períodos no tiene producto que los distinga; el texto emergente de la red rotula el tamaño escalado como «Frequency»; nombres de autores con ID de Scopus persistidos (datos bibliográficos públicos).
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S07 declaradas; dependencias demostrables de P100/P101/P106 (prácticas) y P120 (`questions.json`); salida no evidenciada.
- **Auditoría de Analytics:** descripción de un campo tecnológico por actor, lugar, tiempo y tema; disciplinas contribuyentes visibles. Auditoría con reserva: usuario y decisión no evidenciados y decisiones analíticas no expuestas en un notebook.

## S03.P123.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - procesamiento de texto (bag-of-words, word-count, TF-IDF, n-gramas, *stop words*, *stemming*; DG-Working with Various Types of Data, p. 71) — marginal: P100 H02 ya fija la unidad textual por reglas de normalización y P123 H02–H03 normaliza vocabularios. Añadir TF-IDF o lematización sería otra técnica para lo mismo.
  - estrategia de búsqueda, «narrowing and broadening», operadores booleanos (DM-Information Retrieval, p. 82); descubrimiento de comunidades (DM-Mining Web Data, p. 81); enmarcar la pregunta y obtener datos (DM-Data Preparation, p. 76) — ya cubierta: P123 H01 (consulta persistida) y H05 (Louvain). Documentar el refinamiento de la cadena sería marginal frente al límite ya registrado (falta de fecha y conteo).
  - calidad del *clustering* (DM-Cluster Analysis, p. 77) — marginal: la falta de modularidad o estabilidad en P123 H05 ya está registrada por S02, y ACM sólo lo enuncia como conocimiento genérico de minería.

## S03.P123.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - criterios de éxito y línea base del estado actual (p. 11: Task 2.4 «Define primary measures of success»; Task 2.5 «Identify baseline performance of the current state») — marginal: en descriptiva la «línea base» ya aparece como KPI global del período (P120 H04, P121 H03, P122 H02) y como referencia de pares (P125 H02); medidas de éxito de una solución pertenecen a predictiva/prescriptiva.
  - caso de negocio, costos, beneficios y consecuencias indirectas (p. 8: Task 1.5 «Create an initial business case») — fuera de alcance: la evaluación de costo-beneficio de una solución excede la pregunta descriptiva; P122 H04 ya pondera por valor expuesto.
  - sesgo de la fuente al adquirir datos (p. 15: CAP-P.3.4.1 «identify data source bias») y linaje/versionado (CAP-P.3.4.3) — marginal/ya cubierta: P123 H01 delimita el corpus con la consulta persistida (límite de fecha y conteo ya registrado en su actividad); el linaje está en P153 H04.

## S03.P123.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - «processing text into data that can be analyzed» (p. 43) — ya cubierta (P100 H02, P123 H02–H03).

## S03.P123.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reducción de granularidad mediante «Dominios canónicos» de habilidades y roles (pp. 29, 80–92, 96) — ya cubierta: canonización con diccionarios y diagnóstico de colisiones (P106 H02, P107 H03), normalización de vocabularios (P123 H03).

## S03.P123.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de pregrado de 4 unidades, con prerrequisitos de programación y de un curso de ciencia de datos (DATA C100 o equivalente), sobre gestión de datos a escala para análisis y machine learning a lo largo de todo el ciclo de vida, con foco en operacionalización confiable y escalable. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado en Data Science (antes Statistics 102). Cubre fundamentos probabilísticos de la inferencia y el ciclo de modelado y decisión, con sus implicaciones humanas, sociales y éticas. Sólo lista temas: no tiene resultados de aprendizaje, casos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de 11 semanas, sin codificación, organizado en sesgos de decisión, análisis descriptivo, Big Data, experimentación, predictivo (ML, redes neuronales), prescriptivo y cuestiones ético-jurídicas; casos y tareas de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso ejecutivo de 8 semanas sobre liderazgo de datos: IA para líderes, marcos de innovación continua de datos, arquitectura TI y SQL, plataformas de datos y diseño de bases, *modern data stack*, nube, ética y gobierno de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - redes con «Centrality measures: degree, eigenvector, and page-rank» y «Degree distribution, clustering» (p. 11) y «Modularity Clustering» (p. 7) — marginal: P123 ya construye co-ocurrencias, comunidades Louvain y redes (H04–H05); la ausencia de modularidad/estabilidad ya está registrada como límite en su actividad (H05) y el folleto sólo nombra el tema, sin argumento descriptivo que justifique la mejora por sí mismo. Una medida de centralidad sería una variante de la frecuencia (diagonal) ya reportada.
  - caso «Finding themes in the project description» con clustering (p. 7) — marginal/fuera de alcance: la estructura temática ya se describe con co-ocurrencia de palabras clave y comunidades (P123 H04–H05); clustering de texto sería modelado no supervisado propio de otro curso.

## S03.P123.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado de 6 meses en ingeniería de datos: Python/pandas, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, NiFi, Kafka, DASK, seguridad web, ML y aprendizaje por refuerzo; portafolio GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado en línea de 6 meses (24 módulos en cinco partes: fundamentos de ciencia de datos, optimización, ML, ML avanzado y despliegue) con casos de la facultad de MIT Sloan; orientación dominante a modelado predictivo y prescriptivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - visualización e interacción con el *tradespace*, búsqueda de *clusters* y del frente de Pareto (pp. 3–4: «looking for patterns in the tradespace, such as clusters and the Pareto Front») — fuera de alcance: el patrón que se busca es el de alternativas de diseño para optimizar. La búsqueda de estructura descriptiva sobre datos observados ya la cubre P123 H04/H05 (co-ocurrencia y comunidades).

## S03.P123.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, termoformado), mapeo de atributos prototipo–producto, decisiones de fabricación y análisis de costo-valor, con un proyecto final sobre una careta facial o un giróscopo satelital. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Describing a corpus of documents with a term–document matrix» (p. 13) — ya cubierta: P100 H02 (unidad textual), P123 H02–H04 (conteo de campos multivaluados y co-ocurrencia ítem × ítem).
  - «Capturing important connections with Social Network Analysis» (p. 13) — ya cubierta: P123 H04–H05 (matriz de co-ocurrencia, Louvain, redes).

## S03.P123.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto (asíncrono + 3,5 días presenciales) sobre estrategia, modelos de negocio, IA generativa y agéntica, pensamiento de futuros y gobernanza de IA, con un *capstone* de iniciativa organizacional; requiere 10+ años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Conocer distintos métodos de visualización para mostrar los datos temporales, espaciales y espacio-temporales» (p. 8) — ya cubierta: temporales en P121 H04 y H06 (matriz calendario día × hora; serie frente a patrón por mes), P122 y P150; espaciales en P123 (mapa coroplético de países, inventario y S05). Espacio-temporal combinado: marginal, sin caso con ambas dimensiones de grano adecuado en el curso.
  - «Contar una historia con los puntos claves para fundamentar las decisiones empresariales mediante informes, cuadros de mando, historias e infografías» y «Anticipar y gestionar las preguntas de los diversos públicos y audiencias» (p. 8) — marginal desde este documento: la falta de interpretación escrita en varios talleres ya está registrada en S02 y el patrón de conclusiones con límite existe en P125 H06; un folleto institucional no describe un mecanismo evaluable que justifique cambiar un taller concreto.

## S03.P123.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relata cuatro talleres participativos con 17 programas de pregrado de la UNAL sobre currículo, contextos, funciones misionales y prácticas pedagógicas, y recoge propuestas institucionales de armonización (superar el «currículo endogámico», egresados, unificación de conceptos). No contiene ningún programa ni curso de analítica, ningún resultado de aprendizaje disciplinar y ningún contenido de analítica descriptiva o de visualización. Estadística y Administración de Empresas sólo figuran como programas participantes (p. 8: «Economía, Zootecnia, Estadística…»). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular administrativa de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular» (Acuerdo 02 de 2020 del CESU, resultados de aprendizaje, PEP, planes de mejoramiento) en dimensiones macro/meso/microcurricular y cuatro etapas; no contiene contenidos disciplinares. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - Sílabo de un curso de minería de datos aplicada a salud (textos de Albright–Winston y Han–Kamber): preprocesamiento, exploración, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, *clustering* y atípicos, minería de texto; proyecto por entregables (propuesta, reporte de recolección, reporte de preparación, informe final) y artículo de revisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Sílabo de un curso introductorio de 16 semanas centrado en herramientas (Excel, Access, SQL, MongoDB, SAS, Tableau): modelado ER y normalización, SQL (agregación, joins, subconsultas), NoSQL, sistemas de BI, visualización y tableros, proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.29

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa en línea de 12 semanas, con o sin código, sobre IA generativa, ingeniería de *prompts* y RAG, agentes con herramientas y memoria, planificación y razonamiento, sistemas multiagente, pruebas y evaluación de sistemas agénticos y su protección; casos y proyectos de automatización empresarial. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P123.30

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - grafos, centralidad e importancia en redes sociales (p. 3) — marginal: P123 H04–H05 ya construye redes de co-ocurrencia con comunidades; añadir centralidad sería otra métrica sobre el mismo producto sin cambiar lo que el estudiante entiende.
