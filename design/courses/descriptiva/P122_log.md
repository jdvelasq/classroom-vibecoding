# Log — P122

## S02.P122.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P122_supply_chain/` (`data/supply_chain.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con `questions.json` y ocho CSV, `tests/`); P106, P120 y P121 como comparación.
- **Trazabilidad revisada:** P122 → `descriptiva.C01`, `C02`, `C03`; coherente. La declaración de cobertura de flete roza C05, no mapeada.
- **Highlights añadidos:** H01–H07 (grano y calidad, KPI desde fechas, proporción vs promedio, valor expuesto, cobertura de flete, umbrales por nivel, persistencia y pruebas). Highlights obligatorios de caso y datos: H02 y H05.
- **Cambios realizados:** creación de `P122_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** procedencia y licencia del dataset no documentadas (insumos de salud por país); el comentario mensual promete controlar «cambio de mezcla» pero el código no lo hace; serie mensual sin volumen mínimo; umbrales 50/20/30 sin justificación; el contraste proporción–promedio (H03) es observable pero no comentado; pruebas más laxas que en P120/P121 y sin verificación de `questions.json`; `priority_segments.csv` se guarda sin el ordenamiento que se muestra.
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; dependencias demostrables de P120/P121 (plantilla) y P106 (conversión de tipos); salida no evidenciada.
- **Auditoría de Analytics:** diagnóstico de cumplimiento y valor expuesto con límite de cobertura explícito; disciplinas al servicio del producto. Sin declaración explícita de límite causal.

## S03.P122.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - *scores* y *rankings* con características deseables (DM-Proximity, p. 75) — ya cubierta: umbrales de volumen y separación entre riesgo y prioridad (P120 H06–H07, P121 H05, P122 H04/H06).

## S03.P122.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta: P120 H02, P121 H02, P122 H01, H05.
  - Task 3.8 «Validate and update the business and analytics problem statements» (p. 5) — ya cubierta: P122 H05.

## S03.P122.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - brechas de calidad «accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y métodos para evaluarla (CAP-E.3.6.1, 3.6.4, p. 15) — ya cubierta: P120 H02, P121 H02, P122 H01 y H05.
  - hallazgo de calidad que obliga a actualizar el enunciado del problema analítico (CAP-E.3.8.1, p. 16) — ya cubierta: P122 H05 (la cobertura del flete cambia el denominador y el límite de la comparación).
  - perfil univariado («data profiling outputs») y visualizaciones comunes con su propósito (CAP-E.3.6.2, 3.6.3, p. 15) — ya cubierta en la secuencia: histograma de P122 H02, mediana/percentiles y caja de P125 H03; la ausencia de distribución en P103 es marginal porque la secuencia la ejerce después.

## S03.P122.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - criterios de éxito y línea base del estado actual (p. 11: Task 2.4 «Define primary measures of success»; Task 2.5 «Identify baseline performance of the current state») — marginal: en descriptiva la «línea base» ya aparece como KPI global del período (P120 H04, P121 H03, P122 H02) y como referencia de pares (P125 H02); medidas de éxito de una solución pertenecen a predictiva/prescriptiva.
  - caso de negocio, costos, beneficios y consecuencias indirectas (p. 8: Task 1.5 «Create an initial business case») — fuera de alcance: la evaluación de costo-beneficio de una solución excede la pregunta descriptiva; P122 H04 ya pondera por valor expuesto.
  - documentar y reportar hallazgos de datos (p. 16: Task 3.7 «Identify appropriate elements of a data report») — ya cubierta en lo esencial: P122 H01/H05 (tabla de calidad y cobertura de flete), P120 H02 (grano y consistencia); un «reporte de datos» formal sería una variante.

## S03.P122.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «use simple graphics to check data for artifacts, snafus, and inconsistencies» (p. 45) — ya cubierta (P122 H01–H02, histograma con referencia en cero; regla de evidencia visual de `AGENTS.md`).
  - «Variability, uncertainty, sampling error, and inference» (p. 44) frente a tasas sin intervalos — marginal: el umbral de volumen (P120 H06, P121 H05, P122 H06) ya cumple la función descriptiva; intervalos desplazarían hacia Estadística.
  - «Data consistency checking» (p. 46), «document data quality problems» (p. 37) — ya cubierta (P121 H02 conciliación; P122 H05 cobertura; P153 H03).

## S03.P122.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diagnóstico nacional de la brecha cuantitativa y cualitativa de talento TI en Colombia (demanda por roles, habilidades hard/soft, pertinencia curricular, salarios y rotación). Su valor para el curso es de pertinencia laboral del perfil analista de datos/BI; no define estándar ni prescribe herramientas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad de datos, representatividad y por qué fallan los modelos» (p. 5) — fuera de alcance/ya cubierta: el encuadre es de entrenamiento de modelos (predictiva); la calidad y el grano antes de agregar ya están en P120 H02, P122 H01 y P121 H02. El folleto no desarrolla método ni caso.

## S03.P122.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclo «from data preparation to exploration, visualization and analysis» (p. 1) — ya cubierta: preparación y calidad (P106 H01–H05, P107 H01–H02), exploración y visualización al servicio de un diagnóstico (P120 H02–H05, P121 H02–H04, P122 H01–H05). La ficha no da detalle que permita contrastar más.

## S03.P122.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - intervalos de confianza, pruebas de permutación y *false discovery rate* (p. 1: «permutation testing, false discovery rate, … confidence intervals») — fuera de alcance: los índices de P120–P122 registran como límite que las tasas por segmento no tienen intervalos ni pruebas de diferencia. Convertir ese límite en inferencia formal (por ejemplo, controlar comparaciones múltiples en un top N de segmentos) mete Estadística inferencial en el curso. Además, el documento no da caso ni profundidad para hacerlo con rigor. Los umbrales de volumen (P120 H06, P121 H05, P122 H06) siguen siendo la salvaguarda descriptiva vigente.

## S03.P122.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Estadísticas descriptivas», «Distribuciones normales y no normales» (p. 7) — ya cubierta: histograma con referencia en cero (P122 H02), mediana/percentiles y caja (P125 H03).

## S03.P122.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso ejecutivo de 8 semanas sobre liderazgo de datos: IA para líderes, marcos de innovación continua de datos, arquitectura TI y SQL, plataformas de datos y diseño de bases, *modern data stack*, nube, ética y gobierno de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa en línea de 12 semanas: fundamentos de Python/estadística (pandas, visualización, estadística descriptiva e inferencial), aprendizaje no supervisado (clustering, PCA, clustering espectral y de modularidad), regresión y predicción, clasificación y pruebas de hipótesis, deep learning, sistemas de recomendación y redes/modelos gráficos; con casos de estudio por semana. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre diseño de productos de IA: proceso de diseño de IA en cuatro etapas, fundamentos de ML y deep learning, interacción humano-computador, «superminds», GANs y un proyecto final con el «Lawler Model» para definir un problema de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso sobre estrategia y diseño de plataformas digitales y mercados de dos lados: efectos de red, casos de éxito y fracaso, precios, arquitectura y APIs, gobierno de calidad, regulación y modelado de dinámicas de plataforma. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cronograma de un curso profesional del MIT en ocho módulos: ecuaciones diferenciales ordinarias y parciales, métodos numéricos, optimización y estimación de parámetros, regresión y clasificación, métodos probabilísticos (Monte Carlo, pronóstico) y estudios de caso industriales. Sólo lista títulos y duraciones. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un certificado de 6 meses en ingeniería de datos: Python/pandas, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, NiFi, Kafka, DASK, seguridad web, ML y aprendizaje por refuerzo; portafolio GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Correlation» (Módulo 3, p. 7) — marginal: técnica aislada sin caso descriptivo asociado en el documento; las relaciones entre dimensiones ya se describen con matrices de segmentos (P120 H06, P121 H04, P122 H06).

## S03.P122.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cronograma de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño: selección de conceptos (Pugh), estudios de *trade-off*, modelos de valor, generación y evaluación de espacios de diseño, visualización del *tradespace*, frente de Pareto y sensibilidad. Sólo trae títulos de unidades y una descripción breve de cada una. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo, termoformado), mapeo de atributos prototipo–producto, decisiones de fabricación y análisis de costo-valor, con un proyecto final sobre una careta facial o un giróscopo satelital. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo comercial de cursos cortos presenciales (3–5 días): Data Science para profesionales (visualización/dashboards con Power BI o Tableau), Data Science para principiantes e intermedios (R/Python, SQL, regresión, ML), programa de analítica avanzada y predictiva, *masterclasses* para directivos y *fast tracks* temáticos (texto, regresión, clasificación, clustering y redes). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo mixto (asíncrono + 3,5 días presenciales) sobre estrategia, modelos de negocio, IA generativa y agéntica, pensamiento de futuros y gobernanza de IA, con un *capstone* de iniciativa organizacional; requiere 10+ años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P122.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Conocer distintos métodos de visualización para mostrar los datos temporales, espaciales y espacio-temporales» (p. 8) — ya cubierta: temporales en P121 H04 y H06 (matriz calendario día × hora; serie frente a patrón por mes), P122 y P150; espaciales en P123 (mapa coroplético de países, inventario y S05). Espacio-temporal combinado: marginal, sin caso con ambas dimensiones de grano adecuado en el curso.
  - «Contar una historia con los puntos claves para fundamentar las decisiones empresariales mediante informes, cuadros de mando, historias e infografías» y «Anticipar y gestionar las preguntas de los diversos públicos y audiencias» (p. 8) — marginal desde este documento: la falta de interpretación escrita en varios talleres ya está registrada en S02 y el patrón de conclusiones con límite existe en P125 H06; un folleto institucional no describe un mecanismo evaluable que justifique cambiar un taller concreto.

## S03.P122.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - relata cuatro talleres participativos con 17 programas de pregrado de la UNAL sobre currículo, contextos, funciones misionales y prácticas pedagógicas, y recoge propuestas institucionales de armonización (superar el «currículo endogámico», egresados, unificación de conceptos). No contiene ningún programa ni curso de analítica, ningún resultado de aprendizaje disciplinar y ningún contenido de analítica descriptiva o de visualización. Estadística y Administración de Empresas sólo figuran como programas participantes (p. 8: «Economía, Zootecnia, Estadística…»). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
