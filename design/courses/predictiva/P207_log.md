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
