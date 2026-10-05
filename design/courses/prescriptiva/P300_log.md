# Log — P300

## S02.P300.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/` (`data/policy_options.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` con sólo `.gitkeep`, `submission/decision_brief.csv`, `submission/policy_contract.csv`, `tests/test_activity.py`); contexto de diseño en `s05-diseno-prescriptiva.md`, `activity-architecture.md` y `audit-against-design.md`.
- **Trazabilidad revisada:** P300 → `prescriptiva.C01`, `C04`; ambas sustentadas.
- **Highlights:** añadidos H01–H04 (factibilidad antes que objetivo; restricciones que cambian la acción en un menú agregado; contrato de política; prueba del contrato). Ninguno corregido ni descartado.
- **Ambigüedades:** (1) el notebook importa `main` desde `src/`, que sólo contiene `.gitkeep`; `main.py` está en `professor/`, por lo que la ejecución del notebook tal como está no queda demostrada; (2) procedencia del dataset no documentada y segmentos «probabilidad alta/media» sin definición; (3) la tabla de evaluación de las cuatro alternativas no se persiste; (4) la política es una elección entre cuatro alternativas preagregadas, no una regla por cliente.
- **Superficies / contrato / dependencias:** S01–S05 declaradas; contrato de evidencia separa código, dos CSV y pruebas de columnas; habilita el patrón de P302 y P307; no recibe de actividades previas.
- **Auditoría de Analytics:** producto prescriptivo parcial: acción factible con restricciones, salvaguarda, autoridad humana, cadencia y gatillo de revisión declarados; no hay registro de decisiones ni monitoreo ejecutado. La identidad de Analytics se preserva; no se reduce a un ejercicio de optimización.

## S03.P300.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - presentar datos, modelos e inferencias a clientes, «Knowing the audience», dashboards (AP, pp. 43–45). Categoría: ya cubierta por los planeadores persistidos (P304, P305, P309, P313, P316–P318). User-centred design, Interaction e Interface design (pp. 45–47) son fuera de alcance (Productos de datos).
  - «It is important for data science education to incorporate real data used in an appropriate context» (cap. 4.2, p. 29). Categoría: marginal. Es una expectativa general que `AGENTS.md` ya fija como regla de procedencia, y muchos Pxxx declaran casos sintéticos justificados por control experimental. El documento no aporta ningún caso ni dato concreto que permita sustituirlos.
  - privacidad y GDPR, «Apply techniques to provide data privacy … such as provide ranges or salting» (PR-Privacy, pp. 106–107; DPSIA/DP-Social Responsibility, p. 83). Categoría: fuera de alcance (Fundamentos de data / Productos de datos).
  - el currículo INFORMS 2015 incluye un curso de «Prescriptive Analytics» (p. 15). Categoría: marginal. Es una mención de contexto, sin contenidos.

## S03.P300.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Task 4.1–4.2 selección de métodos según el problema (p. 6) — ya cubierta: P306 H03, P316 H05, P317 H04 y P319 H03 justifican el método por la estructura del problema.
  - Task 5.3 «Run, verify, and evaluate the model performance and outputs» (p. 6) — ya cubierta: verificación cruzada enumeración/solver (P305 H03, P308 H04, P315 H03), validación independiente del LP (P316 H06) y validación analítica (P317 H05).
  - Task 2.5 «Identify baseline performance of the current state» (p. 5) — ya cubierta: líneas base operativas en P304 H04 (aceptar todo), P305 H02, P313 H05, P316 H03 y P318 H02.
  - Task 2.3 y 5.6 supuestos, limitaciones y restricciones documentados (pp. 5–6) — ya cubierta: `data_limitation` de P302 H03 y los contratos de P304–P319.
  - Domain III Data (p. 5: limpieza, armonización, plan de gestión de datos) — fuera de alcance: pertenece a Fundamentos de data / Productos de datos; los talleres prescriptivos reciben datos preparados.
  - Domain VI Deployment, tareas 6.4–6.6 (requisitos de producción, pruebas, flujos de datos de producción; p. 7) — fuera de alcance: frontera con Productos de datos fijada en `s05-diseno-prescriptiva.md`.
  - Task 6.1–6.2 validación de negocio e informe (p. 7) — marginal: los contratos de política con autoridad y aprobación ya cumplen esa función; un informe adicional no cambia lo que el estudiante hace.
  - Task 1.2 y 2.7 identificación de partes interesadas y acuerdo del patrocinador (pp. 4–5) — ya cubierta: autoridades y escalamientos declarados desde P300 H03 y P303 H01.

