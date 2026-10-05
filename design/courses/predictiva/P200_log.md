# Log — P200

## S01.P200.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se mapearon preparación, regresión, comparación y artefactos persistentes.

## S01.P200.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P200_regresion_basica/`
  (notebook de profesor, datos, `submission/` y pruebas) y la entrada P200 de
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights que separan contribuciones observables:
  tipado y tratamiento de entradas, aislamiento entrenamiento/prueba,
  especificaciones lineales, MLP, comparación fuera de muestra y persistencia
  conjunta de transformadores y modelos. No se modificó la implementación ni
  se añadieron mejoras pendientes.

## S01.P200.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se precisaron dos highlights: `OneHotEncoder` como método para
  representar categorías nominales, y el contraste aislado entre regresión
  lineal y MLP usando sólo `Horsepower`. La comparación persistida sustenta MSE
  de prueba 22.03 y 15.60, respectivamente.

## S01.P200.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P200_regresion_basica/`
  (notebook de profesor, `submission/model_comparison.csv` y pruebas) y P200
  en `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato reescrito de S01: cada highlight quedó
  contrastado contra una ruta y con su límite de inferencia. Se confirmó la
  granularidad de semántica categórica, preprocesamiento sin filtración,
  especificaciones lineales, contraste de MLP de una entrada y persistencia.
- **Auditoría de Analytics:** el producto permanece como estimación verificable
  de MPG; preprocesamiento, regresión y MLP contribuyen a ese producto y no
  reorganizan la actividad como un curso introductorio de ML.

## S01.P200.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se asignaron IDs estables H01–H10 y se documentaron superficies
  de cambio, contrato de evidencia y dependencias demostrables para que futuras
  propuestas de benchmarks puedan afectar un componente concreto.

## S01.P200.06

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se declaró el producto predictivo, se añadió el índice externo y se vinculó H01–H10 con superficies existentes; se preservaron implementación y mejoras pendientes.
- **Auditoría de Analytics:** regresión, MLP y preprocesamiento sirven a estimar MPG verificablemente.

## S03.P200.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios; aporta a N01 (árboles y ensambles).
- **Señales descartadas relevantes:**
  - regresión lineal con una y varias variables (p. 8): ya cubierta (H01, H04, H07–H09).
  - regresión para inferencia causal, RCT y confusión (p. 8): fuera de alcance; la inferencia causal no es el producto de Predictiva y P200 ya declara el límite causal.
  - árboles, Random Forest y boosting (p. 8): se descartó incluirlos en P200 por la carga del primer taller; se proponen como actividad nueva N01.

## S03.P200.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje supervisado y entrenamiento/validación/prueba (p. 5): ya cubiertos (H03: partición reproducible sin filtración).
  - calidad de datos, representatividad y por qué fallan los modelos (p. 5): no cubierta como capacidad en esta actividad ni en el curso (ningún taller trata representatividad o cambio de distribución entre entrenamiento y uso); no sustentada como propuesta por este documento, que sólo la enuncia en un programa ejecutivo. Señal a contrastar con fuentes *authoritative*.
  - aprendizaje profundo y redes neuronales (p. 5): marginal; P200 ya contrasta MLP con regresión para la predicción cuantitativa del caso (H08–H09), y añadir otra arquitectura no cambiaría qué aprende el estudiante a producir.
  - casos de estrategia y creación de valor de IA (pp. 5–6): no anclan mejora a P200; su producto estima MPG, sin una decisión de flota ni caso organizacional de adopción de IA definido.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; se separó «calidad/representatividad» de «entrenamiento/validación/prueba»: la primera no está cubierta por H02–H03 (nulos y fuga de información), como afirmaba la entrada.

## S03.P200.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - aprendizaje supervisado; entrenamiento, validación y prueba (p. 5): ya cubierta (H03: partición reproducible sin filtración).
  - calidad de datos, representatividad y «por qué fallan los modelos» (p. 5): no cubierta; ningún taller del curso trata representatividad ni cambio de distribución entre entrenamiento y uso. No sustentada como propuesta por este documento (un enunciado en un programa ejecutivo sin método ni caso); señal a contrastar con fuentes *authoritative*.
  - del ML tradicional a redes neuronales (p. 5): ya cubierta (H08–H09: MLP contrastada con regresión sobre la misma partición).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P200.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - árboles y ensambles como extensión supervisada T1 (pp. 97–98): se suman como fuente a N01; incluirlos en P200 sobrecargaría el primer taller.
  - sesgo/varianza y curvas de aprendizaje (T2, p. 98): parcialmente cubierta (H08–H09 contrastan capacidad con MSE de prueba); se recoge en el criterio de N01 (sobreajuste con la profundidad).
  - comparación de modelos con bootstrap (T2, p. 97): se propone en P204 (T01), donde las diferencias entre especificaciones son mínimas; en P200 la diferencia MLP–lineal (15.60 frente a 22.03) es grande.
  - representatividad de los datos («truly representative», PR p. 108; BDS p. 58): fuente *authoritative* que confirma la señal ya registrada; sigue sin una competencia técnica concreta (método, evaluación) que permita anclarla a un taller.

## S03.P200.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01 (encuadre, medida de éxito y línea base ingenua).
- **Señales descartadas relevantes:**
  - documentación de supuestos y limitaciones del modelo (Task 5.6, p. 6): ya cubierta parcialmente en los límites declarados; T01 añade el encuadre explícito.

## S03.P200.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - encuadre, medidas de éxito y línea base del estado actual (Tasks 1.1–2.5, pp. 7–11): se añade como fuente de T01.

## S03.P200.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - medidas de éxito, línea base frente a desempeño esperado y explicación no técnica de resultados (CAP-P.2.4.2, 2.5.1, 5.6.1): se añade como fuente de T01.
  - riesgo de usar datos de entrenamiento sesgados (CAP-P.2.6.2, p. 12): confirma la señal de representatividad ya registrada; sin método ni caso que permita anclarla.

## S03.P200.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - formular buenas preguntas y entender las necesidades del cliente (pp. 40, 48): se añade como fuente de T01.
  - modelos que fallan cuando cambian los datos: «Google Flu Trends overpredicted… overreliance on outdated models» (p. 34) y relaciones que «will not necessarily hold in the next set of records» (p. 44): segunda fuente *authoritative* (con ACM) para la señal de representatividad y cambio de distribución; sigue sin método ni caso que permita anclarla a un taller.
  - «Model interpretation (particularly for black box models)» (p. 46): ningún taller interpreta modelos de caja negra (las MLP de P200 y P216 sólo se evalúan por error); el documento enuncia el concepto sin método ni caso. Se registra como señal de curso.

## S03.P200.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Análisis de negocio» y «Visión de negocio» como habilidades blandas de la capa ejecutiva (Tabla 36, p. 98): pertinencia general del encuadre de T01; no se añade como fuente porque no se refiere al encuadre de un producto predictivo.
  - Lectura: índice completo (371 págs.), brecha cualitativa (cap. 1 §5, pp. 95–105), percepciones de pertinencia curricular (cap. 2 §2.1.2, pp. 135–138), oferta en IA y ciencia de datos (pp. 204–206) y búsqueda de términos de analítica, ML y predicción en todo el texto; las tablas estadísticas regionales y salariales no se leyeron en detalle porque no contienen señales curriculares.

## S03.P200.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de un proyecto de inversión pública de bootcamps (159 horas) en ejes temáticos genéricos (análisis de datos, IA, programación, nube, blockchain; pp. 1–3); no contiene contenidos, prácticas ni competencias que contrastar con esta actividad.

## S03.P200.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ficha de catálogo de un curso de ingeniería de datos (p. 1): ciclo de vida de gestión de datos a escala; sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - árboles de decisión y métodos de ensamble (p. 1): se añade como fuente de N01.

## S03.P200.13

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - sobreajuste, árboles, bosques aleatorios, ensambles e interpretación (pp. 7–8): se añade como fuente de N01.
  - redes neuronales: cómo predicen y cómo elegir arquitectura (p. 8): ya cubierta en lo que el curso necesita (H08–H09).

## S03.P200.14

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de computación en la nube y DevOps (temario, pp. 12–14: web, Node.js, contenedores, PKI, métricas DevOps, casos de migración); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.15

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso ejecutivo de liderazgo de datos (temario, pp. 13–14: IA para líderes, marcos de innovación, SQL y arquitectura, plataformas de datos, nube, ética y gobierno); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.16

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - modelo de Lawler para definir un problema de IA y su caso organizacional (Week 8, p. 5): relacionado con el encuadre de T01, pero orientado al diseño de productos de IA y sin detalle; no se añade como fuente.

## S03.P200.17

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de estrategia de plataformas digitales y mercados de dos lados (temario, pp. 13–15: efectos de red, precios, arquitectura, gobierno de calidad); sin contenidos de modelado predictivo.

## S03.P200.18

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - regresión, regularización, regresión logística y evaluación del ajuste (módulo 5, p. 2): ya cubiertas en el curso (P200, P204, P219, P223).

## S03.P200.19

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - modelo de predicción de precios de vivienda con regresión lineal (módulos 7–8, p. 11): ya cubierta (H01–H09).

## S03.P200.20

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - árboles CART y aprendizaje por ensambles como modelos no lineales de regresión y clasificación (módulos 14–15, p. 8): se añaden como fuente de N01.
  - caso BlueBike: regresión para predecir demanda y R² para elegir el modelo (p. 10): ya cubierta (H04, H07–H09).
  - «Interpretability and Causality in Models» (módulo 22, p. 9): segunda fuente para la señal de interpretación de modelos (con National Academies); N01 recoge la lectura de importancia de variables de árboles y ensambles.

## S03.P200.21

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso de ingeniería de sistemas orientada al valor (semanas 1–4: modelos de valor, generación y evaluación de alternativas, exploración de *tradespace* bajo incertidumbre); es contenido de decisión multicriterio, propio de Prescriptiva; sin señales para esta actividad.

## S03.P200.22

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa de prototipado físico rápido y fabricación (módulos 1–5); sin contenidos de analítica predictiva.

## S03.P200.23

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - métodos basados en árboles y Random Forest (pp. 6, 8): se añaden como fuente de N01.
  - diagnóstico de regresión y diferencia entre modelos para inferencia estadística y para predicción (pp. 5, 8): marginal; P200 ya delimita que su producto es predictivo y no causal.

## S03.P200.24

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa para altos ejecutivos sobre estrategia y gobierno de IA (fases I–V: modelos de negocio, liderazgo, innovación, gobierno y controles); trata la analítica predictiva sólo como capacidad organizacional que el líder integra; sin señales para esta actividad.

## S03.P200.25

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Desarrollar una comprensión integral de la interpretación y evaluación del modelo» (curso 4, p. 5): tercera fuente para la señal de interpretación de modelos; sin método ni caso.
  - definir casos de negocio costo–beneficio y contar la historia a los interesados (curso 5, p. 5): relacionado con el encuadre de T01, pero orientado a comunicación; no se añade como fuente.

## S03.P200.26

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica (Sede Manizales) sobre la ruta de armonización curricular: acreditación por logros (Acuerdo 02 de 2020 del CESU), resultados de aprendizaje, PEP y planes de mejoramiento (pp. 1–4); opera en el nivel de programa y de proceso, sin contenidos que contrastar con esta actividad. La noción de resultados de aprendizaje es pertinente para la trazabilidad del curso (`traceability.yaml`), no para un cambio de taller.

## S03.P200.27

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - memoria del ejercicio piloto de armonización curricular de la UNAL (contextos, dinámicas, prácticas pedagógicas y proyecciones, construidos en talleres con la comunidad académica). Lectura: estructura completa y capítulo de prácticas pedagógicas (pp. 67–94); el documento trata fines formativos, integración docencia–investigación–extensión y participación en el nivel institucional, sin contenidos ni prácticas de analítica predictiva que contrastar con esta actividad.

## S03.P200.28

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto por entregas que parte de definir el problema y la propuesta (Deliverable 1, p. 6): coherente con el encuadre de T01, pero es formato de evaluación de curso; no se añade como fuente.

## S03.P200.29

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sílabo de introducción a la analítica centrado en bases de datos, SQL, NoSQL, BI y visualización (calendario, pp. 5–7); sin contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.30

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el `.md` sólo contiene encabezados repetidos de la página web impresa; el contenido está en imágenes, por lo que se consultaron directamente las páginas del PDF homónimo (pp. 1–12). Es un programa de 12 semanas sobre IA agéntica: LLM, ingeniería de *prompts*, RAG, agentes con herramientas y memoria (LangChain, MCP), sistemas multiagente y su evaluación. Queda fuera de la línea Predictiva; sin señales para esta actividad.

## S03.P200.31

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - árboles de decisión para clasificación (p. 1): se añade como fuente de N01.
  - regresión lineal, mínimos cuadrados y regresión logística (p. 1): ya cubiertas (P200, P201, P204).

## S03.P200.32

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Decision Trees» (p. 1): en este programa son árboles de análisis de decisión usados con optimización y simulación (prescriptivo), no árboles de aprendizaje; no se añade como fuente de N01.

## S03.P200.33

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el `.md` está vacío (PDF de una página en imagen); se consultó la página del PDF homónimo: módulos de analítica descriptiva, predictiva y prescriptiva de un programa ejecutivo. Para esta actividad no añade señales.

## S03.P200.34

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - CART, ensambles y gradient boosting como familias competitivas para datos tabulares (pp. 9, 25, 52): se añade como fuente de N01.

## S03.P200.35

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre los problemas reales de los proyectos de analítica (objetivos cambiantes, silos, calidad de datos, mitos como «el modelo es sabio y omnisciente»); el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.36

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - caso de valor de mantenimiento predictivo y conexión entre objetivos e iniciativas (pp. 7–9): orientado a estrategia organizacional; no se añade como fuente de T01.

## S03.P200.37

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - formular el problema de negocio, fijar línea base y criterios de éxito, y traducirlo en un problema analítico orientado a una decisión (pp. 9, 11): se añade como fuente de T01.

## S03.P200.38

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre pensamiento lean (Toyota, eliminación de desperdicios, mejora continua) aplicado a analítica; el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.39

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre colaboración ágil (Scrum, Kanban, XP, SAFe, manifiesto DataOps); el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.40

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre la definición de DataOps (DevOps, lean, cadena de suministro de datos, ciclo de vida de ciencia de datos, implementación de MLOps); el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.41

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre el rol del CDO y los silos entre equipos de datos; el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.42

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre DataOps para ingenieros y científicos de datos (arquitectura, reuso de código, deuda técnica, modelado tradicional frente a ML); el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.43

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - pruebas automáticas que verifican comportamiento y no sólo existencia (p. 2): S02 registra que las pruebas de esta actividad sólo comprueban presencia de artefactos. Es una señal sobre el contrato de evidencia del curso (cómo se verifica la entrega), no sobre lo que el estudiante aprende; se deja para una decisión de curso.

## S03.P200.44

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre estructuras organizacionales de equipos DataOps; el documento trata la organización y el proceso de los equipos de analítica (DataOps); no contiene contenidos de modelado predictivo que contrastar con esta actividad.

## S03.P200.45

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - criterios de éxito técnicos y de negocio definidos desde el alcance y comparación sistemática contra referencias en la evaluación (pp. 13–14, 18–19): se añade como fuente de T01.

## S03.P200.46

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - árboles de decisión (C5.0, CHAID, C&RT) en ejemplos aplicados (caps. 8, 9, 19): se añaden como fuente de N01.
  - modelado automático que compara muchas familias a la vez (caps. 4–5): marginal; P200 ya enseña a comparar especificaciones sobre la misma partición (H09).

## S03.P200.47

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - entendimiento del negocio, solución actual y criterios de éxito acordados antes de modelar (pp. 9–10): se añade como fuente de T01.
  - diseño de pruebas con partición entrenamiento/prueba (p. 30): ya cubierta (H03).

## S03.P200.48

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de inicio rápido de la interfaz de KNIME (instalación, nodos, flujos, metanodos, vistas); sin contenidos de analítica que contrastar con esta actividad.

## S03.P200.49

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - árboles de decisión y de regresión en la lista de algoritmos (p. 2): mención sin detalle; N01 ya tiene respaldo suficiente y no se añade como fuente.

## S03.P200.50

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios; aporta a N01.
- **Señales descartadas relevantes:**
  - árboles de decisión con reglas interpretables, confianza y soporte (pp. 27, 83–84): se añade como fuente de N01.
  - prueba de modelos de regresión con datos separados para construir y probar (p. 47): ya cubierta (H03).
