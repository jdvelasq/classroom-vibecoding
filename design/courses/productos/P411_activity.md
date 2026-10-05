# P411 — Pull request: incorporar el responsable del producto mediante revisión en GitHub

## Actividad actual implementada

**Implementación:** `implementation/productos/P411_pull_request/`.

### Preguntas analíticas actuales

- ¿Cómo se propone, revisa e integra en la versión publicada un cambio en la definición de un producto analítico?

`HOW_TO_RUN_ME.txt` declara que el taller «continúa P410»: copia `../P410_github_remote/temp/github_remote_case` a `temp/pull_request_case`, abre la rama `add-owner`, agrega a `product_card.md` «Responsable: líder de operaciones», confirma y publica la rama; en GitHub crea un pull request de `add-owner` hacia `main` con título «docs: define product owner», pide revisar el cambio mostrado y fusionarlo; finalmente actualiza `main` con `git pull --ff-only` y guarda `git log --oneline -2`. `submission/git_log.txt` contiene `565b098 merge: add product owner` y `4d8becc chore: create product card`. `data/repository_template/` sólo tiene `.gitkeep`; `data/pull_request_case.bundle` (714 bytes) no se menciona.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** asignar un responsable al producto; responsable declarado: «líder de operaciones».
- **Producto terminal:** tarjeta del producto con responsable, integrada en `main` remoto mediante pull request.
- **Uso y límite:** muestra el flujo propuesta–revisión–integración en plataforma. La revisión la hace el mismo estudiante que propone, sin criterio de aprobación ni segundo revisor; la evidencia persistida no corresponde a la secuencia instruida.
- **Disciplinas contribuyentes:** flujo de colaboración en GitHub al servicio de la gobernanza de la definición del producto.

### Highlights de contribución

- **H01 — Integra un cambio de definición mediante pull request:** rama publicada con `git push -u origin add-owner`, verificación de rama base y de comparación, revisión del diff en GitHub, fusión remota y sincronización local con `git pull --ff-only`, que rechaza actualizar si exigiría una fusión local. Extiende la fusión local de P409 a una integración revisable en plataforma. Sin este hito, P415 no tendría el flujo de pull request al que añade un check automático.
- **H02 — Añade la autoridad responsable al contrato del producto (caso y datos):** con el responsable, la tarjeta acumulada en P408–P411 reúne producto, consumidor, métrica, unidad y responsable. El campo agregado asigna quién responde por el producto, pero no hay criterio de revisión ni responsabilidades descritas. Sin este hito, la tarjeta no declararía autoridad.
- **H03 — Deja una evidencia que no corresponde al flujo instruido (límite):** siguiendo las instrucciones, `git log --oneline -2` mostraría el commit de fusión creado por GitHub y el commit «docs: define product owner»; la evidencia persistida muestra «merge: add product owner» y «chore: create product card», y el hash de este último (`4d8becc`) difiere del de P410 (`60a3756`). La prueba no puede detectarlo. Sin este hito no se vería que la evidencia del profesor fue producida por otra vía.

### Inventario técnico de implementación

- **Introduce:** rama remota, pull request en GitHub (creación, revisión, fusión), `git pull --ff-only`.
- **Reutiliza:** repositorio y remoto de P410; rama de cambio de P409.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Pull request | H01 | Base `main`, comparación `add-owner`, fusión en GitHub | Autorrevisión; no persistido. |
| Sincronización segura | H01 | `pull --ff-only` | Sin conflicto ensayado. |
| Responsable del producto | H02 | Campo «Responsable» | Sin criterio de revisión. |
| Evidencia del flujo | H03 | `git_log.txt` de dos líneas | No coincide con el flujo instruido. |

### Relación técnica con actividades anteriores

Misma tarjeta con nueva práctica: integración por revisión en plataforma frente a la fusión local de P409. Depende operativamente de P410 (repositorio y remoto). No se observa duplicación, aunque P409 y P411 integran ramas con distinta mediación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Pull request | S01 | `implementation/productos/P411_pull_request/HOW_TO_RUN_ME.txt` | Sin evidencia persistida de la revisión. |
| H02 — Responsable | S01, S02 | `implementation/productos/P411_pull_request/HOW_TO_RUN_ME.txt` | La tarjeta resultante no está persistida. |
| H03 — Evidencia divergente | S02, S03, S04 | `implementation/productos/P411_pull_request/submission/git_log.txt`; `implementation/productos/P410_github_remote/submission/git_log.txt`; `implementation/productos/P411_pull_request/data/pull_request_case.bundle` | Origen de la evidencia no documentado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Instrucciones | `HOW_TO_RUN_ME.txt` | Depende de `../P410_github_remote/temp/`. |
| S02 | Evidencia | `submission/git_log.txt` | Dos líneas; no coincide con el flujo. |
| S03 | Prueba | `tests/test_activity.py` | Sólo existencia. |
| S04 | Material auxiliar | `data/pull_request_case.bundle`; `data/repository_template/.gitkeep` | Bundle no referido; plantilla vacía. |

### Contrato de evidencia actual

- **Notebook o código:** no hay código; secuencia en `HOW_TO_RUN_ME.txt`.
- **`submission/`:** `git_log.txt` con dos commits.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `git_log.txt`; no verifica el pull request, la fusión ni el responsable.
- **Trazabilidad:** `productos.C01` y `productos.C04`.

### Dependencias en la secuencia

- **Recibe de P410:** carpeta `temp/github_remote_case` y remoto personal; de P409, la práctica de rama.
- **Habilita para P415:** P415 copia `../P411_pull_request/temp/pull_request_case` y repite el flujo de pull request con un check automático.

## Trazabilidad y auditoría

Entrada revisada: P411 → `productos.C01`, `productos.C04`. C01 se sostiene por el responsable añadido a la definición del producto; C04 parcialmente por la revisión humana previa a integrar, aunque sea autorrevisión. El producto gobernado es identificable; el taller se lee principalmente como práctica de GitHub (pregunta de auditoría 5). La dependencia de rutas hermanas (`../P410_github_remote/`) supone que la distribución conserva los nombres y la adyacencia de las actividades.
