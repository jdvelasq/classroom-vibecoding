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
