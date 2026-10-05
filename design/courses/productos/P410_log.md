# Log — P410

## S02.P410.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P410_github_remote/` (`HOW_TO_RUN_ME.txt`, `data/repository_template/product_card.md`, `data/github_remote_case.bundle` como binario, `submission/git_log.txt`, `tests/test_activity.py`); HOW_TO de P411 y P415 para dependencias.
- **Trazabilidad revisada:** P410 → `productos.C02`, `productos.C04`. C04 débil (sólo instrucción).
- **Highlights:** añadidos H01 (remoto con seguimiento), H02 (credenciales fuera del repositorio), H03 (caso y datos: tarjeta completa con evidencia sólo local).
- **Ambigüedades:** la evidencia no demuestra el push; el hash `60a3756` no coincide con el commit «chore: create product card» de la evidencia de P411 (`4d8becc`), aunque P411 declara continuar este repositorio; uso del `.bundle` no documentado.
- **Superficies / contrato / dependencias:** S01–S05; habilita P411 (y por cadena P415).
- **Auditoría de Analytics:** no resuelta: práctica de GitHub anclada a la tarjeta del producto.

## S03.P410.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Temario del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con tareas y subtareas evaluables (pesos: Deployment 10 %, Lifecycle Management 9 %). Sólo los dominios VI–VII y algunas subtareas de III (linaje, gobierno, calidad) tocan la operación de capacidades. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Source code (version) control systems», «Collaboration» (p. 47) — ya cubierta: P408 H02, P409 H01, P411 H01.

## S03.P410.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Estudio de política pública que cuantifica la brecha de talento TI en Colombia y la pertinencia de la oferta educativa. Para Productos de datos su valor es de pertinencia laboral: escasez de perfiles DevOps/SRE/MLOps y una brecha formativa en prácticas de producción (CI/CD real, rollback, secretos, monitoreo de deriva, seguridad). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de dos meses sin requisitos técnicos sobre capacidades de IA (ML, redes neuronales, visión, NLP, robótica), estrategia de IA y equipos de IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «collaboration» como parte del ciclo de vida (p. 1) — ya cubierta: control de versiones, ramas, remoto y pull request (P408 H02, P409 H01, P411 H01). La ficha no detalla la práctica.

## S03.P410.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: fundamentos probabilísticos de la inferencia y «ciclo de vida de modelado y toma de decisiones» con sus implicaciones humanas, sociales y éticas. Lista temas (decisión frecuentista y bayesiana, FDR, inferencia causal, Thompson sampling, Q-learning, privacidad diferencial, sistemas de recomendación) sin resultados de aprendizaje ni prácticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de 11 semanas sin codificación sobre sesgos en decisiones, análisis descriptivo, Big Data, experimentación, ML, analítica prescriptiva y cuestiones ético-jurídicas y organizacionales, con casos (UPS, Netflix, TalkTalk). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «we will use keys to communicate with cloud services, for example, GitHub and Docker Hub… Public Key Infrastructure (PKI)» (p. 13) — ya cubierta en lo que importa al curso: credencial fuera del código y de la evidencia (P427 H01–H02) y separación de credenciales del repositorio (P410 H02); PKI como tema es seguridad informática general (fuera de alcance).
  - «hands-on practice with Git and GitHub, Docker, Node, and NPM» (p. 6) — ya cubierta (cadena de repositorio y CI P408–P416); el documento confirma el riesgo de identidad registrado (capacitación en herramientas) en vez de ayudar a resolverlo.

## S03.P410.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Understand how the principles of Lean DevOps can be applied to optimizing data systems» (p. 7, resultado 08); testimonio sobre «data pipelines, low code/no-code, CI/CD, cloud deployment, data compliance» (p. 9) — ya cubierta: versiones, revisión y CI (P408–P416); «cloud deployment» y no-code son fuera de alcance (cloud engineering, capacitación en plataforma).

