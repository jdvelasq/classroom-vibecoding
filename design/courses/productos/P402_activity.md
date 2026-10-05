# P402 — Data testing con pytest y pandas: contrato de un extracto máquina-día

## Actividad actual implementada

**Implementación:** `implementation/productos/P402_data_testing_pytest_pandas/`.

### Preguntas analíticas actuales

- ¿Cumple un extracto de producción máquina-día el contrato de datos necesario antes de usarlo para indicadores operativos?

El notebook del profesor abre con: «El equipo de operaciones necesita decidir si un extracto máquina-día cumple el contrato antes de usarlo para sus indicadores». `data/machine_throughput_export.csv` tiene 18350 filas (`factory_id`, `machine_id`, `daily_units_produced`, `factory_date`). Cuatro archivos de dos filas introducen cada uno una violación: fecha inválida, llave duplicada, producción negativa y esquema sin `factory_date`. `validate_data` devuelve la lista de violaciones y `main` persiste `submission/validation_report.json`: el extracto real se acepta y los cuatro archivos inválidos se rechazan con un único mensaje cada uno. No hay procedencia documentada del extracto.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** aceptar o rechazar un extracto antes de producir indicadores; usuario declarado: «equipo de operaciones».
- **Producto terminal:** `submission/validation_report.json`, decisión de aceptación por archivo con sus violaciones.
- **Uso y límite:** permite bloquear un insumo que viola el contrato. No dice qué hacer con un extracto rechazado (cuarentena, corrección o aviso) ni valida rangos plausibles, completitud temporal o coherencia entre máquinas y fábricas.
- **Disciplinas contribuyentes:** validación de datos con pandas y diseño de contratos de datos al servicio de la confiabilidad de indicadores.

### Highlights de contribución

- **H01 — Convierte expectativas operativas en un contrato de datos verificable:** `validate_data` comprueba orden exacto de columnas (`EXPECTED_COLUMNS`), identificadores positivos, producción no negativa, fecha ISO con `pd.to_datetime(..., format="%Y-%m-%d", errors="coerce")` y unicidad de `BUSINESS_KEY`; el esquema incorrecto corta la validación y las demás reglas se acumulan como mensajes. Extiende la precondición de columnas de P401 (subconjunto) a esquema exacto, valores y llave. Sin este hito, el curso no tendría su primera compuerta sobre datos de entrada.
- **H02 — Deriva la llave de negocio de la granularidad máquina-día (caso y datos):** cada fila es la producción de una máquina de una fábrica en una fecha; por eso `factory_id`–`machine_id`–`factory_date` debe ser única y `invalid_duplicate_key.csv` repite esa combinación con dos producciones distintas. El extracto agrega `factory_date` al esquema de P400 y sus primeras filas coinciden con los valores de `daily_operations.csv`. Cada archivo inválido aísla una sola regla, de modo que el reporte muestra una correspondencia uno a uno entre defecto y mensaje. Sin este hito, la unicidad sería una regla genérica y no una consecuencia de la unidad de análisis.
- **H03 — Persiste la decisión de aceptación como evidencia revisable:** el reporte registra `dataset`, `accepted` y `violations` para los cinco archivos. El notebook añade `rows`, `contract_columns` y `business_key`, pero el archivo persistido corresponde a `main.py` y no los contiene; el texto del mensaje de llave duplicada también difiere entre notebook («está duplicada») y `main.py` («debe ser única»). Sin este hito, la validación no dejaría rastro para revisar qué datos se aceptaron.
- **H04 — Prueba la validación en ambos sentidos:** `test_01_accepts_data_that_satisfies_the_contract` exige lista vacía para una fila válida y `test_02_reports_a_duplicate_business_key` exige exactamente el mensaje de llave duplicada. Primera prueba del curso que verifica un rechazo. No prueba las otras cuatro reglas. Sin este hito, el contrato podría aceptar todo sin que ninguna prueba falle.

### Inventario técnico de implementación

