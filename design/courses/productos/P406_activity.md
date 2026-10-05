# P406 — Configuración por línea de comandos: evaluar un clasificador de frases en train, test o prod

## Actividad actual implementada

**Implementación:** `implementation/productos/P406_config_cmd_line/`.

### Preguntas analíticas actuales

- ¿Cómo se ejecuta el mismo modelo sobre distintos conjuntos de datos sin editar el código, y qué desempeño tiene en cada uno?

`HOW_TO_RUN_ME.txt` pide ejecutar `python3 src/main.py test`, repetir con `train` y `prod`, comparar métricas y probar un valor no admitido. `professor/main.py` define un argumento posicional con `choices=("train", "test", "prod")`, lee `data/<conjunto>/sentences.csv.gz`, carga `ESTIMATOR.pkl` (203183 bytes) y predice directamente sobre la columna de texto `phrase`, comparando con `target`. `submission/metrics.json` guarda la última ejecución: `test`, accuracy 0,956 y balanced accuracy 0,918. El contenido de los CSV comprimidos, el significado de `target` y la procedencia del modelo y de los datos no están documentados.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** desempeño del modelo por conjunto; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/metrics.json` con el conjunto evaluado y sus dos métricas.
- **Uso y límite:** permite ejecutar el mismo artefacto en contextos de datos distintos sin editarlo. Sólo conserva la última ejecución, así que la comparación entre conjuntos que piden las instrucciones no queda persistida; no hay umbral ni consecuencia.
- **Disciplinas contribuyentes:** parametrización de programas (`argparse`) y métricas de clasificación al servicio de la evaluación repetible de un modelo.

### Highlights de contribución

- **H01 — Parametriza el contexto de ejecución con valores admitidos:** el argumento posicional `dataset` con `choices` rechaza un valor no listado al interpretar los argumentos, antes de cargar datos (paso 3 de `HOW_TO_RUN_ME.txt` con `development`). Los comentarios justifican la lista cerrada: «evitan que una ejecución reproducible dependa de nombres improvisados». Primera configuración externa del curso. Sin este hito, cambiar de conjunto exigiría editar el código.
- **H02 — Opera un artefacto de texto sobre particiones con etiqueta (caso y datos):** el estimador recibe la columna `phrase` sin transformación previa en el código, de modo que el artefacto encapsula su propia representación del texto; los tres conjuntos `train`, `test` y `prod` tienen `target`, incluido `prod`. La diferencia persistida entre accuracy (0,956) y balanced accuracy (0,918) en `test` es visible, pero la distribución de clases no se muestra. Sin este hito, el modelo sería intercambiable con el de P403; con él queda visible que «prod» aquí es un conjunto etiquetado, no tráfico de producción.
- **H03 — Registra en la evidencia qué configuración produjo las métricas:** `metrics.json` incluye `dataset` junto a las métricas; la misma información se imprime en consola. El archivo se sobrescribe en cada ejecución. Sin este hito, unas métricas persistidas no podrían atribuirse a su conjunto.

### Inventario técnico de implementación

- **Introduce:** `argparse` con argumento posicional y `choices`; rutas de datos derivadas de la configuración; lectura de CSV comprimido; modelo de texto serializado.
- **Reutiliza:** carga de artefacto congelado con `pickle` (P403); métricas accuracy y balanced accuracy (P403).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Configuración por argumento | H01 | Posicional con `choices` | Un único parámetro. |
| Particiones train/test/prod | H02 | Tres CSV con `phrase` y `target` | Contenido y procedencia no documentados. |
| Métricas atribuidas | H03 | `dataset` en `metrics.json` | Sólo última ejecución. |

### Relación técnica con actividades anteriores

Reutiliza la práctica de P403 (artefacto congelado, métricas) en un caso nuevo de texto, sin umbrales ni compuerta. La contribución es la configuración externa; el resto del flujo es una evaluación sin decisión. Antecede a P407, que repite el caso con otra forma de configuración.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Parametrización | S02, S05 | `implementation/productos/P406_config_cmd_line/professor/main.py`: `parse_arguments`, `ALLOWED_DATASETS`; `implementation/productos/P406_config_cmd_line/HOW_TO_RUN_ME.txt` | El rechazo previo a la carga se infiere del orden en `main`. |
| H02 — Texto con particiones | S01, S03 | `implementation/productos/P406_config_cmd_line/data/{train,test,prod}/sentences.csv.gz`; `implementation/productos/P406_config_cmd_line/ESTIMATOR.pkl`; `implementation/productos/P406_config_cmd_line/submission/metrics.json` | Archivos binarios en el digest. |
| H03 — Métricas atribuidas | S03, S04 | `implementation/productos/P406_config_cmd_line/submission/metrics.json` | Sobrescritura en cada ejecución. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Artefacto y datos | `ESTIMATOR.pkl`; `data/*/sentences.csv.gz` | `prod` etiquetado; sin documentación. |
| S02 | Configuración y evaluación | `professor/main.py` | Un parámetro posicional. |
| S03 | Producto | `submission/metrics.json` | Última ejecución. |
| S04 | Prueba | `tests/test_activity.py` | Sólo existencia. |
| S05 | Instrucciones e interfaz | `HOW_TO_RUN_ME.txt`; `src/main.py` | Plantilla vacía; instrucciones sobre `src/main.py`. |

### Contrato de evidencia actual

- **Notebook o código:** lee el argumento, evalúa el modelo en el conjunto elegido e imprime y persiste las métricas.
- **`submission/`:** `metrics.json` con `dataset`, `accuracy` y `balanced_accuracy` de la última ejecución.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `metrics.json`; no verifica conjunto, valores ni el rechazo de valores no admitidos. No hay prueba del profesor.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P403:** práctica de evaluación de un artefacto congelado; ningún artefacto.
- **Habilita para P407:** el mismo `ESTIMATOR.pkl` (203183 bytes) y los mismos `sentences.csv.gz` (mismos tamaños) se reutilizan con configuración por archivo.

## Trazabilidad y auditoría

Entrada revisada: P406 → `productos.C02`, `productos.C03`, `productos.C05`. C02 se sostiene (ejecución repetible parametrizada); C03 débilmente (métricas sin umbral ni criterio); C05 no se evidencia. Sin usuario, semántica de la clase ni decisión, el taller se lee como práctica de `argparse` (pregunta de auditoría 5); el modelo de texto es el artefacto operado, pero su capacidad analítica no está identificada.
