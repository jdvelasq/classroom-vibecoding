# P443 — Linaje de datos: tabla curada por fábrica con huella de su insumo

## Actividad actual implementada

**Implementación:** `implementation/productos/P443_data_lineage/`.

### Preguntas analíticas actuales

- ¿De qué versión exacta del insumo proviene la tabla curada de producción por fábrica?

`data/raw_operations.csv` tiene cuatro filas; cada fila es una máquina (`factory_id`, `machine_id`) con sus `daily_units_produced`, sin columna de fecha. `professor/main.py` agrega por fábrica (`build_factory_totals`), guarda `submission/factory_totals.csv` (fábrica 1: 9303; fábrica 2: 9300) y escribe `submission/lineage.json` con la ruta y el SHA-256 del insumo, la ruta y el número de filas de la salida (2) y una marca `created_at`. El SHA-256 registrado (`29bc4958…a101`) es idéntico al de `P431_data_versioning/submission/data_manifest.json`: el insumo es byte a byte el mismo archivo de operaciones diarias usado desde P412. Procedencia del dato de fábricas no documentada en la actividad. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** explicar un resultado sin reconstruir la transformación (docstring de `main`); usuario no evidenciado.
- **Producto terminal:** tabla curada por fábrica más registro de linaje entrada→salida.
- **Uso y límite:** permite comprobar si la tabla proviene de un insumo con huella conocida. El linaje no identifica la transformación (ni función, ni versión de código, ni parámetros), por lo que no permite explicar *cómo* se obtuvo el resultado; `created_at` cambia en cada ejecución.
- **Disciplinas contribuyentes:** Data Engineering (linaje, hash de contenido) al servicio de la trazabilidad del agregado de producción por fábrica.

### Highlights de contribución

- **H01 — Registra el cambio de grano que el linaje debe explicar (caso y datos):** el insumo tiene grano máquina y la salida grano fábrica; `lineage.json` declara `rows: 2` frente a cuatro filas de entrada, y la prueba de profesor exige que cada fila curada represente una fábrica (`test_build_factory_totals_preserves_the_grain_declared_by_lineage`). El linaje cobra sentido porque la salida ya no muestra las máquinas que la componen. Sin este hito, el agregado no conservaría vínculo con su unidad original.
- **H02 — Ancla la salida a la huella del insumo:** `file_checksum` calcula SHA-256 del archivo leído y lo escribe junto a la ruta de la salida. Extiende P431, que registra la identidad de un archivo aislado, a una relación entrada→salida; la huella coincide con la de P431, lo que demuestra continuidad del insumo en la secuencia. Sin este hito, el curso tendría identidad de datos pero no relación entre un resultado y su origen.
- **H03 — Verifica el agregado, no el linaje:** `professor/test_main.py` prueba sólo `build_factory_totals`; ninguna prueba comprueba que `lineage.json` contenga la huella correcta ni que `rows` coincida con la salida. `tests/test_activity.py` exige que existan ambos archivos. Sin este hito como límite explícito, se sobrestimaría lo que el linaje garantiza.

### Inventario técnico de implementación

- **Introduce:** registro de linaje con entrada (ruta, SHA-256) y salida (ruta, filas).
- **Extiende:** el manifiesto con SHA-256 de P431 a una relación entre artefactos.
- **Reutiliza:** el mismo insumo y el mismo agregado por fábrica de P412, P417, P428 y P432 (totales 9303 y 9300).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Cambio de grano | H01 | Máquina → fábrica; `rows: 2` en linaje | Sin fecha en el insumo; un solo agregado. |
| Linaje por huella | H02 | SHA-256 del insumo junto a la salida | No registra la transformación. |
| Garantía probada | H03 | Prueba del agregado | El contenido del linaje no se prueba. |

### Relación técnica con actividades anteriores

Misma tabla curada que P412, P417, P428 y P432, con nueva exigencia de evidencia: el registro de su origen. Frente a P431, misma técnica (hash) con nuevo producto (relación entrada→salida). El agregado se repite por quinta vez en el curso; el cambio está en la evidencia, no en el cálculo. P433 (dbt) ya produce linaje implícito en su `manifest.json`; posible solapamiento conceptual no resuelto. La actividad conserva un `requirements.txt` local (`pandas==2.2.3`) que `dig/structure-audit.md` no registra como excepción.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Cambio de grano | S01, S02, S03 | `implementation/productos/P443_data_lineage/data/raw_operations.csv`; `implementation/productos/P443_data_lineage/professor/main.py`: `build_factory_totals`; `implementation/productos/P443_data_lineage/submission/lineage.json` | Grano máquina sin fecha; no se sabe a qué día corresponde. |
| H02 — Huella del insumo | S02, S03 | `implementation/productos/P443_data_lineage/professor/main.py`: `file_checksum`; `implementation/productos/P443_data_lineage/submission/lineage.json`; `implementation/productos/P431_data_versioning/submission/data_manifest.json` | Identifica el insumo, no la transformación. |
| H03 — Lo que se prueba | S04 | `implementation/productos/P443_data_lineage/professor/test_main.py`; `implementation/productos/P443_data_lineage/tests/test_activity.py` | Linaje sin verificación de contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Insumo | `data/raw_operations.csv` | Cuatro filas máquina; mismo archivo que P431. |
| S02 | Transformación y linaje | `professor/main.py` | Un paso; linaje sin identificador de transformación. |
| S03 | Entregables | `submission/factory_totals.csv`; `submission/lineage.json` | `created_at` no determinista. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Agregado probado; linaje sólo existencia. |
| S05 | Interfaz y entorno | `src/main.py`; `notebooks/`; `requirements.txt` | Plantilla vacía; manifiesto local no registrado como excepción. |

### Contrato de evidencia actual

- **Notebook o código:** agrega por fábrica, calcula SHA-256 del insumo y escribe linaje con entrada, salida y fecha de creación.
- **`submission/`:** `factory_totals.csv` y `lineage.json`.
- **Pruebas:** la de profesor verifica el agregado por fábrica; `test_01` verifica que existan ambos archivos. No se verifica la huella ni el conteo de filas del linaje.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P431:** el mismo insumo (SHA-256 idéntico) y la práctica de huella de contenido; de P412/P432 el agregado por fábrica.
- **Habilita para P454:** no evidenciada como artefacto; el catálogo de P454 no referencia este linaje.

## Trazabilidad y auditoría

P443 mapea `productos.C02` y `productos.C05`; C05 nombra explícitamente «linaje» y la actividad lo ejerce sobre la tabla curada del caso de fábricas, que es la capacidad descriptiva recurrente del curso. El producto de Analytics es un agregado trazable a su insumo; el linaje sirve a ese producto. Límite: sin la transformación registrada, el linaje no explica el resultado como promete el docstring.
