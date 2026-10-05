# Log — P308

## S02.P308.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/` (`data/` tres CSV, `professor/notebook.ipynb`, `submission/` siete artefactos, `tests/test_activity.py`; notebook de estudiante sin celdas); contexto de P300–P307 para relaciones.
- **Trazabilidad revisada:** P308 → `prescriptiva.C01`, `C02`, `C04` en `implementation/prescriptiva/traceability.yaml`. Sostenidas; `C05` tendría evidencia (monitoreo con brecha y anulación) pero no está mapeada.
- **Highlights añadidos:** H01–H07 (incompatibilidad estructural como dato; inviabilidad individual; efecto del orden; modelo de asignación verificado; intercambio explicado; recomendación con aprobación y retención; monitoreo por cohorte). Ninguno corregido ni descartado.
- **Ambigüedades:** sin manifiesto de procedencia; el nombre «Annie Moore» no se explica en el notebook. Comentario de celda dice que «los resultados base mantienen la política secuencial», pero la recomendación persistida es la óptima. Valores de F06–F08 no visibles en el encabezado del digest; el intercambio F08 se apoya en `assert`. `exception_status` constante: ninguna condición de retención se ejercita. Posible duplicación de plantilla con P305 y P315.
- **Superficies / contrato / dependencias:** S01–S05 declaradas; pruebas sólo de existencia de tres archivos; recibe patrón de optimización de P305 y contrato de P302/P303; habilita patrón reutilizado en P315.
- **Auditoría de Analytics:** producto = política de recomendación por cohorte con autoridad humana obligatoria, guardas, retención y monitoreo; la optimización sirve a la factibilidad. Se preserva la identidad prescriptiva; límite: probabilidades dadas sin validación ni incertidumbre.

## S03.P308.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Algorithms for combinatorial optimization problems», «Use common algorithms … (e.g., Branch and Bound algorithms)», max-flow, «Heuristic optimization techniques» y «Implement Dynamic Programming solutions» (PDA-Algorithms, pp. 115–116). Categoría: ya cubierta en el uso (mochila P305 H03, asignación P308 H04, localización P315 H03, flujo LP P316 H05, heurísticas como línea base P316 H03). Implementar B&B o DP es fuera de alcance: `s05-diseno-prescriptiva.md` excluye la implementación de solvers.
  - explicar las decisiones de un modelo a los interesados, con LIME, LEMNA o TCAV en aplicaciones de seguridad (DPSIA/AS, pp. 92–93). Categoría: fuera de alcance, porque es explicabilidad de modelos predictivos (Predictiva). La explicación a nivel de política ya existe: exclusiones en P305 H04, intercambios familia por familia en P308 H05.

## S03.P308.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P308.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.5.4.2 «Identify which data or model issue is the cause of a client concern about the output of a simple prescriptive analytics model» (p. 21) — marginal: P308 H05 explica el óptimo familia por familia ante la autoridad y H07 trata la tasa de anulación como señal de revisión; diagnosticar una objeción del usuario sería una variante de esa explicación.

## S03.P308.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - explicación no técnica de resultados y preocupación del cliente sobre la salida prescriptiva (p. 21: CAP-P.5.4.2, 5.6.1) — ya cubierta: exclusiones explicadas al supervisor (P305 H04) e intercambio familia por familia (P308 H05).

## S03.P308.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P308.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Optimization» entre los fundamentos matemáticos (p. 42) y «Simulations» (p. 43). Categoría: ya cubierta. Optimización y simulación aparecen como contribuyentes en P305, P308, P313, P315–P318 y P310. El documento sólo las lista como fundamento, sin decir cómo usarlas en una política.
  - «Inaccurate predictions of flu trends … overreliance on outdated models» (p. 34). Categoría: ya cubierta. La recalibración y la brecha entre lo observado y lo estimado como gatillo están en P306 H07 y P308 H07.

## S03.P308.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 364. Lectura: índice + secciones. Se recorrió la tabla de contenido completa (pp. 3–12) y se leyeron completas las secciones con relación posible con decisión, optimización, simulación/escenarios, gobierno de IA y comunicación: cap. 1 §2.4.4–2.5 (justificación, gobierno y sensibilidad del modelo de proyección, pp. 43–44), §6.2–6.5 (escenarios de brecha e implicaciones de política, pp. 109–110, 114), §7.2–7.4 (pp. 120–123); cap. 2 §2.5–2.7 (desajustes, soft skills, roles emergentes, pp. 156–160), §4.1.1–4.1.3 (competencias técnicas y transversales, pp. 173–178), §4.5.2–4.5.3 (pp. 196–198), §5.3 (IA y ciencia de datos, pp. 204–206), §6.4 y §7 (pp. 217–221); cap. 4 §4.9 (área de analítica, ciencia de datos e IA, pp. 289–292) y recomendaciones 9–10 (pp. 312–314); Anexo B «Nuevos roles» (pp. 331–336). El resto (oferta/demanda por programas, BEBRAS, bandas salariales por área, fichas técnicas, diccionario) se revisó por grep (prescriptiv*, optimiza*, simulaci*, gobernanza, ética, sesgo, explicab*, toma de decisiones, incertidumbre, trade-off, riesgo, escenario). Las pp. 350–363 (anexo «documento publicable de necesidades del sector productivo») están en imagen y el PDF no está disponible en la ruta indicada; por su título corresponden a un resumen del cap. 2 §3, ya leído en texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P308.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión del MinTIC: bootcamps de 159 horas en programación, IA, análisis de datos, blockchain, nube y ciberseguridad para formar al menos 94.696 personas entre 2024 y 2026, con focalización poblacional, cronograma por cohortes y fuentes de financiación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P308.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un programa ejecutivo en línea de ocho módulos sobre capacidades de IA, aprendizaje automático, NLP, robótica, estrategia, equipos y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P308.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Páginas: 1. Lectura: completa. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
