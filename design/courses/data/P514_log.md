# Log — P514

## S01.P514.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró ETL por etapas como diferencia técnica frente a P511.

## S02.P514.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P514_superstore_etl/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/test_activity.py`); P511 y P513 para relaciones; P515 para contraste.
- **Trazabilidad revisada:** P514 → `data.C01`–`data.C05`.
- **Highlights:** añadidos H01 (integración organizada en `extract`/`transform`/`publish`), H02 (reporte de filas por etapa con granos distintos; caso y datos).
- **Preservado:** pregunta, etapas raw/staging/curated, joins validados heredados, reporte de etapas y relación de extensión con P511.
- **Corregido:** «introduce publicación de datos curados» se precisa: staging y curated son el mismo DataFrame escrito dos veces, sin transformación entre ellas; el detalle publicado es igual al de P511.
- **Añadido:** raw = 5926 como suma de cuatro granos; estado constante; respuesta más gruesa que la de P511; posible duplicación con P511; interfaz del estudiante en `src/main.py`.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** duplicación de producto con P511 y de pregunta con P515, pendiente de decisión de curso.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P511; habilita la forma de reporte y la pregunta para P515.
- **Auditoría de Analytics:** no resuelta; lo nuevo es la organización ETL y el producto no cambia respecto de P511.
