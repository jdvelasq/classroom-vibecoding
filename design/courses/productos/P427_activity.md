# P427 — Configuración secreta: credencial por variable de ambiente sin exponer su valor

## Actividad actual implementada

**Implementación:** `implementation/productos/P427_secret_config/`.

### Preguntas analíticas actuales

- ¿Cómo recibe una aplicación una credencial sin escribirla en el código, en el repositorio ni en sus reportes?

`professor/main.py` lee `ANALYTICS_API_KEY` con `os.environ.get`; si falta o está vacía, `get_api_key` lanza `RuntimeError` con el nombre de la variable. `main()` escribe `submission/secret_config_report.json` con `secret_name` y `configured: true`, sin el valor. `HOW_TO_RUN_ME.txt` crea la variable con `export ANALYTICS_API_KEY="clave-de-practica"` (declarada como no real), ejecuta el programa y la retira con `unset`. `data/` está vacía.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/secret_config_report.json`, evidencia de configuración presente sin revelar el secreto.
- **Uso y límite:** muestra cómo separar una credencial del código y de la evidencia. La credencial no protege ni habilita nada: no se usa para autenticar el servicio de P425–P426 ni para acceder a datos.
- **Disciplinas contribuyentes:** configuración segura de aplicaciones al servicio del uso responsable de una capacidad.

### Highlights de contribución

- **H01 — Separa la credencial del código y de la evidencia:** el valor se lee del ambiente y el reporte registra sólo el nombre y `configured: true`. Extiende la configuración de P406 (línea de comandos) y P407 (archivo) a un tercer canal reservado para valores sensibles. Sin este hito, la secuencia no distinguiría configuración ordinaria de secretos.
- **H02 — Falla de forma explicable ante configuración ausente (caso y datos):** `test_get_api_key_explains_the_missing_configuration` borra la variable con `monkeypatch` y exige un `RuntimeError` que nombre `ANALYTICS_API_KEY`; `test_get_api_key_reads_the_configured_secret` verifica la lectura. No hay caso ni datos: la clave es explícitamente de práctica y no se conecta con una capacidad. Ese límite define el taller como mecanismo aislado.

### Inventario técnico de implementación

- **Introduce:** lectura de secretos con `os.environ.get`, `export`/`unset`, reporte que omite el valor, `monkeypatch.setenv`/`delenv`.
- **Extiende:** configuración externa al código de P406–P407.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Secreto por variable de ambiente | H01 | `os.environ.get("ANALYTICS_API_KEY")` | Sin gestor de secretos ni `.gitignore` de archivos de ambiente. |
| Falla explicable | H02 | `RuntimeError` con nombre de la variable | La clave no se usa. |

### Relación técnica con actividades anteriores

Misma técnica (configuración externa) que P406–P407 con nueva exigencia: no persistir el valor. No consume artefactos de P425–P426 pese a que el nombre de la variable sugiere una API. P452 (posterior) controla el acceso por roles con una política propia, sin relación demostrable con esta clave.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Credencial separada | S01, S02 | `implementation/productos/P427_secret_config/professor/main.py`: `get_api_key`, `main`; `implementation/productos/P427_secret_config/submission/secret_config_report.json`; `implementation/productos/P427_secret_config/HOW_TO_RUN_ME.txt` | No se verifica que el valor no aparezca en el reporte. |
| H02 — Falla explicable | S01, S03 | `implementation/productos/P427_secret_config/professor/test_main.py` | Sin capacidad que proteger. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Lectura del secreto | `professor/main.py`; `src/main.py` | Una variable; plantilla `NotImplementedError`. |
| S02 | Evidencia | `submission/secret_config_report.json` | Nombre y estado. |
| S03 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Lectura y ausencia; existencia del reporte. |
| S04 | Instrucciones | `HOW_TO_RUN_ME.txt` | `export`/`unset` de shell Unix. |

### Contrato de evidencia actual

- **Notebook o código:** `get_api_key` y escritura del reporte.
- **`submission/`:** `secret_config_report.json`.
- **Pruebas:** `professor/test_main.py` verifica lectura del valor configurado y error explicable cuando falta. `tests/test_activity.py` sólo exige el reporte; no comprueba que omita el valor.
- **Trazabilidad:** `productos.C02`, `productos.C04`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P406–P407:** práctica de configuración externa al código.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P427 → `productos.C02`, `productos.C04`, `productos.C05`. C04 (uso responsable, control de acceso) y C05 (seguridad) se sostienen sólo en el mecanismo, sin capacidad protegida; C02 secundario. Auditoría (pregunta 5): práctica genérica de ingeniería de software; riesgo de identidad no resuelto.
