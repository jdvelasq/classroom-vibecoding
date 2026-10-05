# Log — P407

## S02.P407.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P407_config_file/` (`CONFIG.json`, `ESTIMATOR.pkl` y `data/*/sentences.csv.gz` como binarios, `professor/main.py`, `src/main.py`, `submission/metrics.json`, `tests/test_activity.py`); comparación con P406.
- **Trazabilidad revisada:** P407 → `productos.C02`, `productos.C03`, `productos.C05`. C03 y C05 sin evidencia nueva.
- **Highlights:** añadidos H01 (configuración por archivo validada), H02 (caso y datos: caso repetido de P406 como límite).
- **Ambigüedades:** posible duplicación con P406; sin `HOW_TO_RUN_ME.txt` para el estudiante (P406 sí lo tiene); `metrics.json` idéntico al de P406, por lo que la evaluación no distingue el mecanismo.
- **Superficies / contrato / dependencias:** S01–S06; recibe todo el caso de P406.
- **Auditoría de Analytics:** no resuelta: práctica de configuración sin capacidad analítica identificada.

## S03.P407.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Temario del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con tareas y subtareas evaluables (pesos: Deployment 10 %, Lifecycle Management 9 %). Sólo los dominios VI–VII y algunas subtareas de III (linaje, gobierno, calidad) tocan la operación de capacidades. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Marco de pregrado que define la «data acumen» (diez áreas conceptuales) y recomienda que la ética y la reproducibilidad atraviesen el currículo; trata el flujo de trabajo y la gestión de datos como competencias generales, no la operación de productos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Estudio de política pública que cuantifica la brecha de talento TI en Colombia y la pertinencia de la oferta educativa. Para Productos de datos su valor es de pertinencia laboral: escasez de perfiles DevOps/SRE/MLOps y una brecha formativa en prácticas de producción (CI/CD real, rollback, secretos, monitoreo de deriva, seguridad). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de dos meses sin requisitos técnicos sobre capacidades de IA (ML, redes neuronales, visión, NLP, robótica), estrategia de IA y equipos de IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de 4 unidades (cruzado con COMPSCI C187) sobre gestión de datos a escala para análisis y ML, con énfasis en una operacionalización confiable. Sólo incluye la descripción, los prerrequisitos y datos administrativos; no trae temario, prácticas ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: fundamentos probabilísticos de la inferencia y «ciclo de vida de modelado y toma de decisiones» con sus implicaciones humanas, sociales y éticas. Lista temas (decisión frecuentista y bayesiana, FDR, inferencia causal, Thompson sampling, Q-learning, privacidad diferencial, sistemas de recomendación) sin resultados de aprendizaje ni prácticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de 11 semanas sin codificación sobre sesgos en decisiones, análisis descriptivo, Big Data, experimentación, ML, analítica prescriptiva y cuestiones ético-jurídicas y organizacionales, con casos (UPS, Netflix, TalkTalk). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un curso en línea de educación continua: historia de la web y la nube, servidor Node.js, contenedores y llaves PKI, DevOps y sus cuatro métricas, casos (Microsoft, Netflix, GE, AWS), serverless, «Agile corporation» y cloud native/Kubernetes. Sin vínculo con capacidades analíticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto de un curso ejecutivo en línea de 8 semanas sobre liderazgo de datos: historia de datos y nube, plataformas y diseño de bases de datos, «Lean DevOps», marcos organizacionales, gobierno, ciberseguridad y ética; sólo enumera módulos y resultados, sin métodos ni evidencias. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas de ciencia de datos y ML (Python y estadística, no supervisado, regresión, clasificación, deep learning, sistemas de recomendación, redes y modelos gráficos) con casos de estudio; no trata despliegue, operación ni monitoreo de capacidades analíticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso de 8 semanas (MIT xPRO/Emeritus) sobre el proceso de diseño de productos de IA: etapas de diseño, fundamentos de ML y deep learning, HCI inteligente, «superminds», GANs, modelo de Lawler para definir un problema de IA y un capstone que es una propuesta de diseño (resumen ejecutivo), no una capacidad operada. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura de plataformas y APIs, estándares, gating de calidad, regulación, antimonopolio y modelado de dinámicas de plataforma. Es estrategia de producto/plataforma, no operación de capacidades analíticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso profesional del MIT: EDO y métodos numéricos, modelado espacial (EDP), optimización y modelado basado en datos, de optimización a ML (regresión, regularización, logística), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos (Aurora, Schlumberger, BASF). No contiene contenidos de operación, despliegue, validación operativa, monitoreo ni gobierno. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un certificado de 6 meses (MIT xPRO/Emeritus) de ingeniería de datos: Python, SQL, contenedores de bases de datos, CDC, APIs y seguridad web con JWT, ETL con NiFi, Hadoop/Spark/Airflow, ML y aprendizaje por refuerzo, streaming con Kafka/MQTT y portafolio en GitHub; el resto es servicios de carrera y financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto comercial de un certificado en línea de seis meses (MIT xPRO/Emeritus). Cubre fundamentos de ciencia de datos, optimización, ML y aprendizaje profundo, y una parte final titulada «Deployment» que en realidad trata transformación digital y un portafolio de cierre. No describe prácticas de operación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh y estudios de compromiso (trade studies), modelos de valor, generación y evaluación de espacios de diseño, exploración del tradespace (frente de Pareto, sensibilidad, robustez, incertidumbre) y asignación de tareas entre modelos y personas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto de un programa de ocho semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, DFM). Incluye un proyecto final que decide la fabricación y analiza costos de un prototipo. Queda fuera del dominio de Analytics y de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos para principiantes, nivel intermedio y avanzado, analítica predictiva, clases magistrales para ejecutivos y cursos rápidos), centrado en visualización con Power BI, R y Python, estadística, ML y algo de optimización. No tiene contenido de operación ni de ciclo de vida de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo (10+ años de experiencia) sobre estrategia, modelos de negocio, liderazgo, futuros y gobierno de IA; temario por fases sin contenidos operativos ni técnicos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto en español de un certificado de 10 meses con cinco cursos de 8 semanas (Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, Storytelling y visualización); sólo una línea toca la operación de modelos (despliegue como API o puntuación por lotes). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P407.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de la Dirección Nacional de Programas Curriculares de Pregrado (2021) sobre cuatro talleres de co-creación con programas de pregrado de varias sedes (contextos, dinámicas, prácticas pedagógicas, proyecciones). No contiene programas de analítica, cursos de datos/ingeniería de datos/MLOps ni resultados de aprendizaje disciplinares: «analítica» no aparece ni una vez; «datos» aparece sólo para la metodología de teoría fundamentada del propio estudio (p. 20) y «software» para Atlas.ti (p. 21). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
