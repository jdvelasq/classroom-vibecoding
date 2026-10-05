# Log — P437

## S02.P437.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P437_late_arriving_data/` (`data/arrival.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/arrival_classification.json`, `tests/test_activity.py`); P436 y P438 para relación.
- **Trazabilidad revisada:** P437 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (evento frente a procesamiento; caso y datos), H02 (acción de reproceso).
- **Ambigüedades:** `arrival_date` se lee pero no interviene; todo evento pasado es «tardío»; sin ventana de tolerancia; reproceso no ejecutado; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; relaciones conceptuales con P436 y P438.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): patrón genérico sin indicador afectado.

## S03.P437.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P437.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P437.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P437.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.6.6.1 «Identify causes of incorrect data in production systems» (p. 23) — ya cubierta: contrato de datos (P402), compatibilidad de entradas (P404), registros tardíos (P437), frescura (P439), conciliación (P440), cuarentena (P441), observabilidad integrada (P442).

## S03.P437.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - hechos tardíos (p. 20: «the relevant dimensions must be searched to find the dimension keys that were effective when the late arriving measurement event occurred») — el principio operativo (asignar el registro según el instante del evento, no el de procesamiento) ya está cubierto por P437 H01; la búsqueda de claves sustitutas vigentes en una dimensión versionada es modelado dimensional, fuera de alcance (el curso no tiene dimensiones versionadas ni debe construirlas).
  - dimensiones tardías con fila provisional «unknown» que luego se sobrescribe con tipo 1 (p. 23: «special dimension rows are created with the unresolved natural keys as attributes … updated with type 1 overwrites») — fuera de alcance: alternativa de diseño físico a la cuarentena que exige un esquema estrella; el contraste «publicar con contexto desconocido frente a retener» sería interesante pero no hay caso ni datos en el curso que lo sostengan con rigor.

## S03.P437.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Marco de pregrado que define la «data acumen» (diez áreas conceptuales) y recomienda que la ética y la reproducibilidad atraviesen el currículo; trata el flujo de trabajo y la gestión de datos como competencias generales, no la operación de productos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