- **Introduce:** contrato de datos como función que acumula violaciones; llave de negocio con `duplicated`; validación de fechas con `errors="coerce"`; archivos de prueba que aíslan una violación cada uno; reporte JSON de aceptación.
- **Extiende:** precondición de columnas (P401) a esquema exacto y reglas de valor.
- **Reutiliza:** pruebas en `professor/test_main.py` con carga por `importlib` (P400).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Contrato de esquema y valores | H01 | Columnas exactas, positivos, no negativos, fecha ISO | Sin rangos ni completitud temporal. |
| Llave de negocio | H02 | Unicidad fábrica-máquina-fecha | Derivada de la granularidad; sin procedencia. |
| Archivos de defecto controlado | H02, H04 | Cuatro CSV con una violación cada uno | Construidos; no provienen de fallas reales observadas. |
| Reporte de aceptación | H03 | `validation_report.json` | Diverge del reporte del notebook. |

### Relación técnica con actividades anteriores

Nuevo método (contrato de datos) al servicio de un indicador de producción cercano al de P400: mismo esquema más fecha y valores iniciales coincidentes. Frente a P401, el control de entrada pasa de precondición a contrato completo con reporte persistido. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Contrato | S02 | `implementation/productos/P402_data_testing_pytest_pandas/professor/main.py`: `validate_data`, `EXPECTED_COLUMNS`, `BUSINESS_KEY` | Reglas fijas en el código. |
| H02 — Llave y granularidad | S01, S02 | `implementation/productos/P402_data_testing_pytest_pandas/data/machine_throughput_export.csv`; `implementation/productos/P402_data_testing_pytest_pandas/data/invalid_duplicate_key.csv` y demás `invalid_*.csv` | Procedencia del extracto no documentada. |
| H03 — Reporte | S03, S04 | `implementation/productos/P402_data_testing_pytest_pandas/submission/validation_report.json`; `implementation/productos/P402_data_testing_pytest_pandas/professor/notebook.ipynb` | El persistido no es el del notebook. |
| H04 — Pruebas de aceptación y rechazo | S05 | `implementation/productos/P402_data_testing_pytest_pandas/professor/test_main.py`: `test_01`, `test_02` | Dos de seis reglas probadas. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datasets | `data/machine_throughput_export.csv`; `data/invalid_*.csv` | Un extracto real y cuatro defectos construidos. |
| S02 | Contrato de validación | `professor/main.py`: `validate_data` | Seis reglas; esquema corta la evaluación. |
| S03 | Material del profesor | `professor/notebook.ipynb` | Reporte y mensajes distintos de `main.py`. |
| S04 | Producto | `submission/validation_report.json` | Sin filas ni contrato en el persistido. |
| S05 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Evaluación sólo por existencia. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** valida cada CSV de `data/` y persiste la decisión; el notebook muestra además una tabla con filas por archivo.
- **`submission/`:** `validation_report.json` con cinco decisiones (cuatro rechazos, una aceptación).
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista el reporte. `professor/test_main.py` verifica aceptación de una fila válida y el mensaje de llave duplicada; no verifica fecha, negativos, identificadores ni esquema.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** práctica de P400–P401 (función aislada y probada); el esquema de producción de P400 ampliado con fecha, sin dependencia de archivo.
- **Habilita para Pyyy:** P405 usa un `machine_throughput_export.csv` de tres filas cuyas filas coinciden con el inicio de este extracto.

## Trazabilidad y auditoría

Entrada revisada: P402 → `productos.C02`, `productos.C05`. La actividad es la evidencia más directa del bloque para `productos.C03` («validar datos… frente al uso operativo previsto»), que no está mapeada; vacío a escalar. C05 no se evidencia. El producto de Analytics es una compuerta de aceptación de insumos para indicadores de operaciones, con usuario declarado; la validación de datos sirve a ese producto. Riesgo de identidad bajo frente a P400–P401, aunque el indicador al que protege no se calcula aquí.
