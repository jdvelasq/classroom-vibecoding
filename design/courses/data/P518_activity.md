# P518 — Ingestión recuperable de una página de issues de GitHub

## Actividad actual implementada

**Implementación:** `implementation/data/P518_github_api/`.

### Preguntas analíticas actuales

- No hay pregunta analítica declarada. El docstring de `professor/main.py` fija un objetivo operativo: «Ingiere una respuesta congelada de GitHub como si fuera una página de API». Reconstrucción prudente (no declarada): ¿se obtuvo la página completa, sin llaves duplicadas, pese a una falla transitoria de la fuente?

`data/github_issues_page_1.json` (132819 bytes) es un arreglo JSON de objetos de issue del repositorio `pandas-dev/pandas` (los campos `url` y `repository_url` lo indican). No hay manifiesto: fecha de captura, parámetros de la consulta (estado, tamaño de página) y condiciones de uso no están documentados. `request_page(attempt)` simula la API: devuelve `503` en el primer intento y `200` con el JSON en el siguiente. `main` reintenta hasta tres veces, proyecta cada objeto a ocho campos, verifica unicidad de `issue_id` y persiste `submission/github_issues.parquet` y `submission/api_ingestion_report.csv` (`records_retrieved=20`, `retry_count=1`, `status=SUCCESS`). No hay notebook de profesor ni de estudiante (sólo `.gitkeep`); `src/main.py` levanta `NotImplementedError`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** tabla Parquet de una fila por objeto de la página (`issue_id`, `issue_number`, `title`, `state`, `created_at`, `closed_at`, `comment_count`, `is_pull_request`) y un reporte de ingestión de una fila.
- **Uso y límite:** deja una tabla tabular y tipable a partir de una respuesta anidada, con rastro de reintentos. No permite inferir nada sobre el repositorio: es una sola página congelada de 20 registros, sin paginación ni criterio de muestreo documentado. El contenido del Parquet no es inspeccionable en el resumen disponible, por lo que no se reporta cuántos registros son pull requests.
- **Disciplinas contribuyentes:** consumo de APIs y manejo de fallas (ingeniería de datos) y pandas/Parquet; no se conectan con un uso analítico declarado.

### Highlights de contribución

- **H01 — Hace visible una falla transitoria de la fuente y su recuperación acotada:** `request_page` devuelve `503` en el intento 1; el bucle `for attempt in range(1, 4)` cuenta reintentos y su cláusula `else` levanta `RuntimeError("La API no se recuperó")` si no hay éxito. El reporte persiste `retry_count=1`. Primera aparición en el curso de una ingestión que puede fallar: P513 ingería lotes locales siempre con `SUCCESS`. Sin este hito, el curso no mostraría que obtener datos de una fuente externa puede fallar ni cómo dejar constancia de ello.
- **H02 — Proyecta un JSON anidado a una unidad de análisis explícita y separa issues de pull requests (caso y datos):** cada objeto trae decenas de campos y URLs anidadas; `main` conserva ocho, renombra `comments` a `comment_count`, deja `closed_at` nulo para lo abierto y deriva `is_pull_request` de la presencia de la llave `pull_request`. La condición del caso es que la respuesta de issues puede incluir pull requests, de modo que contar «issues» sin esa marca mezclaría dos entidades. Sin este hito, la unidad de análisis de la tabla quedaría implícita y contaminada.
- **H03 — Verifica la llave y deja un reporte de ingestión persistente:** `assert frame.issue_id.is_unique` antes de escribir y un reporte con `source_name`, `pages_requested`, `records_retrieved`, `retry_count`, `status`, `output_path`. Extiende el `ingestion_report.csv` de P513 (`source_name`, `row_count`, `status`, `raw_path`) con reintentos y páginas. Sin este hito, la recuperación no dejaría evidencia revisable.

### Inventario técnico de implementación