## S03.P300.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - CAP-E.5.2.2 «Identify the appropriate decision variables, constraints, and objective(s)» (p. 20) — ya cubierta: bloques `MODEL`/`DECISION MODEL` en P305, P308, P313–P319.
  - CAP-E.5.3.4 «Identify the correct verification of the solution of a simple prescriptive analytics model output» (p. 20) — ya cubierta: P305 H03, P308 H04, P316 H06, P317 H05, P318 H04.
  - CAP-E.5.2.4 «Identify an error from a list of candidate errors for a prescriptive model» (p. 20) — ya cubierta en su forma más material: P318 H02 (regla miope infactible) y P319 H03 (MILP aditivo incorrecto para un objetivo no aditivo).
  - CAP-E.2.5.1 «Identify how to measure the baseline values of the primary measures of success of the current state» (p. 12) — ya cubierta: líneas base operativas en P304, P305, P313, P316 y P318.
  - CAP-E.1.5.6 «Identify unintended direct consequences of the potential solution» y CAP-E.6.1.2 «Identify a potential ethical analytics risk» (pp. 8, 22) — ya cubierta: P320 H01–H02, P305 H06 (excepción por restricción legal/equidad) y P308 H06.
  - CAP-E.2.6.2 y 5.3.5 sesgo de modelos predictivos (pp. 12, 20) — fuera de alcance: pertenece a Predictiva; Prescriptiva recibe la estimación como evidencia.
  - Domain III (pp. 13–16: gobierno de datos, arquitectura, 4 V, normalización) y CAP-E.4.4 stack tecnológico y hoja de cálculo (p. 18) — fuera de alcance: Fundamentos de data / Productos de datos.

## S03.P300.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - beneficios, costos y sus *tradeoffs* en el caso de negocio (p. 8: CAP-P.1.5.4 «Identify the tradeoffs of business benefits and costs») — ya cubierta: valor esperado bajo factibilidad (P300 H01–H02) y razón de descarte por valor (P302 H01).
- **Señales de alcance de curso** (registradas sólo en este log):
  - sesgo de datos de entrenamiento y causas de resultados no éticos de modelos predictivos (p. 12: CAP-P.2.6.2; p. 20: CAP-P.5.3.5) — fuera de alcance: pertenece a Predictiva; Prescriptiva recibe la estimación como insumo.
  - gestión de datos, arquitectura, *stack* tecnológico, debilidades de hojas de cálculo, pruebas de despliegue y flujos de producción (p. 13–18, 23) — fuera de alcance: Fundamentos de data y Productos de datos.

## S03.P300.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Audit Dimensions» y «Error Event Schemas» (pp. 23–24) para trazabilidad — fuera de alcance: control de calidad del ETL, frontera con Productos de datos.
  - resto del documento (esquemas estrella, OLAP, jerarquías, claves sustitutas) — fuera de alcance: pertenece a Fundamentos de data / BI descriptiva.

