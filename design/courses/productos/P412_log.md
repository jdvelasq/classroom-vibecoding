# Log — P412

## S02.P412.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P412_repro_environment/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `data/daily_operations.csv`, `professor/main.py`, `src/main.py`, `submission/environment_report.json`, `tests/test_activity.py`, `tests/test_environment_report.py`); `structure-audit.md`; P400 para comparación.
- **Trazabilidad revisada:** P412 → `productos.C02`, `productos.C05`. C05 débil.
- **Highlights:** añadidos H01 (ambiente aislado), H02 (procedencia de ejecución), H03 (prueba de regresión), H04 (caso y datos: indicador fijo de referencia y contrato de salida inestable).
- **Ambigüedades:** `requirements.txt` local no registrado como excepción en `structure-audit.md` y compatibilidad con la raíz no verificable; Python 3.9.6 en la evidencia sin versión de referencia del repositorio; docstrings descriptivos frente a la regla de claridad de `AGENTS.md`; columna `total_units_produced` frente a `total_units` de P400; la prueba sobrescribe `submission/`.
- **Superficies / contrato / dependencias:** S01–S07; recibe de P400; habilita P413–P414.
- **Auditoría de Analytics:** resuelta con reservas: reproducibilidad de un indicador real del curso, pero trivial.

## S03.P412.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).

## S03.P412.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P412.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P412.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.4.4.2 «Identify the weaknesses of a spreadsheet analytics model» (p. 18) — marginal: motivación posible para la ejecución reproducible de P412 (H01–H03), sin cambio en lo que el estudiante hace.

## S03.P412.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - hechos conformados: misma definición ⇒ mismo nombre; definiciones incompatibles ⇒ nombres distintos (p. 7) — marginal como propuesta de aprendizaje: S02 ya registra el defecto de consistencia (P412 H04: `total_units` frente a `total_units_produced`, «el contrato de salida del mismo indicador no es estable entre actividades»); su corrección es higiene de implementación. Puede citarse como fuente si se propone uniformar el contrato del indicador por fábrica.
  - sellos de tiempo de ejecución y versiones del entorno como metadatos de auditoría (p. 23) — ya cubierta en parte: P405 H01 (ciclo de vida de la ejecución) y P412 H02 (versiones de dependencias); lo que falta (versión de la lógica ligada a la salida) se recoge en la candidata de P443.

## S03.P412.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Reproducible analysis» (p. 47); «Documenting and sharing workflows enable others to understand how data have been used and refined» (pp. 46–47) — ya cubierta: P412 H01–H03 (ambiente y procedencia), P414 H01, P419 H01.

## S03.P412.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Estudio de política pública que cuantifica la brecha de talento TI en Colombia y la pertinencia de la oferta educativa. Para Productos de datos su valor es de pertinencia laboral: escasez de perfiles DevOps/SRE/MLOps y una brecha formativa en prácticas de producción (CI/CD real, rollback, secretos, monitoreo de deriva, seguridad). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P412.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de un proyecto de inversión pública: bootcamps de 159 horas para formar al menos 94.696 personas en programación, IA, análisis de datos, blockchain, arquitectura en la nube y ciberseguridad, con cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
