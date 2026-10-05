# Log — P102

## S02.P102.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P102_csv2json/` (`data/drivers.csv`, `professor/main.py`, `src/main.py`, `submission/drivers.json`, `tests/`). Comparado con P100–P101.
- **Trazabilidad revisada:** entrada P102 → `descriptiva.C02`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (validación de estructura), H02 (minimización de `ssn` y `location`; highlight de caso y datos), H03 (tabla a registros JSON), H04 (composición en funciones).
- **Ambigüedades:** el docstring califica la exportación como «segura», pero conserva `name`; procedencia de `drivers.csv` no documentada; las ramas de error no se prueban.
- **Superficies / contrato / dependencias:** S01–S06; habilita el uso del mismo dataset en P103–P105, sin artefacto compartido.
- **Auditoría de Analytics:** producto = capacidad de datos (exportación minimizada). C05 parcialmente sustentado (minimización); C02 débil (sólo validación estructural). Dominan ingeniería de datos y protección de datos.

## S03.P102.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - minimización de datos sensibles, regulaciones (GDPR, etc.; DG-Data Privacy and Security, p. 74; PR-Privacy, pp. 106–107) — ya cubierta en lo técnico (H02). El marco legal comparado es fuera de alcance: no hay caso que lo exija.
  - métodos de validación «input validation, data type validation, range and constraint validation, and cross-reference validation» (DPSIA/DI, p. 92) — ya cubierta: P102 H01, P124 H02 y P120 H02 (identidad `Quantity × Price = TotalAmount`).

## S03.P102.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad y seguridad como protocolos del dominio de datos (p. 5) — ya cubierta: P102 H02, P108, P109.

## S03.P102.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - datos sensibles, uso restringido y riesgo de adquirir datos innecesarios (CAP-E.3.1.2, 3.3.1, 3.4.2, pp. 13–15) — ya cubierta: P102 H02 (minimización), P108 H01–H03.

## S03.P102.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad, seguridad y datos con implicaciones éticas (p. 13: «maintaining its privacy and security»; p. 15: CAP-P.3.4.2) — ya cubierta: P102 H02, P108 H01–H06, P109 H02–H03, P125 H07.

## S03.P102.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data subject privacy» (p. 45), «Privacy and confidentiality» (p. 50) — ya cubierta (P102 H02; P108 H01–H06; P109 H02–H03).

## S03.P102.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diagnóstico nacional de la brecha cuantitativa y cualitativa de talento TI en Colombia (demanda por roles, habilidades hard/soft, pertinencia curricular, salarios y rotación). Su valor para el curso es de pertinencia laboral del perfil analista de datos/BI; no define estándar ni prescribe herramientas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de pregrado de 4 unidades, con prerrequisitos de programación y de un curso de ciencia de datos (DATA C100 o equivalente), sobre gestión de datos a escala para análisis y machine learning a lo largo de todo el ciclo de vida, con foco en operacionalización confiable y escalable. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado en Data Science (antes Statistics 102). Cubre fundamentos probabilísticos de la inferencia y el ciclo de modelado y decisión, con sus implicaciones humanas, sociales y éticas. Sólo lista temas: no tiene resultados de aprendizaje, casos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «RGPD», «Privacidad y anonimización» (p. 8) — ya cubierta: P102 H02, P108 H01–H06, P109 H02–H03.

## S03.P102.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso ejecutivo de 8 semanas sobre liderazgo de datos: IA para líderes, marcos de innovación continua de datos, arquitectura TI y SQL, plataformas de datos y diseño de bases, *modern data stack*, nube, ética y gobierno de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python/estadística (pandas, visualización, estadística descriptiva e inferencial), aprendizaje no supervisado (clustering, PCA, clustering espectral y de modularidad), regresión y predicción, clasificación y pruebas de hipótesis, deep learning, sistemas de recomendación y redes/modelos gráficos; con casos de estudio por semana. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Configure a network to ensure data security», cifrado, autenticación, JSON web tokens (p. 8) — fuera de alcance: seguridad informática, no protección de datos en el producto descriptivo (cubierta por P102 H02 y P108).

