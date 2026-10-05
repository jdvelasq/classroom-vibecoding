# P101 — Manejo del editor: refactorización del conteo MapReduce

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P101_manejo_editor/`.

### Preguntas analíticas actuales

- No hay una pregunta analítica declarada. La implementación responde a una pregunta de organización de código: ¿cómo reestructurar el script lineal de conteo de palabras en funciones reutilizables sin cambiar su resultado?

Usa los mismos cuatro textos y la misma replicación (1.000 copias) que P100. El punto de partida del estudiante (`src/main.py`) es el script lineal de P100, sin la copia final a `submission/`. La solución del profesor lo reorganiza en funciones de preparación de carpetas, generación de copias, `mapper`, `reducer`, un motor `hadoop(...)` parametrizado y la copia del resultado. El nombre de la carpeta alude al manejo del editor, pero la implementación no contiene instrucciones, notebook ni `DESCRIPTION.md` que evidencien operaciones de editor; lo observable es la refactorización.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** el mismo conteo de palabras de P100 (`part-00000`, `_SUCCESS`), ahora producido por código modular.
- **Uso y límite:** demuestra que una reorganización preserva el resultado; no agrega información analítica, interpretación ni nuevo dato. Hereda todos los límites de P100 (volumen artificial, simulación secuencial).
- **Disciplinas contribuyentes:** ingeniería de software (descomposición en funciones, funciones de orden superior, precondiciones) e ingeniería de datos. El producto es una destreza de disciplina contribuyente.

### Highlights de contribución

- **H01 — Refactoriza un script lineal en funciones con responsabilidad nombrada:** `clear_folder`, `initialize_folder`, `delete_folder`, `generate_file_copies(n)`, `mapper(sequence)`, `reducer(pairs_sequence)` y `copy_hdfs_output_to_submission` sustituyen las secciones comentadas del script de P100; la ejecución queda bajo `if __name__ == "__main__":`. Contrasta directamente con P100 y con `src/main.py`. Sin este hito la secuencia no mostraría la transición de script a código reutilizable antes de P102.
- **H02 — Separa el motor genérico de la lógica del problema:** `hadoop(input_folder, output_folder, mapper_fn, reducer_fn)` recibe mapper y reducer como argumentos y encapsula lectura, ordenamiento, escritura y marcador de éxito en funciones internas. Sin este hito, el patrón MapReduce seguiría acoplado al conteo de palabras; el límite es que ningún otro mapper/reducer se ejercita en la actividad.
- **H03 — Hace explícita una precondición del motor:** `create_output_directory` lanza `FileExistsError` si la carpeta de salida ya existe, y el bloque principal llama antes a `delete_folder(OUTPUT_FOLDER)`. P100 vaciaba la carpeta en silencio; aquí la condición se vuelve un error visible. Sin este hito, la convención de no sobrescribir salidas quedaría implícita.
- **H04 — Usa el corpus fijo como oráculo de regresión (caso y datos):** los datos y la replicación son idénticos a P100, de modo que el resultado esperado no cambia; las pruebas repiten las mismas cinco aserciones de conteo. La particularidad del caso aquí no es el texto, sino que su salida conocida permite comprobar que la refactorización preserva el comportamiento. Sin este hito, la reorganización del código carecería de criterio de corrección.
- **H05 — Completa el flujo de entrega a partir de un punto de partida incompleto:** `src/main.py` escribe en `temp/output/` pero no copia a `submission/`; la solución añade `copy_hdfs_output_to_submission`. Sin este hito el estudiante podría reorganizar el código sin cerrar el contrato de entrega.

### Inventario técnico de implementación

- **Reutiliza de P100:** datos, replicación, tokenización, map/sort/reduce, `part-00000` y `_SUCCESS`.
- **Introduce:** funciones con parámetros, funciones anidadas, funciones pasadas como argumento, `pathlib.Path` para rutas, `shutil.rmtree` para eliminar la salida y `FileExistsError` como precondición.
- **Interfaz de estudiante:** script lineal funcional (no esqueleto), a diferencia de P100.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Refactorización a funciones | H01, H05 | Script lineal → funciones nombradas y bloque `__main__` | `src/main.py` frente a `professor/main.py`; no hay rúbrica de calidad de código. |
| Motor parametrizado | H02, H03 | `hadoop(...)` con `mapper_fn` y `reducer_fn`; error si la salida existe | `professor/main.py`; sólo un par mapper/reducer. |
| Prueba de regresión | H04 | Mismos cinco conteos que P100 | `tests/test_activity.py`; no prueba funciones individuales. |

### Relación técnica con actividades anteriores

Misma pregunta operativa, mismos datos y mismo contrato que P100, con nueva implementación: el cambio es exclusivamente de organización del código. No es duplicación del método, pero sí del producto y de las aserciones; la decisión sobre si ambas actividades deben coexistir corresponde a una revisión posterior. La relación con «manejo del editor» no es verificable con la evidencia disponible.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Funciones con responsabilidad nombrada | S02, S05 | `implementation/descriptiva/P101_manejo_editor/professor/main.py`; `implementation/descriptiva/P101_manejo_editor/src/main.py` | Las pruebas no examinan la estructura del código. |
| H02 — Motor genérico | S02 | `implementation/descriptiva/P101_manejo_editor/professor/main.py`: `hadoop(...)` | No se ejercita con otro problema. |
| H03 — Precondición de salida | S02 | `implementation/descriptiva/P101_manejo_editor/professor/main.py`: `create_output_directory`, `delete_folder` | No hay prueba que provoque el error. |
| H04 — Oráculo de regresión | S01, S04 | `implementation/descriptiva/P101_manejo_editor/data/`; `implementation/descriptiva/P101_manejo_editor/tests/test_activity.py` | Cinco conteos; no cubren toda la salida. |
| H05 — Cierre del flujo de entrega | S03, S05 | `implementation/descriptiva/P101_manejo_editor/src/main.py`; `implementation/descriptiva/P101_manejo_editor/professor/main.py`: `copy_hdfs_output_to_submission`; `implementation/descriptiva/P101_manejo_editor/submission/` | `submission/` ya contiene `part-00000` y `_SUCCESS` versionados, por lo que la prueba podría pasar sin que el código del estudiante los regenere. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y replicación | `data/file1.txt`–`data/file4.txt` | Idénticos a P100; los conteos esperados dependen de ellos. |
| S02 | Método: estructura modular y motor `hadoop` | `professor/main.py` | Comentario «Reducer» duplicado sobre `hadoop`; sin docstrings de decisión. |
| S03 | Producto y persistencia | `submission/part-00000`; `submission/_SUCCESS` | Artefactos versionados en el repositorio. |
| S04 | Pruebas | `tests/test_activity.py`; `tests/conftest.py` | Una prueba; mismas aserciones que P100. |
| S05 | Interfaz de estudiante | `src/main.py` | Script lineal sin copia a `submission/`; no hay instrucciones de editor ni notebook. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe producir el mismo conteo que P100 mediante funciones y un motor parametrizado, eliminando primero la salida previa.
- **`submission/`:** `part-00000` (2.844 bytes) y `_SUCCESS`; mismo contenido esperado que P100.
- **Pruebas:** ejecutan `main.py` y verifican existencia de archivos y cinco conteos. No verifican la refactorización, el uso de `hadoop(...)` ni el manejo del editor.
- **Trazabilidad:** P101 mapea sólo `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P100:** datos, flujo map/sort/reduce y contrato de conteos; `src/main.py` es ese flujo en forma de script.
- **Habilita para P102:** la práctica de organizar el código en funciones pequeñas y un `main()` reaparece en `professor/main.py` de P102; no hay artefacto compartido.

## Trazabilidad y auditoría

P101 está mapeada a `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. La evidencia observable es código legible y modular, que puede apoyar reproducibilidad, pero no documenta ni comunica un análisis para usuarios o decisores; el mapeo a C05 es indirecto. La actividad no responde la pregunta descriptiva del curso y su producto es una destreza de ingeniería de software aplicada al mismo conteo de P100. Puede caracterizarse como un ejercicio técnico habilitador; la auditoría de identidad queda no resuelta a nivel de actividad y la correspondencia entre nombre («manejo del editor») y contenido requiere aclaración.
