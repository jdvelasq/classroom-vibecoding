# Log — P310

## S02.P310.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P310_monte_carlo_para_politicas/` (`data/project_parameters.csv`, `professor/main.py`, `professor/notebook.ipynb`, `submission/` dos CSV, `tests/test_activity.py`; `src/` sólo `.gitkeep`).
- **Trazabilidad revisada:** P310 → `prescriptiva.C01`, `C03`, `C04`, `C05`. C01/C04 sostenidas; C03 parcial (sin línea base ni sensibilidad); C05 débil.
- **Highlights añadidos:** H01 (resumen de distribución), H02 (guardas y rama de escalamiento). **No inferible como contribución:** H03 se registra como límite: la simulación no cambia la acción en el caso persistido.
- **Ambigüedades:** media −204.852,96 y probabilidad de pérdida 0.9997 llevan a `no_aprobar` por la primera rama; las guardas y el escalamiento previstos en `activity-architecture.md` no se ejercitan. Recurrencia de la decisión no demostrada (un proyecto). Sin procedencia ni declaración de sintético. El notebook importa desde `src/`, que no contiene `main.py`.
- **Superficies / contrato / dependencias:** S01–S05; pruebas sólo de existencia; recibe práctica de P303; dependencia hacia P313 no evidenciada; posible duplicación con P313 (Monte Carlo).
- **Auditoría de Analytics:** producto = regla de inversión con autoridad y guardas; Monte Carlo contribuye. Auditoría no resuelta: la conexión incertidumbre → acción no se observa con los datos actuales.

## S03.P310.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Random Number Generators», «Use random number generators … to allow reproducibility», «Monte Carlo Simulation» (PDA-Numerical, pp. 117–118). Categoría: ya cubierta por la semilla fija (P310 H01) y por CRN, IC95 % y convergencia (P313 H02–H04). Que P310 no reporte error de Monte Carlo es marginal frente a su defecto real (H03), que este documento no aborda.

## S03.P310.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P310.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P310.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Plan de examen de la certificación CAP-Pro, derivado del INFORMS Analytics Framework: siete dominios (encuadre del problema de negocio y del problema analítico, datos, selección de método, desarrollo de modelos, despliegue y gestión del ciclo de vida de la solución) con subtareas evaluables. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P310.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
