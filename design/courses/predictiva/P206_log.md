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
