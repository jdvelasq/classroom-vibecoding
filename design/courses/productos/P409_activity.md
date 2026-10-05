# P409 — Ramas y fusión: incorporar el consumidor del producto `factory_totals`

## Actividad actual implementada

**Implementación:** `implementation/productos/P409_branch_merge/`.

### Preguntas analíticas actuales

- ¿Cómo se prepara un cambio en la definición de un producto analítico de forma aislada y se integra después a la versión principal dejando visible su origen?

`HOW_TO_RUN_ME.txt` crea en `temp/branch_merge_case` un repositorio con rama inicial `main` y un primer commit de `product_card.md`; abre la rama `add-consumer`, reemplaza «Consumidor: Pendiente de definir» por «Consumidor: equipo de mantenimiento», confirma, vuelve a `main` y fusiona con `git merge --no-ff`. La evidencia es `git log --oneline -3` en `submission/git_log.txt`: `merge: add product consumer`, `chore: create product card` y `docs: define product consumer`. La plantilla ya trae la unidad definida en P408. `data/branch_merge_case.bundle` (715 bytes) no se menciona en las instrucciones.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** declarar el consumidor del producto; el valor incorporado es «equipo de mantenimiento».
- **Producto terminal:** historial con rama y commit de fusión sobre `product_card.md`.
- **Uso y límite:** muestra cómo aislar e integrar un cambio de definición. No hay revisión, conflicto ni criterio de aceptación: la fusión es incondicional y local.
- **Disciplinas contribuyentes:** ramas y fusión en Git al servicio de la evolución de la definición del producto.

### Highlights de contribución

- **H01 — Aísla un cambio de definición en una rama y lo integra con fusión explícita:** `git switch -c add-consumer`, `git branch` para identificar la rama activa, `git merge --no-ff` para «conservar un commit de fusión» y `git log --graph` para ver la topología. Extiende el commit lineal de P408. Sin este hito, P411 no tendría el modelo de rama que luego se integra mediante pull request.
- **H02 — Cambia el consumidor del producto respecto de la tarjeta previa (caso y datos):** la plantilla hereda de P408 métrica y unidad, pero restablece el consumidor como pendiente y lo define como «equipo de mantenimiento», mientras la tarjeta de P408 y la de P410 declaran «equipo de operaciones». El campo que se modifica es el usuario del producto, el elemento central de un contrato operativo, pero el cambio no se justifica ni se reconcilia. Sin este hito, el caso sería un archivo cualquiera; con él queda visible una inconsistencia en la continuidad del caso.

### Inventario técnico de implementación

- **Introduce:** `git init --initial-branch=main`, `git switch -c`, `git switch`, `git branch`, `git merge --no-ff -m`, `git log --oneline --graph -3`.
- **Reutiliza:** repositorio aislado en `temp/`, identidad fija y extracción de evidencia con `git -C` (P408).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Rama de cambio | H01 | `add-consumer` | Sin revisión. |
| Fusión explícita | H01 | `--no-ff` con mensaje | Sin conflicto. |
| Consumidor del producto | H02 | Campo «Consumidor» | Contradice P408 y P410. |

### Relación técnica con actividades anteriores

Misma tarjeta que P408 con nueva práctica (ramas). La continuidad del caso es parcial: hereda la unidad de P408 pero no su consumidor. No se observa duplicación técnica.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Rama y fusión | S02, S03, S04 | `implementation/productos/P409_branch_merge/HOW_TO_RUN_ME.txt`; `implementation/productos/P409_branch_merge/submission/git_log.txt` | El log no muestra el grafo ni el contenido. |
| H02 — Consumidor | S01 | `implementation/productos/P409_branch_merge/data/repository_template/product_card.md`; `implementation/productos/P408_version_control/data/repository_template/product_card.md`; `implementation/productos/P410_github_remote/data/repository_template/product_card.md` | La inconsistencia puede ser deliberada; no está declarada. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Tarjeta de producto | `data/repository_template/product_card.md` | Consumidor pendiente. |
| S02 | Instrucciones | `HOW_TO_RUN_ME.txt` | Fusión local sin revisión. |
| S03 | Evidencia | `submission/git_log.txt` | Tres líneas. |
| S04 | Prueba | `tests/test_activity.py` | Sólo existencia. |
| S05 | Material auxiliar | `data/branch_merge_case.bundle` | No referido por las instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** no hay código; secuencia de comandos en `HOW_TO_RUN_ME.txt`.
- **`submission/`:** `git_log.txt` con tres commits, incluido el de fusión.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `git_log.txt`; no verifica la fusión ni el número de commits.
- **Trazabilidad:** `productos.C01` y `productos.C04`.

### Dependencias en la secuencia

- **Recibe de P408:** tarjeta con la unidad de medida ya definida; práctica de commit.
- **Habilita para Pyyy:** no evidenciada como artefacto; la práctica de rama reaparece en P411.

## Trazabilidad y auditoría

Entrada revisada: P409 → `productos.C01`, `productos.C04`. C01 se sostiene por la definición del consumidor. C04 (uso responsable mediante control de acceso, revisión humana o retroalimentación) no se evidencia: la fusión es local y sin revisión. El producto versionado es identificable, pero el taller se lee como práctica de ramas en Git (pregunta de auditoría 5).
