# Log — P400

## S02.P400.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P400_code_testing_unittest/` (`data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_totals.csv`, `tests/test_activity.py`); contexto en `s05-diseno-productos.md` y `structure-audit.md`.
- **Trazabilidad revisada:** P400 → `productos.C02`, `productos.C05`. C05 sin evidencia observable.
- **Highlights:** añadidos H01 (regla aislada), H02 (prueba `unittest`), H03 (caso y datos: ausencia de particularidad como límite).
- **Ambigüedades:** la prueba de lógica vive en `professor/` y no forma parte de la evaluación; no hay `HOW_TO_RUN_ME.txt` ni notebook para el estudiante; el dato no tiene procedencia y la variable `daily_units_produced` no tiene fecha.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; la prueba de evaluación sólo verifica existencia; habilita P408 y P412–P414 por reutilización del indicador y del archivo.
- **Auditoría de Analytics:** no resuelta. El indicador es trivial y sin usuario; la actividad se lee como práctica genérica de pruebas unitarias (pregunta 5).

## S03.P400.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).
- **Señales de alcance de curso** (registradas sólo en este log):
  - DPSIA/DS y DP-Cryptography/Communication Protocols (pp. 84–89: cifrado, PKI, modelos de amenaza, árboles de ataque), DG-Data Privacy (p. 74: GDPR, HIPAA, leyes transfronterizas), PR-Intellectual Property (pp. 109–110) — fuera de alcance: ciberseguridad y derecho; no hacen operable una capacidad analítica concreta.
  - DPSIA/AS (pp. 92–94: ML para telemetría de seguridad, aprendizaje adversarial, LIME) y PR-Ethical (p. 108: sesgo en datos y algoritmos) — fuera de alcance: métodos analíticos y evaluación de modelos (Predictiva) y aplicación de dominio.
  - BDS-Cloud Computing y Software Support (pp. 60–61: diseño de centros de datos, «Concepts of auto scaling and serverless computing») — fuera de alcance: frontera explícita (no Big Data ni cloud engineering).
  - SDM-Software Design (p. 121: «Execute a basic Data (Science) Lifecycle on a simple data product»; mentalidad de ciclo de vida) y AP-User-centred design (p. 47: «Diagram the life of an interface, dashboard, or visualization including long-term use and maintenance») — ya cubierta a nivel de curso: es la pregunta organizadora de productos (C01–C05); no aporta mecanismo nuevo.
  - DG-Data Acquisition/Integration/Reduction/Transformation (pp. 70–73) — fuera de alcance: pertenecen a Fundamentos de data; el curso no vuelve a preparar datos.

## S03.P400.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** aporta a N01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Dominios I, II, IV y V (p. 4–6: encuadre del problema de negocio y del problema analítico, selección de método, desarrollo del modelo) — fuera de alcance: pertenecen a Fundamentos, Descriptiva, Predictiva y Prescriptiva; el curso no vuelve a formular ni a modelar el problema.
  - Task 7.3 «Support training activities» (p. 7) — fuera de alcance: capacitación de usuarios; no hay caso ni producto analítico que la haga enseñable con rigor en un taller.
  - Task 7.5 «Analyze the side effects of the analytics solution over time» (p. 7) — fuera de alcance por ahora: exige una capacidad en operación con historia de efectos (bucles de retroalimentación, efectos no previstos) que ningún caso del curso tiene; podría retomarse si P451 alimentara una mejora real.
  - Task 4.3/4.4 arquitectura y stack tecnológico (p. 6) — fuera de alcance: arquitectura empresarial y elección de plataforma, que son fronteras explícitas del curso.

## S03.P400.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Support training activities» (p. 25, CAP-E.7.3.1) — fuera de alcance: capacitación de audiencias, no operación de la capacidad.
  - dominios I–V (encuadre del problema de negocio y analítico, datos, selección de método, desarrollo de modelos; pp. 7–21) — fuera de alcance: responsabilidades de Fundamentos, Descriptiva, Predictiva y Prescriptiva según las fronteras del curso.

## S03.P400.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Temario del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con tareas y subtareas evaluables (pesos: Deployment 10 %, Lifecycle Management 9 %). Sólo los dominios VI–VII y algunas subtareas de III (linaje, gobierno, calidad) tocan la operación de capacidades. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Task 6.4 «Create requirements for a deployed analytics solution including model, usability, system, and business» (p. 23); CAP-P.6.4.1 «Identify what is missing or does not belong in an outline of the requirements of a production system» — marginal: los elementos del contrato operativo ya se acumulan en la tarjeta de producto (P408 H01, P409 H02 consumidor, P411 H02 responsable), el contrato de API (P425 H01), la compatibilidad de contrato (P434 H01), el nivel de servicio (P445) y la ficha de catálogo (P454 H01). Añadir campos a la tarjeta no cambia la contribución (Git) de P408–P411; la falta de mapeo de C01 es una decisión de curso ya registrada en S02 (P425, P434, P445).
  - Task 7.3 «Support training activities»; CAP-P.7.3.1 «type of training that is needed for an IT audience» (p. 25) — fuera de alcance: gestión del cambio/capacitación, no operación de la capacidad.
  - CAP-P.4.4.1 fortalezas y debilidades del stack «on-premise, cloud, open source vs. proprietary, platforms» (p. 18) — fuera de alcance: selección de plataforma/cloud engineering, excluida por las fronteras del curso.
  - CAP-P.2.6.2 y CAP-P.5.3.5 sesgo en datos de entrenamiento y resultados no éticos (pp. 12, 20) — fuera de alcance: método predictivo de origen.

## S03.P400.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - dimensiones lentamente cambiantes tipos 0–7 (pp. 15–16: tipo 1 «destroys history»; tipo 2 con «row effective date … row expiration date … current row indicator») — fuera de alcance: el diseño de historia de atributos es modelado dimensional (Fundamentos de data / Descriptiva). Como preocupación operativa (un agregado publicado cambia según se reporte «as-was» o «as-is»), no existe en el curso un atributo de referencia que cambie (p. ej., reasignación de máquina a fábrica) y crear uno sería un dato sintético por conveniencia; sólo se recuperó la consecuencia operativa (reexpresar agregados) en la candidata de P438.
  - arquitectura de bus, matriz de bus y matriz oportunidad/interesados (pp. 13–14), agregados y navegación de agregados (p. 8), tablas de hechos en tiempo real con «hot partition» (p. 24), monedas y unidades múltiples (p. 19) — fuera de alcance: arquitectura empresarial de datos y diseño físico de bodegas, excluidos por las fronteras del curso.

