# Log — P400

## S02.P400.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P400_code_testing_unittest/` (`data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_totals.csv`, `tests/test_activity.py`); contexto en `s05-diseno-productos.md` y `structure-audit.md`.
- **Trazabilidad revisada:** P400 → `productos.C02`, `productos.C05`. C05 sin evidencia observable.
- **Highlights:** añadidos H01 (regla aislada), H02 (prueba `unittest`), H03 (caso y datos: ausencia de particularidad como límite).
- **Ambigüedades:** la prueba de lógica vive en `professor/` y no forma parte de la evaluación; no hay `HOW_TO_RUN_ME.txt` ni notebook para el estudiante; el dato no tiene procedencia y la variable `daily_units_produced` no tiene fecha.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; la prueba de evaluación sólo verifica existencia; habilita P408 y P412–P414 por reutilización del indicador y del archivo.
- **Auditoría de Analytics:** no resuelta. El indicador es trivial y sin usuario; la actividad se lee como práctica genérica de pruebas unitarias (pregunta 5).

## S03.P400.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).
- **Señales de alcance de curso** (registradas sólo en este log):
  - DPSIA/DS y DP-Cryptography/Communication Protocols (pp. 84–89: cifrado, PKI, modelos de amenaza, árboles de ataque), DG-Data Privacy (p. 74: GDPR, HIPAA, leyes transfronterizas), PR-Intellectual Property (pp. 109–110) — fuera de alcance: ciberseguridad y derecho; no hacen operable una capacidad analítica concreta.
  - DPSIA/AS (pp. 92–94: ML para telemetría de seguridad, aprendizaje adversarial, LIME) y PR-Ethical (p. 108: sesgo en datos y algoritmos) — fuera de alcance: métodos analíticos y evaluación de modelos (Predictiva) y aplicación de dominio.
  - BDS-Cloud Computing y Software Support (pp. 60–61: diseño de centros de datos, «Concepts of auto scaling and serverless computing») — fuera de alcance: frontera explícita (no Big Data ni cloud engineering).
  - SDM-Software Design (p. 121: «Execute a basic Data (Science) Lifecycle on a simple data product»; mentalidad de ciclo de vida) y AP-User-centred design (p. 47: «Diagram the life of an interface, dashboard, or visualization including long-term use and maintenance») — ya cubierta a nivel de curso: es la pregunta organizadora de productos (C01–C05); no aporta mecanismo nuevo.
  - DG-Data Acquisition/Integration/Reduction/Transformation (pp. 70–73) — fuera de alcance: pertenecen a Fundamentos de data; el curso no vuelve a preparar datos.

## S03.P400.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** aporta a N01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Dominios I, II, IV y V (p. 4–6: encuadre del problema de negocio y del problema analítico, selección de método, desarrollo del modelo) — fuera de alcance: pertenecen a Fundamentos, Descriptiva, Predictiva y Prescriptiva; el curso no vuelve a formular ni a modelar el problema.
  - Task 7.3 «Support training activities» (p. 7) — fuera de alcance: capacitación de usuarios; no hay caso ni producto analítico que la haga enseñable con rigor en un taller.
  - Task 7.5 «Analyze the side effects of the analytics solution over time» (p. 7) — fuera de alcance por ahora: exige una capacidad en operación con historia de efectos (bucles de retroalimentación, efectos no previstos) que ningún caso del curso tiene; podría retomarse si P451 alimentara una mejora real.
  - Task 4.3/4.4 arquitectura y stack tecnológico (p. 6) — fuera de alcance: arquitectura empresarial y elección de plataforma, que son fronteras explícitas del curso.

## S03.P400.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Support training activities» (p. 25, CAP-E.7.3.1) — fuera de alcance: capacitación de audiencias, no operación de la capacidad.
  - dominios I–V (encuadre del problema de negocio y analítico, datos, selección de método, desarrollo de modelos; pp. 7–21) — fuera de alcance: responsabilidades de Fundamentos, Descriptiva, Predictiva y Prescriptiva según las fronteras del curso.

## S03.P400.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Temario del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con tareas y subtareas evaluables (pesos: Deployment 10 %, Lifecycle Management 9 %). Sólo los dominios VI–VII y algunas subtareas de III (linaje, gobierno, calidad) tocan la operación de capacidades. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Task 6.4 «Create requirements for a deployed analytics solution including model, usability, system, and business» (p. 23); CAP-P.6.4.1 «Identify what is missing or does not belong in an outline of the requirements of a production system» — marginal: los elementos del contrato operativo ya se acumulan en la tarjeta de producto (P408 H01, P409 H02 consumidor, P411 H02 responsable), el contrato de API (P425 H01), la compatibilidad de contrato (P434 H01), el nivel de servicio (P445) y la ficha de catálogo (P454 H01). Añadir campos a la tarjeta no cambia la contribución (Git) de P408–P411; la falta de mapeo de C01 es una decisión de curso ya registrada en S02 (P425, P434, P445).
  - Task 7.3 «Support training activities»; CAP-P.7.3.1 «type of training that is needed for an IT audience» (p. 25) — fuera de alcance: gestión del cambio/capacitación, no operación de la capacidad.
  - CAP-P.4.4.1 fortalezas y debilidades del stack «on-premise, cloud, open source vs. proprietary, platforms» (p. 18) — fuera de alcance: selección de plataforma/cloud engineering, excluida por las fronteras del curso.
  - CAP-P.2.6.2 y CAP-P.5.3.5 sesgo en datos de entrenamiento y resultados no éticos (pp. 12, 20) — fuera de alcance: método predictivo de origen.

## S03.P400.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Catálogo «oficial» de técnicas de modelado dimensional del Kimball Group (Toolkit, 3.ª ed.): proceso en cuatro pasos, grano, hechos y dimensiones, dimensiones lentamente cambiantes (tipos 0–7), jerarquías, técnicas avanzadas y, como preocupaciones operativas del back room ETL, hechos tardíos, dimensiones tardías, dimensión de auditoría y esquemas de eventos de error. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - dimensiones lentamente cambiantes tipos 0–7 (pp. 15–16: tipo 1 «destroys history»; tipo 2 con «row effective date … row expiration date … current row indicator») — fuera de alcance: el diseño de historia de atributos es modelado dimensional (Fundamentos de data / Descriptiva). Como preocupación operativa (un agregado publicado cambia según se reporte «as-was» o «as-is»), no existe en el curso un atributo de referencia que cambie (p. ej., reasignación de máquina a fábrica) y crear uno sería un dato sintético por conveniencia; sólo se recuperó la consecuencia operativa (reexpresar agregados) en la candidata de P438.
  - arquitectura de bus, matriz de bus y matriz oportunidad/interesados (pp. 13–14), agregados y navegación de agregados (p. 8), tablas de hechos en tiempo real con «hot partition» (p. 24), monedas y unidades múltiples (p. 19) — fuera de alcance: arquitectura empresarial de datos y diseño físico de bodegas, excluidos por las fronteras del curso.