## S03.P300.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de consenso sobre la formación de pregrado en ciencia de datos. Define el *data acumen*, es decir, la capacidad de «make good judgments … and ultimately make good decisions using data» (p. 22), en diez áreas conceptuales, y recomienda integrar la ética en todo el currículo y adoptar un código o juramento profesional. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - la ciencia de datos produce «processes that continuously take in new data … recommendations—often take on a life of their own» (p. 33). Categoría: ya cubierta. Es la definición de producto del curso (política recurrente gobernada), visible en P303 H03, P306 H07, P308 H07 y P321 H01–H02.
  - «decisions based on data are increasingly automated and in real time» y la gradación de riesgo, desde recomendadores de bajo impacto hasta sentencias o asignación de fondos con impactos «profound» (p. 32). Categoría: ya cubierta. El modo proporcional de ejecución está en P304 H06 (automatización acotada por latencia), P303 H01/H04 (escalamiento por motivo) y P308 H06 (aprobación obligatoria en una decisión que afecta derechos).
  - «a policy might be enacted that has unintended consequences for large segments of the population» (p. 32). Categoría: ya cubierta. Las consecuencias distintas ante los mismos futuros y el riesgo residual están en P304 H04, P309 H05 y P314 H04–H05.
  - Recomendación 2.4, ética «from the beginning and throughout» (p. 50), aplicada como principio transversal. Categoría: ya cubierta en lo que toca al curso. Las salvaguardas y límites de equidad aparecen declarados desde el núcleo (P305 H06, P306 en el contrato, P308 H06–H07) y P320 es transversal por arquitectura. La parte material se canaliza en la candidata de P320.
  - «It is insufficient for them to be handed a "canned" data set … they need repeated practice with the entire cycle beginning with ill-posed questions and "messy" data» (pp. 38–39). Categoría: fuera de alcance como propuesta. Es una expectativa de programa de pregrado completo y la mayoría de los Pxxx usan casos sintéticos declarados. Proponer otros datos exigiría un caso concreto que el documento no aporta. La política de procedencia de `AGENTS.md` ya gobierna esta decisión.
  - «Students also need to consider the provenance of the data used» (p. 40), con «Data provenance» como competencia (p. 45). Categoría: ya cubierta como práctica en P302 H03. La falta de procedencia en varios Pxxx ya está registrada en sus logs S02, y el documento no aporta nada específico.
  - el flujo de trabajo y la reproducibilidad (p. 46–47: «Workflows and workflow systems», «Reproducible analysis», «Source code (version) control systems»; «Longer-term projects involving interim reports … are critical»). Categoría: marginal. El curso ya fija semillas, aserciones y artefactos persistidos (P301 H05, P304 H07, P313 H02). El defecto recurrente del notebook que importa desde un `src/` vacío está registrado en S02 y es de implementación, no de este documento. Los proyectos largos con informes intermedios son estructura de programa.
  - evaluación del aprendizaje (p. 89: «Develop a code of conduct», «Create challenge questions», «Conduct long-term follow-up»), *capstone* y práctica (cap. 3) y evaluación de programas (Rec. 5.3). Categoría: fuera de alcance. Son decisiones de programa y de evaluación institucional, no de un taller. Las pruebas `pytest` de los Pxxx evalúan participación por contrato de `AGENTS.md`.

## S03.P300.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «la realidad empresarial, los problemas llegan incompletos, contradictorios, y debemos navegar la incertidumbre» (p. 177); los egresados «tienen dificultades para navegar la incertidumbre de problemas de negocio reales y mal definidos» (p. 221) — marginal: señal genérica de competencia transversal. P300 ya obliga a pasar de una recomendación a un contrato con objetivo, restricción, salvaguarda y excepción (H03). Que P300 elija dentro de un menú fijo es un límite registrado en S02. Una fuente gubernamental de empleabilidad no basta para reabrir el caso.
  - «Necesitamos personas que… entiendan el problema de negocio, que puedan traducir preguntas estratégicas en modelos analíticos y que comuniquen resultados de manera efectiva a stakeholders no técnicos» (p. 173); «evaluar trade-offs y tomar decisiones informadas» (p. 177) — ya cubierta: el contrato de política (P300 H03, P302 H04) y las razones de descarte (P302 H01) responden a esa traducción. El intercambio explícito aparece en P307 H02, P309 H04 y P317 H02.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «los analistas Big Data y especialistas BI migrarán de un rol descriptivo (reportes) a uno predictivo y prescriptivo explicando qué va a pasar y qué debemos hacer» (p. 291) — ya cubierta: es pertinencia laboral de la línea, no de un taller. La frontera entre predecir y decidir ya organiza el curso (s05; P300 H01, P306 H02, P307 H01).
  - «Los Científicos de Datos y Desarrolladores de IA/ML serán responsables de sistemas que asignan créditos, detectan fraudes, recomiendan tratamientos médicos, organizan el tráfico o priorizan casos en la justicia. La discusión sobre sesgos, ética y transparencia algorítmica…» (p. 291) — ya cubierta: hay asignación de crédito con autoridad humana (P303 H01–H04), priorización de inspecciones bajo supervisión (P305 H06), asignación sensible con anulación y retención (P308 H06–H07) y auditoría de equidad (P320 H01–H03). El documento no especifica cómo auditar ni qué métrica usar. Los defectos conocidos de P320 (no hay corrección, una sola métrica) ya están en su log S02 y no los respalda esta fuente.
  - recomendaciones de política pública (observatorio de talento, actualización curricular cada dos años, articulación academia–industria, certificaciones; pp. 122–123, 158–159, 196–197, 313–314) — fuera de alcance: se dirigen al diseño del programa y del sistema educativo, no al contenido de un taller prescriptivo.

