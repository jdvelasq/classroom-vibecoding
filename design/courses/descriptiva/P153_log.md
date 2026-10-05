# Log — P153

## S02.P153.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P153_ventas_kpis/` (`data/sales_mart.db`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` con cinco archivos, `tests/`); contexto de P120, P121, P122, P124 y P150–P152.
- **Trazabilidad revisada:** P153 → `descriptiva.C01`, `C02`, `C03`, `C05`; `audit-against-design.md` omite C01.
- **Highlights añadidos:** H01 (KPI como contrato), H02 (tasa ponderada como ratio de sumas sobre `discount_pct` por línea; obligatorio de caso y datos), H03 (calidad como compuerta de publicación), H04 (linaje).
- **Ambigüedades:** ningún valor de KPI se calcula; las reglas cubren integridad del hecho pero no «problemas de definición» que la pregunta menciona; la rama `BLOQUEADO` nunca se ejercita sobre datos íntegros por construcción; «Gerencia comercial» es sólo etiqueta de propietario; «segmento» en el linaje no se define; prueba de linaje débil (longitud > 8); gráfico sobre booleanos; notebook de estudiante vacío.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; P154 no consume el catálogo y publica `orders`, ausente de él.
- **Auditoría de Analytics:** producto = gobierno de métricas; fortalece C01/C05 pero no describe lo que ocurre. Se lee como práctica de BI/gobierno de datos.

## S02.P153.02

- **Fecha / curso / executor:** 2026-10-04 / `descriptiva` / Claude; **estado:** incremental.
- **Origen:** aclaración del profesor: *business intelligence* es un predecesor que, por su importancia, está contenido en la analítica descriptiva (como la minería de datos en la predictiva).
- **Cambio en la auditoría de Analytics:** la auditoría decía que la actividad «se lee como práctica de BI/gobierno de datos». Se corrige: el gobierno de métricas es BI y forma parte de la analítica descriptiva; se conserva como límite que las reglas no ejercitan el bloqueo.
- **Highlights, superficies y dependencias:** sin cambios; no se renumeran IDs.

## S03.P153.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - integridad lógica «Entity integrity, referential integrity, domain integrity» (DPSIA/DI, p. 90); integración de fuentes y *data warehouse* (DG-Data Integration, p. 71) — ya cubierta: P150 H02, P151 H02–H03, P153 H03.
  - procedencia de datos (DPSIA/DI, p. 91: «Data provenance assurance») y auditabilidad de sistemas de decisión (PR-On Automation, p. 111) — ya cubierta en lo descriptivo por el linaje de P153 H04. Lo demás es fuera de alcance (seguridad y automatización).

## S03.P153.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - linaje, trazabilidad y control de versiones de los datos (CAP-E.3.4.3, p. 15) — ya cubierta: P153 H04.

## S03.P153.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio 17 %, encuadre analítico 15 %, datos 19 %, selección de metodología 15 %, desarrollo de modelos 15 %, despliegue 10 %, ciclo de vida 9 %) con subtareas evaluables. Respalda expectativas profesionales generales, no un syllabus. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - «Data consistency checking» (p. 46), «document data quality problems» (p. 37) — ya cubierta (P121 H02 conciliación; P122 H05 cobertura; P153 H03).

## S03.P153.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Formular preguntas correctas ... interpretar métricas y KPIs» (p. 219); Índice de Rotación definido con variables, numerador y promedio de planta (pp. 305–306) — ya cubierta: pregunta enlazada a evidencia (P120 H01) y KPI como contrato con numerador/denominador (P153 H01).
  - rotación «promedio simple ≈ 27,5 %» frente a «ponderada por número de empleados ≈ 29,8 %» (p. 307) — ya cubierta: razón de sumas vs promedio de razones (P121 H03, P153 H02); ejemplo equivalente, no cambia lo que el estudiante hace.
  - gobernanza y «linaje» como responsabilidad del arquitecto de datos (p. 290); SIEET-D «con un enfoque de gobernanza, trazabilidad y calidad» (p. 128) — ya cubierta: linaje campo→KPI (P153 H04) y calidad como compuerta (P153 H03); más allá es ingeniería de datos (fuera de alcance).

## S03.P153.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de pregrado de 4 unidades, con prerrequisitos de programación y de un curso de ciencia de datos (DATA C100 o equivalente), sobre gestión de datos a escala para análisis y machine learning a lo largo de todo el ciclo de vida, con foco en operacionalización confiable y escalable. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado en Data Science (antes Statistics 102). Cubre fundamentos probabilísticos de la inferencia y el ciclo de modelado y decisión, con sus implicaciones humanas, sociales y éticas. Sólo lista temas: no tiene resultados de aprendizaje, casos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de 11 semanas, sin codificación, organizado en sesgos de decisión, análisis descriptivo, Big Data, experimentación, predictivo (ML, redes neuronales), prescriptivo y cuestiones ético-jurídicas; casos y tareas de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P153.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the typical metrics of high-performing companies … Wait Time, Deployment Frequency, Service Restoration Time, and Failure Rate» (p. 14) y «KPIs» como contenido técnico (p. 7) — fuera de alcance: métricas de operación de software; la definición de KPI como contrato ya está cubierta (P153 H01–H02).

## S03.P153.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Apply best practices in data governance» (p. 7); «Data Governance and Compliance» (p. 15) — ya cubierta: P153 H01, H03–H04 (catálogo, compuerta de calidad, linaje).
