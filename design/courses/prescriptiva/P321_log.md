# Log — P321

## S02.P321.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/` (`data/recommendation.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `submission/policy_register.csv`, `tests/test_activity.py`); para relaciones, P300 y P311.
- **Trazabilidad revisada:** P321 → `prescriptiva.C04`, `C05`. Ambas sustentadas como declaración; C05 sin datos de seguimiento.
- **Highlights:** añadidos H01–H03. H01 es el highlight obligatorio de caso y datos (la entrada es una recomendación ya tomada, no observaciones).
- **Ambigüedades:** (1) la recomendación no proviene de ninguna actividad previa, aunque su contexto recuerda a P311; (2) 12 de los 17 campos del registro están escritos en el código; (3) no hay datos de seguimiento, por lo que el gatillo nunca se evalúa; (4) solapamiento posible con los contratos JSON que cierran cada taller.
- **Superficies / contrato / dependencias:** S01–S05 declaradas. Sin dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = registro operativo de una política con autoridad, meta y gatillo. Auditoría parcialmente resuelta: el producto documenta una política pero no la produce ni la monitorea con evidencia.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P321.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Design situation reports for senior managers …» y «Communication … must be underpinned by an evidence-based approach to decision making … where the reasons for decisions may require clarification» (PR-Communication, pp. 104–105), más la entrega de resultados «in the client's terminology» (cap. 6, p. 39). Categoría: ya cubierta por el registro operativo con supuesto, alternativa no elegida, indicador y responsable (H01–H03). La falta de evidencia que sustente la recomendación ya es un límite de S02 que este documento no especifica.

## S03.P321.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P321.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P321.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - métricas de desempeño aceptable, documentación para distintas audiencias y para reutilizar la solución si cambian las circunstancias (p. 23: CAP-P.6.4.2; p. 24–25: CAP-P.7.1.1, 7.6.1) — ya cubierta: P321 H01–H02 conserva supuesto y alternativa no elegida y vincula indicador, meta, gatillo y responsable.

## S03.P321.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dashboards que dan «situational awareness for decision makers» (p. 45) y comunicación a no expertos (pp. 47–48: «Ability to understand client needs», «Clear and comprehensive reporting»). Categoría: ya cubierta y, en parte, fuera de alcance. El registro operativo con indicador, gatillo y responsable está en P321 H01–H02, y la explicación ante la autoridad en P305 H04 y P308 H05. El dashboard descriptivo corresponde a Descriptiva o a Productos de datos.

## S03.P321.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Capacidad de explicar conceptos técnicos complejos a audiencias no técnicas» (p. 158); «comunicación efectiva» (pp. 177, 196) — marginal: la competencia comunicativa genérica no cambia el producto de P321 (registro operativo con indicador, meta, gatillo y responsable, H01–H02). Los límites de P321 (recomendación dada, sin datos de seguimiento) ya están en S02 y esta fuente no los toca.
  - monitoreo de modelos («model drift, data drift») y reentrenamiento; «justificar predicciones (explicabilidad/interpretabilidad de modelos)» (p. 176) — fuera de alcance: son monitoreo y explicabilidad del modelo predictivo, que pertenecen a Predictiva y Productos de datos. El monitoreo de la política (resultados, gatillos y respuesta) ya está cubierto en P306 H07, P308 H07 y P319 H06.
  - rol «AI Safety & Governance Lead: políticas de IA responsable, privacidad, cumplimiento, gestión de riesgo de modelo» (pp. 160, 332); «evals, observabilidad, gobierno y seguridad como “primeras clases”» (p. 333) — fuera de alcance: es gobierno de plataformas de IA y LLM (cumplimiento, privacidad, red-teaming), propio de Productos de datos o de un curso de IA. Prescriptiva gobierna la política (autoridad, salvaguardas, gatillos), lo que ya hacen P303, P308, P320 y P321.

## S03.P321.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - implementación responsable con tolerancia al riesgo, supervisión y gobernanza (p. 5) y sesgos (p. 5–6) — ya cubierta: guardas, autoridad y gatillos de P320 H01–H03 y registro operativo de P321; el folleto es de nivel directivo y no aporta método.

## S03.P321.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «a focus on ensuring reliable, scalable operationalization» (p. 1) — fuera de alcance: operacionalizar con confiabilidad y escala es infraestructura (frontera con Productos de datos en s05). La operación de la política que sí toca a Prescriptiva ya está en el registro, los gatillos y el monitoreo (P303 H03, P306 H07, P321 H01–H02). Además, la ficha no describe prácticas concretas que puedan contrastarse.