## S03.P300.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - pertinencia laboral de «Análisis de Datos» e «Inteligencia Artificial» como temáticas priorizadas (p. 2: «temáticas priorizadas: … 2. Inteligencia Artificial 3. Análisis de Datos») — marginal: confirma pertinencia general de la analítica, pero no menciona decisión, optimización, simulación ni gobierno de políticas; governmental no define estándar ni herramientas.
  - metodología de bootcamp, *learning by doing* y mentoría (p. 1) — fuera de alcance: modalidad pedagógica de otro tipo de formación; los talleres presenciales ya son guiados y prácticos.

## S03.P300.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de ocho módulos sobre capacidades de IA, aprendizaje automático, NLP, robótica, estrategia, equipos y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «simulaciones para hacer predicciones» y capacidad de IA para «toma de decisiones» (p. 1, 4–5) — marginal: mención de folleto sin contenido operable; la simulación para validar políticas ya está en P310 y P313.
  - fundamentos de ML, redes neuronales, visión, NLP, robótica, construcción de equipos y estrategia corporativa de IA (p. 5–6) — fuera de alcance: Predictiva u otros programas; institutional ilustra, no impone identidad.

## S03.P300.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «principles and practices of managing data at scale… entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1) — fuera de alcance: gestionar datos a escala y su ciclo de vida corresponde a Fundamentos de data y a Productos de datos, no a Prescriptiva (s05: Prescriptiva «no necesita convertirse en arquitectura o despliegue de software»).

## S03.P300.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: describe los fundamentos probabilísticos de la inferencia y «the modeling and decision-making life cycle … including its human, social, and ethical implications». Sólo lista temas; no hay syllabus, casos, productos ni evaluación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «differential privacy», «permutation testing, false discovery rate», «Bayesian hierarchical models», «clustering», «recommendation systems», «decision trees, neural networks and ensemble methods» (p. 1) — fuera de alcance: son temas de Estadística, Predictiva o Productos de datos, o de protección de datos, no de diseño ni de gobierno de políticas.

## S03.P300.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa ejecutivo online de 11 semanas sin código: sesgos, descriptiva, big data, experimentación, ML, redes neuronales, dos módulos de prescriptiva (árboles de decisión; sesgos de economía del comportamiento) y ética/legal, con casos y tareas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Módulo 1 «Trampas en decisión» y tarea Carter Racing «si participar o no en una carrera» (pp. 7, 11) — fuera de alcance: decisión única de deliberación sobre sesgo de selección de datos; no es una decisión recurrente.
  - módulos de ML y redes neuronales, incluido «Aprendizaje de refuerzo para empresas» (pp. 7–8) — fuera de alcance: Predictiva; el aprendizaje por refuerzo como mecanismo de política no tiene caso ni datos en el curso y desplazaría la identidad hacia una técnica.

## S03.P300.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online sobre historia de la web y la nube, Node.js, contenedores y llaves, DevOps y sus métricas, casos de migración, serverless, empresa ágil y cloud native. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «The OODA Loop» (Módulos 5 y 7, pp. 14–15) — marginal: el ciclo observar–orientar–decidir–actuar se menciona como consigna de agilidad organizacional sin contenido; el ciclo contexto observable → acción → registro → revisión ya es el contrato de política del curso (P300 H03; arquitectura del curso).
  - contenedores, Docker, Kubernetes, serverless, PKI (pp. 13–15) — fuera de alcance: infraestructura y despliegue (Productos de datos).

## S03.P300.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso ejecutivo de 8 semanas sobre estrategia y ecosistema de datos (IA para líderes, plataformas y diseño de bases de datos, modern data stack, nube, Lean DevOps, ética/gobierno de datos). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Effective business decisions depend on precise forecasting» y «Envision and practice precise decision making based on data» (pp. 6–7) — marginal: declaración genérica; el curso ya separa explícitamente la estimación (Predictiva) de la política que la usa (P303 H02, P306 H02, P307 H01).
  - Módulo 2 «Decision-Making Frameworks», «Axiomatic Design», «Design of Organizations» (p. 14) — marginal/fuera de alcance: marcos organizacionales de diseño y decisión sin contenido operativo enseñable; la autoridad y el modo de ejecución de cada política ya están en P303 H01, P304 H06, P308 H06.
  - Módulo 1 «Reinforcement Learning» (p. 14) — fuera de alcance: técnica de IA mencionada sin caso; no hay datos ni secuencia para enseñarla como mecanismo de política con rigor.
  - Lean DevOps, data platforms, modern data stack, nube (pp. 7, 14–15) — fuera de alcance: Productos de datos / Fundamentos de data.

