# P418 — Contenedor: ejecución empaquetada del indicador con resultado fuera del contenedor

## Actividad actual implementada

**Implementación:** `implementation/productos/P418_container/`.

### Preguntas analíticas actuales

- ¿Cómo se ejecuta el indicador por fábrica de la misma manera en otro computador, sin instalar Python ni pandas localmente?

`Dockerfile` parte de `python:3.11-slim`, instala `requirements.txt` (`pandas==2.2.3`), copia `data/` y `src/` dentro de la imagen y ejecuta `python src/main.py`. `.dockerignore` excluye `.venv`, cachés y `submission/*.json`. `HOW_TO_RUN_ME.txt` construye la imagen (`docker build --tag p418-container .`) y la ejecuta con `--rm` y `--volume "$(pwd)/submission:/app/submission"`, de modo que el reporte escrito dentro del contenedor queda en la carpeta local. `professor/main.py` produce `submission/factory_report.json` con `total_units_produced` 9303 y 9300. Advierte que cambiar código, datos o dependencias exige reconstruir la imagen.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** imagen de contenedor que ejecuta el indicador en lote y `submission/factory_report.json` como salida montada.
- **Uso y límite:** muestra que el resultado puede obtenerse en un ambiente empaquetado y salir del contenedor. No hay prueba que ejecute el contenedor ni registro de la versión de la imagen usada.
- **Disciplinas contribuyentes:** contenedores al servicio de ejecutar un indicador de forma portable.

### Highlights de contribución

- **H01 — Empaqueta código, datos y dependencias en una imagen ejecutable en lote:** el `Dockerfile` copia `data` y `src` a la imagen y fija pandas por `requirements.txt`; la regla de reconstruir tras cualquier cambio se declara en `HOW_TO_RUN_ME.txt`. P412 aislaba dependencias con `venv`, pero el intérprete seguía siendo el del equipo (el reporte de P412 registra Python 3.9.6); aquí el intérprete (3.11) también queda fijado por la imagen base. Sin este hito, la portabilidad del producto dependería del sistema anfitrión.
- **H02 — Separa la salida del ciclo de vida del contenedor (caso y datos):** el contenedor se elimina al terminar (`--rm`) y el reporte persiste gracias al volumen sobre `submission/`; `.dockerignore` impide copiar reportes previos a la imagen. El dato es el mismo CSV de cuatro filas, ahora incrustado en la imagen: cambiar los datos obliga a reconstruirla. Esa es la única condición del caso que la actividad hace visible. Sin este hito, el resultado se perdería con el contenedor o la imagen arrastraría salidas viejas.

### Inventario técnico de implementación

- **Introduce:** `Dockerfile`, `.dockerignore`, `docker build --tag`, `docker run --rm --volume`.
- **Reutiliza:** dataset, función `summarize_by_factory` y estructura del reporte de P412; `requirements.txt` local.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Contenedor de ejecución en lote | H01 | Imagen con intérprete, dependencia, datos y código | Sin etiqueta de versión ni prueba del contenedor. |
| Salida por volumen | H02 | `--volume` sobre `submission/`; `.dockerignore` | Datos incrustados en la imagen. |

### Relación técnica con actividades anteriores

Misma pregunta y dato que P412–P417; nueva forma de ejecución. Extiende P412 (ambiente) al nivel del sistema. P426 reutiliza la práctica para un servicio en lugar de un lote.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Imagen ejecutable | S02, S03 | `implementation/productos/P418_container/Dockerfile`; `implementation/productos/P418_container/requirements.txt`; `implementation/productos/P418_container/HOW_TO_RUN_ME.txt` | No hay evidencia persistida de una construcción o ejecución. |
| H02 — Salida fuera del contenedor | S01, S03, S04 | `implementation/productos/P418_container/.dockerignore`; `implementation/productos/P418_container/HOW_TO_RUN_ME.txt` (paso 2); `implementation/productos/P418_container/submission/factory_report.json` | El reporte persistido pudo generarse fuera del contenedor; no registra cómo se produjo. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset e indicador | `data/daily_operations.csv`; `professor/main.py`; `src/main.py` | Cuatro filas; plantilla `NotImplementedError`. |
| S02 | Imagen | `Dockerfile`; `.dockerignore`; `requirements.txt` | `python:3.11-slim`; datos copiados a la imagen. |
| S03 | Ejecución | `HOW_TO_RUN_ME.txt` | Requiere Docker Desktop; volumen sobre `submission/`. |
| S04 | Evidencia y prueba | `submission/factory_report.json`; `tests/test_activity.py` | Sólo existencia del reporte. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` agrega y escribe `factory_report.json`.
- **`submission/`:** `factory_report.json` con totales por fábrica.
- **Pruebas:** `tests/test_activity.py` exige que exista el reporte; no verifica que provenga del contenedor ni su contenido.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P412:** función `summarize_by_factory`, formato del reporte y manifiesto.
- **Habilita para P426:** patrón `Dockerfile` (misma imagen base y manifiesto local) aplicado a un servicio.

## Trazabilidad y auditoría

Entrada revisada: P418 → `productos.C02`, `productos.C05`. C02 se sostiene (entrega desplegable). C05 sin evidencia propia (sin observación ni recuperación). Auditoría (pregunta 5): se lee como introducción a Docker sobre un indicador trivial sin usuario; riesgo de identidad no resuelto.
