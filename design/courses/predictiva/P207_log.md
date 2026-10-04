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
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización de experiencia del cliente/marketing (p. 2): fuera de alcance para la actividad tal como está anclada; P207 usa perfiles estudiantiles para describir intereses, no datos de clientes ni resultados futuros. Adaptar segmentos a targeting o acción exigiría otra pregunta, producto y evidencia de intervención, y no puede afirmarse sin caso apropiado.
  - sesgo algorítmico, tolerancia al riesgo y gobernanza (pp. 5–6): marginal como temas generales; H01–H02 y los límites de uso ya reconocen riesgo de proxies, pero el folleto no define un criterio/evidencia de equidad operacional para este dataset.