## S03.P300.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión e inferencia causal, clasificación, deep learning, sistemas de recomendación y redes y modelos gráficos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - maximización de influencia en redes y filtro de Kalman (p. 11) — fuera de alcance: no hay caso ni datos en el curso para enseñarlo con rigor como política, y desplazaría la identidad hacia modelado de redes.

## S03.P300.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre el proceso de diseño de productos de IA (fundamentos de ML y deep learning, interacción humano–computador, «superminds», modelo de Lawler) con capstone de propuesta de producto. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - diseño de productos de IA, modelo de Lawler, GANs, HCI (pp. 6–7) — fuera de alcance: Productos de datos / IA; desplaza la identidad del curso.

## S03.P300.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un curso online de estrategia y arquitectura de plataformas digitales y mercados de dos lados (efectos de red, precios, APIs y estándares, gating de calidad, regulación, modelado de dinámica de plataforma). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «effective decision-making processes… when to open a platform, how to use APIs to build an ecosystem of partners» (p. 8) — fuera de alcance: decisiones estratégicas únicas de producto/negocio, no decisiones operativas recurrentes con contexto observable.

## S03.P300.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso corto en línea de MIT: ODE y métodos numéricos, PDE y modelado espacial, mínimos cuadrados y optimización (gradiente, Newton), del ajuste al aprendizaje automático, métodos probabilísticos (Monte Carlo, pronóstico probabilístico, sensibilidad, eventos raros) y tres casos industriales. Sólo lista títulos de módulos y duraciones. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - ODE, Euler, métodos implícitos, PDE, discretización espacial, sistemas lineales y raíces (p. 1) — fuera de alcance: computación científica, sin relación con políticas de decisión.
  - Regresión, regularización, regresión logística, ajuste de modelos (p. 2) y «Probabilistic Forecasting» (p. 2) — fuera de alcance: construcción y validación de estimaciones, propia de Predictiva; en Prescriptiva entran como insumo (P306 H02, P307 H01).
  - Casos Aurora Flight Sciences, Schlumberger y BASF (p. 2) — fuera de alcance: sólo títulos, sin contenido para inferir un caso o una práctica; la familia institutional sólo ilustra posibilidades.

## S03.P300.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un certificado de 6 meses en ingeniería de datos (Python, SQL, ETL/CDC, contenedores, Hadoop/Spark/Airflow, streaming con Kafka/MQTT, nociones de ML, aprendizaje por refuerzo y redes profundas) con proyectos de portafolio. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Learn the fundamental concepts of reinforcement learning, including the reward matrix, the quality matrix, the Bellman equation» y proyecto «Build a reinforcement learning model for robot navigation» (pp. 8, 12) — fuera de alcance: aprendizaje por refuerzo como técnica de ML en un certificado de ingeniería de datos; el caso (navegación de robot) no es una decisión operativa gobernada y no hay datos en el curso para enseñarlo como política con autoridad y salvaguardas. La idea de política intertemporal ya se ejerce en P318 con un modelo explícito.
  - «A Model to Predict Housing Prices» / regresión lineal (pp. 9–10) — fuera de alcance: Predictiva.
  - ETL, CDC, Spark, Airflow, Kafka, streaming y seguridad web (pp. 8–11) — fuera de alcance: Fundamentos de data / Productos de datos.

## S03.P300.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de seis meses con cinco partes (fundamentos, optimización, ML, ML avanzado, despliegue), casos de estudio y capstone de portafolio. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Module 23: Data, Models, and Decisions» (p. 9) — marginal: título sin contenido verificable; la conexión modelo–decisión es la identidad del curso.
  - regresión, clustering, CART, redes neuronales, NLP (pp. 7–9) — fuera de alcance: Predictiva / Descriptiva.

