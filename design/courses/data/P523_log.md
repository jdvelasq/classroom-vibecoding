# Log — P523

## S02.P523.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P523_mapreduce_particionamiento/` (`data/truck_events.csv.gz` sólo como binario, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/partition_loads.csv`, `submission/shuffle_comparison.csv`, `tests/test_activity.py`); P519 y P522 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P523 → `data.C02`, `data.C03`, `data.C05`; C03 no sustentado (sesgo de carga, no de evidencia), a escalar.
- **Highlights:** añadidos H01 (sesgo por clave; caso y datos), H02 (particionador determinista), H03 (agregación local, con defecto de modelado).
- **Ambigüedades:** el «combiner» se indexa por partición de destino y su cifra (5) equivale a la salida final, no a pares enviados al shuffle; `hot_key_load` es carga de partición, no de una clave; operadores de P519 copiados sin uso; semántica de `eventKey` y procedencia no documentadas; P523 no figura en el diseño de `case-selection.md`.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P522; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; internos de procesamiento distribuido sin producto analítico.

## S03.P523.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - BDS-Problems of Scale (p. 56: «Execute a computational task at multiple scale-levels»), BDS-Big Data Computing Architectures (pp. 56–57, E), BDS-Parallel Programming (p. 59: «load balancing issues»; «Evaluate a parallel algorithm’s load-balance») y BDS-Techniques (pp. 59–60: hashing, sampling, «Be attentive of pitfalls such as bias in performing sampling and filtering») — fuera de alcance: medición de aceleración, particionamiento, sesgo de carga y combiner son contenido T2/E de Big Data Systems, área que `s05-diseno-data.md` excluye; el documento refuerza las auditorías no resueltas de S02 y no justifica ampliar ese bloque.

## S03.P523.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.7 las 4 V (p. 14) — marginal: concepto de reconocimiento; no justifica reforzar el bloque de procesamiento cuya identidad ya está en duda.

## S03.P523.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «distributed data storage, multicore processing, and parallel computation» (p. 87) — fuera de alcance: frontera explícita del curso (operaciones distribuidas). El documento lo trata como infraestructura del programa, no como resultado de un curso de fundamentos.

## S03.P523.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «escasez de profesionales con experiencia práctica en procesamiento distribuido de datos a escala» con Spark, Hadoop, Kafka (p. 175); Analista Big Data que domina «Hadoop/Spark, bases de datos NoSQL, streaming» (p. 291). Categoría: fuera de alcance. Operaciones distribuidas están excluidas por `s05-diseno-data.md` y `case-selection.md` («No introducen PySpark, RDD, Pig, Hive»); reforzarlo agravaría el riesgo de identidad ya registrado en P522–P523.

## S03.P523.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «managing data at scale … with a focus on use cases in data analysis and machine learning» (p. 1). Categoría: fuera de alcance. Sin temario, la ficha no muestra qué mecanismos de escala enseña; no aporta argumento para reforzar el bloque MapReduce/particionamiento, cuyo riesgo de identidad ya está registrado (P522–P523).

## S03.P523.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso de educación profesional del MIT: ecuaciones diferenciales y métodos numéricos, modelado espacial (EDP), optimización y modelado guiado por datos, de la optimización al ML (regresión, regularización, clasificación), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos industriales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «use the DASK library to create, read, write, and analyze multiple files in parallel and simulate parallel processing across distributed machines» (p. 11); portafolio «Stream load 100 million lines of data and create and write 20 files in parallel using DASK» (p. 12) — fuera de alcance: refuerza precisamente el riesgo de identidad Big Data ya señalado en P522–P523; no justifica ampliarlo.

## S03.P523.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de 6 meses con cinco partes (fundamentos de data science, optimización, ML, ML avanzado, despliegue), casos (retail, análisis facial, Filatoi Riuniti, BlueBike) y *capstone* de portafolio; herramientas Python y Google Colab. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh, estudios de trade-off, modelos de valor, generación de espacios de diseño, tradespace, frente de Pareto y sensibilidad. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo), mapeo de atributos de prototipo y producto, decisiones de fabricación y análisis de costo-valor. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos presenciales cortos (3–5 días): Data Science for Business Professionals/Beginners/Intermediate, Advanced and Predictive Analytics, masterclasses ejecutivas y *fast tracks*, centrados en visualización con PowerBI, R/Python, estadística, regresión, ML y series de tiempo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo combinado (en línea + 3,5 días en campus) sobre estrategia, liderazgo, innovación, futuros y gobernanza de IA generativa y agéntica para directivos con más de 10 años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses en español con cinco cursos de ocho semanas: Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, y Storytelling y visualización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - informe de la Dirección Nacional de Programas Curriculares de Pregrado de la UNAL sobre cuatro talleres participativos con 17 programas de pregrado (p. 8) acerca de qué es el currículo, pertinencia frente al contexto, integración de docencia/investigación/extensión, prácticas pedagógicas (fines, contenidos, estrategias, recursos, evaluación) y propuestas para superar el «currículo endogámico». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica de la Sede Manizales. Establece una «Ruta de Armonización Curricular» en cuatro etapas: marco normativo, pertinencia y resultados de aprendizaje, organización curricular, e implementación y evaluación continua. La orienta al Acuerdo 02 de 2020 del CESU (resultados de aprendizaje) y al Acuerdo 033 de 2007 del CSU, en las dimensiones macro, meso y microcurricular. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso de posgrado de minería de datos aplicada a datos de salud (EHR), con un proyecto por entregables (propuesta, reporte de recolección de datos, reporte de preparación, informe final) y un survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de pregrado sin prerrequisitos que combina modelado relacional, normalización, SQL, NoSQL/MongoDB, BI y visualización con Excel/Access/Tableau, más un proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa online de 12 semanas, con ruta con o sin código, sobre IA generativa, prompts, RAG, agentes con herramientas y memoria (LangChain, LangGraph, MCP), sistemas multiagente, su evaluación y protección. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
