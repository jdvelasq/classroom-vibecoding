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

## S03.P207.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): toca la identidad Predictiva que S02 dejó sin resolver; el producto actual es una segmentación descriptiva de intereses (H05–H06). El documento sólo enuncia la distinción, sin caso ni criterio; queda como insumo para la decisión de curso.
  - personalización de la experiencia del cliente (p. 2): fuera de alcance; P207 no tiene datos de intervención ni de clientes y la segmentación no autoriza acción de mercadeo.
  - sesgos algorítmicos (p. 5): ya cubierta como límite (H01: atributos personales excluidos de la segmentación; riesgo de proxies declarado).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P207.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - importancia de la selección de *features* para clustering e inicialización de k-means (DM-Cluster Analysis, T1): ya cubierta (H01, H04).

## S03.P207.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reformular el problema como descriptivo, predictivo o prescriptivo (Domain II, p. 4): toca la identidad sin resolver de P207 (producto descriptivo).

## S03.P207.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de los métodos descriptivos frente a predictivos (Task 4.1, p. 17): toca la identidad sin resolver (producto descriptivo).

## S03.P207.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el blueprint de nivel intermedio detalla las mismas tareas del INFORMS Analytics Framework ya revisado; para esta actividad no añade señales distintas.

## S03.P207.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el informe define áreas de conocimiento a nivel de programa (fundamentos, datos, modelado, flujo de trabajo, comunicación, ética); para esta actividad no añade una señal distinta de las ya registradas.