- **Introduce:** fuente simulada con código de estado; reintento acotado con `for…else`; aplanamiento de objetos JSON por comprensión de diccionarios; derivación de bandera por presencia de llave.
- **Extiende:** reporte de ingestión de P513 con `pages_requested` y `retry_count`.
- **Reutiliza:** persistencia Parquet con `to_parquet` (P513 lo hacía en `temp/raw/`; aquí en `submission/`).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Reintento ante falla transitoria | H01 | Tres intentos, `RuntimeError` al agotar | Falla simulada; sin espera entre intentos, límite de tasa ni HTTP real. |
| Aplanamiento de respuesta de API | H02 | Ocho campos por objeto; `is_pull_request` | Una página de 20 objetos; `created_at` queda como texto; etiquetas y usuario descartados. |
| Llave única y reporte | H03 | `assert` de `issue_id`; `api_ingestion_report.csv` | `pages_requested` y `status` escritos como constantes. |

### Relación técnica con actividades anteriores

Nuevo origen de datos (API JSON) con la misma forma de evidencia que P513 (reporte de ingestión más Parquet). La exigencia nueva es la falla de la fuente y la estructura anidada. Con P516–P517 comparte la idea de compuerta antes del uso, pero aquí la compuerta es sólo unicidad de llave. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Falla y recuperación | S02, S05 | `implementation/data/P518_github_api/professor/main.py`: `request_page`, bucle de `main`; `implementation/data/P518_github_api/submission/api_ingestion_report.csv` | Falla determinista; un reporte sólo se escribe en éxito. |
| H02 — Proyección y unidad | S01, S03 | `implementation/data/P518_github_api/data/github_issues_page_1.json`; `implementation/data/P518_github_api/professor/main.py`: construcción de `frame` | Proporción de pull requests no visible; procedencia no documentada. |
| H03 — Llave y reporte | S04, S05 | `implementation/data/P518_github_api/professor/main.py`: `assert frame.issue_id.is_unique`, escritura de `REPORT`; `implementation/data/P518_github_api/submission/github_issues.parquet` | No hay prueba que lea el reporte o el Parquet. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/github_issues_page_1.json` | Una página congelada de `pandas-dev/pandas`; sin manifiesto. |
| S02 | Fuente simulada y reintento | `professor/main.py`: `request_page`, bucle | Falla siempre en el intento 1. |
| S03 | Representación | `professor/main.py`: proyección a ocho campos | Fechas como texto. |
| S04 | Validación y reporte | `professor/main.py`: `assert`, `REPORT` | Valores constantes en el reporte. |
| S05 | Producto | `submission/github_issues.parquet`; `submission/api_ingestion_report.csv` | Sin `questions.json` ni uso analítico. |
| S06 | Pruebas | `tests/test_activity.py` | Acepta cualquier archivo. |
| S07 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin notebook. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe reintentar, fallar explícitamente al agotar intentos, proyectar ocho campos, verificar unicidad y escribir dos archivos.
- **`submission/`:** Parquet de 20 registros y reporte con un reintento y estado `SUCCESS`.
- **Pruebas:** `test_submission_contains_an_artifact` sólo exige algún archivo distinto de `.gitkeep` en `submission/`; no verifica nombres, columnas, reintentos ni unicidad.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** forma del reporte de ingestión y persistencia Parquet de P513 (práctica; sin archivo compartido).
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P518 → `data.C01`–`data.C05`. `data.C01` (requisitos desde una pregunta) no se sostiene: no hay pregunta y la selección de campos no se justifica por un uso; vacío a escalar. `data.C03` se apoya sólo en unicidad y en la marca de pull requests; `data.C04` en el reporte. Auditoría (pregunta 5): el taller se lee como entrenamiento en ingestión de APIs con reintentos, una práctica de Data Engineering, porque falta la finalidad analítica que daría sentido a la tabla resultante; auditoría no resuelta. La marca `is_pull_request` es el único elemento que conecta la ingestión con una unidad de análisis.