## S03.P410.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas de ciencia de datos y ML (Python y estadística, no supervisado, regresión, clasificación, deep learning, sistemas de recomendación, redes y modelos gráficos) con casos de estudio; no trata despliegue, operación ni monitoreo de capacidades analíticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso de 8 semanas (MIT xPRO/Emeritus) sobre el proceso de diseño de productos de IA: etapas de diseño, fundamentos de ML y deep learning, HCI inteligente, «superminds», GANs, modelo de Lawler para definir un problema de IA y un capstone que es una propuesta de diseño (resumen ejecutivo), no una capacidad operada. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura de plataformas y APIs, estándares, gating de calidad, regulación, antimonopolio y modelado de dinámicas de plataforma. Es estrategia de producto/plataforma, no operación de capacidades analíticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso profesional del MIT: EDO y métodos numéricos, modelado espacial (EDP), optimización y modelado basado en datos, de optimización a ML (regresión, regularización, logística), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos (Aurora, Schlumberger, BASF). No contiene contenidos de operación, despliegue, validación operativa, monitoreo ni gobierno. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Build a GitHub portfolio» y uso de Git (p. 3, p. 8, p. 12) — ya cubierta: P408–P411 versionan la tarjeta de producto; el portafolio es un objetivo de empleabilidad, no de operación.