## S03.P400.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Marco de pregrado que define la «data acumen» (diez áreas conceptuales) y recomienda que la ética y la reproducibilidad atraviesen el currículo; trata el flujo de trabajo y la gestión de datos como competencias generales, no la operación de productos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - los productos de la ciencia de datos «take on a life of their own far beyond the initial question» y adquieren rasgos de ingeniería: infraestructuras que «must safely withstand unanticipated changes in demand and use» (p. 33); los flujos de trabajo «also produce data—such as intermediate data sets» (p. 31) — ya cubierta: es la razón de ser del curso (capacidades `productos.C01`–`C05` en `s05-diseno-productos.md`); respalda la línea sin cambiar ningún taller.
  - los estudiantes necesitan «repeated practice with the entire cycle beginning with ill-posed questions and “messy” data» y es «insufficient for them to be handed a “canned” data set» (pp. 38–39); también «real-world data and problems that can reinforce the limitations of tools» (p. 41) — ya registrada: coincide con el riesgo de identidad que S02 anota en H03/H02 «caso y datos (límite)» de P400, P405, P407, P412–P419, P428–P441 (indicador trivial de cuatro filas o datos sin capacidad). Es evidencia de apoyo para esa discusión de curso, pero el documento no aporta un caso ni un criterio operable que permita proponer aquí un cambio concreto distinto del ya registrado.
  - niveles de riesgo de las aplicaciones (recomendador de bajo riesgo frente a decisiones de libertad condicional, tratamiento o asignación de fondos, p. 32) — marginal: podría graduar salvaguardas (revisión humana, acceso), pero el documento no da criterio operable; P450 y P452 ya ejercen las salvaguardas.
  - juramento: «avoiding misrepresentations of data and analysis results» y «tread with care in matters of privacy and security» (p. 138); código de ética con la responsabilidad de «ensure that results produced by the analyst are reproducible» (p. 51) — ya cubierta en principio (P412, P419, P453); es un marco normativo general, sin práctica propia que añadir.
  - detección de sesgo algorítmico y equidad en el uso de modelos y en la elección de datos de entrenamiento (pp. 50–51) — fuera de alcance: evaluarlos pertenece a la línea predictiva; en productos sólo entraría como monitoreo por subgrupo de una capacidad real, y ningún taller tiene caso ni datos con grupos y etiquetas que lo permitan con rigor.
  - «Documentation and code standards» y la mejora incremental de los flujos «in an evidence-based fashion» (p. 47) — marginal: no especifica una práctica distinta de las pruebas, CI y registro ya presentes (P400–P417); la falta de mejora a partir de la retroalimentación en P451 (C05 «mejorar» no ejercido) ya está registrada en S02 y este documento habla de flujos de trabajo, no de retroalimentación de usuarios.
  - programas de pregrado con resultados sobre «software development and refinement» (Nashua, p. 67) y capstone CRISP-DM con «original yet reproducible analyses» (Montgomery, p. 67); plataformas en la nube (p. 87) — fuera de alcance: describen otras modalidades o infraestructura institucional, no prácticas del curso.

## S03.P400.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Estudio de política pública que cuantifica la brecha de talento TI en Colombia y la pertinencia de la oferta educativa. Para Productos de datos su valor es de pertinencia laboral: escasez de perfiles DevOps/SRE/MLOps y una brecha formativa en prácticas de producción (CI/CD real, rollback, secretos, monitoreo de deriva, seguridad). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - escasez de MLOps, DevOps y SRE y baja oferta curricular (p. 157: «ingenieros MLOps evidencian una alta demanda con oferta limitada»; p. 163: «DevOps y SRE | 36 % escasez. CI/CD, IaC, Kubernetes, monitoring»; p. 171: «DevOps y SRE | 36 % escasez | <15 % con formación») — ya cubierta: confirma la pertinencia de la línea DataOps/MLOps del curso (`productos.C02`, `C05`); no prescribe contenidos.
  - los proyectos académicos se hacen «con alcance limitado, requisitos completamente definidos, sin integración con sistemas existentes, sin consideraciones de escalabilidad, seguridad o mantenibilidad» (p. 183), y las herramientas se usan en «escenarios académicos simples» (p. 176) — ya registrada: coincide con el riesgo de identidad que S02 anota en P400–P441 (indicador trivial, sin usuario). Respalda las mejoras que fortalezcan el caso, pero por sí sola no define una propuesta.
  - el científico de datos senior combina «despliegue de modelos en producción» con «experiencia real en impacto medible» (p. 291); el arquitecto de IA responde por «modelos, pipelines de datos, integración con aplicaciones core, gobernanza y ética/seguridad de datos» (p. 285) — ya cubierta: corresponde al encuadre C01–C05; es una descripción de rol, no un mecanismo enseñable distinto.
  - Kubernetes, service mesh, infraestructura como código, multi-cloud, alta disponibilidad y disaster recovery en la nube, serverless (pp. 173, 175–176) — fuera de alcance: cloud engineering y arquitectura de plataforma, excluidas explícitamente por `s05-diseno-productos.md`.
  - roles emergentes de LLMOps, AI Evaluations Engineer («define gold sets, métricas… red-teaming y reporting continuo») y AI Reliability/Observability (p. 160; pp. 331–336) — fuera de alcance: no hay una capacidad basada en LLM en el curso y el anexo es prospectivo («propuestos por inferencia», p. 336). Sus componentes generales (evaluación continua, deriva, observabilidad) ya están en P403, P422, P423 y P442.
  - habilidades blandas y comunicación con no técnicos (pp. 158, 164–165, 177) — fuera de alcance: transversales y no específicas de Productos de datos.

## S03.P400.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - temáticas priorizadas «Programación», «Inteligencia Artificial», «Análisis de Datos», «BlockChain», «Arquitectura en la nube», «Ciberseguridad» (p. 2) — fuera de alcance: confirman pertinencia laboral general de datos e IA, pero cloud, ciberseguridad y blockchain están explícitamente fuera de la frontera del curso (no es cloud engineering ni ingeniería de software general); la familia governmental no prescribe temas.
  - metodología «Learning by doing», aula que «simula situaciones reales de trabajo» y «desafíos concretos» (p. 1) — ya cubierta: la convención de talleres presenciales `Pxxx_` guiados por el profesor; la debilidad registrada del curso (indicadores triviales sin usuario) no la resuelve este documento, que no aporta caso ni datos.
  - «metodologías ágiles, la colaboración y el aprendizaje compartido» y papel del mentor (p. 1) — fuera de alcance: rasgos pedagógicos del formato bootcamp; no definen contenido de Productos de datos.
  - meta de 94.696 personas, cohortes y regionalización (pp. 2–4) — fuera de alcance: datos de política pública sin relación con ninguna capacidad `productos.C01`–`C05`.

## S03.P400.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de dos meses sin requisitos técnicos sobre capacidades de IA (ML, redes neuronales, visión, NLP, robótica), estrategia de IA y equipos de IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Implementación responsable de la IA: tolerancia al riesgo, supervisión y gobernanza» (p. 5) — ya cubierta en el nivel de mecanismos (P450, P452, P446–P447); el enfoque estratégico-ejecutivo es fuera de alcance.
  - «Calidad de datos, representatividad y por qué fallan los modelos» (p. 5) — fuera de alcance: pertenece a Predictiva; la validación operacional de entradas ya está en P404/P422.
  - módulos de redes neuronales, visión, NLP, robótica, estrategia y equipos de IA (p. 4–6) — fuera de alcance: capacitación ejecutiva en IA, sin relación con operar una capacidad analítica.

## S03.P400.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de 4 unidades (cruzado con COMPSCI C187) sobre gestión de datos a escala para análisis y ML, con énfasis en una operacionalización confiable. Sólo incluye la descripción, los prerrequisitos y datos administrativos; no trae temario, prácticas ni evaluación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration, with a focus on ensuring reliable, scalable operationalization» (p. 1) — ya cubierta: el énfasis en una operacionalización confiable coincide con `productos.C02`/`C05`. Preparación, exploración, visualización y ML corresponden a Fundamentos, Descriptiva y Predictiva, a los que el curso no vuelve.
  - «managing data at scale» (p. 1) — fuera de alcance: escala y Big Data son una frontera explícita del curso. Además, la ficha no dice cómo se operacionaliza, así que no hay mecanismo que contrastar.
  - prerrequisitos de programación (COMPSCI 61B o equivalente) y de ciencia de datos de nivel superior (DATA C100 o equivalente) (p. 1) — fuera de alcance: es una decisión de otra institución. El programa admite cohortes heterogéneas y declara que no hay prerrequisitos entre cursos (`s05-diseno-productos.md`).

## S03.P400.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: fundamentos probabilísticos de la inferencia y «ciclo de vida de modelado y toma de decisiones» con sus implicaciones humanas, sociales y éticas. Lista temas (decisión frecuentista y bayesiana, FDR, inferencia causal, Thompson sampling, Q-learning, privacidad diferencial, sistemas de recomendación) sin resultados de aprendizaje ni prácticas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - diseño experimental, inferencia causal, Thompson sampling, control óptimo y Q-learning (p. 1). Categoría: **fuera de alcance**. Pertenecen a Fundamentos, Predictiva o Prescriptiva. Las pruebas A/B o los bandits como mecanismo de liberación no aparecen en el documento; sólo se nombran las técnicas.

