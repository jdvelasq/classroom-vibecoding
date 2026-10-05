# P408 — Control de versiones: versionar la definición del producto `factory_totals`

## Actividad actual implementada

**Implementación:** `implementation/productos/P408_version_control/`.

### Preguntas analíticas actuales

- ¿Cómo se deja una versión recuperable y revisable de una decisión sobre la definición de un producto analítico?

`HOW_TO_RUN_ME.txt` guía a copiar `data/repository_template/` a `temp/version_control_case`, iniciar un repositorio Git con identidad fija («Estudiante»), reemplazar en `product_card.md` «Unidad de medida: Pendiente de definir» por «unidades producidas por fábrica y día», revisar con `git diff`, confirmar con `git commit -m "docs: define unit of measure"` y guardar `git log --oneline -1` en `submission/git_log.txt`. La tarjeta declara «Producto analítico: factory_totals», «Consumidor: equipo de operaciones» y «Métrica: producción acumulada». `submission/git_log.txt` contiene `7c4638b docs: define unit of measure`. `data/version_control_case.bundle` (482 bytes) no se menciona en las instrucciones.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** fijar la unidad de medida del producto; consumidor declarado en la tarjeta: «equipo de operaciones».
- **Producto terminal:** historial Git de `product_card.md` con un commit que define la unidad, evidenciado en `submission/git_log.txt`.
- **Uso y límite:** muestra que la definición de un indicador puede versionarse como un cambio revisable. No versiona el código ni los datos del indicador, y la evidencia es una línea de log que no prueba el contenido del cambio.
- **Disciplinas contribuyentes:** control de versiones con Git al servicio de la definición documentada de un producto.

### Highlights de contribución

- **H01 — Versiona una decisión semántica del producto, no código (caso y datos):** el cambio confirmado define la unidad de medida de `factory_totals`, el indicador que P400 calcula como suma por fábrica de la producción diaria de sus máquinas; la tarjeta reúne consumidor, métrica y unidad, primer esbozo de contrato operativo del producto en el curso. Sin este hito, el control de versiones se ejercitaría sobre un archivo arbitrario; con él, el objeto versionado es la definición del indicador.
- **H02 — Crea una versión recuperable con el ciclo revisar–preparar–confirmar:** `git diff` antes de `git add`, `git status` para ver el área de preparación, mensaje con prefijo convencional `docs:` y `git log --oneline -1`; el repositorio se crea en `temp/` para no tocar el repositorio del curso, y la evidencia se extrae con `git -C`. Primera actividad de Git del curso. Sin este hito, las actividades P409–P411 no tendrían base.

### Inventario técnico de implementación

- **Introduce:** `git init`, `git config` local, `git diff`, `git add`, `git status`, `git commit -m`, `git log --oneline -1`, `git -C`; repositorio aislado en `temp/`; tarjeta de producto en Markdown.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Tarjeta de producto | H01 | Producto, consumidor, métrica, unidad | Tres campos; sin entradas, límites ni nivel de servicio. |
| Commit revisado | H02 | `diff` → `add` → `commit` | Evidencia de una línea. |

### Relación técnica con actividades anteriores

Cambia de objeto: de código y artefactos (P400–P407) a la definición documentada del producto de P400. No reutiliza código ni datos de P400; sólo su nombre de producto y su semántica.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Definición versionada | S01 | `implementation/productos/P408_version_control/data/repository_template/product_card.md` | Vínculo con P400 por nombre del producto. |
| H02 — Ciclo de commit | S02, S03, S04 | `implementation/productos/P408_version_control/HOW_TO_RUN_ME.txt`; `implementation/productos/P408_version_control/submission/git_log.txt` | La línea de log no prueba el contenido del cambio. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Tarjeta de producto | `data/repository_template/product_card.md` | Tres campos. |
| S02 | Instrucciones | `HOW_TO_RUN_ME.txt` | Identidad Git fija «Estudiante». |
| S03 | Evidencia | `submission/git_log.txt` | Una línea. |
| S04 | Prueba | `tests/test_activity.py` | Sólo existencia. |
| S05 | Material auxiliar | `data/version_control_case.bundle` | No referido por las instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** no hay código; la secuencia de comandos está en `HOW_TO_RUN_ME.txt`.
- **`submission/`:** `git_log.txt` con hash y mensaje del commit.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `git_log.txt`; no verifica mensaje, número de commits ni contenido de la tarjeta.
- **Trazabilidad:** `productos.C01` y `productos.C02`.

### Dependencias en la secuencia

- **Recibe de P400:** nombre y semántica del producto `factory_totals`; ningún archivo.
- **Habilita para P409:** la plantilla de P409 parte de la tarjeta con la unidad ya definida en P408.

## Trazabilidad y auditoría

Entrada revisada: P408 → `productos.C01`, `productos.C02`. C01 se sostiene mínimamente (consumidor, métrica y unidad del producto); C02 por la versión recuperable. El producto analítico versionado es identificable (`factory_totals`), lo que ancla la práctica de Git a una capacidad concreta; aun así, el contenido técnico es entrenamiento básico en Git (pregunta de auditoría 5).
