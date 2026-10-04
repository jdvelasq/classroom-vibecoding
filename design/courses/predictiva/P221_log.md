# Log — P221

## S01.P221.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se clasificó como extensión técnica de P200, no como repetición:
  añade selección de variables dentro de la evaluación reproducible.

## S01.P221.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies y ausencia de trazabilidad; no se modificó implementación.

## S03.P221.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - predicción con datos de alta dimensión y validación cruzada (p. 8): ya cubierta (H01–H02).

## S03.P221.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad, representatividad y gestión de datos para ML (p. 5): ya cubierta parcialmente por la selección integrada y validación de H01–H02; no identifica defecto del conjunto Auto MPG ni evidencia que cambie qué información usar para estimar MPG.