## S03.P400.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de 11 semanas sin codificación sobre sesgos en decisiones, análisis descriptivo, Big Data, experimentación, ML, analítica prescriptiva y cuestiones ético-jurídicas y organizacionales, con casos (UPS, Netflix, TalkTalk). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Desafíos de implementación. Creación de la infraestructura adecuada. Estrategia de Big Data» (p. 8) — fuera de alcance: estrategia/infraestructura organizacional y Big Data, excluidas por las fronteras.
  - cita «Los proyectos impulsados por datos no terminarán nunca, pues están en constante evolución e iteración» (p. 2) — ya cubierta como principio por C05 (observar y mejorar); sin práctica concreta.
  - web scraping, API como fuente, limpieza, estadística descriptiva, experimentación, ML y árboles de decisión (p. 7–8) — fuera de alcance: Fundamentos, Descriptiva, Predictiva y Prescriptiva.

## S03.P400.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un curso en línea de educación continua: historia de la web y la nube, servidor Node.js, contenedores y llaves PKI, DevOps y sus cuatro métricas, casos (Microsoft, Netflix, GE, AWS), serverless, «Agile corporation» y cloud native/Kubernetes. Sin vínculo con capacidades analíticas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Módulos 6 y 8 serverless/FaaS, cloud native, migración a la nube (pp. 14–15); Módulos 5 y 7 transformación organizacional, OODA, «Agile Corporation» (pp. 14–15) — fuera de alcance: cloud engineering y estrategia organizacional, excluidos por las fronteras del curso.
  - Módulo 2 servidor web Node.js asíncrono (p. 13) — fuera de alcance: ingeniería de software general; la exposición de una capacidad por interfaz ya está en P425 H01.

## S03.P400.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto de un curso ejecutivo en línea de 8 semanas sobre liderazgo de datos: historia de datos y nube, plataformas y diseño de bases de datos, «Lean DevOps», marcos organizacionales, gobierno, ciberseguridad y ética; sólo enumera módulos y resultados, sin métodos ni evidencias. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - módulos de IA para líderes, SQL y diseño de bases de datos, «Modern Data Stack», nube, blockchain y diseño de organizaciones (pp. 7, 14–15) — fuera de alcance: liderazgo, arquitectura de datos y cloud, excluidos explícitamente por las fronteras del curso.
  - «Ethics – AI Bias and Fairness» (p. 15) — fuera de alcance: la evaluación de sesgo de un modelo pertenece a Predictiva y el curso no tiene caso con grupos.

## S03.P400.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas de ciencia de datos y ML (Python y estadística, no supervisado, regresión, clasificación, deep learning, sistemas de recomendación, redes y modelos gráficos) con casos de estudio; no trata despliegue, operación ni monitoreo de capacidades analíticas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Building a system: Algorithmic and system challenges» de un sistema de recomendación (p. 10) — fuera de alcance: sin contenido detallado, y el curso no opera recomendadores.
  - resto del temario (estadística, clustering, PCA, regresión causal, deep learning, redes, Kalman; pp. 6–11) — fuera de alcance: contenidos de Descriptiva/Predictiva u otras disciplinas contribuyentes.

## S03.P400.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso de 8 semanas (MIT xPRO/Emeritus) sobre el proceso de diseño de productos de IA: etapas de diseño, fundamentos de ML y deep learning, HCI inteligente, «superminds», GANs, modelo de Lawler para definir un problema de IA y un capstone que es una propuesta de diseño (resumen ejecutivo), no una capacidad operada. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Implement the Lawler Model for defining an AI problem and identify key steps to build an organization case» (p. 6; p. 7, semana 8); «Identify an operational challenge and propose a technical solution» (p. 6); capstone «plan for an AI-based product or service» (p. 8) — fuera de alcance: formular el problema y el caso organizacional corresponde a Fundamentos; el producto terminal es una propuesta, no una capacidad versionada, comprobable y observable.
  - ML, deep learning, algoritmos bayesianos y de regresión (p. 6–7) — fuera de alcance (Predictiva/IA); diseño de interfaces HCI (p. 7) — fuera de alcance (UX), salvo la dimensión de autoridad humana ya tratada en P450; GANs y medios sintéticos, impacto social y económico (p. 4, p. 7) — fuera de alcance; «superminds» y diseño organizacional (p. 7) — fuera de alcance.

## S03.P400.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura de plataformas y APIs, estándares, gating de calidad, regulación, antimonopolio y modelado de dinámicas de plataforma. Es estrategia de producto/plataforma, no operación de capacidades analíticas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - efectos de red, precios, kick-starting, antimonopolio, modelado de dinámicas de plataforma (pp. 9, 15) — fuera de alcance: estrategia y economía de plataformas.

## S03.P400.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso profesional del MIT: EDO y métodos numéricos, modelado espacial (EDP), optimización y modelado basado en datos, de optimización a ML (regresión, regularización, logística), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos (Aurora, Schlumberger, BASF). No contiene contenidos de operación, despliegue, validación operativa, monitoreo ni gobierno. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - módulos 2–3, simulación numérica con EDO/EDP (p. 1: «The Forward Euler Method», «Explicit and Implicit PDE Solutions») — fuera de alcance: modelado y simulación científica; no hacen operable una capacidad analítica.
  - módulos 4–5, optimización y ML (p. 2: «Gradient Descent», «Regularization», «Assessing Model Fit») — fuera de alcance: construcción y ajuste de modelos corresponden a Predictiva/Prescriptiva; Productos no vuelve a predecir ni optimizar.
  - módulo 6, Monte Carlo, pronóstico probabilístico, análisis de sensibilidad, eventos raros (p. 2: «Probabilistic Forecasting», «Simulating Rare Events») — fuera de alcance: pertenecen a Predictiva/Prescriptiva; ningún Pxxx los requiere para operar una capacidad.
  - casos industriales con evaluación (p. 2: «✭ Aurora Flight Sciences», «✭ Schlumberger», «✭ BASF») — marginal: el temario no describe su contenido; la familia institucional sólo ilustra un formato (casos al cierre), que no cambia ningún taller de Productos.

## S03.P400.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un certificado de 6 meses (MIT xPRO/Emeritus) de ingeniería de datos: Python, SQL, contenedores de bases de datos, CDC, APIs y seguridad web con JWT, ETL con NiFi, Hadoop/Spark/Airflow, ML y aprendizaje por refuerzo, streaming con Kafka/MQTT y portafolio en GitHub; el resto es servicios de carrera y financiación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Hadoop, Spark, DASK, Kafka, MQTT/ThingsBoard, streaming en vivo (p. 8, p. 11, p. 12) — fuera de alcance (Big Data); regresión lineal, Naïve Bayes, k-means, aprendizaje por refuerzo, redes profundas (p. 8, p. 11, p. 12) — fuera de alcance (Predictiva/IA); diseño de bases de datos y SQL (p. 8–10) — fuera de alcance (Fundamentos de data); aplicaciones web en Java, Mapbox, Maven, Node.js (p. 8, p. 10–11) — fuera de alcance (ingeniería de software general). El certificado ilustra justamente la lectura que el curso debe evitar: un programa organizado por herramientas de data engineering.

