# Log — P205

## S01.P205.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se delimitó calibración/priorización como análisis predictivo, no política crediticia.

## S01.P205.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:**
  `implementation/predictiva/P205_priorizacion_con_probabilidades/` (notebook,
  entrada simulada, tres tablas y pruebas) y P205 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato actual de S01 y se añadieron highlights
  para calibración, consecuencias de umbral, frontera con política, revisión
  por grupo y persistencia; se incorporó la naturaleza simulada del dataset y
  los tamaños desiguales de sus dos grupos.
- **Auditoría de Analytics:** el producto es evidencia predictiva previa a una
  priorización; no define una política prescriptiva real.

## S01.P205.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05 y se documentaron superficies, contrato de
  evidencia y dependencia comprobada con P204; no se inventó una dependencia
  técnica con los talleres posteriores.

## S01.P205.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H05 con superficies existentes. Se preservó el límite entre evidencia predictiva simulada y política crediticia.
- **Auditoría de Analytics:** calibración y umbrales sirven a evidencia previa, no a una política prescriptiva real.

## S03.P205.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - falsos positivos/negativos y precision/recall (p. 9): ya cubierta (H02: conteos y costos por umbral).

## S03.P205.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - supervisión y criterio humano, tolerancia al riesgo, gobernanza (pp. 5–6): ya expresan el límite que H03 traza entre probabilidad/umbral y política, pero no cambian materialmente la capacidad de P205 para revisar probabilidades simuladas; tampoco justifican crear una política con datos ficticios. Se conserva la identidad Predictiva, no se convierte la actividad en Prescriptiva.