## S03.P102.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado en línea de 6 meses (24 módulos en cinco partes: fundamentos de ciencia de datos, optimización, ML, ML avanzado y despliegue) con casos de la facultad de MIT Sloan; orientación dominante a modelado predictivo y prescriptivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño: selección de conceptos (Pugh), estudios de *trade-off*, modelos de valor, generación y evaluación de espacios de diseño, visualización del *tradespace*, frente de Pareto y sensibilidad. Sólo trae títulos de unidades y una descripción breve de cada una. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, termoformado), mapeo de atributos prototipo–producto, decisiones de fabricación y análisis de costo-valor, con un proyecto final sobre una careta facial o un giróscopo satelital. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Evaluate constraints on the use of data» (p. 7) — ya cubierta: P102 H02, P108 H01–H06.

## S03.P102.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto (asíncrono + 3,5 días presenciales) sobre estrategia, modelos de negocio, IA generativa y agéntica, pensamiento de futuros y gobernanza de IA, con un *capstone* de iniciativa organizacional; requiere 10+ años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Conocer los distintos tipos de datos, sobre su privacidad y seguridad» (p. 5) — ya cubierta: P102 H02, P108 H01–H06.

## S03.P102.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relata cuatro talleres participativos con 17 programas de pregrado de la UNAL sobre currículo, contextos, funciones misionales y prácticas pedagógicas, y recoge propuestas institucionales de armonización (superar el «currículo endogámico», egresados, unificación de conceptos). No contiene ningún programa ni curso de analítica, ningún resultado de aprendizaje disciplinar y ningún contenido de analítica descriptiva o de visualización. Estadística y Administración de Empresas sólo figuran como programas participantes (p. 8: «Economía, Zootecnia, Estadística…»). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Circular administrativa de la Dirección Académica de la Sede Manizales que fija la «Ruta de Armonización Curricular» (Acuerdo 02 de 2020 del CESU, resultados de aprendizaje, PEP, planes de mejoramiento) en dimensiones macro/meso/microcurricular y cuatro etapas; no contiene contenidos disciplinares. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Sílabo de un curso de minería de datos aplicada a salud (textos de Albright–Winston y Han–Kamber): preprocesamiento, exploración, probabilidad e incertidumbre, regresión, patrones frecuentes, clasificación, *clustering* y atípicos, minería de texto; proyecto por entregables (propuesta, reporte de recolección, reporte de preparación, informe final) y artículo de revisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Sílabo de un curso introductorio de 16 semanas centrado en herramientas (Excel, Access, SQL, MongoDB, SAS, Tableau): modelado ER y normalización, SQL (agregación, joins, subconsultas), NoSQL, sistemas de BI, visualización y tableros, proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.29

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa en línea de 12 semanas, con o sin código, sobre IA generativa, ingeniería de *prompts* y RAG, agentes con herramientas y memoria, planificación y razonamiento, sistemas multiagente, pruebas y evaluación de sistemas agénticos y su protección; casos y proyectos de automatización empresarial. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.30

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de módulo de posgrado (15 créditos, 10 semanas) del Departamento de Ciencias de la Computación: temario indicativo que va de herramientas y estadística a regresión, clustering, clasificación, estructuras para big data, privacidad y grafos; evaluación por proyecto (35 %), hojas de ejercicios y examen. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.31

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de métodos y herramientas de un programa de *business analytics*, sin descripciones: recolección de datos (encuestas, NPS, pasiva, medios), A/B testing, correlación y causalidad, pronóstico (suavizamiento exponencial, tendencia y estacionalidad, estadística descriptiva, nuevo producto), regresión, *simulation toolkit* (Analysis ToolPak, Solver), visualización e interpretación de datos, modelos de optimización y árboles de decisión. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.32

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lista de un módulo de orientación y nueve módulos con una línea de descripción cada uno, organizados por la tríada descriptiva (M1–M2), predictiva (M3–M6) y prescriptiva (M4, M7–M8), más aplicación en el negocio (M9). No incluye contenidos detallados, datos, evaluación ni resultados de aprendizaje. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.33

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación (diapositivas) de perspectiva histórica: recorre 1970–2026 (RDBMS, SQL, DW, ETL, BI 1.0/2.0, data mining, KDD, OLAP, data marts, CRISP-DM, data science, Hadoop/MapReduce, data lake, NoSQL, producto de datos, DataOps, MLOps, modelos fundacionales, IA agéntica) y define los tipos de analítica; es contexto, no prescripción. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.34

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diapositivas de un módulo DataOps que enumeran problemas organizacionales de la analítica (objetivos cambiantes, silos, mala calidad, desconfianza en los datos), mitos y brechas de conocimiento (alfabetización de datos, liderazgo) y falta de soporte (objetivos poco claros, acceso a datos, paso a producción). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.35

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - uso responsable: «¿Existe un propósito legítimo y se utilizan solamente los datos necesarios?», equidad y sesgo (p. 18) — ya cubierta: minimización (P102 H02), roles de riesgo y generalización con utilidad medida (P108 H01–H05).

