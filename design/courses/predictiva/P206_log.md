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