## S03.P400.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto comercial de un certificado en línea de seis meses (MIT xPRO/Emeritus). Cubre fundamentos de ciencia de datos, optimización, ML y aprendizaje profundo, y una parte final titulada «Deployment» que en realidad trata transformación digital y un portafolio de cierre. No describe prácticas de operación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Part 5 Deployment»: «Discover real-world applications of AI/ML», «Explore new applications of digital transformation», «Module 23: Data, Models, and Decisions», «Module 24: Leading Digital Transformations» (p. 9) — fuera de alcance: el rótulo «despliegue» no corresponde a práctica operativa alguna; es liderazgo de transformación digital.
  - «Module 16: Fairness and Bias Issues in Data-Driven Predictions» y el caso de análisis facial: «detect, diagnose, and mitigate biases that can arise in model-based, data-driven decision-making» (p. 8, 10) — fuera de alcance: la detección y mitigación de sesgo es parte del método predictivo. El uso responsable en operación (revisión humana, acceso) ya está en P450 y P452.
  - «Module 22: Interpretability and Causality in Models» (p. 9) — fuera de alcance: pertenece a Predictiva.
  - regresión, clustering, filtrado colaborativo, optimización lineal, CART, ensambles, redes neuronales, NLP (p. 7–9) — fuera de alcance: métodos de otras líneas del programa.

## S03.P400.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh y estudios de compromiso (trade studies), modelos de valor, generación y evaluación de espacios de diseño, exploración del tradespace (frente de Pareto, sensibilidad, robustez, incertidumbre) y asignación de tareas entre modelos y personas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Concept Selection Methods», «Overview of Trade Studies», método de Pugh (p. 1); «Developing Value Models», «Operationalizing Value Models» (p. 2); «Generating Design Spaces», «Tradespace Representations» (p. 3); «clusters and the Pareto Front», «Determining Sensitivity and Robustness» (p. 4) — fuera de alcance: decisión multicriterio y exploración de alternativas de diseño corresponden a Prescriptiva (o a Fundamentos en la formulación); Productos no vuelve a prescribir el problema analítico.
  - pre- y post-evaluación, proyecto semanal y plan de acción (pp. 1–4) — fuera de alcance: rasgos de formato de un programa ejecutivo en línea; la familia institutional ilustra posibilidades, no impone evaluación.

## S03.P400.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto de un programa de ocho semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, DFM). Incluye un proyecto final que decide la fabricación y analiza costos de un prototipo. Queda fuera del dominio de Analytics y de productos de datos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Understand how to map desired product attributes to concept prototype attributes» y «Establish nontechnical and technical goals and requirements for a prototype» (p. 5, 7) — fuera de alcance: requisitos de diseño mecánico. La analogía con el contrato operativo (`productos.C01`) es sólo terminológica.
  - procesos de fabricación serial y paralela, 3D printing, CNC, moldeo de silicona (p. 6) — fuera de alcance: ingeniería mecánica y manufactura.

## S03.P400.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos cortos presenciales de PwC Nigeria (ciencia de datos para principiantes, nivel intermedio y avanzado, analítica predictiva, clases magistrales para ejecutivos y cursos rápidos), centrado en visualización con Power BI, R y Python, estadística, ML y algo de optimización. No tiene contenido de operación ni de ciclo de vida de productos de datos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Generalised Linear Models … addresses issues of data preparation, model development, model validation, and model deployment» (p. 8) — fuera de alcance: el despliegue aparece sólo nombrado dentro de un curso de modelado predictivo, sin práctica operativa que contrastar.
  - «Evaluate constraints on the use of data» y «Assess data structure and data lifecycle» (p. 7) — marginal: son objetivos genéricos sin desarrollo. Las restricciones de uso ya están en P452–P453 y el ciclo de vida en P455.
  - «Build data solutions that integrate with other systems» (p. 6) — marginal: es un objetivo declarado sin contenido. La integración ya está en P417 y P425.
  - proyecto guiado con «organizational issues in implementing systems for predictive analytics … generating analytics project implementation plans» (p. 9) y «Analytics Requires Process and Incentive Changes» (p. 11) — fuera de alcance: gestión organizacional de proyectos analíticos, no operación de una capacidad.
  - visualización y dashboards, regresión, ML, series de tiempo, texto, optimización, experimentación A/B (p. 4–14) — fuera de alcance: pertenecen a Descriptiva, Predictiva y Prescriptiva.

## S03.P400.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo (10+ años de experiencia) sobre estrategia, modelos de negocio, liderazgo, futuros y gobierno de IA; temario por fases sin contenidos operativos ni técnicos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «AI risk and safety • AI governance • AI and trust» y «AI Governance, Enterprise Controls» (p. 5; p. 17) — fuera de alcance: gobierno corporativo de IA y controles empresariales para ejecutivos; el gobierno operativo de una capacidad ya está en P450–P455.
  - «Creating a culture of data excellence» (p. 16) y diseño de modelos operativos y capacidades organizacionales (p. 7) — fuera de alcance: transformación organizacional, no operación de una capacidad.
  - capstone «Built around the pillars of technology, strategy, and organizational readiness … from vision toward execution» (p. 17) — fuera de alcance: proyecto de transformación empresarial; no ilustra una forma de evidencia aplicable a talleres del curso.
  - futuros, prospectiva y planificación de escenarios (p. 17) — fuera de alcance: decisión estratégica bajo incertidumbre, ajena a la línea de productos.

## S03.P400.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto en español de un certificado de 10 meses con cinco cursos de 8 semanas (Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, Storytelling y visualización); sólo una línea toca la operación de modelos (despliegue como API o puntuación por lotes). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Definir casos de negocio (coste-beneficio) [...] para dar recomendaciones justificadas sobre una acción» (p. 8) — fuera de alcance (Fundamentos/Prescriptiva); SQL, NoSQL y carga en bases de datos (p. 5–6) — fuera de alcance (Fundamentos de data); Tableau y paneles (p. 6) — fuera de alcance (Descriptiva/BI); entrenamiento y evaluación de modelos, interpretación (p. 6–7) — fuera de alcance (Predictiva); multiprocesamiento y multihilo (p. 6) — fuera de alcance (ingeniería de software).

## S03.P400.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de la Dirección Nacional de Programas Curriculares de Pregrado (2021) sobre cuatro talleres de co-creación con programas de pregrado de varias sedes (contextos, dinámicas, prácticas pedagógicas, proyecciones). No contiene programas de analítica, cursos de datos/ingeniería de datos/MLOps ni resultados de aprendizaje disciplinares: «analítica» no aparece ni una vez; «datos» aparece sólo para la metodología de teoría fundamentada del propio estudio (p. 20) y «software» para Atlas.ti (p. 21). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - paso «de la enseñanza al aprendizaje»: «el estudiante no aprende simplemente escuchando, sino dialogando y haciendo» (p. 79) — ya cubierta: el formato `Pxxx_` de taller presencial guiado con desarrollo progresivo en código (AGENTS.md) ya lo encarna; no cambia ningún HNN.
  - evaluación orientada al «seguimiento del “saber hacer”», con autoevaluación y coevaluación (pp. 80–82) — fuera de alcance: es una política pedagógica institucional general (pregrado UNAL) que no habla de productos de datos; el contrato de evaluación de talleres (`pytest` sobre `submission/`) es una decisión de programa, no de un Pxxx, y la familia institucional no impone un cambio de instrumento.
  - «prácticas en el sector productivo», proyectos de extensión y salidas de campo como estrategia (pp. 56–57, 80) — marginal/fuera de alcance: no aporta caso, datos ni práctica operativa concreta; la necesidad de un caso con usuario y decisión en P400–P455 ya está registrada en las auditorías S02 y este documento no ofrece uno.
  - «uso de metadatos para la investigación a través de ejercicios de modelación» y recursos como laboratorios virtuales, simuladores o repositorios de software (pp. 72, 79) — marginal: menciones genéricas de recursos didácticos sin relación con catálogo/linaje (P443, P454) más allá de la palabra.
  - crítica a la «ausencia de objetivos medibles, y metas» en la armonización (p. 110) — fuera de alcance: se refiere al proceso institucional de reforma curricular, no a criterios de éxito de una capacidad analítica (C01).

