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
