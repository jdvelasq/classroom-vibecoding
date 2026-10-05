# Log — P454

## S02.P454.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P454_data_catalog/` (`data/catalog.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/catalog_entry.json`, `tests/test_activity.py`); `P434_contract_versioning/data/contract.json`, `P447_incident_response/professor/main.py`, `P452_access_control/data/access_policy.json`, P431, P433, P443.
- **Trazabilidad revisada:** P454 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (ficha del caso, caso y datos), H02 (prueba de contenido).
- **Ambigüedades:** la ficha es copia sin transformación; coincidencias con P434/P447/P452 son de texto; C02 débil y C04 (documentación) no mapeada; posible solapamiento con documentación de dbt en P433.
- **Superficies / contrato / dependencias:** S01–S05; sin dependencias de artefacto.
- **Auditoría de Analytics:** resuelta con límite; gobierno del dataset de riesgo sin verificación contra el producto.

## S03.P454.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P454.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 7.6 «Ensure documentation is complete and/or maintained» (p. 7) y Task 3.7 (p. 5) — ya cubierta en el mecanismo: ficha operacional (P454 H01–H02), manifiesto y changelog (P444 H02). Su refuerzo queda absorbido por la candidata NUEVA (contrato).

## S03.P454.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify the types of documentation needed for various analytics methodologies» (p. 25, CAP-E.7.6.1) — ya cubierta: runbook (P446 H01–H02), ficha de catálogo (P454 H01), contrato documentado con respuestas ejecutadas (P425 H02).
  - roles de gobierno «data owner, data steward, data custodian» (p. 14, CAP-E.3.2.2) — marginal: P454 H01 y P411 H02 ya fijan un responsable; distinguir tres roles no cambia lo que el estudiante hace con la capacidad.

## S03.P454.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.6.4.2 documentación del modelo y del reporte «so that the analytics solutions can be reused if the business circumstances should change» (p. 23); Task 7.6 y CAP-P.7.6.1 «Identify the types of documentation needed for various audiences» (p. 25) — ya cubierta: ficha operacional (P454 H01–H02), runbook para quien atiende (P446 H01–H02), contrato documentado con respuestas ejecutadas para el consumidor (P425 H02).
  - CAP-P.3.2.2 «overlaps and gaps in responsibility, including roles responsible for data governance» (p. 14); CAP-P.3.3.1 consecuencias de «lack of responsibility for data ownership» (p. 14) — ya cubierta: responsable en la tarjeta (P411 H02) y en la ficha de catálogo (P454 H01).

## S03.P454.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P454.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Marco de pregrado que define la «data acumen» (diez áreas conceptuales) y recomienda que la ética y la reproducibilidad atraviesen el currículo; trata el flujo de trabajo y la gestión de datos como competencias generales, no la operación de productos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P454.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el arquitecto de datos responde por «gobernanza, linaje, seguridad y soporte a modelos de IA en producción» (p. 290) — ya cubierta (P443 H02, P454 H01); el diseño de plataformas de datos es fuera de alcance.

## S03.P454.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
