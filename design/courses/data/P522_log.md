# Log — P522

## S02.P522.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P522_mapreduce_multiprocessing/` (`data/flights.csv.gz` sólo como binario, `professor/main.py`, `src/main.py`, `submission/origin_flights.csv`, `submission/benchmark.csv`, `tests/test_activity.py`); P519–P521 y P524 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P522 → `data.C02`, `data.C05`; C03 (filtro de cancelados) no mapeado; C05 tensionado.
- **Highlights:** añadidos H01 (filtro de cancelados en el mapper; caso y datos), H02 (reducción en dos niveles), H03 (equivalencia secuencial–paralela), H04 (medición de aceleración).
- **Ambigüedades:** sin pregunta analítica; procedencia y periodo de vuelos no documentados; `temp/` no aparece en la implementación y `TEMP_DIR / "input"` se crea con `mkdir()` sin `parents` (posible fallo de ejecución); benchmark de una corrida dependiente del equipo; sin notebook de profesor; P522 no figura en el diseño del bloque MapReduce de `case-selection.md`, que llega sólo a P521.
- **Superficies / contrato / dependencias:** S01–S07; recibe operadores de P519; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; lectura de computación paralela/Big Data sin producto analítico.

## S03.P522.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - BDS-Problems of Scale (p. 56: «Execute a computational task at multiple scale-levels»), BDS-Big Data Computing Architectures (pp. 56–57, E), BDS-Parallel Programming (p. 59: «load balancing issues»; «Evaluate a parallel algorithm’s load-balance») y BDS-Techniques (pp. 59–60: hashing, sampling, «Be attentive of pitfalls such as bias in performing sampling and filtering») — fuera de alcance: medición de aceleración, particionamiento, sesgo de carga y combiner son contenido T2/E de Big Data Systems, área que `s05-diseno-data.md` excluye; el documento refuerza las auditorías no resueltas de S02 y no justifica ampliar ese bloque.

## S03.P522.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P522.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.7 las 4 V (p. 14) — marginal: concepto de reconocimiento; no justifica reforzar el bloque de procesamiento cuya identidad ya está en duda.

## S03.P522.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P522.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P522.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «distributed data storage, multicore processing, and parallel computation» (p. 87) — fuera de alcance: frontera explícita del curso (operaciones distribuidas). El documento lo trata como infraestructura del programa, no como resultado de un curso de fundamentos.

## S03.P522.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «escasez de profesionales con experiencia práctica en procesamiento distribuido de datos a escala» con Spark, Hadoop, Kafka (p. 175); Analista Big Data que domina «Hadoop/Spark, bases de datos NoSQL, streaming» (p. 291). Categoría: fuera de alcance. Operaciones distribuidas están excluidas por `s05-diseno-data.md` y `case-selection.md` («No introducen PySpark, RDD, Pig, Hive»); reforzarlo agravaría el riesgo de identidad ya registrado en P522–P523.

## S03.P522.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
