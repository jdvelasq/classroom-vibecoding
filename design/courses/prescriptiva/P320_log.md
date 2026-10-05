# Log — P320

## S02.P320.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/` (`data/policy_impacts.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, cuatro artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P300 y P306.
- **Trazabilidad revisada:** P320 → `prescriptiva.C04`, `C05`. Ambas sustentadas en el contrato.
- **Highlights:** añadidos H01–H03. H01 es el highlight obligatorio de caso y datos (grano política × grupo; la unidad de juicio es la política). Cifras de `equity_audit.csv` y `policy_correction_decisions.csv`; los totales de beneficio (21.000 y 18.000) son sumas de filas de los datos.
- **Ambigüedades:** (1) las celdas de `professor/notebook.ipynb` contienen secuencias `\n` literales en vez de saltos de línea: la primera celda es un único comentario y la segunda no es Python válido, por lo que el notebook no se ejecuta; (2) la decisión «suspend_and_correct» no va acompañada de una corrección; (3) no se audita ninguna política producida en el curso, aunque la arquitectura la define como transversal; (4) procedencia del dataset no declarada; (5) la prueba sólo verifica presencia de archivos.
- **Superficies / contrato / dependencias:** S01–S06 declaradas. Recibe sólo el patrón de contrato; no habilita dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = decisión de aprobar o suspender una política con guarda, autoridad, escalamiento y gatillos. Auditoría resuelta en el contrato; incompleta frente a la arquitectura (falta la corrección).
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P320.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P320.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 7.5 efectos colaterales en el tiempo (p. 7) — marginal para P320: su auditoría de equidad ya convierte una consecuencia distributiva en guarda (H01); el seguimiento temporal se integra en la candidata de P321.

## S03.P320.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.1.2.2 «Identify stakeholders and bystanders» (p. 7) — marginal: P308 y P320 ya distinguen afectados (familias, grupos) de decisores; no cambia lo que el estudiante hace.

## S03.P320.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - consecuencias indirectas y efectos adversos a lo largo del tiempo (p. 8: CAP-P.1.5.6; p. 25: CAP-P.7.5.1 «Identify likely adverse consequences of implementing the analytics solution») y temas éticos en el informe de validación (p. 22: CAP-P.6.1.2) — ya cubierta en su núcleo por P320 H01–H03 (guarda de equidad que decide y gobernanza) y, como consecuencias operativas, por P304 H04 y P309 H05; el documento sólo fija una expectativa general, sin método nuevo que enseñar.

## S03.P320.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - sesgos en *predictive policing* (p. 34) y «algorithmic bias» en la priorización de inspecciones o controles. Categoría: fuera de alcance para P305, porque su caso declara que no hay atributos protegidos (S01) y no hay datos para modelar equidad con rigor. La auditoría por grupo está cubierta en P320 H01–H02.

## S03.P320.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - rol «AI Safety & Governance Lead: políticas de IA responsable, privacidad, cumplimiento, gestión de riesgo de modelo» (pp. 160, 332); «evals, observabilidad, gobierno y seguridad como “primeras clases”» (p. 333) — fuera de alcance: es gobierno de plataformas de IA y LLM (cumplimiento, privacidad, red-teaming), propio de Productos de datos o de un curso de IA. Prescriptiva gobierna la política (autoridad, salvaguardas, gatillos), lo que ya hacen P303, P308, P320 y P321.

## S03.P320.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - focalización de la inversión en grupos poblacionales (p. 3: «Equidad de la mujer … Grupos Étnicos … Víctimas») — fuera de alcance: describe a quién se dirige el programa público, no un método de auditoría de equidad de políticas; no aporta caso ni datos utilizables.

## S03.P320.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - implementación responsable con tolerancia al riesgo, supervisión y gobernanza (p. 5) y sesgos (p. 5–6) — ya cubierta: guardas, autoridad y gatillos de P320 H01–H03 y registro operativo de P321; el folleto es de nivel directivo y no aporta método.