## S03.P400.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular institucional que establece una «Ruta de Armonización Curricular» de cuatro etapas (marco normativo, pertinencia y resultados de aprendizaje, organización curricular, implementación y evaluación continua de los resultados de aprendizaje) en las dimensiones macro, meso y microcurricular, en el marco del Acuerdo 02 de 2020 del CESU. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - resultados de aprendizaje como «declaraciones expresas de lo que se espera que un estudiante conozca y demuestre» y eje de mejora curricular (p. 2) — fuera de alcance de S03: es un requisito de diseño de programa y curso (RAA/RAP), ya registrado como pendiente en `s05-diseno-productos.md` («Pendiente: detallar programa-calendario, RAA…»); no cambia lo que el estudiante hace en ningún taller.
  - etapa 4, «diseñar los mecanismos de monitoreo y evaluación» de los resultados de aprendizaje y «evaluación continua de la gestión curricular» (p. 3) — fuera de alcance: se refiere a la evaluación institucional del currículo, no al monitoreo de capacidades analíticas en operación (P422, P423 y P442 no guardan relación).
  - dimensión microcurricular: «didácticas y procesos de evaluación de los aprendizajes» (p. 2) — marginal: es un marco general; la evaluación con `pytest` y la prueba de participación (`tests/test_activity.py`) ya están definidas en `AGENTS.md`, y la debilidad de la evaluación por existencia de archivos ya está registrada en S02 para cada Pxxx.
  - atender «las exigencias y necesidades del medio, la actualidad de las áreas de conocimiento, las características de los estudiantes» (p. 3) — marginal: principio de pertinencia sin contenido operable para un taller de productos de datos.

## S03.P400.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de un curso de posgrado en línea de minería de datos aplicada a datos de salud: preprocesamiento, probabilidad, regresión, patrones frecuentes, clasificación, clustering y minería de texto, evaluado con un proyecto por entregables (propuesta, recolección, preparación, informe final), póster y un survey paper. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «methods for deploying these techniques using the open source tools» (p. 2) — marginal: una frase del catálogo sin contenido de despliegue en el calendario (p. 9–10), que no incluye ninguna semana sobre operación. Preprocesamiento, regresión, clasificación, clustering, texto y analítica en salud (p. 1–2, p. 9) — fuera de alcance (Descriptiva/Predictiva). Survey paper, póster y foros (p. 6–8) — fuera de alcance (formato de evaluación de otro tipo de curso).

## S03.P400.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus introductorio de pregrado: Excel, Access, modelado entidad-relación, normalización, SQL (consultas, joins, subconsultas), NoSQL/MongoDB y su pipeline de agregación, BI y data warehouses, visualización y dashboards; proyecto final en equipo. Sin contenido de operación, despliegue ni gobierno de capacidades. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - NoSQL, MongoDB «Creating aggregation pipeline» (p. 6), data warehouses y data marts (p. 6), dashboards (p. 7) — fuera de alcance: bases de datos, BI y Descriptiva.

## S03.P400.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Pruebas y Evaluación de Sistemas Agentivos: Pruebas unitarias, Pruebas de integración, Pruebas del sistema» (p. 13) — ya cubierta: pruebas de regla, de transformación y del flujo publicado; el objeto (agentes LLM) es fuera de alcance.
- **Señales de alcance de curso** (registradas sólo en este log):
  - IA generativa, prompts, RAG, agentes, MCP, multiagente, LangChain/LangGraph/n8n (p. 3, 9–16, 18) — fuera de alcance: capacitación en una tecnología/plataforma, no operación de una capacidad analítica.

## S03.P400.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de bodegas de datos tradicionales: modelado ER y dimensional de Kimball (incluye SCD tipos 1–3, hechos sin hechos, snapshots), y BI con SAP Business Objects (universos, loops, traps, seguridad por fila) y Tableau; declara explícitamente «ETL is not covered in this course» (p. 1). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Slowly Changing Dimensions - Type 1, Type 2, and Type 3 … Classroom Hands-on – Design a Type 2 SCD» (p. 2), modelado dimensional, bus architecture, dimensiones conformadas y de tiempo, manejo de nulos (p. 2) — fuera de alcance: modelado de datos (Fundamentos de data / Descriptiva); no se plantea como preocupación operativa.
  - SAP Business Objects (universos, loops, chasm/fan traps, IDT, Web Intelligence) y Tableau (pp. 3–4) — fuera de alcance: capacitación en plataformas de BI, excluida por las fronteras del curso.
  - «Publishing and sharing reports», «Sharing your dashboards» (p. 4) — marginal: publicación como función de herramienta; el control de acceso y la entrega de un producto ya están en P452 y P425–P426.

## S03.P400.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un módulo introductorio de posgrado, de 10 semanas, del departamento de Computer Science. Recorre herramientas básicas, estadística, calidad de datos y SQL/NoSQL, regresión, matrices, clustering, clasificación, estructuras para big data, privacidad y anonimización, y grafos. Se evalúa con un proyecto, ejercicios y un examen. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Data Structures: Bloom Filters, Sketches, Summaries… to scale analytics to big data» y «NoSQL systems» (pp. 2–3). Categoría: fuera de alcance, por la frontera Big Data y arquitectura de datos. Regresión, clustering, clasificación, SVD/PCA y grafos (p. 2) corresponden a Predictiva, Descriptiva y Fundamentos. Herramientas de línea de comandos, gnuplot y Perl/Python/R (p. 2) son formación en herramientas.

## S03.P400.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de una página de métodos y herramientas de un programa de business analytics: recolección de datos (encuestas, NPS, pasiva, medios), A/B testing, correlación y causalidad, pronóstico (suavizamiento exponencial, tendencia y estacionalidad, nuevo producto), regresión, simulación con Analysis ToolPak y Solver, visualización, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - métodos analíticos (p. 1: «A/B Testing», «Correlation and Causation», «Forecasting», «Exponential Smoothing», «Regression Analysis», «Optimization Models», «Decision Trees») — fuera de alcance: son métodos para formular, describir, predecir o prescribir (Descriptiva, Predictiva, Prescriptiva); productos no vuelve a enseñarlos.
  - herramientas de hoja de cálculo (p. 1: «Simulation Toolkit», «Analysis ToolPak», «Solver Optimization Tool») — fuera de alcance: capacitación en una plataforma y métodos de otro curso.
  - recolección de datos (p. 1: «Descriptive Data Collection: Surveys, Net Promoter Score (NPS), and Self-Reports»; «Passive Data Collection») — fuera de alcance: adquisición de datos (Fundamentos/Descriptiva). La captura de una señal de utilidad del consumidor ya está en P451 H01–H02 y la lista no aporta mecanismo operativo.
  - «Data Visualization and Interpretation» (p. 1) — fuera de alcance: Descriptiva; no hay señal de interfaz operativa ni de mantenimiento.
  - No hay en el documento ninguna señal de despliegue, pruebas, calidad, monitoreo, gobierno, versionado ni operación.

## S03.P400.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Lista de módulos de un programa ejecutivo de Business Analytics: orientación, descriptiva (módulos 1–2), predictiva (3–6), prescriptiva (4, 7–8) y aplicación de la analítica en el negocio (9), cada uno con una línea de propósito. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Módulo 9 «Explain important components of different use cases of analytics in business and create a plan to put data to work in your organization» (p. 1) — fuera de alcance/marginal: es un plan organizacional de adopción de analítica (estrategia de negocio), no la operación de una capacidad; lo más cercano en el curso es el contrato operativo de C01 (tarjeta de producto en P408–P411, catálogo P454), que ya define consumidor, responsable y uso con más precisión que esta línea.
  - módulos descriptivos, predictivos y prescriptivos (1–8) (p. 1) — fuera de alcance: pertenecen a Descriptiva, Predictiva y Prescriptiva; la frontera de Productos prohíbe volver a formular, predecir o prescribir el problema analítico.
  - el programa no contiene ningún módulo de despliegue, operación, monitoreo, gobierno ni DataOps/MLOps (p. 1) — señal de contexto, no propuesta: confirma que la línea de productos de datos es una contribución diferencial del programa propio frente a este referente ejecutivo, pero no justifica cambios en ningún Pxxx.

