# Log — P207

## S01.P207.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Escalación:** falta entrada P207 en `traceability.yaml`.

## S01.P207.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P207_clustering_mercadeo/`
  (notebook de profesor, entradas, perfiles, visualizaciones y pruebas). No hay
  entrada P207 correspondiente en `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights para separar intereses de atributos
  personales, limpiar edad, ponderar intereses con TF–IDF, seleccionar clusters,
  justificar perfiles y persistir resultados.
- **Límite y escalación:** se preserva la ausencia de trazabilidad; excluir
  atributos personales de la entrada no elimina posibles proxies ni autoriza uso
  automático de los segmentos para mercadeo.

## S01.P207.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se asignaron H01–H07 y se documentaron superficies de datos,
  representación, interpretación y trazabilidad, junto con dependencia
  comprobada de P206. Se mantuvo como no demostrable cualquier dependencia con
  P225.

## S01.P207.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H07 con superficies existentes. Se preservaron la ausencia de trazabilidad y los límites sobre proxies y uso de segmentos.
- **Auditoría de Analytics:** TF–IDF y clustering sirven a una explicación segmentada, no a una decisión automatizada de mercadeo.

## S03.P207.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - agrupación de textos por temas (p. 7): ya cubierta conceptualmente (H03: TF–IDF antes de KMeans).

## S03.P207.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): señal relevante para la identidad Predictiva que S02 dejó sin resolver en esta actividad, cuyo producto actual es descriptivo; el documento sólo enuncia la distinción, sin caso ni criterio para resolverla. Queda como insumo para la decisión de curso, no como propuesta.
  - personalización de experiencia del cliente/marketing (p. 2): fuera de alcance para la actividad tal como está anclada; P207 usa perfiles estudiantiles para describir intereses, no datos de clientes ni resultados futuros. Adaptar segmentos a targeting o acción exigiría otra pregunta, producto y evidencia de intervención, y no puede afirmarse sin caso apropiado.
  - sesgo algorítmico, tolerancia al riesgo y gobernanza (pp. 5–6): marginal como temas generales; H01–H02 y los límites de uso ya reconocen riesgo de proxies, pero el folleto no define un criterio/evidencia de equidad operacional para este dataset.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; se añadió la señal «analítica descriptiva frente a predictiva» (p. 5), omitida en la entrada original.
