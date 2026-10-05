# P414 — Nox: sesión aislada que recalcula y comprueba el indicador por fábrica

## Actividad actual implementada

**Implementación:** `implementation/productos/P414_nox/`.

### Preguntas analíticas actuales

- ¿Puede comprobarse el indicador de producción por fábrica en un ambiente creado desde cero, con una sola orden, sin depender de lo instalado en el equipo?

`data/daily_operations.csv` tiene cuatro filas máquina-día (dos fábricas, dos máquinas cada una) con `daily_units_produced`. `professor/main.py` suma la producción por `factory_id` y escribe `submission/report.json` (`{"1": 9303, "2": 9300}`). `noxfile.py` declara la sesión `tests`, que instala `requirements.txt` (`pandas==2.2.3`) y `pytest` en un ambiente propio y ejecuta `tests/test_report.py`. Esa prueba ejecuta `src/main.py` en un subproceso y exige los totales exactos. El indicador es el mismo de P400 y P412–P413; lo nuevo es el ejecutor de la verificación.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; la tarjeta de producto de P408–P411 nombra al «equipo de operaciones» como consumidor, pero P414 no la incluye.
- **Producto terminal:** `submission/report.json` con totales por fábrica, más una sesión Nox que lo recalcula y compara con valores esperados.
- **Uso y límite:** permite afirmar que el indicador se reproduce en un ambiente aislado con la dependencia declarada. No dice nada nuevo sobre producción ni sobre la validez del indicador; los valores esperados están escritos en la prueba.
- **Disciplinas contribuyentes:** automatización de tareas de Python (Nox) y pruebas con pytest, al servicio de la verificación repetible de un indicador descriptivo mínimo.

### Highlights de contribución

- **H01 — Encapsula ambiente y verificación en una sesión declarada:** `noxfile.py` define `tests`, que instala exactamente `requirements.txt` y `pytest` y ejecuta sólo `tests/test_report.py`. P412 creaba el ambiente a mano (`venv` + `pip`) y P413 nombraba comandos con Make sin aislar el ambiente; P414 une ambas cosas en una orden (`python3 -m nox -s tests`). Sin este hito, P416 no tendría una sesión local que GitHub pueda reutilizar.
- **H02 — Fija el resultado analítico como criterio de la sesión (caso y datos):** el dato es una tabla de cuatro filas cuyo total por fábrica (9303 y 9300) se conoce de antemano; `professor/main.py` lo declara («El cálculo conocido permite concentrar el taller en el ambiente automatizado»). Esa trivialidad es deliberada: hace que la prueba compare un valor exacto y no una tolerancia. La particularidad no proviene del dominio; la diferencia de tres unidades entre fábricas no se interpreta. Sin este hito, la sesión no tendría un criterio analítico que comprobar.

### Inventario técnico de implementación

- **Introduce:** `noxfile.py` con `@nox.session`, `session.install("--requirement", ...)` y `session.run("pytest", ...)`.
- **Reutiliza:** dataset, cálculo y valores esperados de P400/P412/P413; `requirements.txt` local con `pandas==2.2.3`; prueba que ejecuta `src/main.py` por subproceso (patrón de P412–P413).
- **Aplica en nuevo caso:** ninguno; mismo indicador.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Sesión de verificación aislada | H01 | Nox instala dependencias declaradas y ejecuta una prueba | Una sesión, un intérprete; sin matriz de versiones. |
| Prueba de resultado exacto | H02 | `assert report["factory_totals"] == {"1": 9303, "2": 9300}` | Indicador trivial de cuatro filas. |

### Relación técnica con actividades anteriores

Misma pregunta y mismo dato que P400, P412 y P413, con nueva herramienta de ejecución. `tests/test_report.py` es casi idéntico al de P413 (Make) y equivalente al `unittest` de P412; la contribución distinguible es el ambiente aislado creado por la sesión. Posible solapamiento P412–P414 (tres formas de ejecutar la misma prueba sobre el mismo indicador) que requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Sesión declarada | S02, S03 | `implementation/productos/P414_nox/noxfile.py`; `implementation/productos/P414_nox/HOW_TO_RUN_ME.txt`; `implementation/productos/P414_nox/requirements.txt` | No hay evidencia persistida de una ejecución de Nox (sin log en `submission/`). |
| H02 — Resultado exacto como criterio | S01, S03 | `implementation/productos/P414_nox/data/daily_operations.csv`; `implementation/productos/P414_nox/professor/main.py`; `implementation/productos/P414_nox/tests/test_report.py`; `implementation/productos/P414_nox/submission/report.json` | El valor esperado está escrito en la prueba; no se deriva de un contrato del producto. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset e indicador | `data/daily_operations.csv`; `professor/main.py`; `src/main.py` | Cuatro filas; plantilla `src/main.py` lanza `NotImplementedError`. |
| S02 | Sesión Nox y manifiesto local | `noxfile.py`; `requirements.txt` | Una sesión `tests`; sólo pandas fijado. |
| S03 | Pruebas | `tests/test_report.py`; `tests/test_activity.py` | `test_report.py` ejecuta `src/main.py`; `test_activity.py` sólo exige `report.json`. |
| S04 | Secuencia | `HOW_TO_RUN_ME.txt` | Sin enlace explícito con P412–P413 ni con P416. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` suma por fábrica y escribe `report.json`; no hay notebook.
- **`submission/`:** `report.json` con los totales por fábrica.
- **Pruebas:** `tests/test_activity.py` exige que exista `report.json`. `tests/test_report.py` ejecuta `src/main.py` y compara los totales exactos; con la plantilla sin resolver, esta prueba falla en ejecución (no en descubrimiento). No se verifica que la sesión Nox se haya ejecutado.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400/P412/P413:** dataset, cálculo, valores esperados y patrón de prueba por subproceso; de P412, el manifiesto `requirements.txt`.
- **Habilita para P416:** `noxfile.py` y el `src/main.py` de P414 reaparecen como plantilla en `P416_github_actions_nox/data/repository_template/` (mismo tamaño: 246 y 616 bytes).

## Trazabilidad y auditoría

Entrada revisada: P414 → `productos.C02`, `productos.C05`. C02 se sostiene (verificación reproducible y automatizada). C05 no tiene evidencia propia: no hay monitoreo, recuperación ni gobierno; a lo sumo, la sesión es una condición para detectar regresiones. Auditoría de identidad (pregunta 5): el taller puede describirse como capacitación en una herramienta de automatización de Python; el producto analítico es un total por fábrica sin usuario ni decisión dentro de la actividad. Riesgo de identidad no resuelto, compartido con P412–P419.