## S03.P400.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación histórica (1970–2026) de cómo las organizaciones pasaron de registrar datos a decidir y actuar con ellos: RDBMS, SQL, DW/ETL, BI, minería de datos, CRISP-DM, ciencia de datos, Big Data, Business Analytics, producto de datos, DataOps, MLOps, modelos fundacionales y agentes. Es contexto y encuadre, no prescripción vigente. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - definición de producto de datos: «aplicación o servicio que integra datos y algoritmos para generar continuamente predicciones, recomendaciones, decisiones o información útil y que, además, produce nuevos datos que pueden ser consumidos por otros productos» (p. 44); DataOps: «Los productos analíticos pasan de ser proyectos con un final definido a convertirse en activos que evolucionan junto con el negocio» (p. 53) — ya cubierta como encuadre: coincide con el propósito y el producto terminal de `s05-diseno-productos.md` (capacidad versionada, comprobable, desplegable y observable). Útil para la presentación del curso; no cambia un taller.
  - modelos de servicio IaaS/PaaS/SaaS/FaaS, serverless, low-code, «Vibe Coding» (p. 27); Hadoop, Spark, Hive, data lake, NoSQL (pp. 28–31, 38–40, 50–51) — fuera de alcance: cloud engineering y Big Data, excluidos por las fronteras del curso.
  - CRISP-DM con fase «Distribución» (p. 21), tipos de analítica (p. 37), casos Netflix/Moneyball/Amazon (pp. 3–4, 33, 35) — fuera de alcance: contexto histórico y de formulación (Fundamentos).

## S03.P400.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el contraste entre programación tradicional y ML/DA: «El testeo prueba la lógica contra ejemplos» frente a «El testeo se basa en precisión no en ejemplos»; «Se usan datos de producción» (p. 4) — ya cubierta: la secuencia pasa de pruebas de código con casos construidos (P400 H02, P401 H02) a datos (P402 H01) y a compuertas de desempeño de un modelo (P403 H02). La dicotomía de la diapositiva es además una simplificación, porque P403 H03 combina con razón pruebas por ejemplos (interfaz, comportamiento conocido) con pruebas por métricas. Importarla tal cual sería una regresión.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Formación de DS focalizada en los algoritmos y no en la creación de un producto de datos operativo» y «Malas prácticas de desarrollo de software y desconocimiento de los requerimientos para ir a productivo» (p. 9); «No se tienen las habilidades para llevar un modelo a producción» (p. 3) — ya cubierta: es la razón de ser del curso (`productos.C01`–`C05`). Es contexto que confirma la identidad, no una práctica nueva.
  - «Datos, conocimientos, decisiones y acciones no son sinónimos» y «No se deben buscar insights interesantes… sin un objetivo claro» (p. 8) — ya registrada: coincide con el límite que S02 anota en casi todo el bloque P400–P441 (capacidad sin usuario ni decisión). Respalda en lo conceptual `productos.C01`, pero no aporta un mecanismo ni un caso.
  - «Se sigue CRISP-DM y modelos de cascada» (p. 2); «Se requiere HPC y hardware especializado» (p. 4); cultura, data literacy y apoyo de la gerencia (pp. 6–8) — fuera de alcance: son temas de metodología de proyectos, infraestructura u organización, no de operar una capacidad.
  - «No hay un producto mínimo viable» (p. 3) — marginal: idea de gestión de producto que la diapositiva no desarrolla. El contrato operativo con criterios de éxito ya es `productos.C01`.

## S03.P400.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de estrategia de datos organizacional (diagnóstico, mecanismos de valor, brechas, objetivos, iniciativas, gobierno, arquitectura, uso responsable, caso de valor, portafolio, hoja de ruta, ejecución y evaluación) ilustrado con mantenimiento predictivo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - estrategia, diagnóstico, brechas, objetivos estratégicos, portafolio y hoja de ruta (p. 4–15, 19–21, 24) — fuera de alcance: gestión estratégica de datos a nivel organizacional; el curso excluye arquitectura empresarial y no formula el problema. La brecha «Procesos: ausencia de una operación reproducible del producto de datos» (p. 11) confirma la pertinencia del curso, pero no cambia ningún taller.
  - arquitectura de datos (warehouse, lake, lakehouse, data mesh) (p. 17) — fuera de alcance: arquitectura empresarial de datos, excluida por las fronteras.
  - caso de valor (VPN, ROI, costo total) (p. 19) — fuera de alcance: evaluación económica de iniciativas (Fundamentos/gestión), sin caso en el curso.

## S03.P400.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - recorre KDD → CRISP-DM → metodologías de ciclo de vida (TDSP, CRISP-ML(Q), MAISTRO) con un caso de abandono de clientes que avanza de pregunta descriptiva a predicción, decisión, despliegue, monitoreo/degradación y gobierno transversal. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «El modelo no es la solución. Datos + Modelos + Reglas de decisión + Interfaces → Solución analítica» (p. 19) y «La analítica genera valor cuando cambia una decisión o una acción» (p. 24) — ya cubierta como principio en `s05-diseno-productos.md` (C01, producto terminal); confirma el riesgo de identidad registrado en S02 (indicadores sin usuario ni decisión), pero no aporta un cambio localizable.
  - framing, problema analítico, entendimiento y preparación de datos, selección de métodos (p. 9–17) — fuera de alcance: responsabilidad de Fundamentos/Descriptiva/Predictiva/Prescriptiva según las fronteras del curso.
  - «Evaluar sesgos y equidad» e impactos sociales y ambientales (p. 28–29) — fuera de alcance: la evaluación de sesgo de un modelo pertenece a Predictiva y no hay caso con grupos en el curso.

## S03.P400.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Test-driven Development: pruebas unitarias y de aceptación» (p. 3) y «Errores de código y datos» como desperdicio (p. 6) — ya cubierta: pruebas de la regla y de la transformación (P400 H02, P401 H02) y contrato de datos con aceptación/rechazo (P402 H01, H04).
- **Señales de alcance de curso** (registradas sólo en este log):
  - «No contribuye a tomar decisiones o mejorar la experiencia del usuario», «No ayudan al usuario a tomar decisiones» y «Problema equivocado» como desperdicios (p. 6) — ya registrado: confirma el riesgo de identidad de S02 (indicadores sin usuario ni decisión en P400–P419, P428–P438), pero no aporta un cambio localizable en un taller.
  - value pipeline «Ingestión Transformación Modelado Visualización Reporte» con entregas «Archivos, Herramientas BI, Dashboards, Web Apps, APIs» e innovation pipeline (p. 5) — ya cubierta como encuadre del curso (integración y entrega: C02; API en P425–P426).
  - value stream mapping, proporción espera/valor agregado, tiempo de ciclo de producción y desarrollo (pp. 7–8) y teoría de restricciones en cinco pasos (p. 9) — fuera de alcance: mejora de procesos organizacionales sin caso ni datos en el curso.
  - capas del ciclo de vida del dato: «Control de versiones, despliegue, monitoreo, herramientas de planificación y orquestación» (p. 12) — ya cubierta (P408–P416, P418, P422–P423, P428–P429); cómputo distribuido, flujos, NoSQL y almacenamiento en la nube son fuera de alcance (Big Data, cloud engineering).

## S03.P400.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - XP «Continuous Integration», «10 Minutes Build», «Test-driven development» (p. 5) — ya cubierta: P415 H01, P416 H01, P400–P401.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Scrum, Kanban, XP, SAFe, Scrum of Scrums y Disciplined Agile Delivery (pp. 3–9), principios «Reduce heroism», «Self-organize», «It’s a team sport» (p. 10) — fuera de alcance: gestión ágil de proyectos y equipos, no operación de una capacidad analítica.