## S03.P410.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto comercial de un certificado en línea de seis meses (MIT xPRO/Emeritus). Cubre fundamentos de ciencia de datos, optimización, ML y aprendizaje profundo, y una parte final titulada «Deployment» que en realidad trata transformación digital y un portafolio de cierre. No describe prácticas de operación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh y estudios de compromiso (trade studies), modelos de valor, generación y evaluación de espacios de diseño, exploración del tradespace (frente de Pareto, sensibilidad, robustez, incertidumbre) y asignación de tareas entre modelos y personas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto de un programa de ocho semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, DFM). Incluye un proyecto final que decide la fabricación y analiza costos de un prototipo. Queda fuera del dominio de Analytics y de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos para principiantes, nivel intermedio y avanzado, analítica predictiva, clases magistrales para ejecutivos y cursos rápidos), centrado en visualización con Power BI, R y Python, estadística, ML y algo de optimización. No tiene contenido de operación ni de ciclo de vida de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo (10+ años de experiencia) sobre estrategia, modelos de negocio, liderazgo, futuros y gobierno de IA; temario por fases sin contenidos operativos ni técnicos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto en español de un certificado de 10 meses con cinco cursos de 8 semanas (Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, Storytelling y visualización); sólo una línea toca la operación de modelos (despliegue como API o puntuación por lotes). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de la Dirección Nacional de Programas Curriculares de Pregrado (2021) sobre cuatro talleres de co-creación con programas de pregrado de varias sedes (contextos, dinámicas, prácticas pedagógicas, proyecciones). No contiene programas de analítica, cursos de datos/ingeniería de datos/MLOps ni resultados de aprendizaje disciplinares: «analítica» no aparece ni una vez; «datos» aparece sólo para la metodología de teoría fundamentada del propio estudio (p. 20) y «software» para Atlas.ti (p. 21). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular institucional que establece una «Ruta de Armonización Curricular» de cuatro etapas (marco normativo, pertinencia y resultados de aprendizaje, organización curricular, implementación y evaluación continua de los resultados de aprendizaje) en las dimensiones macro, meso y microcurricular, en el marco del Acuerdo 02 de 2020 del CESU. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de un curso de posgrado en línea de minería de datos aplicada a datos de salud: preprocesamiento, probabilidad, regresión, patrones frecuentes, clasificación, clustering y minería de texto, evaluado con un proyecto por entregables (propuesta, recolección, preparación, informe final), póster y un survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus introductorio de pregrado: Excel, Access, modelado entidad-relación, normalización, SQL (consultas, joins, subconsultas), NoSQL/MongoDB y su pipeline de agregación, BI y data warehouses, visualización y dashboards; proyecto final en equipo. Sin contenido de operación, despliegue ni gobierno de capacidades. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas (rutas con y sin código) sobre IA generativa, prompts y RAG, agentes con herramientas y memoria, planificación, sistemas multiagente, pruebas/evaluación y protección de soluciones agénticas, con proyectos y casos prácticos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de bodegas de datos tradicionales: modelado ER y dimensional de Kimball (incluye SCD tipos 1–3, hechos sin hechos, snapshots), y BI con SAP Business Objects (universos, loops, traps, seguridad por fila) y Tableau; declara explícitamente «ETL is not covered in this course» (p. 1). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un módulo introductorio de posgrado, de 10 semanas, del departamento de Computer Science. Recorre herramientas básicas, estadística, calidad de datos y SQL/NoSQL, regresión, matrices, clustering, clasificación, estructuras para big data, privacidad y anonimización, y grafos. Se evalúa con un proyecto, ejercicios y un examen. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de una página de métodos y herramientas de un programa de business analytics: recolección de datos (encuestas, NPS, pasiva, medios), A/B testing, correlación y causalidad, pronóstico (suavizamiento exponencial, tendencia y estacionalidad, nuevo producto), regresión, simulación con Analysis ToolPak y Solver, visualización, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Lista de módulos de un programa ejecutivo de Business Analytics: orientación, descriptiva (módulos 1–2), predictiva (3–6), prescriptiva (4, 7–8) y aplicación de la analítica en el negocio (9), cada uno con una línea de propósito. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación histórica (1970–2026) de cómo las organizaciones pasaron de registrar datos a decidir y actuar con ellos: RDBMS, SQL, DW/ETL, BI, minería de datos, CRISP-DM, ciencia de datos, Big Data, Business Analytics, producto de datos, DataOps, MLOps, modelos fundacionales y agentes. Es contexto y encuadre, no prescripción vigente. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación de diapositivas, en lista, sobre por qué fracasan los proyectos de analítica: mala calidad de los datos, procesos manuales, mitos sobre la ciencia de datos, objetivos poco claros, falta de soporte organizacional y dificultad para llevar modelos a producción. Sirve como motivación organizacional de DataOps, no como prescripción de prácticas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de estrategia de datos organizacional (diagnóstico, mecanismos de valor, brechas, objetivos, iniciativas, gobierno, arquitectura, uso responsable, caso de valor, portafolio, hoja de ruta, ejecución y evaluación) ilustrado con mantenimiento predictivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - recorre KDD → CRISP-DM → metodologías de ciclo de vida (TDSP, CRISP-ML(Q), MAISTRO) con un caso de abandono de clientes que avanza de pregunta descriptiva a predicción, decisión, despliegue, monitoreo/degradación y gobierno transversal. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - traslada Lean (Toyota, Lean Software Development, Lean Startup) a la analítica: analítica como sistema de producción («value pipeline») y de desarrollo («innovation pipeline»), desperdicios en analítica, value stream mapping, entrega rápida (colas, ciclo, control estadístico de procesos), teoría de restricciones, análisis de causa raíz (5 porqués, árbol de realidad actual) y capas del ciclo de vida del dato. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre gestión de proyectos: problemas de waterfall, manifiesto ágil, Scrum, XP, Kanban, escalamiento (Scrum of Scrums, SAFe, Disciplined Agile Delivery), manifiesto y principios DataOps, ciclo de vida analítico (ideación → retiro) y prácticas ágiles de DataOps (epic hypothesis statement, epic owner, MVP). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Hay al menos un test en cada paso» del pipeline ingestión→reporte (p. 9) — ya cubierta: el bloque de pruebas cubre regla, transformación, datos, modelo, entradas y flujo publicado (P400–P404, P417, P433). El documento no ayuda con el riesgo de identidad del bloque (indicador trivial), sólo lista prácticas.
  - control de versiones, bifurcar y fusionar (p. 10–11) — ya cubierta (H01–H02 de P408–P411).
  - «Epic hypothesis statement» con «For [customers]… Measured by [metrics]… And requiring [non-functional requirements] … 99.99% availability» (p. 25) — marginal: la tarjeta de producto (P408–P411) y la ficha de catálogo (P454) ya declaran consumidor, métrica y responsable; agregar requisitos no funcionales sería un campo más; la desconexión de C01 con nivel de servicio ya está registrada en P445.

