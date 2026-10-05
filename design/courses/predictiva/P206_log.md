# Log — P206

## S01.P206.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró clustering de demanda como rama no supervisada.

## S01.P206.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P206_clustering_demanda/`
  (notebook de profesor, selección, perfiles, asignación y pruebas) y P206 en
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights para el caso de demanda horaria: separar
  forma y nivel, definir el día como perfil, elegir clusters con silueta,
  interpretar centroides sin causalidad y asignar un perfil persistido.
- **Límite:** la normalización elimina nivel absoluto; la actividad no pronostica
  demanda ni define capacidad operativa.

## S01.P206.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se fijaron H01–H05 y se declararon superficies de serie,
  clustering y producto, con contrato de evidencia y dependencia comprobada
  hacia P207.

## S01.P206.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Corrección:** H02 declara ahora la orientación filas=días, columnas=horas y
  su consecuencia interpretativa: cada cluster es un arquetipo de forma diaria,
  no una agrupación de horas individuales ni un pronóstico.

## S01.P206.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se añadió producto, índice externo y vínculo H01–H05 con superficies actuales; se mantuvo que el clustering describe patrones, no pronostica demanda.
- **Auditoría de Analytics:** normalización y clustering sirven al producto descriptivo limitado del taller.

## S03.P206.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - K-means, evaluación de clustering, otras distancias y preprocesamiento (p. 7): ya cubiertas (H01–H03).
  - clustering espectral y de modularidad (p. 7): marginal; otro algoritmo para la misma segmentación.

## S03.P206.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): señal relevante para la identidad Predictiva que S02 dejó sin resolver en esta actividad, cuyo producto actual es descriptivo; el documento sólo enuncia la distinción, sin caso ni criterio para resolverla. Queda como insumo para la decisión de curso, no como propuesta.
  - optimización de cadena de suministro y robótica (pp. 2, 5): fuera de alcance; P206 produce una descripción de perfiles diarios, no estimación futura ni política. Reorientarlo exigiría un producto distinto y datos/decisión de operación no presentes en el S02.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera; se añadió la señal «analítica descriptiva frente a predictiva» (p. 5), omitida en la entrada original.

## S03.P206.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - analítica descriptiva frente a analítica predictiva (p. 5): toca la identidad Predictiva que S02 dejó sin resolver; el producto actual es una segmentación descriptiva de perfiles de demanda (H04). El documento sólo enuncia la distinción, sin caso ni criterio; queda como insumo para la decisión de curso.
  - aprendizaje no supervisado (p. 5): ya cubierta (H01–H05).
- **Nota:** Repetición independiente solicitada por el profesor; se omitió la precondición de documento ya revisado (entrada `.02` de OpenWork, corregida). Ningún hallazgo genera propuesta: el documento es un programa ejecutivo para líderes no técnicos con temas enunciados sin método, caso ni evaluación.

## S03.P206.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad del clustering y selección del número de grupos (T1, p. 100; DM-Cluster Analysis): ya cubierta (H03).
  - clustering basado en densidad (DM, T1): marginal; otro algoritmo para la misma segmentación.

## S03.P206.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reformular el problema como descriptivo, predictivo o prescriptivo (Domain II, p. 4): toca la identidad sin resolver de P206 (producto descriptivo); el documento no aporta criterio para resolverla.

## S03.P206.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - características de los métodos descriptivos frente a predictivos (Task 4.1, p. 17): toca la identidad sin resolver (producto descriptivo); sin criterio para resolverla.
