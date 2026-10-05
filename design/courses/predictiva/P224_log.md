# Log — P224

## S01.P224.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `Codex`; **estado:** inicial.
- **Rutas inspeccionadas:** notebook de profesor, PNG de `submission/`, pruebas y trazabilidad de P224.
- **Decisión:** se registró PCA/t-SNE/UMAP como comparación visual y no como producto predictivo.
- **Trazabilidad:** no existe entrada P224; se registró el vacío.
- **Auditoría Analytics:** identidad Predictiva no resuelta; S01 no propone corregirla ni reubicarla.

## S01.P224.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se confirmó producto, índice externo, highlights vinculados a superficies y tensión de identidad no resuelta; no se modificó implementación.

## S03.P224.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** propone T01 (evaluar información predictiva de los componentes principales).
- **Señales descartadas relevantes:**
  - clustering espectral y embeddings de grafos (p. 7): marginal; más proyecciones sin producto predictivo.

## S03.P224.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): señal relevante para la identidad Predictiva que S02 dejó sin resolver en esta actividad, cuyo producto actual es descriptivo; el documento sólo enuncia la distinción, sin caso ni criterio para resolverla. T01 ya atiende esa identidad; el documento no se agrega a sus fuentes porque no aporta evidencia a la mejora concreta.
  - visión artificial, CNN, redes neuronales y capacidades emergentes (pp. 5–6): marginal; la lista técnica no cambia la capacidad pendiente en P224 —contrastar representación con desempeño predictivo— ni justifica añadir otra arquitectura al producto actual. T01 ya propone el menor cambio anclado a H01–H04/S01–S04.
  - proyecto de negocio integrador y caso aplicado a la organización (p. 6): fuera de alcance para anclar un cambio a P224; esa posibilidad implicaría una contribución distinta de curso, con caso/datos definidos y conexión a decisión de negocio, no disponible en la descripción S02 de P224.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; el resultado decía «refuerza T01» y a la vez que el documento no la respalda, sin agregarlo a sus fuentes; se dejó «sin cambios» y se añadió la señal descriptiva/predictiva omitida.
