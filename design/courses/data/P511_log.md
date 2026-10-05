# Log — P511

## S01.P511.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Evidencia:** manifiesto, notebooks, entregables, pruebas y trazabilidad.
- **Decisión:** mapa creado; se confirmó integración many-to-one y preservación de grano.

## S02.P511.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P511_superstore_integracion/` (`data/*.csv`, `data/source_manifest.json`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/test_activity.py`); P500–P503 para relaciones.
- **Trazabilidad revisada:** P511 → `data.C01`–`data.C05`; C05 mínima.
- **Highlights:** añadidos H01 (claves contextuales porque `Order ID` no es clave; caso y datos), H02 (uniones `many_to_one` validadas y conservación del grano), H03 (agregación posterior a la integración con detalle y respuesta persistidos).
- **Preservado:** pregunta, cuatro fuentes, claves sustitutas, validación many-to-one, preservación del grano y doble entrega.
- **Corregido:** la descripción previa decía que la pregunta «se parece a P500»; P500 responde evolución mensual, la comparación pertinente es `category_sales` de P501.
- **Añadido:** conteos de filas por tabla; ejemplo de `Order ID` repetido; columnas `Customer ID_x/_y` en la salida; fechas como texto; utilidad negativa visible no interpretada; pruebas de sólo existencia; duplicación con P514.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** el generador de las tablas derivadas no está en la actividad; las claves contextuales impiden contar clientes o productos únicos.
- **Superficies / contrato / dependencias:** S01–S06; recibe caso de P500–P502; habilita datos y práctica para P512, P514, P515.
- **Auditoría de Analytics:** integración al servicio de una descripción trazable; sin riesgo de identidad relevante.

## S03.P511.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Integration (pp. 71–72: «schema mapping», «data mapping», «challenges brought by heterogeneous data sources») — ya cubierta: claves contextuales y validación de cardinalidad (H01, H02).