## S03.P102.36

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación docente que recorre la evolución KDD → CRISP-DM → … → MAISTRO y las dimensiones de un proyecto de analítica (problema de negocio, problema analítico, datos, preparación, diseño, evaluación, operación, mejora continua, gobernanza) con un caso de abandono de clientes que transita de una pregunta descriptiva a una solución prescriptiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.37

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas docentes que trasladan Lean (Toyota Production System, Lean Software y Lean Product Development) a la analítica vista como sistema de producción y de desarrollo de producto: desperdicios en analytics, *value stream mapping*, entrega rápida, teoría de restricciones, análisis de causa raíz (5 porqués, árbol de realidad actual) y capas del ciclo de vida del dato (DataOps). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.38

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre gestión de proyectos: cascada frente a Agile (manifiesto, Scrum, XP, Kanban), escalamiento (Scrum of Scrums, SAFe, DAD), manifiesto y principios DataOps, ciclo de vida analítico y prácticas ágiles para épicas de productos de datos. Perspectiva organizacional/metodológica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.39

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas que definen DataOps como combinación de analítica, *lean thinking*, Agile y DevOps; recorren cascada, lean, Agile, DevOps, siete pasos de implementación (pruebas de datos y lógica, control de versiones, ramas, ambientes, contenedores, parametrización, «sin miedo ni heroísmo»), diferencias DevOps/DataOps, cadena de suministro de datos, MLOps, ciclo de vida de ciencia de datos y *epic hypothesis statement*. Perspectiva metodológica/organizacional orientada a productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.40

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación (diapositivas) sobre DataOps desde la perspectiva directiva. Trata los silos entre equipos (TI, ingeniería de datos, ciencia de datos, visualización, gobierno), la coordinación relacional, el flujo de desarrollo con ramas y pruebas, la eliminación de cuellos de botella con Kanban, la priorización por oportunidad, las «trampas» del CDO y las etapas de madurez de la analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.41

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre DataOps aplicado a ML e ingeniería de datos: programación tradicional vs ML, deuda técnica, arquitectura canónica y arquitectura DataOps (Airflow, Jenkins, Docker, Git…), *design thinking*, *agile data warehousing*, data lake/DW/marts, esquemas para análisis, reutilización de código y fallas típicas de proyectos de analítica. Perspectiva organizacional/metodológica orientada a productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.42

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diapositivas sobre DataOps aplicado a la calidad de datos: pruebas automáticas en cada etapa del pipeline analítico (acceso, transformación, modelado, visualización, reportería), distinción entre *value pipeline* e *innovation pipeline*, ejemplos de pruebas de entradas, lógica de negocio y salidas, niveles de severidad y pruebas de balance (de ubicación, histórico, control estadístico de procesos). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.43

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Láminas sobre cómo organizar equipos de datos: estructuras típicas (equipos pequeños, Big Data Ops, Hybrid, Large Scale), equipos por función o por dominio, roles del grupo central y de soporte con sus responsabilidades, habilidades y herramientas, perfiles en T, Pi y M, y estructuras centralizada y descentralizada. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.44

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - anonimización de atributos sensibles y cumplimiento normativo (p. 16: «anonymizing sensitive attributes»; p. 20: LGPD, confidencialidad) — ya cubierta: P102 H02, P108 H01–H06, P109 H02–H03.

