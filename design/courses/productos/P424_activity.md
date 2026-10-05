# P424 — Reversión de modelo: volver a una versión registrada sin reentrenar

## Actividad actual implementada

**Implementación:** `implementation/productos/P424_model_rollback/`.

### Preguntas analíticas actuales

- Cuando la versión en producción falla, ¿cómo se restituye una versión anterior registrada y se deja constancia de la reversión?

`REGISTRY.json` declara `production_version` `v2` y dos versiones (`v1` → `MODEL_V1.pkl`, `v2` → `MODEL_V2.pkl`; ambos de 203183 bytes). `professor/main.py` recibe `--to-version`; `rollback` rechaza versiones no registradas con `ValueError`, copia el pickle de la versión objetivo a `submission/production/model.pkl` y escribe `rollback_record.json` con `previous_version`, `production_version` y `rolled_back_at`. El registro persistido muestra `v2` → `v1`. `data/` está vacía.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** revertir la versión activa; la causa de la falla, quién decide y con qué evidencia no se declaran.
- **Producto terminal:** `submission/production/model.pkl` (modelo activo) y `rollback_record.json`.
- **Uso y límite:** muestra que la reversión es una operación preparada y trazable. `REGISTRY.json` no se actualiza tras la reversión (sigue indicando `v2`), por lo que registro y modelo activo divergen; no se registra el motivo ni se impide «revertir» a la versión vigente.
- **Disciplinas contribuyentes:** gestión de versiones de artefactos al servicio de la recuperación de una capacidad.

### Highlights de contribución

- **H01 — Restituye una versión por copia, sin reconstruir:** `rollback` sólo copia el artefacto registrado; `test_rollback_restores_a_registered_version` verifica que los bytes de `model.pkl` coinciden con `MODEL_V1.pkl` y que el registro guardado indica `v1`, usando `monkeypatch` para escribir en un directorio temporal. Es la primera actividad de recuperación del curso. Sin este hito, volver atrás exigiría reentrenar o reconstruir manualmente.
- **H02 — Deja constancia de la versión previa y la nueva:** `rollback_record.json` conserva `previous_version`, `production_version` y marca temporal UTC; `test_rollback_rejects_an_unknown_version` exige el rechazo de `v3`. P421 sobrescribía la etapa sin historial; aquí el registro de reversión preserva de dónde se vino. Sin este hito, la reversión no sería auditable.
- **H03 — Opera versiones indistinguibles y sin motivo (caso y datos):** las dos versiones tienen el mismo tamaño que `CANDIDATE_V1.pkl` (P421) y `ESTIMATOR.pkl` (P406–P407); no se declara qué modelo son ni en qué difieren, y ninguna evidencia (por ejemplo, la alerta de P423) motiva la reversión. Este límite es la particularidad observable: la operación se ejercita sin una falla de la capacidad que la justifique.

### Inventario técnico de implementación

- **Introduce:** registro de versiones con versión activa, reversión por copia, registro de reversión.
- **Extiende:** registro de modelos de P421 de etapas a versiones; pruebas con `monkeypatch` sobre la ruta de salida.
- **Reutiliza:** `argparse`, `shutil.copy2`, marca temporal UTC (P421).
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Reversión por copia | H01 | `shutil.copy2` de la versión objetivo; igualdad de bytes verificada | El registro maestro no se actualiza. |
| Registro de reversión | H02 | `previous_version`, `production_version`, `rolled_back_at` | Sin motivo ni responsable. |
| Versiones sin procedencia | H03 | Dos pickles de igual tamaño | No se puede saber si difieren. |

### Relación técnica con actividades anteriores

Complementa P421 (promover) con revertir, pero con un registro de esquema distinto y sin consumir su salida. P423 produce una alerta que podría motivar la reversión; la relación no está implementada. P448 (posterior) respalda y restaura un `registry.json` de producción («factory-risk»), con continuidad temática y sin artefacto compartido.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Reversión por copia | S02, S04 | `implementation/productos/P424_model_rollback/professor/main.py`: `rollback`; `implementation/productos/P424_model_rollback/professor/test_main.py` | La igualdad de bytes no distingue v1 de v2 si fueran idénticos. |
| H02 — Registro de reversión | S02, S03, S04 | `implementation/productos/P424_model_rollback/submission/production/rollback_record.json`; `implementation/productos/P424_model_rollback/professor/test_main.py` | `REGISTRY.json` queda en `v2`. |
| H03 — Versiones sin motivo | S01 | `implementation/productos/P424_model_rollback/REGISTRY.json`; `implementation/productos/P424_model_rollback/MODEL_V1.pkl`; `implementation/productos/P424_model_rollback/MODEL_V2.pkl` | El tamaño igual no prueba identidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Registro y versiones | `REGISTRY.json`; `MODEL_V1.pkl`; `MODEL_V2.pkl` | Dos versiones sin procedencia. |
| S02 | Lógica de reversión | `professor/main.py`; `src/main.py` | No actualiza `REGISTRY.json`; no registra motivo. |
| S03 | Evidencia entregada | `submission/production/` | Modelo activo y registro de reversión. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Reversión y rechazo; existencia de dos archivos. |
| S05 | Instrucciones | `HOW_TO_RUN_ME.txt` | Un comando `--to-version v1`. |

### Contrato de evidencia actual

- **Notebook o código:** `rollback(target_version)`.
- **`submission/`:** `production/model.pkl` y `production/rollback_record.json` (`v2` → `v1`).
- **Pruebas:** `professor/test_main.py` verifica restitución por bytes, contenido del registro y rechazo de versión ausente, sin tocar la evidencia distribuida. `tests/test_activity.py` exige que existan ambos archivos.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P421:** práctica de registro con copia de artefacto y marca temporal; no recibe artefactos.
- **Habilita para Pyyy:** no evidenciada (P448 trata un registro distinto).

## Trazabilidad y auditoría

Entrada revisada: P424 → `productos.C02`, `productos.C03`, `productos.C05`. C05 (recuperación) se sostiene; C02 secundario. C03 sin evidencia: no se valida ninguna versión antes ni después de revertir. Auditoría: mecánica de recuperación genérica sobre artefactos cuyo contenido analítico se desconoce; riesgo de identidad no resuelto.
