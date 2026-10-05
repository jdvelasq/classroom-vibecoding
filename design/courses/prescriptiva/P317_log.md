# Log — P317

## S02.P317.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P317_flood_protection_investment/` (`data/protection_parameters.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, seis artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P310, P313–P316 y P318.
- **Trazabilidad revisada:** P317 → `prescriptiva.C02`, `C03`, `C04`, `C05`. C02 y C04 sustentadas; C03 limitada a referencias, validación analítica y sensibilidad determinista; C05 con un gatillo cuantificado y sin plan de monitoreo persistido.
- **Highlights:** añadidos H01–H08. H01 es el highlight obligatorio de caso y datos (caso paramétrico de siete parámetros, riesgo como forma funcional, período de retorno como inverso de probabilidad). Cifras tomadas de `investment_comparison.csv`, `risk_sensitivity.csv`, `flood_protection_policy_actions.csv` y del contrato persistido; la fila `k = 750.000` de sensibilidad no es visible en la cabecera inspeccionada y no se cita.
- **Ambigüedades:** (1) la prueba sólo exige un archivo cualquiera en `submission/`, desproporcionada frente al contrato que el notebook produce; (2) `target_protection_m` = `economic_protection_m` en los tres casos: el óptimo económico coincide con la probabilidad objetivo y el escalamiento depende sólo del presupuesto, sin mostrar conflicto entre eficiencia y objetivo de riesgo; (3) los casos de riesgo se fijan en código pero la columna se llama `observed_annual_flood_probability`; (4) procedencia declarada sólo como «inspirado en» la planeación holandesa; (5) presupuesto y objetivo no aparecen en la cabecera del CSV inspeccionado, sólo en el contrato.
- **Superficies / contrato / dependencias:** S01–S08 declaradas. Recibe de P316 (y P305/P308/P315) el uso de PuLP + HiGHS que aquí se rechaza explícitamente; de P310, el patrón de escalamiento a comité. No habilita dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = regla anual de aprobación de inversión con tope presupuestal, autoridad en dos niveles, escalamiento y gatillos; la optimización no lineal es evidencia, como declara el notebook. Auditoría resuelta con el límite de casos de riesgo hipotéticos y prueba mínima.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P317.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - disposición «there may be multiple acceptable solutions … depending on … the need for optimality, time constraints» y CSP (AI-Planning and Search, pp. 52–53). Categoría: ya cubierta. El método se elige según la estructura del problema en P306 H03, P317 H04 y P319 H03, y la elegibilidad por par entra como restricción en P308 H01.

## S03.P317.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P317.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P317.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - variables de decisión, restricciones y objetivo, errores de un modelo prescriptivo y verificación de su solución (p. 20: CAP-P.5.2.2, 5.2.4, 5.3.4 «Identify the correct verification of the solution of a prescriptive analytics model output») — ya cubierta: verificación cruzada enumeración/HiGHS (P305 H03, P308 H04, P315 H03), validación sin enumeración (P316 H06), forma cerrada y convexidad (P317 H05), balances y duales (P318 H04–H05).

## S03.P317.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P317.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Optimization» entre los fundamentos matemáticos (p. 42) y «Simulations» (p. 43). Categoría: ya cubierta. Optimización y simulación aparecen como contribuyentes en P305, P308, P313, P315–P318 y P310. El documento sólo las lista como fundamento, sin decir cómo usarlas en una política.

## S03.P317.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
