# P416 — GitHub Actions con Nox: la misma verificación local y remota

## Actividad actual implementada

**Implementación:** `implementation/productos/P416_github_actions_nox/`.

### Preguntas analíticas actuales

- ¿Cómo se garantiza que el computador del estudiante y GitHub comprueben el indicador de la misma manera?

El taller copia `../P415_github_actions/temp/github_actions_case`, abre la rama `add-nox-check`, añade `noxfile.py`, sustituye `src/main.py` y la prueba por las versiones de P414 (`tests/test_report.py`), agrega `.github/workflows/tests.yml` y retira con `git rm` el flujo `quality.yml` y `tests/test_environment_report.py` de P415. Antes de publicar, el estudiante ejecuta localmente `python3 -m nox -s tests`; según `HOW_TO_RUN_ME.txt`, `tests.yml` instala Nox y ejecuta esa misma sesión en cada `push` y `pull_request`. La fusión se condiciona al check verde `Nox tests`. La evidencia es `submission/git_log.txt`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** fusionar un cambio sólo con el check verde; no hay usuario del indicador dentro del taller.
- **Producto terminal:** repositorio cuyo `main` verifica el indicador por fábrica mediante una única sesión Nox, local y remota.
- **Uso y límite:** elimina la divergencia entre dos definiciones de la verificación (la de P414 local y la de P415 en CI). No cambia el indicador ni su criterio, y el log persistido no demuestra el resultado del check.
- **Disciplinas contribuyentes:** integración continua y automatización de tareas al servicio de una verificación única del indicador.

### Highlights de contribución

- **H01 — Unifica la definición de la verificación:** el flujo `tests.yml` delega en `noxfile.py`, y el paso 3 exige ejecutar la misma sesión localmente antes de publicar. Contrasta con P415, donde el flujo instalaba dependencias y ejecutaba la prueba por su cuenta. Sin este hito, local y CI podrían divergir sin que el estudiante lo note.
- **H02 — Retira explícitamente la verificación reemplazada (caso y datos):** `git rm .github/workflows/quality.yml tests/test_environment_report.py` deja una sola prueba del mismo indicador de cuatro filas en el repositorio continuo de P408–P415 (`Merge pull request #3 from add-nox-check`). La particularidad es del repositorio, no del dato: el historial acumula el producto, su tarjeta y su verificación. Sin este hito, convivirían dos pruebas del mismo resultado.

### Inventario técnico de implementación

- **Introduce:** flujo de CI que instala Nox y ejecuta una sesión; retiro versionado de una verificación anterior con `git rm`.
- **Reutiliza:** `noxfile.py`, `src/main.py` y `tests/test_report.py` de P414; repositorio, ramas y pull request de P411/P415.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Paridad local/CI | H01 | Flujo que ejecuta `nox -s tests` | Pasos del flujo descritos en `HOW_TO_RUN_ME.txt`; digest muestra sólo cabecera. |
| Sustitución de verificación | H02 | `git rm` del flujo y prueba de P415 | Sin evidencia persistida del árbol final. |

### Relación técnica con actividades anteriores

Combina P414 (Nox local) y P415 (CI remota) sin nueva pregunta ni dato. Es una composición deliberada de dos actividades previas. Posible solapamiento con P414–P415 que requiere decisión posterior de curso; la contribución distinguible es la paridad local/remota y el retiro de la verificación duplicada.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Verificación única | S02, S03 | `implementation/productos/P416_github_actions_nox/data/repository_template/.github/workflows/tests.yml`; `implementation/productos/P416_github_actions_nox/data/repository_template/noxfile.py`; `implementation/productos/P416_github_actions_nox/HOW_TO_RUN_ME.txt` | No hay evidencia persistida de ejecución local ni remota. |
| H02 — Retiro de verificación previa | S01, S04 | `implementation/productos/P416_github_actions_nox/HOW_TO_RUN_ME.txt` (paso 2); `implementation/productos/P416_github_actions_nox/submission/git_log.txt` | El log no muestra los archivos retirados. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Plantilla del producto y prueba | `data/repository_template/src/main.py`; `data/repository_template/tests/test_report.py`; `data/repository_template/data/` | Indicador de cuatro filas. |
| S02 | Flujo de CI | `data/repository_template/.github/workflows/tests.yml` | Ejecuta una sesión Nox. |
| S03 | Sesión Nox | `data/repository_template/noxfile.py`; `data/repository_template/requirements.txt` | Una sesión `tests`. |
| S04 | Evidencia y prueba de participación | `submission/git_log.txt`; `tests/test_activity.py` | Sólo existencia del log. |
| S05 | Secuencia | `HOW_TO_RUN_ME.txt` | Requiere `temp/` de P415. |

### Contrato de evidencia actual

- **Notebook o código:** sin solución de profesor; pasos en `HOW_TO_RUN_ME.txt`.
- **`submission/`:** `git_log.txt` con el commit `ci: run nox tests` y la fusión del pull request #3.
- **Pruebas:** `tests/test_activity.py` exige que exista `git_log.txt`; no verifica contenido, flujo ni estado del check.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P415:** repositorio `temp/github_actions_case`; de P414, `noxfile.py`, `src/main.py` y la prueba del reporte.
- **Habilita para Pyyy:** no evidenciada; ninguna actividad posterior copia `temp/github_actions_nox_case`.

## Trazabilidad y auditoría

Entrada revisada: P416 → `productos.C02`, `productos.C05`. C02 se sostiene; C05 sin evidencia propia. Auditoría (pregunta 5): taller de herramientas de CI sobre un indicador sin usuario ni decisión; riesgo de identidad no resuelto. Cierra la cadena de repositorio P408–P416, que no continúa en actividades posteriores.