## S03.P300.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso profesional en línea de MIT: decisiones tempranas de trade-off (Pugh, estudios de trade), modelos de valor con atributos jerárquicos, generación y evaluación de espacios de diseño, y exploración del tradespace (Pareto, sensibilidad, robustez, asignación de tareas entre modelos y personas). Sólo títulos y descripciones semanales; sin contenido técnico. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Pugh method, generación de conceptos y estructura de un trade study (p. 1) — fuera de alcance: selección de conceptos en diseño de sistemas, decisión única no recurrente; desplazaría la identidad hacia ingeniería de sistemas.
  - value-focused thinking y modelos de valor con jerarquías de atributos (p. 2) — marginal: el objetivo explícito de cada contrato (P300 H03, P302 H04) cumple la función en el curso; un modelo multiatributo completo sería un taller de análisis de decisiones multicriterio sin política recurrente.

## S03.P300.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de ocho semanas sobre prototipado rápido en fabricación (procesos seriales y paralelos, mapeo de atributos de prototipo, costo–valor) con capstone de decisiones de fabricación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Participants will conduct a cost analysis to determine the most efficient process to use to build the prototype» (p. 8) — fuera de alcance: decisión de ingeniería de producto, única y no recurrente; no aporta una política gobernada.
  - procesos de fabricación, DFM y prototipos conceptuales (pp. 5–7) — fuera de alcance: ingeniería mecánica, ajena a Analytics.

## S03.P300.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos, analítica predictiva, ML, IA) con una clase magistral de «Decision Analytics» que introduce optimización, simulación y análisis de decisiones para analítica prescriptiva. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «How To Tell Good Prescriptions from Bad Prescriptions» (p. 11) — ya cubierta: comparación con líneas base bajo el mismo criterio (P305 H02, P313 H05, P316 H03) y contrato de política.
  - «introducing participants to the most commonly used applied optimization, simulation and decision analysis techniques for prescriptive analytics» (p. 10) — ya cubierta y, como lista de técnicas, no impone identidad: el curso usa estas técnicas como evidencia de políticas (P305, P310, P313, P316–P319, P322).
  - módulos de estadística, regresión, ML, series de tiempo, texto y visualización (pp. 4–9, 12–14) — fuera de alcance: Descriptiva y Predictiva.

## S03.P300.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto en cinco fases: panorama y modelos de negocio de IA, liderazgo con analítica predictiva e IA generativa/agéntica, innovación, pensamiento de futuros para la decisión estratégica y gobernanza y controles de IA. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - modelos de negocio, transformación organizacional, capital de riesgo corporativo e IA agéntica (p. 5, 16, 19) — fuera de alcance: estrategia y gestión, no analítica prescriptiva.

## S03.P300.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses con cinco cursos (ingeniería de datos, Python, estadística, IA/ML, storytelling y visualización), sin contenido prescriptivo explícito. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Definir casos de negocio (coste-beneficio) a partir del análisis de un conjunto de datos para dar recomendaciones justificadas sobre una acción a realizar» (p. 8) — ya cubierta: recomendaciones con valor esperado, costo y razón de descarte desde P300 H01 y P302 H01.
  - ingeniería de datos, SQL, Python, estadística y ML (pp. 5–7) — fuera de alcance: Fundamentos de data, Descriptiva y Predictiva.