## S03.P400.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Hay al menos un test en cada paso» del pipeline ingestión→reporte (p. 9) — ya cubierta: el bloque de pruebas cubre regla, transformación, datos, modelo, entradas y flujo publicado (P400–P404, P417, P433). El documento no ayuda con el riesgo de identidad del bloque (indicador trivial), sólo lista prácticas.
- **Señales de alcance de curso** (registradas sólo en este log):
  - ciclo de vida con «Decommission» / «Retirement» (p. 23) — marginal: retirar una capacidad no tiene caso ni datos; se menciona como respuesta de ciclo de vida dentro de la propuesta de P424.
  - kanban de ideación, WIP y priorización de épicas (p. 24) — fuera de alcance: gestión de portafolio/proyectos.

## S03.P400.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - beneficios de DataOps: «Robustez: por el uso de tests», «Transparencia: Alertas automáticas, dashboards» (p. 2). El proceso combina «Tests de datos», «Tests de código», «Tests de integración» y pre-release antes de liberar (p. 5). Categoría: **ya cubierta**. El curso tiene pruebas de código (P400–P401), de datos (P402), de modelo (P403), de integración (P417) y verificación previa a fusionar (P415–P416).
- **Señales de alcance de curso** (registradas sólo en este log):
  - silos y coordinación relacional entre equipos (pp. 2–3), Kanban, trabajo en progreso, tiempo de ciclo y teoría de restricciones (p. 6), trampas del CDO (valor diferido, defensa de los datos; p. 9) y etapas de madurez «Data Desert → Boutique → Waterfall → DataOps Analytics» (p. 11). Categoría: **fuera de alcance**. Son gestión organizacional de equipos y portafolio, no prácticas que hagan operable una capacidad analítica concreta. Servirían a lo sumo como encuadre del curso, no como contenido de un taller.

## S03.P400.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programación tradicional con «Tests basados en ejemplos» frente a ML, donde la lógica se aprende de datos y se prueba por comportamiento (p. 2); «Tests automáticos de data, código y modelos» (p. 3) — ya cubierta: P400–P401 (regla y transformación), P402 (contrato de datos, H01–H04) y P403 (familias de pruebas de modelo, H03).
- **Señales de alcance de curso** (registradas sólo en este log):
  - «El modelo es una pequeña fracción de lo requerido para el despliegue y monitoreo» (p. 3) — ya cubierta como encuadre del curso entero (s05: el producto terminal es la capacidad operable, no el modelo). Design thinking, Agile y Agile data warehousing (p. 7–8, p. 12), data lake/data marts y esquemas optimizados para lectura (p. 5, p. 9–10) — fuera de alcance (gestión de proyectos y arquitectura empresarial de datos).

## S03.P400.44

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - tipos de pruebas unitarias, de integración, funcionales y de regresión (p. 2: «Pruebas de regresión: se ejecutan cada vez que hay un cambio») — ya cubierta: P400–P401 (unitarias), P417 H01 (flujo/artefacto publicado), P412 H03 y P414–P416 (regresión sobre resultado conocido).
  - «Los tests deben incluirse en cada etapa del pipeline» con entradas / lógica del negocio / salidas (p. 4) — ya cubierta a lo largo de la secuencia: entradas (P402 H01, P404), lógica (P400–P401), salidas (P417 H01, P440 H02).
- **Señales de alcance de curso** (registradas sólo en este log):
  - pruebas de desempeño y de humo (p. 2: «capacidad de respuesta, estabilidad y disponibilidad bajo una carga») — fuera de alcance: ingeniería de software/rendimiento; sin capacidad analítica ni datos que lo justifiquen; la disponibilidad como nivel de servicio ya está en P445.
  - «Analytics es código»: innovation pipeline (datos fijos, código variable → pruebas de regresión) vs. value pipeline (código fijo, datos variables → tests de datos y monitoreo) (p. 3) — marginal: encuadre útil que ya está implícito en la secuencia (P412–P416 regresión con datos fijos; P402, P404, P422, P439–P442 datos variables); no cambia lo que el estudiante hace. Puede usarse para aclarar el encuadre de curso si se reorganiza la secuencia.
  - análisis de impacto por equipos y «Proceso Waterfall para reducir miedo e incertidumbre» frente a automatización de pruebas (p. 2) — ya cubierta: P415–P416 (verificación automática antes de fusionar).

## S03.P400.45

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Altos costos debido al trabajo mundano y repetitivo» y «Si algo falla todo falla» (p. 2) — marginal: motivación general para automatizar y probar, ya ejercida en el bloque de pruebas y automatización.
- **Señales de alcance de curso** (registradas sólo en este log):
  - rol «DataOps Engineer»: «Orquestación del pipelines, Automatización de la calidad, Aprovisionamiento de ambientes, Despliegue a producción» con «Frameworks para tests de datos» (p. 5) — ya cubierta como conjunto de prácticas del curso (P429, P402/P433, P412/P414, P415/P426); el documento describe un rol, no una práctica nueva.
  - estructuras de equipo (centralizada, descentralizada, por dominio, centro de excelencia, data platform team), coordinación por capítulos y perfiles T/Pi/M/E-shaped (pp. 2–4, 7–8) — fuera de alcance: diseño organizacional, no operación de una capacidad analítica.

## S03.P400.46

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Revisión sistemática (expansión por citas en Scopus, 18 metodologías) que deriva PRODIG8: seis dimensiones de ejecución (alcance, comprensión y preparación de datos, diseño, evaluación, operación y mantenimiento), Gobierno y Ética como control transversal y Mejora Continua como retroalimentación adaptativa. Es un marco de gestión de proyectos analíticos; sólo §4.6–4.8 tocan directamente la operación de capacidades. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «approximately 87% of data science projects never reach production» y «over 80% of organizations lack a formal methodology» (p. 3) — marginal: motivación general de la línea de Productos; puede citarse en el encuadre del curso, no cambia ningún taller.
  - Project Scope Definition: traducir objetivos en «precise data-science formulations of inputs, outputs, constraints, and quantitative evaluation criteria» (p. 14), project charters, Sprint 0, user stories (p. 14) — fuera de alcance: formulación del problema analítico y gestión de proyecto (Fundamentos); la parte operativa (contrato de entradas, salidas, errores, consumidor, responsable) ya está en P408 H01, P411 H02, P425 H01, P434 y P454 H01.
  - Data Understanding y Data Preparation (pp. 14–17: exploración, 6Vs, limpieza, feature engineering, reducción de dimensionalidad) — fuera de alcance: pertenecen a Descriptiva/Fundamentos; las dimensiones de calidad aplicadas al uso operativo (completitud, frescura, consistencia) ya están en P402 H01, P439 H01 y P442 H01–H02.
  - «user acceptance testing and system verification» antes del despliegue (p. 19) — marginal: sin caso ni usuarios reales en el curso; la verificación de la entrega ya está en P417 H01 y P415 H01.
  - fairness y auditoría de sesgo, «criteria that avoid arbitrary thresholds in variable selection» (p. 20) — fuera de alcance: evaluación del método predictivo/ética del modelo, no operación; sin caso con atributos protegidos tratados (el `ssn` de P401 es privacidad, no equidad).
  - «help-desk administration and user support communities» (p. 21), complejidades políticas y culturales de adopción (p. 21), escalabilidad e infraestructura de alto desempeño (p. 21) — fuera de alcance: soporte organizacional, gestión del cambio y Big Data/cloud.
  - Scrum/XP, sprints, backlog, roles (pp. 5, 11–14, 22) y fases técnicas DMME de sensores (pp. 5, 9) — fuera de alcance: gestión de proyectos y adquisición de datos de ingeniería.
  - encuadre ejecución–control–adaptación (Gobierno y Ética transversal; Mejora Continua como retroalimentación; pp. 12–13, 22–23) — marginal: encuadre útil para presentar el curso (C05 transversal a C02–C04), pero no cambia lo que el estudiante hace en ningún taller.

