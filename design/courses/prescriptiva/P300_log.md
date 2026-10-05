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
