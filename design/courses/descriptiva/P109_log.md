# Log — P109

## S02.P109.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P109_anonimizacion_sql/` (`data/raw.csv`, `data/auxiliary.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/anonymized.csv`, `temp/anonimizacion.db`, `tests/`). Comparado con P108, P107 y P104; revisado que P120–P154 no reutilizan sus datos.
- **Trazabilidad revisada:** entrada P109 → `descriptiva.C05`.
- **Highlights añadidos:** H01 (pregunta declarada), H02 (reglas en una consulta SQL), H03 (consulta de enlace con CTE), H04 (orden por `row_id` exigido por la prueba posicional; highlight de caso y datos), H05 (raíz portable).
- **Ambigüedades:** producto duplicado con P108; se pierden la demostración ingenua y el contraste de utilidad; la consulta de ataque omite perfiles sin candidatos y no se persiste; clave HMAC en el código; reglas `CASE` duplicadas entre transformación y ataque.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P108, P107 y P104; no habilita dependencias demostrables por artefacto.
- **Auditoría de Analytics:** producto = capacidad de datos compartible; C05 sustentado en su dimensión responsable. Domina la privacidad con SQL como disciplina contribuyente.

## S03.P109.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - técnicas de privacidad en datos crudos «provide ranges or salting techniques» (DP-Social Responsibility, p. 84); funciones *hash* (DP-Cryptography, p. 85); tensión transparencia–privacidad (DP-Information Systems, p. 85) — ya cubierta: P108 H03 (`pd.cut`, HMAC con clave), H04–H05 (riesgo frente a utilidad). La clave HMAC escrita en el notebook (P108 S02) es un defecto real ya registrado por S02. ACM no aporta un argumento específico de gestión de secretos, por lo que no justifica aquí una propuesta propia.

## S03.P109.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad y seguridad como protocolos del dominio de datos (p. 5) — ya cubierta: P102 H02, P108, P109.

## S03.P109.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P109.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad, seguridad y datos con implicaciones éticas (p. 13: «maintaining its privacy and security»; p. 15: CAP-P.3.4.2) — ya cubierta: P102 H02, P108 H01–H06, P109 H02–H03, P125 H07.

## S03.P109.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data subject privacy» (p. 45), «Privacy and confidentiality» (p. 50) — ya cubierta (P102 H02; P108 H01–H06; P109 H02–H03).

## S03.P109.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «uso de datos anonimizados y agregados», cortes territoriales sólo «cuando hay masa crítica» y categoría NB «sólo descriptivamente» (p. 238); Privacy Engineer «PII» (p. 335); protección de datos personales (pp. 183, 203) — ya cubierta: minimización y anonimización con riesgo medido (P102 H02, P108 H01–H05), persistir sólo agregados con tamaño mínimo (P125 H04, H07).

## S03.P109.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P109.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Implementación responsable de la IA: tolerancia al riesgo, supervisión y gobernanza» (p. 5) — fuera de alcance: gobernanza organizacional de IA; la dimensión responsable de datos ya está en P108 H01–H06 y P125 H07.
