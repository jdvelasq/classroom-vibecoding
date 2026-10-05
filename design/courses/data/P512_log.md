# Log — P512

## S01.P512.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registraron hecho, dimensiones y preservación de grano como aporte técnico distinto de P511.

## S02.P512.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P512_superstore_warehouse/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/superstore_mart.db`, `tests/test_activity.py`); P500, P501, P503, P505–P507 y P511 para relaciones.
- **Trazabilidad revisada:** P512 → `data.C01`–`data.C05`; C01 limitada a una pregunta de organización.
- **Highlights:** añadidos H01 (dimensión de fecha desde texto `d/m/yy`; caso y datos), H02 (hecho a grano línea separado de dimensiones), H03 (mart persistido y consulta en estrella).
- **Preservado:** pregunta, modelo dimensional en SQLite, preservación del grano, consulta temporal por categoría, relación de extensión con P511.
- **Corregido:** la descripción previa decía que el mart organiza por «geografía»; no hay dimensión geográfica, está dentro de `dim_customer`. Se precisa que el resultado de la consulta no se persiste y que `orders` no entra al mart (no hay `Order ID`).
- **Añadido:** `dim_date` sin calendario completo y con clave por orden de aparición; ausencia de PK/FK; imposibilidad de reconstruir `order_count` de P500; prueba de sólo existencia.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** si la omisión de `orders` en el mart es deliberada.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P511 y P505–P507; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** capacidad de datos descriptiva; riesgo de lectura como taller de modelado dimensional por pregunta de organización y consulta no entregada.

## S03.P512.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Integration (p. 71: «data warehouse») y DPSIA/DI-Logical integrity (p. 90) — marginal: declarar restricciones en el mart (S03) repite lo aprendido en P503 H04 y acentúa la lectura como taller de modelado dimensional.

## S03.P512.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P512.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.4/3.2.5 fortalezas y elección de arquitectura de datos (p. 14) — fuera de alcance (arquitectura excluida).

## S03.P512.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P512.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - dimensión de fecha como calendario completo con clave `YYYYMMDD` y fila «desconocida» (p. 11 «the date dimension table needs a special row to represent unknown … dates») — marginal: mejora local de H01 (hoy `date_key` por orden de aparición y sólo fechas observadas); puede incorporarse como detalle de la candidata anterior si se reconstruye `dim_date`, pero no justifica propuesta propia.
  - proceso de cuatro pasos y requisitos con el negocio (p. 4 «Select the business process. Declare the grain. Identify the dimensions. Identify the facts») — ya cubierta en lo esencial por H02; la declaración explícita de grano se integra en la candidata.
  - dimensiones lentamente cambiantes tipos 0–7 (pp. 15–16), mini-dimensiones, claves durables (p. 10) — fuera de alcance: Superstore no trae historia de cambios de atributos y el tema desplaza hacia arquitectura de data warehouse.
  - copo de nieve frente a dimensión aplanada, jerarquías fijas/irregulares, tablas puente de jerarquía (pp. 12, 17) — marginal/fuera: P512 ya usa dimensiones planas; jerarquías irregulares no tienen caso.
  - tablas agregadas, cubos OLAP y navegación de agregados (pp. 5, 8) — ya cubierta: P501 H01 publica agregados por pregunta; cubos OLAP fuera de alcance.

## S03.P512.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - las bases de datos modernas, relacionales y no relacionales (p. 45) — ya cubierta: relacional en P503–P510 y P512, JSON anidado en P518. Añadir NoSQL sería variante de herramienta.

## S03.P512.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «muchos candidatos presentan consultas SQL básicas, pero carecen de la comprensión de modelado de datos avanzado, … normalización vs. desnormalización» (p. 175); «construir modelos lógicos de datos» como pilar crítico para Data Analyst (p. 252). Categoría: ya cubierta. Normalización de multivalor con PK/FK (P503 H02, H04), tabla plana integrada (P511 H01–H03) y hecho–dimensiones que contrasta con la tabla plana (P512 H02) ya ejercen el contraste.
  - Arquitecto de Datos que define «un data warehouse corporativo, algunos data marts» hasta «lagos de datos, arquitecturas híbridas …, gobernanza, linaje, seguridad» (p. 290); Líder de BD que participa en «arquitectura de datos y gobierno de información» (p. 286). Categoría: ya cubierta / fuera de alcance. Mart mínimo (P512 H02–H03) y linaje con cambio de grano (P502 H03) ya existen; lagos y gobierno corporativo son arquitectura empresarial, excluida.

## S03.P512.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P512.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P512.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P512.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P512.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P512.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
