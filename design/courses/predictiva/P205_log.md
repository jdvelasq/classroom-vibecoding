# Log — P205

## S01.P205.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se delimitó calibración/priorización como análisis predictivo, no política crediticia.

## S01.P205.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:**
  `implementation/predictiva/P205_priorizacion_con_probabilidades/` (notebook,
  entrada simulada, tres tablas y pruebas) y P205 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato actual de S01 y se añadieron highlights
  para calibración, consecuencias de umbral, frontera con política, revisión
  por grupo y persistencia; se incorporó la naturaleza simulada del dataset y
  los tamaños desiguales de sus dos grupos.
- **Auditoría de Analytics:** el producto es evidencia predictiva previa a una
  priorización; no define una política prescriptiva real.

## S01.P205.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05 y se documentaron superficies, contrato de
  evidencia y dependencia comprobada con P204; no se inventó una dependencia
  técnica con los talleres posteriores.

## S01.P205.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H05 con superficies existentes. Se preservó el límite entre evidencia predictiva simulada y política crediticia.
- **Auditoría de Analytics:** calibración y umbrales sirven a evidencia previa, no a una política prescriptiva real.

## S03.P205.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - falsos positivos/negativos y precision/recall (p. 9): ya cubierta (H02: conteos y costos por umbral).

## S03.P205.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - supervisión y criterio humano, tolerancia al riesgo, gobernanza (pp. 5–6): ya expresan el límite que H03 traza entre probabilidad/umbral y política, pero no cambian materialmente la capacidad de P205 para revisar probabilidades simuladas; tampoco justifican crear una política con datos ficticios. Se conserva la identidad Predictiva, no se convierte la actividad en Prescriptiva.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.

## S03.P205.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sesgos algorítmicos (p. 5): ya cubierta en la medida que el caso permite (H04: revisión por grupo simulado, sin inferir equidad).
  - supervisión humana, tolerancia al riesgo y gobernanza (pp. 5–6): ya cubierta como frontera entre umbral y política (H03).
  - gestión de riesgos como capacidad de IA (p. 2): ya cubierta (H02: consecuencias de umbrales con costos).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P205.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sensibilidad, especificidad y costo de errores (T1, p. 97): ya cubierta (H02).

## S03.P205.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - medidas de éxito ligadas a la decisión e identificación de riesgos (Tasks 2.4, 2.6, pp. 4–5): ya cubierta (H02–H03: costos de error y frontera con política).

## S03.P205.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sesgo más probable de un modelo predictivo y causa de resultados sesgados o no éticos (Tasks 2.6, 5.3, pp. 12, 20): ya cubierta en la medida que el caso lo permite (H04: revisión por grupo simulado).

## S03.P205.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - causa de resultados sesgados o no éticos de un modelo predictivo (CAP-P.5.3.5, p. 20): ya cubierta en la medida que el caso lo permite (H04).

## S03.P205.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - capacidad de detectar sesgo algorítmico (p. 52): ya cubierta en la medida que el caso lo permite (H04).

## S03.P205.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calibración de modelos» y «Analítica de riesgos» demandadas (Tabla 35, p. 97): ya cubierta (H01–H02).
  - Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.

## S03.P205.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un proyecto de inversión pública de bootcamps (159 horas) en ejes temáticos genéricos (análisis de datos, IA, programación, nube, blockchain; pp. 1–3); no contiene contenidos, prácticas ni competencias que contrastar con esta actividad.

## S03.P205.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo de un curso de ingeniería de datos (p. 1): ciclo de vida de gestión de datos a escala; sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P205.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - decisión frecuentista y bayesiana, tasa de falsos descubrimientos (p. 1): marginal; el documento sólo enumera los temas, y P205 ya conecta probabilidad, umbral y consecuencias (H02).

## S03.P205.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Conectar el análisis predictivo con un objetivo empresarial» (módulo prescriptivo, p. 8): ya cubierta como frontera entre umbral y política (H02–H03); el resto del módulo es prescriptivo.

## S03.P205.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de computación en la nube y DevOps (temario, pp. 12–14: web, Node.js, contenedores, PKI, métricas DevOps, casos de migración); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P205.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sesgo y equidad en IA (módulo 8, p. 14): ya cubierta en la medida que el caso lo permite (H04); el folleto sólo nombra el tema.

## S03.P205.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de diseño de productos de IA (módulos, pp. 4–5: proceso de diseño, panorama de algoritmos de ML y deep learning, interacción humano–máquina, organizaciones «superminds», GANs); no detalla prácticas de modelado o evaluación que contrastar con esta actividad.

## S03.P205.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de estrategia de plataformas digitales y mercados de dos lados (temario, pp. 13–15: efectos de red, precios, arquitectura, gobierno de calidad); sin contenidos de modelado predictivo.

## S03.P205.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de modelado y simulación (ODE, PDE, optimización); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P205.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado de ingeniería de datos (módulos, pp. 10–11: Python, SQL, contenedores, CDC, almacenes de datos, procesamiento distribuido); para esta actividad no añade señales.

## S03.P205.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - equidad y sesgo en predicciones basadas en datos; caso de algoritmos de análisis facial (módulo 16, pp. 8, 10): ya cubierta en la medida que el caso lo permite (H04); el folleto no detalla métodos.
