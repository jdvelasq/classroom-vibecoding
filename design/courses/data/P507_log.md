# Log — P507

## S01.P507.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`.
- **Estado:** inicial. Se inspeccionaron datos, notebooks, entregables, pruebas
  y trazabilidad.
- **Decisión:** se creó mapa inicial y se conservó la distinción entre respuesta
  observable y técnica de consulta pendiente de validar.

## S02.P507.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P507_scopus_sql_analitico/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`); normalización de palabras clave en `implementation/data/P503_scopus_relacional/professor/notebook.ipynb`.
- **Trazabilidad revisada:** P507 → `data.C01`, `data.C02`, `data.C03`, `data.C05`; C03 sin evidencia.
- **Preservado:** pregunta, entregable, combinación de condición temporal con conteo por año y palabra clave.
- **Completado:** se confirmó la consulta pendiente (dos CTE y `ROW_NUMBER` particionado por año, top 10); pruebas sólo de existencia; notebook del estudiante sin celdas.
- **Highlights añadidos:** H01 (ventana por año), H02 (palabras clave de autor y empates; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** empates de baja frecuencia ordenados alfabéticamente; términos de búsqueda en el ranking; join redundante con `keywords`; el notebook alude a una visualización inexistente.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P503–P506; no habilita una actividad posterior de forma demostrable.
- **Auditoría de Analytics:** descripción temática anual; riesgo moderado de lectura como lección de funciones de ventana.

## S03.P507.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P507.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P507.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P507.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - sesgo de la fuente (p. 15 «CAP-P.3.4.1 Identify the techniques appropriate in acquiring the data and identify data source bias») — marginal: la pertinencia del corpus recuperado y la presencia de términos de búsqueda en el ranking ya están escaladas en S02 (P503 auditoría; P507 S01); el documento no aporta caso ni método concreto para enseñarlo.

## S03.P507.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P507.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - considerar si los datos disponibles son apropiados para la pregunta (p. 39) y los datos observacionales como «found artifacts» no aleatorios (p. 44), aplicados a la pertinencia del corpus Scopus — ya cubierta en lo esencial (P503 H01 consulta preservada, P504 H03 heterogeneidad documental, P507 H02 palabras clave que condicionan el ranking). Ampliar a la evaluación estadística de selección es fuera de alcance (Estadística o Descriptiva).
