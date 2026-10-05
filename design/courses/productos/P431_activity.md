# P431 — Data versioning: manifiesto de identidad de un archivo de datos

## Actividad actual implementada

**Implementación:** `implementation/productos/P431_data_versioning/`.

### Preguntas analíticas actuales

- ¿Cómo se registra la identidad exacta de los datos que alimentan una capacidad, de modo que un cambio de contenido sea detectable aunque el nombre del archivo no cambie?

`data/raw/daily_operations.csv` es el mismo extracto de cuatro filas de P428–P429, ahora bajo `data/raw/`. `professor/main.py` define `describe_data`, que produce un manifiesto con etiqueta de versión literal (`daily-operations-v1`), ruta relativa, SHA-256 del contenido, tamaño en bytes y columnas leídas del encabezado. `submission/data_manifest.json` registra `sha256` `29bc4958…a101`, `bytes: 79` y las tres columnas. La docstring de `main` declara que el manifiesto es «el artefacto que se versionaría junto con el código en Git».

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/data_manifest.json`, huella de la versión de datos de entrada.
- **Uso y límite:** permite afirmar qué contenido exacto tenía el archivo cuando se generó el manifiesto. No hay paso de verificación pese a que la docstring del módulo dice «registra y verifica»: ningún código compara un archivo actual con el manifiesto. La etiqueta de versión es fija y no se incrementa; no se vincula el manifiesto con un resultado analítico producido con esos datos.
- **Disciplinas contribuyentes:** versionado de datos por huella criptográfica; esquema mínimo por encabezado.

### Highlights de contribución

- **H01 — Identifica una versión de datos por contenido, no por nombre:** `hashlib.sha256(path.read_bytes())` junto a `bytes` y `columns`; la prueba de profesor exige que la huella y el tamaño coincidan con el archivo y que las columnas se lean del encabezado. Primera aparición de huella de datos en el curso; P420 conservaba copias de datos por corrida, no una huella. Sin este hito, dos archivos con el mismo nombre y distinto contenido serían indistinguibles.
- **H02 — Separa capa cruda y manifiesto versionable (caso y datos):** el dato se ubica en `data/raw/` y el manifiesto registra su ruta relativa y sus tres columnas (`factory_id`, `machine_id`, `daily_units_produced`), lo que hace explícito el grano máquina–fábrica del extracto. El extracto no tiene fecha ni versiones sucesivas: la actividad no muestra un cambio de contenido detectado, sólo una versión. La particularidad del caso no condiciona el manifiesto más allá del encabezado; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** SHA-256 de archivo; manifiesto JSON con versión, ruta, tamaño y columnas; carpeta `data/raw/`.
- **Reutiliza:** `daily_operations.csv` de P400–P429.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Huella de contenido | H01 | SHA-256, tamaño, columnas | Sin comparación contra el manifiesto. |
| Capa cruda + manifiesto | H02 | `data/raw/` y ruta relativa | Una sola versión; etiqueta literal. |

### Relación técnica con actividades anteriores

Nueva exigencia de evidencia sobre el mismo dato: P412 registraba versiones de Python y pandas; P431 registra la versión de los datos. Complementa P420 (copias de datos por corrida) con un mecanismo más liviano. No se usa ninguna herramienta de versionado de datos; la integración con Git queda declarada en una docstring.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Identidad por contenido | S02, S04 | `implementation/productos/P431_data_versioning/professor/main.py`: `describe_data`; `implementation/productos/P431_data_versioning/professor/test_main.py` | No hay verificación posterior. |
| H02 — Capa cruda y manifiesto | S01, S03 | `implementation/productos/P431_data_versioning/data/raw/daily_operations.csv`; `implementation/productos/P431_data_versioning/submission/data_manifest.json` | Una versión; sin cambio demostrado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset crudo | `data/raw/daily_operations.csv` | Idéntico a actividades previas. |
| S02 | Construcción del manifiesto | `professor/main.py` | Versión literal; sin función de verificación. |
| S03 | Manifiesto entregado | `submission/data_manifest.json` | Cinco campos. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del manifiesto en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** calcula y guarda el manifiesto del archivo crudo.
- **`submission/`:** `data_manifest.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica versión, ruta, columnas, tamaño y huella sobre un CSV temporal. No verifican detección de cambios.
- **Trazabilidad:** P431 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400–P429:** el mismo `daily_operations.csv`.
- **Habilita para P443:** P443 reutiliza la huella SHA-256 del archivo de entrada en un registro de linaje (mismo valor `29bc4958…a101` para `data/raw_operations.csv`).

## Trazabilidad y auditoría

P431 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la reproducibilidad de la entrada; C05 (gobierno) se apoya en la huella, sin verificación ni linaje con salidas. Auditoría de identidad (pregunta 5): la práctica es pertinente para una capacidad analítica, pero no se conecta con un resultado producido con esa versión de datos; riesgo moderado de leerse como técnica genérica de data engineering.