## S03.P102.45

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de ejemplos de una herramienta de minería de datos orientada a modelos predictivos (CRISP-DM); los capítulos de auditoría de datos, gráficos exploratorios, listas de decisión por segmentos y canasta de mercado son los únicos con contenido descriptivo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.46

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - filtrar atributos sensibles («customer name, address, phone number, and credit card numbers», p. 23); «constraints on using particular fields such as _gender_ or _race_» (p. 24) — ya cubierta: P102 H02, P108 H01–H03.

## S03.P102.47

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - exportar flujos excluyendo los datos por defecto (p. 21: «The option to exclude data from being exported is activated by default») y cifrado de contraseñas con clave maestra (p. 17) — marginal: práctica de herramienta; la minimización y la protección de datos ya están en P102 H02 y P108 H03/H06 (la clave HMAC en código está registrada como límite de P108/P109, pero el documento no aporta un argumento descriptivo para corregirlo).

## S03.P102.48

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Hoja comercial de SQL Server 2005 Analysis Services Data Mining: casos de uso (cesta de mercado, abandono, segmentación, pronóstico, exploración, calidad de datos, texto), integración con SSIS/OLAP/Reporting, algoritmos, DMX y arquitectura. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.49

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - tipificar códigos numéricos como categóricos (código postal con ceros a la izquierda) y convertir fechas (p. 128) — marginal: variante de la conversión de tipos de P102 H03 y P106 H03.

## S03.P102.50

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-data-mining.md` (`source_sha256`: 6396a7c9e3efce998f0bbb9907cacb228244737c80bdebcdae17ce913b7f6ce9).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - White paper comercial de SAS (2015) que presenta el ciclo de vida analítico (pregunta → preparación → exploración → modelado → implementación → evaluación) como marco para vender Enterprise Miner, Factory Miner y Decision Manager; foco declarado en minería de datos predictiva. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.51

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-forecasting.md` (`source_sha256`: 7cabe87e23ff9469d7b4b9e17582dd694b8ac329ed0975bf9a26e3dcb26b5569).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Colección de artículos técnicos y de proceso sobre pronóstico con productos SAS; lo pertinente para descriptiva es la preparación y exploración de series (acumulación, intervalo, jerarquías, diagnóstico del índice temporal, descomposición tendencia–estación) y el análisis descriptivo de una distribución sesgada. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.52

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-stat.md` (`source_sha256`: 2977c390790a2e7206c4e754753b180908bbc6165dba6d6b29031a0c9e190ca7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Manual de referencia de PROC REG: ajuste por mínimos cuadrados, nueve métodos de selección de variables, pruebas de hipótesis, colinealidad, residuos e influencia, y gráficos de diagnóstico de ODS Graphics. Ejemplos: salarios de béisbol, predicción de aptitud aeróbica, peso por estatura y edad, variables cualitativas, ridge y falta de ajuste. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.53

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - técnicas oficiales de modelado dimensional de Kimball (hechos, dimensiones de calendario, dimensiones de cambio lento, dimensiones conformadas, jerarquías). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P102.54

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sílabo de un curso de posgrado de data warehousing y BI (modelado ER y dimensional de Kimball, SAP BusinessObjects y Tableau). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
