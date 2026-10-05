# P415 — GitHub Actions: verificación automática del indicador antes de fusionar

## Actividad actual implementada

**Implementación:** `implementation/productos/P415_github_actions/`.

### Preguntas analíticas actuales

- ¿Cómo se obtiene una señal visible de que el indicador sigue produciendo el resultado acordado antes de integrar un cambio a `main`?

El taller continúa el repositorio personal de P411: copia `../P411_pull_request/temp/pull_request_case`, abre la rama `add-quality-check` y añade desde `data/repository_template/` el flujo `.github/workflows/quality.yml`, `requirements.txt`, el dataset de cuatro filas, `src/main.py` y `tests/test_environment_report.py`. Según `HOW_TO_RUN_ME.txt`, el flujo se dispara con cada `push` y `pull_request`, crea `.venv`, instala `requirements.txt` y ejecuta la prueba del reporte. El estudiante abre un pull request, espera el check verde `Quality check` y sólo entonces fusiona. No hay código de profesor: la evidencia es `submission/git_log.txt`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la decisión observable es fusionar o no un cambio, condicionada al check verde; el responsable es el estudiante en su repositorio. No hay usuario del indicador dentro del taller.
- **Producto terminal:** un repositorio cuyo `main` incorpora un flujo de integración continua que verifica el indicador por fábrica; evidencia en `submission/git_log.txt`.
- **Uso y límite:** permite mostrar que el cambio entró por pull request con verificación automática. El log persistido sólo prueba el commit y la fusión, no que el check haya sido verde.
- **Disciplinas contribuyentes:** integración continua y control de versiones al servicio de proteger un indicador acordado frente a cambios.

### Highlights de contribución

- **H01 — Condiciona la fusión a una verificación remota:** el flujo `Quality check` corre en `push` y `pull_request`, y `HOW_TO_RUN_ME.txt` instruye «Solo cuando el check esté en verde, haga Merge pull request». P411 fusionaba un pull request tras revisión humana; P415 añade una señal automática antes de la decisión. Sin este hito, la verificación de P412–P414 dependería de que alguien la ejecutara localmente.
- **H02 — Reutiliza el repositorio y la prueba existentes (caso y datos):** el caso no cambia: mismo dataset de cuatro filas y prueba del reporte de P412 (`tests/test_environment_report.py`), ahora dentro del repositorio que contiene la tarjeta de producto construida en P408–P411. La continuidad del repositorio es la particularidad: el producto verificado y su tarjeta conviven en el mismo historial (`submission/git_log.txt` muestra `Merge pull request #2 from add-quality-check`). No hay particularidad del dato; el indicador sigue siendo trivial. Sin este hito, el flujo se enseñaría sobre un repositorio ajeno a la secuencia.

### Inventario técnico de implementación

- **Introduce:** archivo de flujo en `.github/workflows/` con disparadores `push` y `pull_request`; check de pull request como condición de fusión.
- **Reutiliza:** repositorio de P411, ramas, pull request y `git pull --ff-only` (P409–P411); producto y prueba `unittest` de P412.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Integración continua en pull request | H01 | Flujo `Quality check` en `push`/`pull_request` | El digest muestra sólo la cabecera de `quality.yml`; los pasos se conocen por `HOW_TO_RUN_ME.txt`. |
| Repositorio continuo del producto | H02 | Copia de `P411_pull_request/temp/pull_request_case` | Depende de que el estudiante conserve `temp/` de P411. |

### Relación técnica con actividades anteriores

Misma pregunta y dato que P412–P414; nueva exigencia de evidencia (check remoto previo a la fusión). Es la primera vez que la verificación del indicador se ejecuta fuera del equipo del estudiante. No duplica P411: añade la condición automática a la fusión.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Fusión condicionada | S02, S03 | `implementation/productos/P415_github_actions/data/repository_template/.github/workflows/quality.yml`; `implementation/productos/P415_github_actions/HOW_TO_RUN_ME.txt` | No hay evidencia persistida del resultado del check. |
| H02 — Repositorio y prueba reutilizados | S01, S04 | `implementation/productos/P415_github_actions/HOW_TO_RUN_ME.txt` (paso 1); `implementation/productos/P415_github_actions/data/repository_template/tests/test_environment_report.py`; `implementation/productos/P415_github_actions/submission/git_log.txt` | La equivalencia con P412 se infiere de nombre y propósito; los tamaños difieren levemente. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Plantilla del producto | `data/repository_template/data/`; `data/repository_template/src/main.py`; `data/repository_template/requirements.txt` | Indicador de cuatro filas. |
| S02 | Flujo de CI | `data/repository_template/.github/workflows/quality.yml` | Un trabajo; disparadores `push` y `pull_request`. |
| S03 | Prueba ejecutada en CI | `data/repository_template/tests/test_environment_report.py` | `unittest`, un resultado exacto. |
| S04 | Evidencia y prueba de participación | `submission/git_log.txt`; `tests/test_activity.py` | Sólo existencia del log. |
| S05 | Secuencia | `HOW_TO_RUN_ME.txt` | Requiere `temp/` de P411. |

### Contrato de evidencia actual

- **Notebook o código:** no hay solución de profesor; los pasos están en `HOW_TO_RUN_ME.txt` (excepción justificada en `structure-audit.md`).
- **`submission/`:** `git_log.txt` con dos líneas: el commit `ci: add factory report check` y la fusión del pull request #2.
- **Pruebas:** `tests/test_activity.py` exige que exista `git_log.txt`. No verifica su contenido, la existencia del flujo ni el estado del check.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P411:** el repositorio local `temp/pull_request_case` y su remoto personal; de P412, producto y prueba.
- **Habilita para P416:** P416 copia `../P415_github_actions/temp/github_actions_case` y reemplaza `quality.yml` y `test_environment_report.py`.

## Trazabilidad y auditoría

Entrada revisada: P415 → `productos.C02`, `productos.C05`. C02 se sostiene (automatización e integración). C05 sólo de forma indirecta (una señal antes de publicar), sin monitoreo en operación. Auditoría (pregunta 5): el taller se lee como entrenamiento en GitHub Actions; el producto analítico no cambia y no tiene usuario ni decisión de negocio dentro del taller. Riesgo de identidad no resuelto, compartido con P408–P416.
