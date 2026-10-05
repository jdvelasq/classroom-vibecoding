# Log — P302

## S02.P302.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/` (`data/policy_options.csv`, `data/source.json`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, tres artefactos de `submission/`, `tests/test_activity.py`); relación con P300.
- **Trazabilidad revisada:** P302 → `prescriptiva.C01`, `C02`, `C04`; C02 débil (menú de tres repartos fijos).
- **Highlights:** añadidos H01–H05 (razón de descarte; piso activo sin cambiar la elección; procedencia en el producto; contrato JSON; excepción sin factibles).
- **Ambigüedades:** (1) las tres alternativas son factibles: la razón «no cumple capacidad o mínimo» y el `ValueError` nunca se ejercitan; (2) la alternativa ganadora, «solo_mayor_beneficio», está en el piso, mientras «prioridad_con_piso» se descarta por valor, lo que puede confundir la intención del producto previsto («asignación con garantía mínima»); (3) el gatillo usa asistencia por grado, ausente del caso; (4) la capacidad exige igualdad, no límite superior; (5) mecanismo de decisión casi idéntico al de P300: posible duplicación técnica.
- **Superficies / contrato / dependencias:** S01–S04; pruebas de existencia; recibe de P300; el formato `policy_contract.json` reaparece en actividades posteriores.
- **Auditoría de Analytics:** recomendación gobernada con procedencia declarada; acción factible, autoridad, cadencia y gatillo presentes; sin conexión entre contexto observable por entidad y acción ni monitoreo ejecutado.

## S03.P302.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P302.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P302.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P302.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - beneficios, costos y sus *tradeoffs* en el caso de negocio (p. 8: CAP-P.1.5.4 «Identify the tradeoffs of business benefits and costs») — ya cubierta: valor esperado bajo factibilidad (P300 H01–H02) y razón de descarte por valor (P302 H01).

## S03.P302.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P302.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de consenso sobre la formación de pregrado en ciencia de datos. Define el *data acumen*, es decir, la capacidad de «make good judgments … and ultimately make good decisions using data» (p. 22), en diez áreas conceptuales, y recomienda integrar la ética en todo el currículo y adoptar un código o juramento profesional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
