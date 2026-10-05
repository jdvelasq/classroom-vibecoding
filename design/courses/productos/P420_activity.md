# P420 — Seguimiento de experimentos: corridas recuperables de clasificadores de calidad de vino

## Actividad actual implementada

**Implementación:** `implementation/productos/P420_experiment_tracking/`.

### Preguntas analíticas actuales

- ¿Cómo se registra cada corrida de un modelo para recuperar después su configuración, sus datos, su modelo y sus métricas, y compararla con otras?

`data/winequality-red.csv` tiene 1599 filas (1600 líneas con encabezado), once variables fisicoquímicas y `quality` como objetivo entero. `professor/main.py` recibe `--model {tree,knn}` y `--run-id` opcional (si falta, usa la fecha y hora UTC). `prepare_data()` hace una partición 75/25 estratificada por `quality` con `random_state=123`; `build_model` entrena `DecisionTreeClassifier(max_depth=4, random_state=123)` o `KNeighborsClassifier(n_neighbors=7)`. `save_run` crea `submission/experiments/<run_id>/` con `data/train.csv`, `data/test.csv`, `config.json`, `metrics.json` y `model.pkl`, sin sobrescribir una corrida existente (`exist_ok=False`). `update_index` añade la corrida a `submission/experiments/index.json`. Las dos corridas persistidas registran exactitud de prueba 0.5825 (árbol) y 0.5075 (KNN).

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; no se declara para quién ni para qué se clasifica la calidad.
- **Producto terminal:** un registro de corridas (`index.json`) con carpetas recuperables por corrida.
- **Uso y límite:** permite comparar corridas sobre la misma partición y recuperar el modelo y los datos de cada una. No permite elegir un modelo para un uso: la única métrica es la exactitud, sin referencia, sin incertidumbre y sin criterio de selección; `config.json` omite los hiperparámetros (`max_depth`, `n_neighbors`), que sólo están en el código.
- **Disciplinas contribuyentes:** clasificación supervisada (scikit-learn) y registro de artefactos sirven a la trazabilidad de corridas; el método no se discute («Las opciones acotadas evitan distraer la actividad con el diseño del modelo»).

### Highlights de contribución

- **H01 — Fija la partición para atribuir diferencias al modelo:** `prepare_data()` usa `random_state=123` y `stratify=target`; `test_02_reuses_the_same_data_partition_for_comparison` verifica que dos llamadas devuelven particiones idénticas. Aplica la semilla de P419 a un caso con modelo. Sin este hito, la comparación de corridas mezclaría efecto del modelo y del muestreo.
- **H02 — Persiste cada corrida como unidad recuperable:** cada carpeta guarda datos de entrenamiento y prueba, configuración, métrica y modelo serializado, y `exist_ok=False` impide sobrescribir una corrida con el mismo identificador. Es la primera actividad del curso que produce y conserva un modelo entrenado (P403–P407 recibían `ESTIMATOR.pkl` ya hecho). Sin este hito, la secuencia de registro (P421) y reversión (P424) no tendría un antecedente de artefactos versionados.
- **H03 — Compara corridas desde un índice:** `index.json` acumula `run_id`, `model`, `test_accuracy` y `created_at`; el paso 4 de `HOW_TO_RUN_ME.txt` pide comparar ahí las dos exactitudes. Sin este hito, comparar exigiría abrir carpeta por carpeta.
- **H04 — Opera sobre un objetivo ordinal tratado como clases (caso y datos):** `quality` es una calificación entera usada como etiqueta multiclase; la estratificación conserva su distribución en la partición, pero la exactitud trata igual confundir 5 con 6 que 5 con 8. Además, KNN se entrena sin escalar variables de escalas muy distintas (por ejemplo `total_sulfur_dioxide` frente a `density`), lo que condiciona la comparación 0.5825 frente a 0.5075. Estas condiciones del caso limitan lo que el registro permite concluir: documenta corridas, no prueba que un modelo sea mejor para un uso.

### Inventario técnico de implementación

- **Introduce:** directorio por corrida, índice JSON acumulativo, identificador de corrida por argumento o marca temporal, instantánea de datos por corrida, serialización con `pickle` de un modelo entrenado en la actividad.
- **Extiende:** configuración por línea de comandos de P406 (`argparse` con `choices`) a la selección de modelo; semilla de P419 a partición y modelo.
- **Reutiliza:** `accuracy_score` (P403, P406).
- **Aplica en nuevo caso:** calidad de vino tinto, primer uso de este dataset en el curso.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Partición fija para comparar | H01 | `train_test_split(..., random_state=123, stratify=target)` | Una sola partición; sin validación cruzada. |
| Corrida como unidad recuperable | H02 | Carpeta con datos, config, métrica y modelo | Config sin hiperparámetros ni versiones de librerías. |
| Índice de corridas | H03 | `index.json` con exactitud y marca temporal | Registro local en archivos, sin herramienta de tracking. |
| Objetivo ordinal como clases | H04 | `quality` multiclase con exactitud | Sin métrica sensible al orden ni al desbalance. |