## S03.P300.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relato institucional de cuatro talleres participativos con 17 programas de pregrado de la UNAL (p. 7) sobre la noción de currículo, las funciones misionales, las prácticas pedagógicas y las propuestas de armonización. No contiene ningún programa ni curso de analítica, optimización, decisión o simulación, ni resultados de aprendizaje disciplinares. Sus señales son de pedagogía general y de gestión curricular institucional. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Centrar fines y contenidos en la resolución de problemas del contexto (p. 77: «enfocar fines y contenidos en la resolución de problemas»). Lo mismo en los nodos «Apuntar a problemas reales», «Simulaciones, casos de estudio» y «Análisis de casos» del árbol del taller 3 (p. 72), y en «¿En qué campos es pertinente la enseñanza basada en problemas?» (p. 94). Categoría: **ya cubierta**. Cada Pxxx abre con una pregunta analítica dentro de un contexto de decisión. P310–P314 se apoyan en casos y simulación, y la arquitectura organiza el curso por casos (`activity-architecture.md`). El documento no aporta un método ni un caso que cambie lo que hace el estudiante.
  - Equilibrio entre teoría y práctica (pp. 76–77: «encontrar en los planes de estudio, un equilibrio entre los componentes teóricos y los prácticos»). Categoría: **ya cubierta**. Los Pxxx son talleres presenciales en los que la solución se construye progresivamente en código (`AGENTS.md`).
  - Recursos de modelación con datos (pp. 79–80: «el uso de metadatos para la investigación a través de ejercicios de modelación aplicables en distintos aspectos de la realidad»). Categoría: **marginal**. Es una mención genérica, sin técnica, caso ni producto. El curso ya ejerce la modelación al servicio de una política (P305, P308, P313, P316–P319).
  - Evaluación como seguimiento del avance en problemas largos (p. 82: «debería expresarse como un seguimiento a diferentes porcentajes de su avance»), y autoevaluación y coevaluación (p. 82). Categoría: **fuera de alcance**. La evaluación de los Pxxx está fijada por `AGENTS.md`: `pytest` de participación sobre artefactos de `submission/`. La evaluación sumativa del curso pertenece a los Lxxx o al programa, no a la contribución de un taller. Es además pedagogía general sin anclaje disciplinar.
  - Evaluación del «saber hacer» y formación por competencias (p. 73 «saber saber… saber ser… saber hacer»; p. 82 «la evaluación debería adoptar una orientación sobre el seguimiento del “saber hacer”»). Categoría: **ya cubierta**. Las capacidades `prescriptiva.C01`–`C05` ya están formuladas como desempeños (formular, diseñar, validar, definir, monitorear), y cada Pxxx persiste un producto verificable.
  - Trabajo cooperativo y redes de apoyo entre estudiantes (pp. 78–79: «se resaltó el éxito de los métodos de estudio grupales»). Categoría: **fuera de alcance**. Es una estrategia didáctica transversal que no cambia lo que un taller enseña en lo analítico.
  - Prácticas en el sector productivo, salidas de campo, pasantías y participación de egresados en la validación de resultados de aprendizaje (p. 80; p. 107: «Egresados que permitan validar el proceso formativo y los resultados de aprendizaje»; p. 112). Categoría: **fuera de alcance**. Pertenecen a la gestión del programa y a la acreditación, no al diseño de un taller.
  - Objetivos medibles e indicadores para dar seguimiento a la propia armonización (p. 110: «la ausencia de objetivos medibles, y metas cuantificables reducen la capacidad de acción»). Categoría: **fuera de alcance**. Se refiere a la gestión institucional del currículo, no a monitorear una política analítica. El parecido con el monitoreo y los gatillos de P321 (H02) es sólo retórico y no aporta evidencia para cambiarlo.

## S03.P300.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular». Tiene cuatro ejes: Acuerdo 02/2020 del CESU, resultados de aprendizaje, actualización del PEP y planes de mejoramiento. Distingue tres dimensiones (macro, meso y microcurricular) y cuatro etapas. No contiene contenidos disciplinares ni menciona analítica, decisión u optimización. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - los resultados de aprendizaje, entendidos como «las declaraciones expresas de lo que se espera que un estudiante conozca y demuestre en el momento de completar su programa académico» (p. 2). Categoría: fuera de alcance para S03. Es un requisito de gobierno curricular del programa. En el curso corresponde a las capacidades `prescriptiva.C01`–`C05` y a la RAA, que `s05-diseno-prescriptiva.md` deja como pendiente. No cambia lo que un taller enseña.
  - el nivel microcurricular, que «compete a las didácticas y procesos de evaluación de los aprendizajes» (p. 2), y la necesidad de «diseñar los mecanismos de monitoreo y evaluación» de los resultados de aprendizaje (p. 3). Categoría: fuera de alcance. Afecta a la trazabilidad (`traceability.yaml`) y a la evaluación del programa, no al producto de ningún Pxxx. Por contrato de `AGENTS.md`, las pruebas `pytest` de los talleres verifican participación y no logro de resultados de aprendizaje. Usarlas para eso contradiría ese contrato.
  - tener en cuenta «las exigencias y necesidades del medio, la actualidad de las áreas de conocimiento, las características de los estudiantes» (p. 3) y los «estándares internacionales» (p. 2). Categoría: fuera de alcance. Es un criterio general de pertinencia que justifica el propio proceso S03 de contraste con benchmarks. No aporta una señal técnica ni pedagógica concreta sobre políticas prescriptivas.

