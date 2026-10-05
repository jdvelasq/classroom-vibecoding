# Log — P225

## S01.P225.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `Codex`; **estado:** inicial.
- **Rutas inspeccionadas:** cotizaciones, notebook de profesor, PNG, pruebas y trazabilidad de P225.
- **Decisión:** se declaró la orientación días×acciones y se separó dependencia parcial de correlación, causalidad, pronóstico o recomendación de inversión.
- **Trazabilidad:** no existe entrada P225; se registró el vacío.
- **Auditoría Analytics:** producto descriptivo de estructura; identidad Predictiva no resuelta.

## S01.P225.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies y tensión de identidad no resuelta; no se modificó implementación.

## S03.P225.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - modelos gráficos no dirigidos y gaussianos, aprendidos desde datos (p. 11): ya cubierta (H02: GraphicalLassoCV).
  - centralidad y modelos de red (p. 11): fuera de alcance; producto descriptivo, no predictivo.

## S03.P225.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): señal relevante para la identidad Predictiva que S02 dejó sin resolver en esta actividad, cuyo producto actual es descriptivo; el documento sólo enuncia la distinción, sin caso ni criterio para resolverla. Queda como insumo para la decisión de curso, no como propuesta.
  - gestión de riesgos y estrategia de negocio mediante IA (pp. 2, 5): fuera de alcance de la red descriptiva actual, que no estima riesgo futuro ni contiene fuentes/horizonte/backtest o decisión de inversión. Convertirla en predicción requeriría resolver primero la identidad/producto señalado en H05–H06/S04 y una contribución curricular distinta, no justificable con este folleto por sí solo.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; se añadió la señal «analítica descriptiva frente a predictiva» (p. 5), omitida en la entrada original.

## S03.P225.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): toca la identidad Predictiva que S02 dejó sin resolver; el producto actual es una red descriptiva de dependencias (H05). El documento sólo enuncia la distinción, sin caso ni criterio; queda como insumo para la decisión de curso.
  - gestión de riesgos (p. 2): no aplica; P225 no estima riesgo futuro (H05).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.
