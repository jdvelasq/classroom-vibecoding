# Log — P301

## S02.P301.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P301_air_france_447/` (`data/search_cells.csv`, `data/search_rounds.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, los cuatro artefactos de `submission/`, `tests/test_activity.py`); contexto en `activity-architecture.md`.
- **Trazabilidad revisada:** P301 → `prescriptiva.C01`; sustentada como contraste (decisión no recurrente).
- **Highlights:** añadidos H01–H06 (frontera excepcional/recurrente; cobertura vs éxito; actualización tras fracaso; repetir vs reasignar; verificación interna; persistencia del protocolo).
- **Ambigüedades:** (1) el nombre AF447 y el mapa titulado «escenario pedagógico AF447» podrían leerse como reconstrucción histórica; el notebook lo niega explícitamente; (2) sólo se observaron cinco filas de `search_cells.csv` en el volcado, aunque las aserciones fijan 25 celdas; (3) autoridad y escalamiento no se ejercen ni registran; (4) el supuesto de efectividad constante al repetir una celda está declarado pero no discutido como límite del plan.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; prueba de existencia de cuatro artefactos; recibe de P300 el formato de frontera de decisión; no habilita artefactos posteriores.
- **Auditoría de Analytics:** el producto es deliberadamente un protocolo excepcional, coherente con el diseño; no debe contarse como política recurrente gobernada. La teoría de búsqueda contribuye sin organizar el taller.

## S03.P301.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Bayesian networks para problemas diagnósticos y la inferencia (AI-Probability-based, p. 51). Categoría: ya cubierta como actualización bayesiana tras un fracaso (H03–H04). Las redes bayesianas como formalismo son fuera de alcance: llevarían el taller hacia IA y no hacia la política.

## S03.P301.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - problema no susceptible de solución analítica (p. 8: CAP-P.1.3.2) — marginal: P301 H01 ya ejerce una frontera de alcance (plan excepcional frente a política recurrente); no cambia lo que el estudiante hace.
  - línea base del estado actual (p. 12: CAP-P.2.5.1 «Identify current baseline performance») — ya cubierta: comparación contra reglas ingenuas con igual capacidad (P301 H02, P305 H02, P308 H02–H03, P313 H05, P318 H02).

## S03.P301.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Informe de consenso sobre la formación de pregrado en ciencia de datos. Define el *data acumen*, es decir, la capacidad de «make good judgments … and ultimately make good decisions using data» (p. 22), en diez áreas conceptuales, y recomienda integrar la ética en todo el currículo y adoptar un código o juramento profesional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P301.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
