# Log — P305

## S02.P305.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P305_tax_inspections/` (`data/taxpayers.csv`, `data/audit_capacity.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, seis artefactos de `submission/`, `tests/test_activity.py`); relación con P303–P304.
- **Trazabilidad revisada:** P305 → `prescriptiva.C01`, `C02`, `C04`; sustentadas; sensibilidad (C03) no mapeada.
- **Highlights:** añadidos H01–H06 (valor por acción indivisible; reglas con igual capacidad; cartera exacta verificada; explicación de exclusiones; composición no anidada; recomendación supervisada).
- **Ambigüedades:** (1) la política se ilustra en una sola semana: la recurrencia es declarativa; (2) el contrato no contiene métricas de monitoreo ni umbrales para «desviación sostenida»; (3) equidad, debido proceso y disuasión se nombran como límites pero no se modelan; (4) celda de verificación duplicada en el notebook; (5) la prueba sólo verifica existencia.
- **Superficies / contrato / dependencias:** S01–S06; recibe registro y contrato de P303–P304; P306 retoma el contraste ranking/optimizador.
- **Auditoría de Analytics:** el riesgo señalado en el diseño (terminar en una solución matemática) está mitigado por el contrato y el registro pendiente de supervisor; el monitoreo de resultados sigue siendo declarativo.

## S03.P305.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Algorithms for combinatorial optimization problems», «Use common algorithms … (e.g., Branch and Bound algorithms)», max-flow, «Heuristic optimization techniques» y «Implement Dynamic Programming solutions» (PDA-Algorithms, pp. 115–116). Categoría: ya cubierta en el uso (mochila P305 H03, asignación P308 H04, localización P315 H03, flujo LP P316 H05, heurísticas como línea base P316 H03). Implementar B&B o DP es fuera de alcance: `s05-diseno-prescriptiva.md` excluye la implementación de solvers.
  - disposición «there may be multiple acceptable solutions … depending on … the need for optimality, time constraints» y CSP (AI-Planning and Search, pp. 52–53). Categoría: ya cubierta. El método se elige según la estructura del problema en P306 H03, P317 H04 y P319 H03, y la elegibilidad por par entra como restricción en P308 H01.
  - explicar las decisiones de un modelo a los interesados, con LIME, LEMNA o TCAV en aplicaciones de seguridad (DPSIA/AS, pp. 92–93). Categoría: fuera de alcance, porque es explicabilidad de modelos predictivos (Predictiva). La explicación a nivel de política ya existe: exclusiones en P305 H04, intercambios familia por familia en P308 H05.

## S03.P305.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P305.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P305.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - línea base del estado actual (p. 12: CAP-P.2.5.1 «Identify current baseline performance») — ya cubierta: comparación contra reglas ingenuas con igual capacidad (P301 H02, P305 H02, P308 H02–H03, P313 H05, P318 H02).
  - variables de decisión, restricciones y objetivo, errores de un modelo prescriptivo y verificación de su solución (p. 20: CAP-P.5.2.2, 5.2.4, 5.3.4 «Identify the correct verification of the solution of a prescriptive analytics model output») — ya cubierta: verificación cruzada enumeración/HiGHS (P305 H03, P308 H04, P315 H03), validación sin enumeración (P316 H06), forma cerrada y convexidad (P317 H05), balances y duales (P318 H04–H05).
  - explicación no técnica de resultados y preocupación del cliente sobre la salida prescriptiva (p. 21: CAP-P.5.4.2, 5.6.1) — ya cubierta: exclusiones explicadas al supervisor (P305 H04) e intercambio familia por familia (P308 H05).

## S03.P305.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - tabla de hechos sin hechos y cobertura para analizar «what didn't happen» (p. 8) aplicada a casos no seleccionados — marginal: P305 H04 y P302 H01 ya explican exclusiones y descartes.

## S03.P305.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Optimization» entre los fundamentos matemáticos (p. 42) y «Simulations» (p. 43). Categoría: ya cubierta. Optimización y simulación aparecen como contribuyentes en P305, P308, P313, P315–P318 y P310. El documento sólo las lista como fundamento, sin decir cómo usarlas en una política.
  - sesgos en *predictive policing* (p. 34) y «algorithmic bias» en la priorización de inspecciones o controles. Categoría: fuera de alcance para P305, porque su caso declara que no hay atributos protegidos (S01) y no hay datos para modelar equidad con rigor. La auditoría por grupo está cubierta en P320 H01–H02.

## S03.P305.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
