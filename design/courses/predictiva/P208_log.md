# Log — P208

## S01.P208.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Escalación:** falta entrada P208 en la trazabilidad del curso.

## S01.P208.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies, contrato y límites de simulación; no se modificó implementación.

## S03.P208.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - modelos estocásticos de contagio en redes (p. 11): marginal; P208 ya modela contagio compartimental y el caso no tiene estructura de red.

## S03.P208.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - simulaciones predictivas y gestión de riesgos (pp. 2, 4–5): ya cubiertas por escenarios SIR y picos (H02–H03); la señal no añade un contraste de aprendizaje material a la comparación existente.
  - cadena de suministro/capacidad de camas (p. 2): marginal como ejemplo de aplicación, no trasladable al caso colombiano de salud pública sin contexto de decisión y datos de capacidad distintos; no sugiere rediseñar el producto de P208.
