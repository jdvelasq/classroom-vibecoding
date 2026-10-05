# Log — P206

## S01.P206.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró clustering de demanda como rama no supervisada.

## S01.P206.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P206_clustering_demanda/`
  (notebook de profesor, selección, perfiles, asignación y pruebas) y P206 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights para el caso de demanda horaria: separar
  forma y nivel, definir el día como perfil, elegir clusters con silueta,
  interpretar centroides sin causalidad y asignar un perfil persistido.
- **Límite:** la normalización elimina nivel absoluto; la actividad no pronostica
  demanda ni define capacidad operativa.

## S01.P206.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05 y se declararon superficies de serie,
  clustering y producto, con contrato de evidencia y dependencia comprobada
  hacia P207.

## S01.P206.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Corrección:** H02 declara ahora la orientación filas=días, columnas=horas y
  su consecuencia interpretativa: cada cluster es un arquetipo de forma diaria,
  no una agrupación de horas individuales ni un pronóstico.

## S01.P206.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H05 con superficies actuales; se mantuvo que el clustering describe patrones, no pronostica demanda.
- **Auditoría de Analytics:** normalización y clustering sirven al producto descriptivo limitado del taller.

## S03.P206.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - K-means, evaluación de clustering, otras distancias y preprocesamiento (p. 7): ya cubiertas (H01–H03).
  - clustering espectral y de modularidad (p. 7): marginal; otro algoritmo para la misma segmentación.

## S03.P206.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): señal relevante para la identidad Predictiva que S02 dejó sin resolver en esta actividad, cuyo producto actual es descriptivo; el documento sólo enuncia la distinción, sin caso ni criterio para resolverla. Queda como insumo para la decisión de curso, no como propuesta.
  - optimización de cadena de suministro y robótica (pp. 2, 5): fuera de alcance; P206 produce una descripción de perfiles diarios, no estimación futura ni política. Reorientarlo exigiría un producto distinto y datos/decisión de operación no presentes en el S02.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; se añadió la señal «analítica descriptiva frente a predictiva» (p. 5), omitida en la entrada original.

## S03.P206.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): toca la identidad Predictiva que S02 dejó sin resolver; el producto actual es una segmentación descriptiva de perfiles de demanda (H04). El documento sólo enuncia la distinción, sin caso ni criterio; queda como insumo para la decisión de curso.
  - aprendizaje no supervisado (p. 5): ya cubierta (H01–H05).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P206.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad del clustering y selección del número de grupos (T1, p. 100; DM-Cluster Analysis): ya cubierta (H03).
  - clustering basado en densidad (DM, T1): marginal; otro algoritmo para la misma segmentación.

## S03.P206.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reformular el problema como descriptivo, predictivo o prescriptivo (Domain II, p. 4): toca la identidad sin resolver de P206 (producto descriptivo); el documento no aporta criterio para resolverla.

## S03.P206.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de los métodos descriptivos frente a predictivos (Task 4.1, p. 17): toca la identidad sin resolver (producto descriptivo); sin criterio para resolverla.

## S03.P206.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel intermedio detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P206.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el informe define áreas de conocimiento a nivel de programa (fundamentos, datos, modelado, flujo de trabajo, comunicación, ética); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P206.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Segmentación de datos» y «Perfiles y arquetipos» aparecen como habilidades demandadas de «Modelado y analítica» (Tabla 35, p. 97): respaldo de pertinencia laboral para la segmentación descriptiva (H04: arquetipos diarios); no resuelve su identidad Predictiva.
  - Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.

## S03.P206.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un proyecto de inversión pública de bootcamps (159 horas) en ejes temáticos genéricos (análisis de datos, IA, programación, nube, blockchain; pp. 1–3); no contiene contenidos, prácticas ni competencias que contrastar con esta actividad.

## S03.P206.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo de un curso de ingeniería de datos (p. 1): ciclo de vida de gestión de datos a escala; sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P206.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - algoritmos de clustering (p. 1): ya cubierta (H03).

## S03.P206.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo sin código (p. 2); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P206.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de computación en la nube y DevOps (temario, pp. 12–14: web, Node.js, contenedores, PKI, métricas DevOps, casos de migración); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P206.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso ejecutivo de liderazgo de datos (temario, pp. 13–14: IA para líderes, marcos de innovación, SQL y arquitectura, plataformas de datos, nube, ética y gobierno); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P206.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de diseño de productos de IA (módulos, pp. 4–5: proceso de diseño, panorama de algoritmos de ML y deep learning, interacción humano–máquina, organizaciones «superminds», GANs); no detalla prácticas de modelado o evaluación que contrastar con esta actividad.

## S03.P206.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de estrategia de plataformas digitales y mercados de dos lados (temario, pp. 13–15: efectos de red, precios, arquitectura, gobierno de calidad); sin contenidos de modelado predictivo.

## S03.P206.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de modelado y simulación (ODE, PDE, optimización); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P206.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - k-means con scikit-learn (p. 10): ya cubierta (H03).

## S03.P206.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado de ciencia de datos y analítica (currículo, pp. 7–9); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P206.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de ingeniería de sistemas orientada al valor (semanas 1–4: modelos de valor, generación y evaluación de alternativas, exploración de *tradespace* bajo incertidumbre); es contenido de decisión multicriterio, propio de Prescriptiva; sin señales para esta actividad.

## S03.P206.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de prototipado físico rápido y fabricación (módulos 1–5); sin contenidos de analítica predictiva.

## S03.P206.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - currículo de una academia corporativa de analítica (pp. 4–8); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P206.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa para altos ejecutivos sobre estrategia y gobierno de IA (fases I–V: modelos de negocio, liderazgo, innovación, gobierno y controles); trata la analítica predictiva sólo como capacidad organizacional que el líder integra; sin señales para esta actividad.

## S03.P206.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado profesional de ciencia de datos para negocios (estructura de contenidos, pp. 4–5); para esta actividad no añade una señal distinta de las ya registradas.

## S03.P206.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica (Sede Manizales) sobre la ruta de armonización curricular: acreditación por logros (Acuerdo 02 de 2020 del CESU), resultados de aprendizaje, PEP y planes de mejoramiento (pp. 1–4); opera en el nivel de programa y de proceso, sin contenidos que contrastar con esta actividad. La noción de resultados de aprendizaje es pertinente para la trazabilidad del curso (`traceability.yaml`), no para un cambio de taller.

## S03.P206.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - memoria del ejercicio piloto de armonización curricular de la UNAL (contextos, dinámicas, prácticas pedagógicas y proyecciones, construidos en talleres con la comunidad académica). Lectura: estructura completa y capítulo de prácticas pedagógicas (pp. 67–94); el documento trata fines formativos, integración docencia–investigación–extensión y participación en el nivel institucional, sin contenidos ni prácticas de analítica predictiva que contrastar con esta actividad.

## S03.P206.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sílabo de posgrado en analítica de datos de salud (calendario, pp. 9–10: preprocesamiento, exploración, probabilidad, regresión, patrones frecuentes, clasificación y predicción, clustering), con evaluación basada en un proyecto de minería de datos por entregas y un artículo de revisión; los temas coinciden con los ya cubiertos y el formato de proyecto integrador es una decisión de curso, no de esta actividad.
