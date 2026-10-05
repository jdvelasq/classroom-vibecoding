# P413 — Makefile: producir y comprobar el indicador por fábrica con objetivos nombrados

## Actividad actual implementada

**Implementación:** `implementation/productos/P413_makefile/`.

### Preguntas analíticas actuales

- ¿Cómo se convierten la producción y la comprobación del indicador por fábrica en tareas repetibles que no dependan de recordar comandos?

`Makefile` declara `.PHONY: report test`; `report` ejecuta `python3 src/main.py` y `test` ejecuta `python3 -m pytest tests/test_report.py`. `HOW_TO_RUN_ME.txt` indica `make report` y `make test` en macOS/Linux y `run.bat report|test` en Windows; `run.bat` aparece como binario y su contenido no es verificable aquí. `professor/main.py` agrega `daily_operations.csv` por fábrica y escribe `submission/report.json` como diccionario `{"1": 9303, "2": 9300}`. `tests/test_report.py` ejecuta `src/main.py` y compara ese diccionario. Hay un `requirements.txt` (`pandas==2.2.3`) que ni el Makefile ni las instrucciones usan.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** producir y verificar el indicador con un comando corto; usuario no evidenciado.
- **Producto terminal:** `submission/report.json` producido y comprobado mediante objetivos del `Makefile`.
- **Uso y límite:** concentra en un lugar los comandos reales de producción y verificación. Los objetivos no dependen entre sí y no preparan el ambiente; no hay más tareas que las dos.
- **Disciplinas contribuyentes:** automatización de tareas con Make al servicio de la ejecución repetible del indicador.

### Highlights de contribución

- **H01 — Nombra la producción y la verificación del indicador como objetivos repetibles:** `report` y `test` como objetivos `.PHONY`; «El Makefile conserva los comandos reales en un único lugar». La prueba invocada por `test` vuelve a ejecutar `src/main.py`, de modo que no depende de haber corrido `report` antes. Ofrece `run.bat` como alternativa en Windows y declara que en clase se discute la diferencia. Primera automatización de tareas del curso. Sin este hito, P414 no tendría el contraste entre un atajo de comandos y una sesión con ambiente propio.
- **H02 — Cambia otra vez la forma del mismo indicador (caso y datos, límite):** el dato es el de P400 y P412, sin particularidad; el reporte pasa a un diccionario con claves de fábrica como texto (`"1"`, `"2"`), consecuencia de serializar en JSON las claves enteras de `groupby(...).to_dict()`, y la prueba fija esa forma. Es la tercera representación del mismo indicador (P400: CSV `total_units`; P412: registros `total_units_produced`). Sin este hito no se vería que la prueba de regresión también fija un contrato de salida, distinto en cada actividad.

### Inventario técnico de implementación

- **Introduce:** `Makefile` con objetivos `.PHONY`; script `run.bat` como alternativa.
- **Reutiliza:** dato y agregación de P400; prueba por `subprocess` con valor conocido de P412, ahora con `pytest`; `requirements.txt` de P412.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Objetivos de tarea | H01 | `make report`, `make test` | Sin dependencias ni ambiente. |
| Alternativa multiplataforma | H01 | `run.bat` | Contenido no verificable. |
| Contrato de salida fijado por prueba | H02 | `{"1": 9303, "2": 9300}` | Distinto de P400 y P412. |

### Relación técnica con actividades anteriores

Mismo dato y misma prueba de valor conocido que P412 con nueva práctica (objetivos nombrados). P414 repite código, dato, prueba y reporte idénticos y sustituye el `Makefile` por `noxfile.py`.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Objetivos | S02, S03, S05 | `implementation/productos/P413_makefile/Makefile`; `implementation/productos/P413_makefile/HOW_TO_RUN_ME.txt`; `implementation/productos/P413_makefile/run.bat`; `implementation/productos/P413_makefile/tests/test_report.py` | `run.bat` binario en el digest. |
| H02 — Forma del indicador | S01, S04, S05 | `implementation/productos/P413_makefile/professor/main.py`; `implementation/productos/P413_makefile/submission/report.json`; `implementation/productos/P413_makefile/tests/test_report.py`: `test_factory_totals` | Sin particularidad de datos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Igual a P400. |
| S02 | Automatización | `Makefile`; `run.bat` | Dos objetivos independientes. |
| S03 | Instrucciones y ambiente | `HOW_TO_RUN_ME.txt`; `requirements.txt` | `requirements.txt` no usado. |
| S04 | Indicador y producto | `professor/main.py`; `submission/report.json` | Claves de fábrica como texto. |
| S05 | Pruebas | `tests/test_report.py`; `tests/test_activity.py` | Una verifica valores; la otra existencia. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` produce el reporte; `Makefile` expone `report` y `test`.
- **`submission/`:** `report.json` con totales por fábrica.
- **Pruebas:** `tests/test_report.py::test_factory_totals` ejecuta `src/main.py` y verifica los totales; no verifica que exista o funcione el `Makefile`. `tests/test_activity.py::test_01` sólo exige que exista el reporte.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400 y P412:** dato y agregación (P400); `requirements.txt` y prueba de valor conocido (P412).
- **Habilita para P414 y P416:** P414 reutiliza `professor/main.py`, `tests/test_report.py` y `report.json` con la misma lógica; la sesión Nox de P416 ejecuta `tests/test_report.py`.

## Trazabilidad y auditoría

Entrada revisada: P413 → `productos.C02`, `productos.C05`. C02 se sostiene (automatización repetible de producción y verificación); C05 no se evidencia. El producto es el indicador de P400 con su verificación automatizada; el taller se lee como introducción a Make (pregunta de auditoría 5), con riesgo de duplicación parcial con P414.