## S03.P321.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: describe los fundamentos probabilísticos de la inferencia y «the modeling and decision-making life cycle … including its human, social, and ethical implications». Sólo lista temas; no hay syllabus, casos, productos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa ejecutivo online de 11 semanas sin código: sesgos, descriptiva, big data, experimentación, ML, redes neuronales, dos módulos de prescriptiva (árboles de decisión; sesgos de economía del comportamiento) y ética/legal, con casos y tareas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - métricas DevOps «Wait Time, Deployment Frequency, Service Restoration Time, and Failure Rate» (p. 14) — fuera de alcance: indicadores de desempeño del proceso de entrega de software (Productos de datos), no indicadores de resultado de una política de decisión.

## S03.P321.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso ejecutivo de 8 semanas sobre estrategia y ecosistema de datos (IA para líderes, plataformas y diseño de bases de datos, modern data stack, nube, Lean DevOps, ética/gobierno de datos). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión e inferencia causal, clasificación, deep learning, sistemas de recomendación y redes y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre el proceso de diseño de productos de IA (fundamentos de ML y deep learning, interacción humano–computador, «superminds», modelo de Lawler) con capstone de propuesta de producto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Define metrics for success in adoption and customer engagement» (p. 8) — marginal: métricas de crecimiento de una plataforma, no indicadores de resultado de una política con gatillo y responsable (P321 H02 ya cubre esto).

## S03.P321.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso corto en línea de MIT: ODE y métodos numéricos, PDE y modelado espacial, mínimos cuadrados y optimización (gradiente, Newton), del ajuste al aprendizaje automático, métodos probabilísticos (Monte Carlo, pronóstico probabilístico, sensibilidad, eventos raros) y tres casos industriales. Sólo lista títulos de módulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un certificado de 6 meses en ingeniería de datos (Python, SQL, ETL/CDC, contenedores, Hadoop/Spark/Airflow, streaming con Kafka/MQTT, nociones de ML, aprendizaje por refuerzo y redes profundas) con proyectos de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de seis meses con cinco partes (fundamentos, optimización, ML, ML avanzado, despliegue), casos de estudio y capstone de portafolio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso profesional en línea de MIT: decisiones tempranas de trade-off (Pugh, estudios de trade), modelos de valor con atributos jerárquicos, generación y evaluación de espacios de diseño, y exploración del tradespace (Pareto, sensibilidad, robustez, asignación de tareas entre modelos y personas). Sólo títulos y descripciones semanales; sin contenido técnico. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre prototipado rápido en fabricación (procesos seriales y paralelos, mapeo de atributos de prototipo, costo–valor) con capstone de decisiones de fabricación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos, analítica predictiva, ML, IA) con una clase magistral de «Decision Analytics» que introduce optimización, simulación y análisis de decisiones para analítica prescriptiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - gobernanza de IA, controles empresariales, riesgo, confianza y rendición de cuentas (p. 4, 8, 17) — ya cubierta: salvaguardas, autoridad, monitoreo y gatillos de P320–P321; el documento sólo lista temas.

## S03.P321.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Anticipar y gestionar las preguntas de los diversos públicos y audiencias» (p. 8) — marginal: la comunicación de la política a su autoridad ya se materializa en contratos y registros (P321 H01–H02); no cambia lo que el estudiante hace.

## S03.P321.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relato institucional de cuatro talleres participativos con 17 programas de pregrado de la UNAL (p. 7) sobre la noción de currículo, las funciones misionales, las prácticas pedagógicas y las propuestas de armonización. No contiene ningún programa ni curso de analítica, optimización, decisión o simulación, ni resultados de aprendizaje disciplinares. Sus señales son de pedagogía general y de gestión curricular institucional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular». Tiene cuatro ejes: Acuerdo 02/2020 del CESU, resultados de aprendizaje, actualización del PEP y planes de mejoramiento. Distingue tres dimensiones (macro, meso y microcurricular) y cuatro etapas. No contiene contenidos disciplinares ni menciona analítica, decisión u optimización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus de posgrado centrado en el proceso de minería de datos aplicado a datos de salud (preprocesamiento, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, clustering, minería de texto) con proyecto por entregables y survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Present data-driven insights using data visualization and dashboards», «Tell compelling stories with data» (p. 1) y semanas 13–14 de visualización (p. 7) — fuera de alcance/marginal: comunicación descriptiva de hallazgos, no comunicación de una recomendación con su gatillo y autoridad, que P321 ya cubre (H01–H02).