## S03.P410.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - flujo de rama de característica, fusión, pre-release y release (p. 5). Categoría: **ya cubierta**. P409 H01 cubre el aislamiento en rama con fusión explícita y P411 H01 la integración mediante revisión. Un ambiente de pre-release intermedio es una variante sin caso que la exija.

## S03.P410.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - prácticas «Uso de un sistema de control de versiones», «Estrategia de ramificación y fusión», «Reuso y contenerización», «Parametrización del proceso» (p. 4, p. 6, p. 11) — ya cubierta: P408–P411 (Git, ramas, remoto, PR), P418 (contenedor), P406–P407 (parametrización).

## S03.P410.44

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre calidad de datos en DataOps: análisis de impacto y automatización de pruebas, tipos de pruebas, «Analytics es código» (innovation pipeline vs. value pipeline), pruebas en cada etapa (entradas, lógica de negocio, salidas) con niveles de severidad y acción, y tipos de prueba con notificación (location balance, historical balance, control estadístico de procesos). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.45

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre estructuras de equipos para DataOps (small teams, Big Data Ops, hybrid, large scale), equipos por función frente a por dominio/producto, roles del grupo core y de soporte (incluidos DataOps engineer y data product owner) y perfiles T/Pi/M-shaped. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.46

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Revisión sistemática (expansión por citas en Scopus, 18 metodologías) que deriva PRODIG8: seis dimensiones de ejecución (alcance, comprensión y preparación de datos, diseño, evaluación, operación y mantenimiento), Gobierno y Ética como control transversal y Mejora Continua como retroalimentación adaptativa. Es un marco de gestión de proyectos analíticos; sólo §4.6–4.8 tocan directamente la operación de capacidades. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.47

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Tutorial de una herramienta comercial de minería de datos: casos de modelado (clasificación, series de tiempo, supervivencia, GLM, SVM, reglas, KNN, TCM) construidos como «streams» de nodos; la operación aparece sólo como menciones a puntuación de datos nuevos, exportación PMML, repositorio de despliegue, modo batch, reaplicación de un modelo de series de tiempo y reentrenamiento mensual. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.48

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de ayuda de SPSS Modeler para CRISP-DM con listas de tareas por fase y un caso de minería web de un e-retailer; el capítulo 7 trata el despliegue como plan por modelo/hallazgo, el monitoreo como criterio de «expiración» del modelo y el cierre como informe final y revisión de lecciones aprendidas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.49

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de inicio de KNIME (versión 2.x): instalación, banco de trabajo, construcción de flujos por nodos y puertos, estados de los nodos, ejecución, consola y log, preferencias, clave maestra, importación y exportación de flujos y metanodos. Es una señal de herramienta, sin contenido de operación de productos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.50

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial previo al lanzamiento de SQL Server 2005 Analysis Services: casos de uso de minería de datos, integración con Integration, Analysis y Reporting Services, API DMX y arquitectura (despliegue, escalabilidad, administración y seguridad por roles). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P410.51

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - manual de producto de un motor de minería integrado en la base de datos (Oracle 11g). Cubre funciones y algoritmos de minería, scoring con SQL, privilegios sobre modelos y modelos que llevan embebidas sus propias transformaciones («supermodels»). Su valor para Productos es sólo de práctica operativa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
