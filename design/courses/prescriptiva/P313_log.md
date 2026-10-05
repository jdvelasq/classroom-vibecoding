# Log — P313

## S02.P313.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P313_delivery_fleet_capacity/` (`data/simulation_parameters.csv`, `professor/notebook.ipynb`, `submission/` seis artefactos, `tests/test_activity.py`; notebook de estudiante sin celdas).
- **Trazabilidad revisada:** P313 → `prescriptiva.C03`, `C04`, `C05`. C03 sólida; C04 sostenida; C05 declarativa.
- **Highlights añadidos:** H01–H06 (demanda Gamma-Poisson y capacidad incierta; números aleatorios comunes; IC del objetivo; pareadas y convergencia; referencias y sensibilidad; política base + contingencia validada).
- **Ambigüedades:** contingencia 10, gatillos 145/185 y error de pronóstico sd 15 fijados sin optimización; validación en la misma muestra; pronóstico = demanda realizada + ruido; el escalamiento no cambia la acción simulada; el planeador PNG no incluye la política; referencias heredadas «W03/W05/W06/W11/W12» sin correspondencia con P3xx. Posible duplicación con P310 (Monte Carlo), que P313 supera en evidencia.
- **Superficies / contrato / dependencias:** S01–S06; pruebas sólo de existencia de tres artefactos; recibe práctica de P310 y P305/P308; vínculo con P314 sugerido por referencia «W12/W13», no documentado.
- **Auditoría de Analytics:** producto = política diaria de reserva con contingencia, guarda y autoridad, validada por simulación. Identidad prescriptiva preservada; la simulación sirve a la regla.

## S03.P313.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Random Number Generators», «Use random number generators … to allow reproducibility», «Monte Carlo Simulation» (PDA-Numerical, pp. 117–118). Categoría: ya cubierta por la semilla fija (P310 H01) y por CRN, IC95 % y convergencia (P313 H02–H04). Que P310 no reporte error de Monte Carlo es marginal frente a su defecto real (H03), que este documento no aborda.

## S03.P313.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
