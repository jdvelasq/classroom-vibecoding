# Log — P108

## S02.P108.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P108_anonimizacion_pandas/` (`data/raw.csv`, `data/auxiliary.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/anonymized.csv`, `tests/`). Comparado con P102 y P103.
- **Trazabilidad revisada:** entrada P108 → `descriptiva.C05`.
- **Highlights añadidos:** H01 (roles de riesgo de columnas; highlight de caso y datos), H02 (insuficiencia de la supresión ante enlace), H03 (técnicas diferenciadas), H04 (generalización con riesgo residual por paso), H05 (costo en utilidad), H06 (contrato del conjunto compartible). No inferibles: conteos de reidentificación (no persistidos ni visibles).
- **Ambigüedades:** clave HMAC escrita en el notebook; en las filas visibles los números de tarjeta son secuenciales y sus cuatro dígitos conservados identifican cada registro; `annual_spend` exacto; riesgo evaluado sólo contra 20 perfiles, sin garantía formal; procedencia no documentada.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P102/P103; habilita P109 (mismos datos, reglas, seudónimo y prueba).
- **Auditoría de Analytics:** producto = capacidad de datos compartible con riesgo y utilidad explícitos; C05 sustentado en su dimensión responsable. Domina la privacidad de datos como disciplina contribuyente.

## S03.P108.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - técnicas de privacidad en datos crudos «provide ranges or salting techniques» (DP-Social Responsibility, p. 84); funciones *hash* (DP-Cryptography, p. 85); tensión transparencia–privacidad (DP-Information Systems, p. 85) — ya cubierta: P108 H03 (`pd.cut`, HMAC con clave), H04–H05 (riesgo frente a utilidad). La clave HMAC escrita en el notebook (P108 S02) es un defecto real ya registrado por S02. ACM no aporta un argumento específico de gestión de secretos, por lo que no justifica aquí una propuesta propia.

## S03.P108.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad y seguridad como protocolos del dominio de datos (p. 5) — ya cubierta: P102 H02, P108, P109.

## S03.P108.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - datos sensibles, uso restringido y riesgo de adquirir datos innecesarios (CAP-E.3.1.2, 3.3.1, 3.4.2, pp. 13–15) — ya cubierta: P102 H02 (minimización), P108 H01–H03.

## S03.P108.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad, seguridad y datos con implicaciones éticas (p. 13: «maintaining its privacy and security»; p. 15: CAP-P.3.4.2) — ya cubierta: P102 H02, P108 H01–H06, P109 H02–H03, P125 H07.

## S03.P108.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data subject privacy» (p. 45), «Privacy and confidentiality» (p. 50) — ya cubierta (P102 H02; P108 H01–H06; P109 H02–H03).

## S03.P108.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «uso de datos anonimizados y agregados», cortes territoriales sólo «cuando hay masa crítica» y categoría NB «sólo descriptivamente» (p. 238); Privacy Engineer «PII» (p. 335); protección de datos personales (pp. 183, 203) — ya cubierta: minimización y anonimización con riesgo medido (P102 H02, P108 H01–H05), persistir sólo agregados con tamaño mínimo (P125 H04, H07).

## S03.P108.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P108.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Implementación responsable de la IA: tolerancia al riesgo, supervisión y gobernanza» (p. 5) — fuera de alcance: gobernanza organizacional de IA; la dimensión responsable de datos ya está en P108 H01–H06 y P125 H07.

## S03.P108.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de pregrado de 4 unidades, con prerrequisitos de programación y de un curso de ciencia de datos (DATA C100 o equivalente), sobre gestión de datos a escala para análisis y machine learning a lo largo de todo el ciclo de vida, con foco en operacionalización confiable y escalable. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P108.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - privacidad diferencial (p. 1: «differential privacy») — fuera de alcance: los índices de P108 y P109 registran como límite que no hay garantía formal de privacidad. Pero el documento sólo nombra la técnica, y en un taller descriptivo no hay caso ni datos para enseñarla con rigor sin desplazar la contribución de P108 (ataque de enlace y generalización medida, H02–H05).

## S03.P108.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «RGPD», «Privacidad y anonimización» (p. 8) — ya cubierta: P102 H02, P108 H01–H06, P109 H02–H03.

## S03.P108.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
