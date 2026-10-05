# P419 — Semilla aleatoria: muestra repetible registrada con su semilla

## Actividad actual implementada

**Implementación:** `implementation/productos/P419_random_seed/`.

### Preguntas analíticas actuales

- ¿Cómo se puede repetir exactamente una decisión aleatoria para investigar después un resultado?

`professor/main.py` define `select_sample(seed)`, que crea un generador local `random.Random(seed)` y toma dos elementos de la lista fija `["factory-1", "factory-2", "factory-3", "factory-4"]`. `main()` escribe `submission/sample.json` con `{"seed": 123, "sample": ["factory-1", "factory-2"]}`. `professor/test_main.py` comprueba que la misma semilla produce la misma muestra. `data/` está vacía; no hay `HOW_TO_RUN_ME.txt`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/sample.json`, una muestra de dos etiquetas junto con la semilla que la reproduce.
- **Uso y límite:** muestra que el registro de la semilla permite repetir una selección aleatoria. La muestra no alimenta ningún análisis, no hay datos y las cuatro etiquetas no corresponden al dataset del curso (que tiene dos fábricas).
- **Disciplinas contribuyentes:** generación pseudoaleatoria al servicio de la reproducibilidad de pasos aleatorios.

### Highlights de contribución

- **H01 — Registra la semilla junto al resultado aleatorio:** `sample.json` persiste `seed` y `sample` juntos, y la selección usa un generador local `random.Random(seed)` en lugar del estado global. Es la primera aparición explícita de la semilla en la secuencia; P420 aplica luego `random_state=123` a la partición y al árbol de decisión. Sin este hito, el uso de `random_state` en P420 aparecería sin explicación previa.
- **H02 — Declara la ausencia de caso (caso y datos):** no hay datos; la población es una lista inventada de cuatro fábricas que no coincide con `daily_operations.csv` (fábricas 1 y 2) usado en P400–P418. La actividad no muestra qué análisis se vería afectado por la aleatoriedad ni cómo cambiaría un resultado con otra semilla. Este límite delimita el taller como demostración del mecanismo, no como operación de una capacidad.

### Inventario técnico de implementación

- **Introduce:** `random.Random(seed)`, `generator.sample`, persistencia de la semilla.
- **Reutiliza:** carga del módulo de profesor con `importlib.util` en la prueba.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Semilla registrada | H01 | `{"seed": 123, "sample": [...]}` | Sin análisis aguas abajo. |
| Generador local | H01, H02 | `random.Random(seed)` | No cubre numpy ni scikit-learn dentro del taller. |

### Relación técnica con actividades anteriores

Nuevo mecanismo sin relación con el indicador por fábrica salvo el vocabulario («factory»). No duplica actividades previas. La reproducibilidad de P412 (ambiente) y P418 (imagen) se complementa aquí con la de un paso aleatorio, pero sin un producto común.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Semilla registrada | S02, S03, S04 | `implementation/productos/P419_random_seed/professor/main.py`: `select_sample`; `implementation/productos/P419_random_seed/submission/sample.json`; `implementation/productos/P419_random_seed/professor/test_main.py` | La prueba sólo compara dos llamadas con la misma semilla. |
| H02 — Ausencia de caso | S01 | `implementation/productos/P419_random_seed/data/.gitkeep`; lista literal en `implementation/productos/P419_random_seed/professor/main.py` | No hay dato del cual inferir una particularidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Población muestreada | `professor/main.py`; `data/` | Cuatro etiquetas literales; `data/` vacía. |
| S02 | Selección aleatoria | `professor/main.py`; `src/main.py` | Semilla 123 fija en `main()`; plantilla sin instrucciones. |
| S03 | Artefacto | `submission/sample.json` | Semilla y muestra. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Igualdad de dos llamadas; existencia del archivo. |

### Contrato de evidencia actual

- **Notebook o código:** `select_sample(seed)` y escritura de semilla y muestra.
- **`submission/`:** `sample.json`.
- **Pruebas:** `professor/test_main.py` verifica que `select_sample(123)` es estable entre llamadas; no verifica que otra semilla cambie la muestra ni que el archivo contenga la semilla. `tests/test_activity.py` sólo verifica existencia.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna.
- **Habilita para P420:** práctica de fijar semilla (P420 usa `random_state=123` en `train_test_split` y `DecisionTreeClassifier`); relación de práctica, no de artefacto.

## Trazabilidad y auditoría

Entrada revisada: P419 → `productos.C02`, `productos.C05`. C02 se sostiene débilmente (reproducibilidad); C05 sólo como condición para investigar un resultado, sin observación. Auditoría (pregunta 5): demostración de un mecanismo de programación sin capacidad analítica que operar; riesgo de identidad no resuelto.