### Relación técnica con actividades anteriores

Nuevo caso y nuevo producto (registro de corridas). Frente a P403 (prueba de un modelo dado con exactitud, exactitud balanceada y AUC sobre datos de cáncer de mama) y P406–P407 (métricas de un `ESTIMATOR.pkl` dado), P420 entrena y conserva sus propios modelos, pero con una métrica más pobre. Los modelos producidos aquí no son consumidos por P421 ni P424, que usan pickles propios de 203183 bytes.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Partición fija | S02, S05 | `implementation/productos/P420_experiment_tracking/professor/main.py`: `prepare_data`; `implementation/productos/P420_experiment_tracking/professor/test_main.py`: `test_02` | Verifica determinismo, no representatividad. |
| H02 — Corrida recuperable | S03, S04 | `implementation/productos/P420_experiment_tracking/professor/main.py`: `save_run`; `implementation/productos/P420_experiment_tracking/submission/experiments/20260928T190053Z/`; `implementation/productos/P420_experiment_tracking/submission/experiments/20260928T190054Z/` | `config.json` no basta para reconstruir el modelo sin el código. |
| H03 — Índice | S04, S06 | `implementation/productos/P420_experiment_tracking/submission/experiments/index.json`; `implementation/productos/P420_experiment_tracking/HOW_TO_RUN_ME.txt` | Exactitudes 0.5825 y 0.5075 de una partición. |
| H04 — Objetivo ordinal | S01, S02 | `implementation/productos/P420_experiment_tracking/data/winequality-red.csv`; `implementation/productos/P420_experiment_tracking/professor/main.py`: `build_model` | La distribución de clases no se persiste ni se muestra. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/winequality-red.csv` | Procedencia no documentada en la actividad; `quality` como etiqueta. |
| S02 | Modelos y partición | `professor/main.py`: `build_model`, `prepare_data` | Dos alternativas fijas; KNN sin escalado. |
| S03 | Configuración registrada | `professor/main.py`: `save_run` | Registra modelo, semilla y tamaño de prueba. |
| S04 | Artefactos de corrida | `submission/experiments/` | Dos corridas persistidas; datos duplicados por corrida. |
| S05 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Tipos de modelo, partición estable, existencia de `index.json`. |
| S06 | Interfaz del estudiante | `src/main.py`; `HOW_TO_RUN_ME.txt` | Plantilla `NotImplementedError`; instrucciones ejecutan `src/main.py --model`. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` entrena, evalúa y registra una corrida por ejecución.
- **`submission/`:** `experiments/index.json` y dos carpetas de corrida con `config.json`, `metrics.json`, `model.pkl`, `data/train.csv` (1199 filas) y `data/test.csv` (400 filas).
- **Pruebas:** `professor/test_main.py` verifica que `build_model` devuelve el tipo declarado y que la partición es idéntica entre llamadas. `tests/test_activity.py` sólo exige `index.json`. Ninguna prueba verifica que existan al menos dos corridas, que cada carpeta esté completa ni que el modelo guardado reproduzca la métrica.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P419:** práctica de semilla fija; de P406, selección por `argparse` con `choices`.
- **Habilita para P422:** el mismo dominio de vino tinto reaparece en `P422_model_monitoring/data/reference.csv`, cuyas primeras filas coinciden con las de `winequality-red.csv`; no consume modelos ni corridas de P420. Para P421/P424: no evidenciada como artefacto.

## Trazabilidad y auditoría

Entrada revisada: P420 → `productos.C02`, `productos.C03`, `productos.C05`. C02 (artefactos reproducibles) y C05 (gobierno de corridas) se sostienen; C03 es débil: la exactitud se registra, pero no se valida frente a un uso operativo. Auditoría: el producto es una capacidad de trazabilidad de modelos, coherente con la línea de productos, pero sin usuario ni decisión que dé sentido a la clasificación de calidad. El taller no se convierte en curso de ML (el método se declara fuera de foco), aunque su limitación metodológica (ordinal como clases, KNN sin escalado) condiciona la comparación que pide hacer.
