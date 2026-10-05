# P102 — Conversión de CSV a JSON con minimización de campos

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P102_csv2json/`.

### Preguntas analíticas actuales

- No hay una pregunta analítica declarada. La pregunta operativa es: ¿cómo exportar la tabla de conductores a JSON conservando sólo los campos necesarios para identificarlos en un análisis y excluyendo los datos sensibles?

El caso es `data/drivers.csv`: 34 conductores con `driverId`, `name`, `ssn`, `location`, `certified` (Y/N) y `wage-plan` (`miles`/`hours`); su procedencia no está documentada. El script del profesor valida encabezados y columnas requeridas, elimina `ssn` y `location` y escribe `submission/drivers.json`. El docstring del módulo lo describe como «exportación JSON mínima y segura».

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; el docstring alude a una «exportación analítica de conductores» sin usuario ni uso concreto.
- **Producto terminal:** capacidad de datos: un JSON de 34 registros con cuatro campos por conductor.
- **Uso y límite:** permite compartir una lista de conductores sin número de seguridad social ni dirección. No es una anonimización: conserva `name`, que es un identificador directo; los valores se mantienen como texto (`"driverId": "10"`), sin tipificación.
- **Disciplinas contribuyentes:** ingeniería de datos (serialización y validación de esquema) y protección de datos (minimización).

### Highlights de contribución

- **H01 — Valida la estructura antes de transformar:** `read_csv_records` rechaza archivos sin encabezados o con encabezados repetidos y `validate_required_columns` rechaza la exportación si falta `driverId`, `name`, `certified` o `wage-plan`, con `ValueError` y mensajes en español. Es la primera validación de entrada del curso: P100–P101 asumían datos válidos. Sin este hito, un archivo mal formado produciría una salida silenciosamente incompleta.
- **H02 — Minimiza campos sensibles impuestos por el dataset (caso y datos):** la tabla contiene `ssn` y `location`, datos personales sin función en la exportación; `make_safe_records` los excluye y la prueba exige que cada registro tenga exactamente las cuatro claves permitidas. Esta condición del caso convierte una conversión de formato en una decisión sobre qué puede salir del archivo fuente. Límite: el nombre permanece. Sin este hito, la exportación copiaría identificadores sensibles por defecto.
- **H03 — Cambia la representación de tabla a lista de registros:** `csv.DictReader` produce diccionarios por fila y `json.dump(..., ensure_ascii=False, indent=2)` los serializa en UTF-8 legible, creando la carpeta de destino si falta. Los valores se conservan como cadenas; la prueba verifica el primer registro literal. Sin este hito no aparecería en la secuencia la diferencia entre formato tabular y registros anidables.
- **H04 — Compone la conversión con funciones pequeñas y un punto de entrada:** `read_csv_records` → `validate_required_columns` → `make_safe_records` → `write_json_records`, orquestadas por `convert_csv_to_json` y `main()`. Extiende la modularización de P101 a un problema nuevo. Límite: las pruebas sólo verifican el resultado final, no cada función.

### Inventario técnico de implementación

- **Introduce:** `csv.DictReader`, validación de encabezados y columnas requeridas, listas blancas y negras de columnas (`REQUIRED_COLUMNS`, `SENSITIVE_COLUMNS`), comprensión de diccionarios, `json.dump` con UTF-8.
- **Extiende de P101:** descomposición en funciones con `main()`.
- **Interfaz de estudiante:** `src/main.py` es un esqueleto con `NotImplementedError`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Validación de esquema de entrada | H01 | Encabezados presentes, no repetidos y columnas requeridas | `professor/main.py`; las pruebas no ejercitan los casos de error. |
| Minimización de datos personales | H02 | Exclusión de `ssn` y `location` | `submission/drivers.json`, prueba de claves exactas; conserva `name`. |
| Serialización CSV → JSON | H03, H04 | Registros como diccionarios, UTF-8, indentación | `submission/drivers.json`; sin conversión de tipos. |

### Relación técnica con actividades anteriores

Cambia de dato (texto libre → tabla de conductores) y de exigencia: por primera vez el código valida la entrada y decide qué campos no deben salir. Reutiliza la práctica modular de P101. No duplica P100–P101.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Validación de estructura | S02, S05 | `implementation/descriptiva/P102_csv2json/professor/main.py`: `read_csv_records`, `validate_required_columns` | No hay prueba con un CSV inválido. |
| H02 — Minimización de campos sensibles | S01, S03, S05 | `implementation/descriptiva/P102_csv2json/data/drivers.csv`; `implementation/descriptiva/P102_csv2json/professor/main.py`: `SENSITIVE_COLUMNS`, `make_safe_records`; `implementation/descriptiva/P102_csv2json/tests/test_activity.py` | No demuestra anonimización; el nombre sigue siendo identificador directo. |
| H03 — Tabla a registros JSON | S04 | `implementation/descriptiva/P102_csv2json/professor/main.py`: `write_json_records`; `implementation/descriptiva/P102_csv2json/submission/drivers.json` | Todos los valores quedan como texto. |
| H04 — Composición en funciones | S02, S06 | `implementation/descriptiva/P102_csv2json/professor/main.py`: `convert_csv_to_json`, `main`; `implementation/descriptiva/P102_csv2json/src/main.py` | Las pruebas no examinan funciones individuales. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset de conductores | `data/drivers.csv` | 34 filas; contiene `ssn` y `location`; procedencia no documentada. |
| S02 | Validación de entrada | `professor/main.py` (`REQUIRED_COLUMNS`, lectura) | Rechaza; no repara. |
| S03 | Regla de minimización | `professor/main.py` (`SENSITIVE_COLUMNS`) | Lista negra de dos columnas; `name` permanece. |
| S04 | Producto JSON | `submission/drivers.json` | 34 registros, cuatro claves, valores como cadenas. |
| S05 | Pruebas | `tests/test_activity.py` | Cantidad de registros, claves exactas y primer registro. |
| S06 | Interfaz de estudiante | `src/main.py` | Esqueleto con `NotImplementedError`; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe validar, minimizar y serializar.
- **`submission/`:** `drivers.json` (3.615 bytes), 34 registros con `driverId`, `name`, `certified`, `wage-plan`.
- **Pruebas:** ejecutan `main.py` y verifican 34 registros, el conjunto exacto de claves y el primer registro. No verifican las validaciones de error ni tipos.
- **Trazabilidad:** P102 mapea `descriptiva.C02` y `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P101:** práctica de funciones pequeñas con `main()`.
- **Habilita para P103–P105:** el mismo `data/drivers.csv` se reutiliza en P103, P104 y P105; P103 y P104 sólo llevan `driverId` y `name` al resumen. No hay artefacto de P102 consumido por ellas.

## Trazabilidad y auditoría

P102 está mapeada a `descriptiva.C02` y `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. C05 tiene respaldo parcial: la minimización es una práctica de manejo responsable de datos, aunque no hay comunicación para usuarios. C02 tiene respaldo débil: la validación de encabezados es control de calidad estructural, no exploración de distribuciones ni de calidad de valores. El producto es una capacidad de datos al servicio de análisis posteriores; la actividad no responde la pregunta descriptiva del curso y su contenido dominante es de ingeniería de datos.