## S03.P320.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «human, social, and ethical implications» (p. 1) — ya cubierta: P320 audita la equidad con una guarda que decide (H01–H03). La ficha no especifica práctica ni criterio que cambie lo que hace el estudiante.

## S03.P320.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Módulo 9 «RGPD… Privacidad y anonimización… Hacking» y tarea TalkTalk (pp. 8, 11) — fuera de alcance: cumplimiento legal y seguridad de datos; no son equidad ni salvaguardas de una política de decisión.

## S03.P320.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online sobre historia de la web y la nube, Node.js, contenedores y llaves, DevOps y sus métricas, casos de migración, serverless, empresa ágil y cloud native. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Módulo 8 «Ethics – AI Bias and Fairness Part I/II», «Data Governance and Compliance» (p. 15) — ya cubierta/marginal: P320 ya convierte un umbral de equidad en guarda que decide (H01–H03); el folleto no aporta métrica, método ni caso distinto. El gobierno de datos y cumplimiento es de Fundamentos/Productos de datos.

## S03.P320.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión e inferencia causal, clasificación, deep learning, sistemas de recomendación y redes y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre el proceso de diseño de productos de IA (fundamentos de ML y deep learning, interacción humano–computador, «superminds», modelo de Lawler) con capstone de propuesta de producto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online de estrategia y arquitectura de plataformas digitales y mercados de dos lados (efectos de red, precios, APIs y estándares, gating de calidad, regulación, modelado de dinámica de plataforma). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso corto en línea de MIT: ODE y métodos numéricos, PDE y modelado espacial, mínimos cuadrados y optimización (gradiente, Newton), del ajuste al aprendizaje automático, métodos probabilísticos (Monte Carlo, pronóstico probabilístico, sensibilidad, eventos raros) y tres casos industriales. Sólo lista títulos de módulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un certificado de 6 meses en ingeniería de datos (Python, SQL, ETL/CDC, contenedores, Hadoop/Spark/Airflow, streaming con Kafka/MQTT, nociones de ML, aprendizaje por refuerzo y redes profundas) con proyectos de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Module 16: Fairness and Bias Issues in Data-Driven Predictions» y caso de algoritmos de análisis facial (pp. 8, 10) — fuera de alcance en su forma predictiva; la equidad de la política está cubierta por P320 H01–H02.

## S03.P320.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - trade-off entre criterios en conflicto (pp. 2–4) — marginal para P320: el intercambio beneficio total–equidad que S02 señala como no discutido es un defecto propio de P320, pero este documento no aporta nada específico sobre equidad.

## S03.P320.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre prototipado rápido en fabricación (procesos seriales y paralelos, mapeo de atributos de prototipo, costo–valor) con capstone de decisiones de fabricación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos, analítica predictiva, ML, IA) con una clase magistral de «Decision Analytics» que introduce optimización, simulación y análisis de decisiones para analítica prescriptiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - gobernanza de IA, controles empresariales, riesgo, confianza y rendición de cuentas (p. 4, 8, 17) — ya cubierta: salvaguardas, autoridad, monitoreo y gatillos de P320–P321; el documento sólo lista temas.

## S03.P320.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses con cinco cursos (ingeniería de datos, Python, estadística, IA/ML, storytelling y visualización), sin contenido prescriptivo explícito. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Igualdad de género como eje transversal del currículo (p. 77: «considerar, como eje transversal, contenidos orientados hacia propósitos de igualdad de género»). Categoría: **marginal**. P320 ya audita brechas entre grupos como guarda que decide (H01–H02). El documento no aporta métrica, caso ni método. La familia institutional ilustra posibilidades y no impone un eje temático.

## S03.P320.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular». Tiene cuatro ejes: Acuerdo 02/2020 del CESU, resultados de aprendizaje, actualización del PEP y planes de mejoramiento. Distingue tres dimensiones (macro, meso y microcurricular) y cuatro etapas. No contiene contenidos disciplinares ni menciona analítica, decisión u optimización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P320.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus de posgrado centrado en el proceso de minería de datos aplicado a datos de salud (preprocesamiento, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, clustering, minería de texto) con proyecto por entregables y survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
