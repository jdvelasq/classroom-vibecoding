# P407 — Configuración por archivo: elegir el conjunto evaluado desde `CONFIG.json`

## Actividad actual implementada

**Implementación:** `implementation/productos/P407_config_file/`.

### Preguntas analíticas actuales

- ¿Cómo se declara fuera del código, en un archivo conservable y revisable, qué conjunto evalúa el modelo?

`CONFIG.json` contiene `{"dataset": "test"}`. `load_dataset_name` lee el archivo, valida que el valor pertenezca a `train`, `test` o `prod` y lanza `ValueError` con los valores admitidos si no. El resto del flujo es el de P406: mismo `ESTIMATOR.pkl` (203183 bytes), mismos `data/<conjunto>/sentences.csv.gz` y `submission/metrics.json` idéntico (test; accuracy 0,956; balanced accuracy 0,918). No hay `HOW_TO_RUN_ME.txt`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** desempeño del modelo en el conjunto configurado; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/metrics.json` producido según `CONFIG.json`.
- **Uso y límite:** permite fijar y revisar la configuración de una ejecución como archivo. El reporte no registra la ruta ni el contenido completo de la configuración, sólo `dataset`; no hay umbral ni decisión.
- **Disciplinas contribuyentes:** configuración externa en JSON al servicio de la ejecución repetible del mismo modelo.

### Highlights de contribución

- **H01 — Externaliza la configuración a un archivo y la valida explícitamente:** la decisión «queda fuera del código para poder conservar y revisar cada ejecución»; como JSON no restringe valores, la validación que en P406 hacía `argparse` con `choices` pasa a código propio (`config.get` + `ValueError`). Sin este hito, la configuración sólo existiría en el comando escrito, sin un artefacto versionable.
- **H02 — Repite el caso de P406 sin cambio de datos (caso y datos, límite):** artefacto, datos y métrica persistida son los de P406; la única variable es el mecanismo de configuración. La particularidad del caso (modelo de texto con `prod` etiquetado) se hereda sin nueva exigencia. Sin este hito no se perdería ninguna práctica sobre datos; queda como límite y como posible duplicación.

### Inventario técnico de implementación

- **Introduce:** archivo de configuración JSON en la raíz; validación manual de valores admitidos.
- **Reutiliza:** evaluación del clasificador de texto, métricas y persistencia de P406.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Configuración declarativa | H01 | `CONFIG.json` + `load_dataset_name` | Un parámetro; el reporte no conserva la configuración. |
| Validación de configuración | H01 | `ValueError` con valores admitidos | Sin prueba. |

### Relación técnica con actividades anteriores

Misma pregunta, mismo dato y mismo producto que P406 con nueva implementación de la configuración. Posible duplicación: P406 y P407 podrían ser una sola actividad que contraste ambos mecanismos; requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Configuración por archivo | S01, S02 | `implementation/productos/P407_config_file/CONFIG.json`; `implementation/productos/P407_config_file/professor/main.py`: `load_dataset_name` | Rama de error no probada. |
| H02 — Caso repetido | S03, S04 | `implementation/productos/P407_config_file/ESTIMATOR.pkl`; `implementation/productos/P407_config_file/data/*/sentences.csv.gz`; `implementation/productos/P407_config_file/submission/metrics.json` | Igualdad con P406 inferida por tamaños y contenido del reporte. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Configuración | `CONFIG.json` | Una clave. |
| S02 | Lectura y validación | `professor/main.py` | Validación manual. |
| S03 | Artefacto y datos | `ESTIMATOR.pkl`; `data/*/sentences.csv.gz` | Idénticos a P406. |
| S04 | Producto | `submission/metrics.json` | Idéntico a P406. |
| S05 | Prueba | `tests/test_activity.py` | Sólo existencia. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** lee y valida `CONFIG.json`, evalúa el modelo y persiste las métricas.
- **`submission/`:** `metrics.json` con el conjunto y dos métricas.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `metrics.json`; como el archivo es idéntico al de P406, no distingue el mecanismo usado. No hay prueba del profesor.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P406:** artefacto, datos, flujo de evaluación y valores admitidos.
- **Habilita para Pyyy:** no evidenciada dentro de P408–P413.

## Trazabilidad y auditoría

Entrada revisada: P407 → `productos.C02`, `productos.C03`, `productos.C05`. C02 se sostiene (configuración versionable); C03 y C05 no aportan evidencia nueva respecto de P406. Se lee como práctica de configuración de software (pregunta de auditoría 5) y como posible duplicado de P406.
