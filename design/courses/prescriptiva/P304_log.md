# Log — P304

## S02.P304.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P304_airline_revenue_management/` (tres archivos de `data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, cinco artefactos de `submission/`, `tests/test_activity.py`); relación con P301 y P303.
- **Trazabilidad revisada:** P304 → `prescriptiva.C01`–`C04`; sustentadas; monitoreo declarado (C05) no mapeado.
- **Highlights:** añadidos H01–H07 (capacidad perecedera secuencial; valor marginal; regla por solicitud; consecuencias por escenario; sensibilidad y gatillo; automatización acotada; identidades de conservación).
- **Ambigüedades:** (1) procedencia de los datos no documentada y caso no declarado sintético; (2) valores de R12/R13 y totales esperados por política sólo verificables por aserciones del notebook, no en las cabeceras persistidas inspeccionadas; (3) la variante de sensibilidad cambia la protección a 12 pero no se persiste; (4) la prueba exige sólo dos de cinco artefactos.
- **Superficies / contrato / dependencias:** S01–S06; recibe la regla por entidad de P303; sin artefactos que habiliten actividades posteriores.
- **Auditoría de Analytics:** política prescriptiva operable con entradas observables, acción factible, restricciones, salvaguardas, autoridad, cadencia inmediata y gatillos; falta evidencia de monitoreo ejecutado. Identidad preservada.

## S03.P304.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Explain to a non-technical audience the extent to which automated decision making occurs» y «The particular concerns of automation in critical situations» (PR-On Automation, p. 110). Categoría: ya cubierta por la automatización acotada con escalamiento y autoridad sobre parámetros (H06). P308 H06 y P303 H04 hacen el contraste con los casos que prohíben automatizar.
  - Markov Decision Processes, «Demonstrate contexts in which MDPs can be useful (e.g., optimization or control problems)» (T2), y Reinforcement Learning (E) (AI, p. 51). Categoría: fuera de alcance. Formalizar MDP o RL convertiría el tramo secuencial en un módulo de IA/IO. La política dependiente del estado ya se ejerce en P304 (H03) y el acoplamiento intertemporal en P318 (H01–H04).

## S03.P304.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P304.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
