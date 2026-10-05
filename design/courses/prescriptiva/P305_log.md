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