## S03.P300.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus de posgrado centrado en el proceso de minería de datos aplicado a datos de salud (preprocesamiento, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, clustering, minería de texto) con proyecto por entregables y survey paper. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Data mining represents a variety of (descriptive, predictive, and prescriptive) models… use varying levels of human input or rules to arrive at a decision» (p. 5) — marginal: mención genérica; el gradiente de intervención humana y reglas ya es el núcleo de C04 (P303 H01, P304 H06, P308 H06) y el syllabus no aporta contenido prescriptivo ejercido.
  - texto guía «Business Analytics: Data Analysis & Decision Making» (Albright y Winston) usado sólo en capítulos 1–6 y 10–12 (descriptiva, probabilidad, regresión; pp. 2, 9) — marginal: no se cubren los capítulos de decisión, optimización ni simulación; no hay señal prescriptiva.
  - «effective processes to convert that information into actionable knowledge» (p. 2) — marginal: consigna sin método.
  - temario de minería de datos (clasificación, clustering, reglas de asociación, minería de texto; p. 9) — fuera de alcance: Predictiva / Descriptiva.
  - proyecto por entregables (propuesta, recolección, preparación, informe final, póster; pp. 5–6) — marginal: formato de evaluación de un curso de minería; los talleres Pxxx se evalúan con pytest por contrato del proyecto.

## S03.P300.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: syllabus introductorio de pregrado centrado en bases de datos (Access, modelado ER, normalización, SQL, MongoDB), BI y visualización/dashboards, con proyecto final en equipo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «leverage data to make critical business decisions… use data to make those decisions confidently» (p. 1) — marginal: declaración genérica de toma de decisiones basada en datos sin ningún contenido de decisión, optimización, simulación ni gobierno; el curso ya opera la decisión como política (P300 H03).
  - temario de modelado relacional, normalización, SQL, NoSQL/MongoDB, data warehouses y BI (pp. 5–6) — fuera de alcance: Fundamentos de data / Descriptiva.
  - proyecto final «identify a problem to solve, collect the necessary data… use insights to develop solutions» con evaluación por enunciado, informe y evaluación de pares (pp. 2–3) — marginal: formato de evaluación genérico; los talleres Pxxx se evalúan con pytest por contrato del proyecto.

## S03.P300.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Resumen del documento en 1–2 líneas: folleto de un programa online de 12 semanas (ruta con o sin código) sobre IA generativa, prompts y RAG, agentes con herramientas, memoria, planificación y razonamiento, sistemas multiagente, pruebas/evaluación y protección de soluciones agénticas, con casos prácticos y proyectos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - caso «Agente de análisis de investigación financiera… mejorando la toma de decisiones de inversión» (p. 14) y «Aplicación para startup de salud… programación de citas» (p. 15) — fuera de alcance: automatización de flujos con LLM, sin objetivo, restricciones ni política de decisión evaluable; no hay caso/datos para el curso.
  - prompts, RAG, LangChain/LangGraph, MCP, multiagente, multimodal (pp. 9–14, 18) — fuera de alcance: herramientas de IA generativa; no pertenecen a Prescriptiva.

## S03.P300.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de curso de bodegas de datos: modelado ER y dimensional (Kimball), dimensiones lentamente cambiantes, tablas de hechos, universos de SAP Business Objects, reportes Web Intelligence y tableros en Tableau. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - modelado dimensional, SCD, *chasm/fan traps*, seguridad por fila (p. 1–4) — fuera de alcance: Fundamentos de data / bases de datos; no hay señal de decisión, optimización ni gobierno de políticas.

## S03.P300.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 5. Lectura: completa. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - el propósito declarado es ir de los datos a patrones «to support making predictions and decision making» (p. 1), y la meta es «abstracting and modeling an analytic question» (p. 1). Fuera de alcance: la decisión aparece sólo como destino genérico. Ningún tema del temario trata acción, restricciones, políticas ni su gobierno, así que no hay nada que contrastar con P300–P322.
  - temario de regresión, clasificación (árboles, Naive Bayes, SVM), clustering, PCA/SVD y recomendación en redes sociales (p. 2). Fuera de alcance: son técnicas de construcción de estimaciones (Predictiva) o de descripción (Descriptiva). En Prescriptiva las estimaciones llegan como insumo (P303, P306, P308).
  - casos de Google, Facebook, Kaggle y Netflix como «how analytics is used in practice» (p. 2). Marginal: son ilustraciones motivacionales de otra institución, sin una decisión recurrente modelable.
  - herramientas (línea de comandos, gnuplot, Perl, R, Weka, SQL y NoSQL; pp. 2–3). Fuera de alcance: herramental de datos sin relación con la política prescriptiva.
