# P421 — Registro de modelos: promoción de un candidato a una etapa

## Actividad actual implementada

**Implementación:** `implementation/productos/P421_model_registry/`.

### Preguntas analíticas actuales

- ¿Qué artefacto está aprobado para producción, desde qué archivo, con qué métrica declarada y en qué momento se aprobó?

`CANDIDATES.json` lista un único candidato (`candidate_v1`, archivo `CANDIDATE_V1.pkl`, `test_accuracy` 0.91, estado `candidate`). `professor/main.py` recibe `--stage {production,archived}` y `--model-id` (por defecto `candidate_v1`). `find_candidate` busca el identificador y falla con `ValueError` si no existe; `promote_model` copia el pickle a `submission/model_registry/<stage>/model.pkl` y escribe `registry.json` con `model_id`, `stage`, `source_artifact`, `test_accuracy` y `promoted_at`. El registro persistido muestra la promoción de `candidate_v1` a `production`. `data/` está vacía.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la decisión es promover un candidato a una etapa; quién la toma y con qué criterio no se declara.
- **Producto terminal:** `submission/model_registry/production/` con el modelo aprobado y su registro.
- **Uso y límite:** deja trazable qué artefacto ocupa una etapa. No valida el candidato: la exactitud 0.91 se copia de `CANDIDATES.json` sin datos ni procedencia; no hay umbral de aprobación ni comparación con el modelo previo; una nueva promoción sobrescribe `model.pkl` y `registry.json` sin conservar historial.
- **Disciplinas contribuyentes:** gestión de artefactos de MLOps al servicio de declarar qué modelo está en uso.

### Highlights de contribución

- **H01 — Separa la promoción de la construcción del modelo:** el docstring de `main()` lo declara («La promoción separa la decisión operativa de la construcción del modelo») y el código sólo copia un artefacto ya entrenado a una etapa con un registro asociado. P420 producía corridas; aquí se decide cuál ocupa producción. Sin este hito, «estar en producción» no tendría un registro explícito.
- **H02 — Promueve por identificador estable, no por nombre de archivo:** `find_candidate` resuelve `model_id` contra `CANDIDATES.json` y `test_02_rejects_a_model_that_is_not_registered_as_a_candidate` verifica el rechazo de un identificador ausente; `test_01` promueve en un directorio temporal sin tocar la evidencia distribuida. Sin este hito, podría promoverse un archivo arbitrario.
- **H03 — Opera sobre un artefacto sin procedencia (caso y datos):** el candidato llega sin datos, sin tipo de modelo declarado y con una métrica escrita a mano; `CANDIDATE_V1.pkl` mide 203183 bytes, igual que `ESTIMATOR.pkl` de P406–P407 y los modelos de P424, pero la actividad no declara esa relación. El registro, por tanto, documenta una aprobación que no puede verificar. Este límite es la particularidad observable: el artefacto operado es intercambiable.

### Inventario técnico de implementación

- **Introduce:** catálogo de candidatos en JSON, etapas como directorios, copia con `shutil.copy2`, registro de promoción con marca temporal UTC.
- **Reutiliza:** `argparse` con `choices` (P406, P420); carga del módulo de profesor y `tmp_path` en pruebas.
- **Aplica en nuevo caso:** ninguno; no hay caso.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Registro por etapa | H01 | `model_registry/<stage>/model.pkl` + `registry.json` | Sin historial; una promoción sobrescribe la anterior. |
| Identificador estable | H02 | `find_candidate` con rechazo explícito | Un solo candidato. |
| Artefacto sin procedencia | H03 | Métrica declarada 0.91 sin datos | No hay validación ni umbral. |

### Relación técnica con actividades anteriores

Nuevo producto (registro de etapas). No consume las corridas de P420, cuyo índice ya tiene `model.pkl` y exactitud por corrida; P421 parte de otro artefacto y otra métrica. P424 usa un `REGISTRY.json` con esquema distinto (versiones en lugar de etapas). La continuidad registro → reversión es conceptual, no de artefactos.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Promoción separada | S02, S03 | `implementation/productos/P421_model_registry/professor/main.py`: `promote_model`, `main`; `implementation/productos/P421_model_registry/submission/model_registry/production/registry.json` | No hay criterio de promoción. |
| H02 — Identificador estable | S02, S04 | `implementation/productos/P421_model_registry/professor/main.py`: `find_candidate`; `implementation/productos/P421_model_registry/professor/test_main.py` | Las pruebas no cubren la etapa `archived`. |
| H03 — Sin procedencia | S01 | `implementation/productos/P421_model_registry/CANDIDATES.json`; `implementation/productos/P421_model_registry/CANDIDATE_V1.pkl` | La igualdad de tamaño con otros pickles no prueba identidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Candidato y su métrica | `CANDIDATES.json`; `CANDIDATE_V1.pkl` | Un candidato; métrica escrita a mano. |
| S02 | Lógica de promoción | `professor/main.py`; `src/main.py` | Sin umbral; sobrescribe la etapa. |
| S03 | Registro entregado | `submission/model_registry/production/` | Sólo la etapa `production`. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Promoción y rechazo; existencia de dos archivos. |
| S05 | Instrucciones | `HOW_TO_RUN_ME.txt` | Un comando con `--stage production`. |

### Contrato de evidencia actual

- **Notebook o código:** `find_candidate` y `promote_model`.
- **`submission/`:** `model_registry/production/model.pkl` y `registry.json`.
- **Pruebas:** `professor/test_main.py` verifica promoción a `production` en directorio temporal y rechazo de un identificador ausente. `tests/test_activity.py` exige que existan `model.pkl` y `registry.json`. Ninguna verifica que el modelo promovido sea el declarado ni que la métrica cumpla un criterio.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** no recibe artefactos; práctica de `argparse` de P406/P420.
- **Habilita para Pyyy:** no evidenciada; P424 trabaja con un registro propio de esquema distinto.

## Trazabilidad y auditoría

Entrada revisada: P421 → `productos.C02`, `productos.C03`, `productos.C05`. C02 y C05 (gobierno del artefacto en uso) se sostienen. C03 no tiene evidencia: no se valida el modelo frente a su uso; la métrica es declarada. Auditoría: el producto es un registro de etapa sin capacidad analítica identificable (se desconoce qué predice el modelo); se lee como mecánica genérica de MLOps. Riesgo de identidad no resuelto.
