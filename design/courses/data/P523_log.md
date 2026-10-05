# Log — P523

## S02.P523.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P523_mapreduce_particionamiento/` (`data/truck_events.csv.gz` sólo como binario, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/partition_loads.csv`, `submission/shuffle_comparison.csv`, `tests/test_activity.py`); P519 y P522 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P523 → `data.C02`, `data.C03`, `data.C05`; C03 no sustentado (sesgo de carga, no de evidencia), a escalar.
- **Highlights:** añadidos H01 (sesgo por clave; caso y datos), H02 (particionador determinista), H03 (agregación local, con defecto de modelado).
- **Ambigüedades:** el «combiner» se indexa por partición de destino y su cifra (5) equivale a la salida final, no a pares enviados al shuffle; `hot_key_load` es carga de partición, no de una clave; operadores de P519 copiados sin uso; semántica de `eventKey` y procedencia no documentadas; P523 no figura en el diseño de `case-selection.md`.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P522; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; internos de procesamiento distribuido sin producto analítico.

## S03.P523.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - BDS-Problems of Scale (p. 56: «Execute a computational task at multiple scale-levels»), BDS-Big Data Computing Architectures (pp. 56–57, E), BDS-Parallel Programming (p. 59: «load balancing issues»; «Evaluate a parallel algorithm’s load-balance») y BDS-Techniques (pp. 59–60: hashing, sampling, «Be attentive of pitfalls such as bias in performing sampling and filtering») — fuera de alcance: medición de aceleración, particionamiento, sesgo de carga y combiner son contenido T2/E de Big Data Systems, área que `s05-diseno-data.md` excluye; el documento refuerza las auditorías no resueltas de S02 y no justifica ampliar ese bloque.

## S03.P523.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.7 las 4 V (p. 14) — marginal: concepto de reconocimiento; no justifica reforzar el bloque de procesamiento cuya identidad ya está en duda.

## S03.P523.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «distributed data storage, multicore processing, and parallel computation» (p. 87) — fuera de alcance: frontera explícita del curso (operaciones distribuidas). El documento lo trata como infraestructura del programa, no como resultado de un curso de fundamentos.

## S03.P523.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «escasez de profesionales con experiencia práctica en procesamiento distribuido de datos a escala» con Spark, Hadoop, Kafka (p. 175); Analista Big Data que domina «Hadoop/Spark, bases de datos NoSQL, streaming» (p. 291). Categoría: fuera de alcance. Operaciones distribuidas están excluidas por `s05-diseno-data.md` y `case-selection.md` («No introducen PySpark, RDD, Pig, Hive»); reforzarlo agravaría el riesgo de identidad ya registrado en P522–P523.

## S03.P523.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P523.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
