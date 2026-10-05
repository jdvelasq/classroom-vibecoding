# Log — P316

## S02.P316.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P316_humanitarian_food_aid/` (`data/suppliers.csv`, `data/destinations.csv`, `data/transport.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, cinco artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P305, P308, P313–P315 y P317–P318. Contexto de diseño: `activity-architecture.md`, `s05-diseno-prescriptiva.md`, `audit-against-design.md`.
- **Trazabilidad revisada:** P316 → `prescriptiva.C02`, `C03`, `C04`, `C05`. C02 y C04 sustentadas; C03 parcial (líneas base y sensibilidad de un parámetro, sin incertidumbre); C05 parcial (monitoreo sin umbrales).
- **Highlights:** añadidos H01–H08. H01 es el highlight obligatorio de caso y datos (red con holgura global 670/550 t y escasez local de S1; matrices filas = proveedores, columnas = destinos). Cifras citadas sólo de `plan_comparison.csv`, `shipment_plan.csv`, `supplier_utilization.csv` y de los datos; penalizaciones y sensibilidad de S1 se describen sin valores por no persistirse.
- **Ambigüedades:** (1) los comentarios «W04–W06» y «W07» usan una numeración heredada que no coincide con P300–P322 (P313/P314 se llaman W12/W13), lo que sugiere que P316 precedía a P313–P315 en el orden original; (2) la guarda «un destino no alcanza 100 %» no puede activarse en el plan porque la demanda es restricción de igualdad, y no hay datos de ejecución; (3) las guardas escalan a una «asignación de escasez» y «priorización por necesidad» no implementadas; (4) el cumplimiento por destino se calcula pero no se persiste; (5) no se discute unicidad del óptimo.
- **Superficies / contrato / dependencias:** S01–S09 declaradas. Pruebas verifican existencia de plan y contrato y campos no vacíos, no cálculos. Recibe el patrón de P305/P308/P315; habilita la práctica de LP continuo sin enumeración reutilizada en P318. Sin artefactos compartidos.
- **Auditoría de Analytics:** el producto terminal es una política de abastecimiento-distribución con recomendación, aprobación humana, bloqueo y gatillos; el LP aporta factibilidad y validación. Auditoría resuelta con el límite de que monitoreo y escasez quedan declarados, no operados.
- **Cambios de IDs:** ninguno (pasada inicial). No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P316.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Algorithms for combinatorial optimization problems», «Use common algorithms … (e.g., Branch and Bound algorithms)», max-flow, «Heuristic optimization techniques» y «Implement Dynamic Programming solutions» (PDA-Algorithms, pp. 115–116). Categoría: ya cubierta en el uso (mochila P305 H03, asignación P308 H04, localización P315 H03, flujo LP P316 H05, heurísticas como línea base P316 H03). Implementar B&B o DP es fuera de alcance: `s05-diseno-prescriptiva.md` excluye la implementación de solvers.

## S03.P316.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - variables de decisión, restricciones y objetivo, errores de un modelo prescriptivo y verificación de su solución (p. 20: CAP-P.5.2.2, 5.2.4, 5.3.4 «Identify the correct verification of the solution of a prescriptive analytics model output») — ya cubierta: verificación cruzada enumeración/HiGHS (P305 H03, P308 H04, P315 H03), validación sin enumeración (P316 H06), forma cerrada y convexidad (P317 H05), balances y duales (P318 H04–H05).

## S03.P316.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Optimization» entre los fundamentos matemáticos (p. 42) y «Simulations» (p. 43). Categoría: ya cubierta. Optimización y simulación aparecen como contribuyentes en P305, P308, P313, P315–P318 y P310. El documento sólo las lista como fundamento, sin decir cómo usarlas en una política.
  - cadenas de suministro *just-in-time* que «forecast consumer demand … and optimize production and shipping», con riesgo de escasez de alimentos o medicinas (p. 32). Categoría: ya cubierta. Pedido por escenarios en P307 H01–H03; abastecimiento con guarda de escasez en P316 H01 y H07.

## S03.P316.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de ocho módulos sobre capacidades de IA, aprendizaje automático, NLP, robótica, estrategia, equipos y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado: describe los fundamentos probabilísticos de la inferencia y «the modeling and decision-making life cycle … including its human, social, and ethical implications». Sólo lista temas; no hay syllabus, casos, productos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
