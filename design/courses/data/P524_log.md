# Log — P524

## S02.P524.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P524_seleccion_formato_datos/` (`data/flights.csv`, `data/flights.json`, `data/flights.csv.gz` y `data/flights.parquet` como binarios, `data/sales.*`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/format_comparison.csv`, `tests/test_activity.py`); P513, P518 y P522 para contraste.
- **Trazabilidad revisada:** P524 → `data.C02`–`data.C05`; C03 débil.
- **Highlights:** añadidos H01 (mismas filas), H02 (costo de representación de un registro ancho con nulos; caso y datos), H03 (tabla de decisión).
- **Ambigüedades:** propiedades booleanas constantes; comparación mezcla formato y compresión y omite el CSV comprimido de entrada; JSON fuera del `assert`; el notebook escribe sus salidas en `data/`; `sales.csv/json/parquet` sin uso y sin procedencia; procedencia de vuelos no documentada.
- **Superficies / contrato / dependencias:** S01–S05; recibe: ninguna demostrable; habilita P525 sólo como práctica.
- **Auditoría de Analytics:** riesgo moderado; formatos sin uso analítico, vinculados a la estructura de los datos.

## S03.P524.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CCF-File Systems (p. 66: «Compare and contrast different approaches to file organization») y DG-Data Reduction and Compression (p. 72: «Select data compression techniques according to the computation, communication and storage requirements», T2) — ya cubierta: tabla de decisión de formato (H03) sobre las mismas filas (H01).

## S03.P524.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.7 las 4 V (p. 14) — marginal: concepto de reconocimiento; no justifica reforzar el bloque de procesamiento cuya identidad ya está en duda.

## S03.P524.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco autorizado de la NASEM para la formación de pregrado en ciencia de datos. Define la «data acumen» y diez áreas conceptuales (entre ellas gestión y curaduría de datos, flujo de trabajo y reproducibilidad, ética) y pide que la ética atraviese todo el currículo. Respalda expectativas generales, no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «se requieren profesionales con conocimientos tanto de bases de datos relacionales … como NoSQL (MongoDB, Cassandra, Redis, DynamoDB)» (p. 175); «Bases de datos NoSQL y Big Data — Alta demanda — Énfasis en Bases de Datos Relacionales tradicionales» (p. 167). Categoría: marginal / fuera de alcance. Lo que tiene de representación semiestructurada ya se ejerce (proyección de JSON anidado a una unidad de análisis en P518 H02; costo de representar un registro ancho en JSON en P524 H02); motores NoSQL concretos son herramienta, y la familia governmental no prescribe herramientas.

## S03.P524.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de 4 unidades, cruzado con COMPSCI C187, que cubre la gestión de datos a escala a lo largo del ciclo de vida, con requisitos previos de programación (CS 61B o equivalente) y de un curso de ciencia de datos de nivel superior (DATA C100 o equivalente); no detalla temario, datos, herramientas ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso de educación profesional del MIT: ecuaciones diferenciales y métodos numéricos, modelado espacial (EDP), optimización y modelado guiado por datos, de la optimización al ML (regresión, regularización, clasificación), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos industriales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «stream big data using the pandas, Parquet, and Feather libraries» (p. 11) — ya cubierta/marginal: P524 compara CSV/JSON/Parquet; Feather sería otro formato equivalente.

## S03.P524.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de 6 meses con cinco partes (fundamentos de data science, optimización, ML, ML avanzado, despliegue), casos (retail, análisis facial, Filatoi Riuniti, BlueBike) y *capstone* de portafolio; herramientas Python y Google Colab. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh, estudios de trade-off, modelos de valor, generación de espacios de diseño, tradespace, frente de Pareto y sensibilidad. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