## S03.P400.47

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Tutorial de una herramienta comercial de minería de datos: casos de modelado (clasificación, series de tiempo, supervivencia, GLM, SVM, reglas, KNN, TCM) construidos como «streams» de nodos; la operación aparece sólo como menciones a puntuación de datos nuevos, exportación PMML, repositorio de despliegue, modo batch, reaplicación de un modelo de series de tiempo y reentrenamiento mensual. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - datos «analíticos o históricos» frente a datos de scoring «operational data» (p. 42) — ya cubierta: distinción entrenamiento/producción en P404, P422 y P423.
  - Administration Console para monitorear y configurar servidores (p. 8) y «License tracking» con logs de uso (p. 11) — fuera de alcance: administración de plataforma y licencias, no observación de una capacidad analítica.
  - Self-Learning Response Model que se actualiza con nuevas respuestas (p. 195), causal temporal y causa raíz de atípicos (p. 346), monitoreo de condición de máquinas con redes neuronales (p. 227) — fuera de alcance: son métodos de modelado (Predictiva/Descriptiva), no prácticas de operación; «Condition Monitoring» es predicción de fallas, no monitoreo del producto.

## S03.P400.48

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de ayuda de SPSS Modeler para CRISP-DM con listas de tareas por fase y un caso de minería web de un e-retailer; el capítulo 7 trata el despliegue como plan por modelo/hallazgo, el monitoreo como criterio de «expiración» del modelo y el cierre como informe final y revisión de lecciones aprendidas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - informe final por audiencia, presentación final y revisión de proyecto con lecciones aprendidas (pp. 35–36, 41–42) — fuera de alcance: gestión y comunicación de proyectos (Fundamentos); no hace más operable una capacidad. La difusión de «findings» a decisores (p. 39) pertenece a Descriptiva.
  - objetivos de negocio, criterios de éxito objetivos/subjetivos con árbitro, riesgos y contingencias, plan de proyecto (pp. 10–15) — fuera de alcance como formulación (Fundamentos); el componente operativo (criterios de éxito en el contrato) ya está en `productos.C01` del diseño.

## S03.P400.49

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de inicio de KNIME (versión 2.x): instalación, banco de trabajo, construcción de flujos por nodos y puertos, estados de los nodos, ejecución, consola y log, preferencias, clave maestra, importación y exportación de flujos y metanodos. Es una señal de herramienta, sin contenido de operación de productos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - interfaz, repositorio de nodos, metanodos, hiliting y vistas (p. 5–25) — fuera de alcance: capacitación en una plataforma.

## S03.P400.50

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial previo al lanzamiento de SQL Server 2005 Analysis Services: casos de uso de minería de datos, integración con Integration, Analysis y Reporting Services, API DMX y arquitectura (despliegue, escalabilidad, administración y seguridad por roles). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - escalabilidad a «thousands of concurrent users and … millions of queries per day» y administración centralizada (p. 2) — fuera de alcance: infraestructura y cloud engineering, excluidos por `s05-diseno-productos.md`.
  - Reporting Services para «select just the right people to receive the reports based on data mining queries» (p. 1) — marginal: la distribución dirigida de reportes no añade una capacidad respecto del control de acceso (P452) y del catálogo de consumidores (P454). Por familia (professional-learning), el folleto sólo aporta señales de herramienta de 2005 y no basta para imponer un tema.

## S03.P400.51

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - manual de producto de un motor de minería integrado en la base de datos (Oracle 11g). Cubre funciones y algoritmos de minería, scoring con SQL, privilegios sobre modelos y modelos que llevan embebidas sus propias transformaciones («supermodels»). Su valor para Productos es sólo de práctica operativa. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - preparación automática (ADP), binning, normalización, winsorizing y transparencia de los detalles del modelo (pp. 129–134), y los algoritmos de las partes II y III. Categoría: fuera de alcance. Son método predictivo o descriptivo, no operación de la capacidad.

## S03.P400.52

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/perceptual-edge-dashboard-design-requirements-questionnaire.md` (`source_sha256`: b2fda9a2366e49604d91b330424c4fdf5d9ee294068f4c8b998f1a188fb30a6c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuestionario de ocho preguntas para levantar requisitos antes de diseñar un dashboard. Pregunta por la frecuencia de actualización, los usuarios, las preguntas y acciones, los datos y su nivel de detalle, los ítems clave, las agrupaciones, las comparaciones (metas o histórico) y qué constituye una excepción (umbrales u outliers). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - agrupaciones lógicas, ítems clave y comparaciones con metas o histórico para el diseño visual (p. 1). Categoría: fuera de alcance. Es diseño de dashboards y comunicación descriptiva (Descriptiva o BI), no operación de la capacidad.

## S03.P400.53

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` (`source_sha256`: 5d936194154a3c8774fd7df35e28c7a427fb9d4348130b86ae9c6ec58946548f).
- **Resultado:** aporta a N01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
- **Señales de alcance de curso** (registradas sólo en este log):
  - adopción y cultura de datos, patrocinio, comunidad de práctica y capacitación (p. 22) — fuera de alcance: estrategia organizacional, no operación de una capacidad.
  - modelado dimensional, DAX, grupos de cálculo, plegado de consultas, DirectQuery y modelos compuestos, ajuste de rendimiento con DAX Studio (p. 32–62, 69–74, 95–97, 100–101) — fuera de alcance: BI y modelado de datos (Descriptiva, Fundamentos) y capacitación en una plataforma, que es frontera explícita del curso.

## S03.P400.54

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-data-mining.md` (`source_sha256`: 6396a7c9e3efce998f0bbb9907cacb228244737c80bdebcdae17ce913b7f6ce9).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - White paper comercial de SAS (2015) centrado en el descubrimiento (preparación, exploración, modelado) dentro de un «ciclo de vida analítico» iterativo; dedica secciones breves a implementación, modelo campeón, monitoreo y gestión de modelos con sus productos (Enterprise Miner, Factory Miner, Decision Manager). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - pregunta de negocio → hipótesis analítica, tabla base analítica, muestreo, partición entrenamiento/prueba, exploración, clustering, reglas de asociación, analítica de texto, transparencia frente a precisión (p. 4–8) — fuera de alcance: formulación, Descriptiva y Predictiva; el curso no vuelve a enseñar el método analítico de origen. Cómputo distribuido en memoria y Hadoop (p. 10–11) — fuera de alcance (Big Data).

## S03.P400.55

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-forecasting.md` (`source_sha256`: 7cabe87e23ff9469d7b4b9e17582dd694b8ac329ed0975bf9a26e3dcb26b5569).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Es una colección comercial de artículos de SAS sobre pronóstico. Trata sobre todo de modelado (TSMODEL, ML, RSM), pero incluye tres textos de proceso que importan para operar un pronóstico: el monitoreo automático de modelos con cartas de control sobre los residuos, el análisis de si los ajustes manuales mejoran el pronóstico y el «Forecast Value Added». Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «more accurate forecasting is not an end in itself… a means to effect better decisions» (p. 7) — ya cubierta: es la pregunta de identidad del curso (`productos.C01`) y no aporta un mecanismo.
  - procesamiento distribuido de millones de series (DFS, ejecución paralela por grupo BY, 1,5 millones de series en 153,5 s; pp. 14–19, 29–31) e integración de Python y R dentro de TSMODEL (pp. 20–28) — fuera de alcance: es arquitectura de Big Data y capacitación en una plataforma, dos cosas que excluye la frontera del curso.
  - análisis de escenarios con factores causales controlables (pp. 100–101), SASEFRED, RSM, redes neuronales, nodo GBM y extracción de características (pp. 35–86, 105–126) — fuera de alcance: son modelado predictivo o prescriptivo, o funciones de un producto comercial.
