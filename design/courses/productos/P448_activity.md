# P448 — Respaldo y restauración de un artefacto de operación

## Actividad actual implementada

**Implementación:** `implementation/productos/P448_backup_restore/`.

### Preguntas analíticas actuales

- ¿Puede restaurarse exactamente, desde su respaldo, el registro que indica qué versión del modelo está en producción?

`data/registry.json` tiene 51 bytes: `{"production_version":"v1","model":"factory-risk"}`. `professor/main.py` (`backup_and_restore`) copia el archivo a `submission/registry.backup.json` y luego copia el respaldo a `submission/registry.restored.json`, devolviendo el contenido restaurado. Ambos archivos persistidos son idénticos al original. No se simula pérdida ni corrupción del original antes de restaurar, no se respalda el binario del modelo y no se registra huella ni fecha. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** que el respaldo sea «más que una copia olvidada» (docstring); usuario no evidenciado.
- **Producto terminal:** par respaldo/restauración del registro de producción.
- **Uso y límite:** demuestra que el contenido restaurado coincide con el respaldado. No demuestra recuperación ante una falla real, ni restaura el artefacto analítico (modelo o datos) al que el registro apunta.
- **Disciplinas contribuyentes:** operación de sistemas (respaldo y recuperación) al servicio de la continuidad de la capacidad en producción.

### Highlights de contribución

- **H01 — Respalda el puntero de producción, no el modelo (caso y datos):** el artefacto es el registro que declara la versión en producción de `factory-risk`. Ese registro no coincide con `P424_model_rollback/REGISTRY.json` (producción `v2`, versiones `MODEL_V1.pkl` y `MODEL_V2.pkl` sin caso documentado en el registro) y en el curso no se evidencia un modelo `factory-risk` entrenado: el riesgo por fábrica aparece como regla de umbral en P425/P426. El artefacto es un sustituto mínimo; se registra esa ausencia como límite. Sin este hito, la secuencia de registro (P421) y reversión (P424) no consideraría la pérdida del propio registro.
- **H02 — Comprueba la restauración por igualdad de bytes:** la restauración parte del respaldo, no del original; la prueba de profesor, en `tmp_path`, exige que respaldo y restaurado sean byte a byte iguales al origen y que el contenido recuperado sea el esperado. `tests/test_activity.py` sólo exige ambos archivos. Sin este hito, el respaldo no tendría verificación de recuperabilidad.

### Inventario técnico de implementación

- **Introduce:** respaldo y restauración con `shutil.copy2` y verificación por bytes.
- **Contrasta:** recuperación de un artefacto (P448) frente a cambio de versión activa (P424).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Objeto respaldado | H01 | Registro de versión en producción | No incluye el modelo; no coincide con P424. |
| Restauración verificada | H02 | Restaurar desde respaldo; igualdad de bytes | Sin pérdida simulada ni huella persistida. |

### Relación técnica con actividades anteriores

Extiende el registro de producción de P421 y P424 a su recuperación, sin consumir sus archivos: el registro de P448 tiene otra estructura y otro modelo. Posible inconsistencia de caso entre `factory-risk` (P448) y los binarios de P421/P424, cuyo caso no declara el registro, que requiere decisión posterior.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Puntero de producción | S01 | `implementation/productos/P448_backup_restore/data/registry.json`; `implementation/productos/P424_model_rollback/REGISTRY.json`; `implementation/productos/P425_api_contract/professor/main.py`: `classify_risk` | No se evidencia modelo `factory-risk`. |
| H02 — Restauración por bytes | S02, S03, S04 | `implementation/productos/P448_backup_restore/professor/main.py`: `backup_and_restore`; `implementation/productos/P448_backup_restore/professor/test_main.py`; `implementation/productos/P448_backup_restore/submission/registry.restored.json` | El original no se pierde antes de restaurar. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Artefacto respaldado | `data/registry.json` | 51 bytes; sólo puntero. |
| S02 | Respaldo y restauración | `professor/main.py` | Copia de copia; sin `main()`. |
| S03 | Entregables | `submission/registry.backup.json`; `submission/registry.restored.json` | Idénticos; sin huella ni fecha. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: bytes; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** copia el registro a respaldo y del respaldo a restaurado.
- **`submission/`:** `registry.backup.json` y `registry.restored.json`.
- **Pruebas:** la de profesor verifica igualdad de bytes y contenido; `test_01` verifica existencia de ambos archivos.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P421/P424:** la noción de registro de versión en producción; ningún artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P448 mapea `productos.C02` y `productos.C05` («recuperar»). C05 se sostiene en la restauración verificada. El objeto recuperado no es la capacidad analítica sino su puntero, y el modelo nombrado no existe en el curso. Auditoría pregunta 5: la actividad puede leerse como práctica genérica de respaldo de archivos.
