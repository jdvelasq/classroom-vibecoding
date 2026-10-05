# Log — P443

## S02.P443.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P443_data_lineage/` (`data/raw_operations.csv`, `professor/main.py`, `professor/test_main.py`, `requirements.txt`, `src/main.py`, `submission/factory_totals.csv`, `submission/lineage.json`, `tests/test_activity.py`); `P431_data_versioning/submission/data_manifest.json`; agregados de P412, P417, P428, P432.
- **Trazabilidad revisada:** P443 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (cambio de grano, caso y datos), H02 (huella del insumo), H03 (lo que se prueba).
- **Ambigüedades:** el linaje no registra la transformación pese al docstring; `created_at` no determinista; `requirements.txt` local no listado como excepción en `structure-audit.md`; quinta repetición del agregado por fábrica; posible solapamiento con el linaje de dbt en P433.
- **Superficies / contrato / dependencias:** S01–S05; recibe insumo demostrable de P431 (SHA-256 idéntico); habilitación no evidenciada.
- **Auditoría de Analytics:** resuelta con límite; el linaje sirve a un agregado descriptivo del caso de fábricas.

## S03.P443.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DI-Methods (p. 91: «Role of hash algorithms in integrity preservation»; «Data provenance assurance», p. 91) — ya cubierta al nivel que el documento pide («explain»): P431 H01 identifica la versión por contenido; P443 H02 ancla la salida a la huella del insumo; P448 H02 verifica restauración por bytes. La falta de función de verificación en P431 es un límite S02, no una señal nueva de este documento.

## S03.P443.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P443.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify characteristics of lineage, traceability, and version control of data» (p. 15, CAP-E.3.4.3) — ya cubierta: P431 H01 (identidad por contenido), P443 H02 (linaje entrada→salida).

## S03.P443.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.3.4.3 «Identify the purpose of lineage, traceability, and version control of data» (p. 15) — ya cubierta: huella de datos (P431 H01), linaje del agregado (P443 H02), versión de la definición (P408 H01–H02).

## S03.P443.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - el grano como «binding contract on the design» y no mezclar granos (p. 5) — ya cubierta: P402 H02 (llave derivada del grano máquina-día) y P443 H01 (cambio de grano que el linaje explica).

## S03.P443.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data provenance» (p. 45); «Students also need to consider the provenance of the data used» (p. 40) — ya cubierta: P431 H01 (huella por contenido), P443 H02 (salida anclada a la huella del insumo). El defecto de P443 (linaje sin identificador de transformación) ya está registrado en S02 y el documento no aporta un criterio más preciso.

## S03.P443.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el arquitecto de datos responde por «gobernanza, linaje, seguridad y soporte a modelos de IA en producción» (p. 290) — ya cubierta (P443 H02, P454 H01); el diseño de plataformas de datos es fuera de alcance.

## S03.P443.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P443.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo de dos meses sin requisitos técnicos sobre capacidades de IA (ML, redes neuronales, visión, NLP, robótica), estrategia de IA y equipos de IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