## S03.P321.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - módulo 03 «Registro de la toma de decisiones para una mayor transparencia», «Evaluación con intervención humana» (p. 13) — ya cubierta: el registro versionado por decisión y la autoridad humana están en P303 H03–H04, P306 H07–H08 y P321 H01–H03; el folleto no aporta método ni forma de evidencia distinta.

## S03.P321.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - construcción y publicación de tableros y reportes con filtros e interactividad (p. 4: «Building dashboards … Sharing your dashboards») — fuera de alcance: inteligencia de negocios descriptiva; el seguimiento de una política se ejerce en P321 mediante registro, indicador, meta y gatillo, no mediante una herramienta de BI.

## S03.P321.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 5. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - una lista de títulos de métodos y herramientas de un programa de business analytics, sin descripciones, objetivos ni evaluación: recolección de datos, A/B testing, correlación y causalidad, pronóstico, regresión, «Simulation Toolkit» (Analysis ToolPak, Solver), visualización, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Módulo 9 (p. 1: «Explain important components of different use cases of analytics in business and create a plan to put data to work in your organization»). Categoría: **marginal**. Cada Pxxx ya cierra con un contrato que hace operable la recomendación (P300 H03 en adelante), y P321 registra la operación y el seguimiento (H01–H02). Un «plan para poner los datos a trabajar» de nivel organizacional no es una política recurrente y desplazaría la identidad del curso.

## S03.P321.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DataOps «Los productos analíticos pasan de ser proyectos con un final definido a convertirse en activos que evolucionan» y MLOps «desplegar, monitorear y gestionar el ciclo de vida de los modelos» (pp. 53–55) — fuera de alcance: operación de productos de datos y modelos (Productos de datos); el monitoreo de resultados de la política ya está en P306 H07, P308 H07, P321 H02.

## S03.P321.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 10. Lectura: completa (pp. 2–9 en texto). Las pp. 1 y 10 tienen poco texto: sólo repiten el título, que funciona como portada y cierre. No se pudieron renderizar porque el PDF no existe en `/mnt/user-data/uploads/classroom-vibecoding/design/benchmarks-pdf/literature-derived/`. Por su posición y su título no parecen tener contenido sustantivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P321.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha mínima de indicador con «Línea base y meta», «Responsable», «Frecuencia» y «Decisión asociada» (p. 23) — ya cubierta en su forma declarativa por P321 H02; su ejercicio con datos se integra en la candidata de P321 de `informs-analytics-framework-2024`.

## S03.P321.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P321.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Root Cause Analysis / 5 Whys / Current reality tree» (p. 10) — fuera de alcance: diagnóstico organizacional de un equipo de data science; no se aplica a la revisión de una política.

## S03.P321.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclos de revisión con cadencias distintas (p. 6: «Trimestral: Strategy reviews / Mensual: Operations & risk reviews … Semanal: replenishment review») — marginal: son cadencias de gestión de trabajo de un equipo; la cadencia de decisión y de revisión de la política ya es campo del contrato desde P300 H03 y del registro de P321 H02.
  - *epic owner* que crea «el panel de monitoreo y medida para los KPIs» (p. 14) — marginal: rol de gestión de proyecto; responsable y acción de revisión ya están en P321 H02.

## S03.P321.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclo de vida con monitoreo/medición de beneficio y retiro (p. 23: «Monitoring / benefit measurement … Decommission») — ya cubierta: gatillos de suspensión y revisión (P312 H02, P309 H06) y registro con acción de revisión (P321 H02); retirar una política está implícito en la suspensión.
  - *epic hypothesis statement* con beneficio predicho y métrica (p. 25: «Resulting in [predicted benefit] … Measured by [metrics]») — marginal: plantilla de gestión de portafolio; el registro operativo de P321 ya vincula supuesto, indicador y meta.

## S03.P321.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Monitoreo de la lógica de negocio y validez de los datos» (p. 10) y «Transparencia: Alertas automáticas, dashboards» (p. 2) — fuera de alcance: la observabilidad y las alertas de un pipeline pertenecen a Productos de datos. En Prescriptiva, la validez de las entradas ya aparece como guarda o condición de retención (P308 H06 «predicción ausente o sin vigencia»; P304 H06 «solicitudes con datos válidos») y el monitoreo de resultados como gatillo (P306 H07, P321 H02).

## S03.P321.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre DataOps aplicado a ciencia de datos y ML: deuda técnica, pruebas automáticas, ambientes, orquestación, contenedores, arquitectura de datos y prácticas ágiles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
