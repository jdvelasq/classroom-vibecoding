# P425 — Contrato de API: clasificación de riesgo por producción diaria con errores explícitos

## Actividad actual implementada

**Implementación:** `implementation/productos/P425_api_contract/`.

### Preguntas analíticas actuales

- ¿Cómo se publica una capacidad analítica con un contrato estable: qué recibe, qué responde y qué error devuelve cuando la solicitud no cumple?

`professor/main.py` crea una aplicación Flask con `POST /score`. `validate_payload` exige un objeto con `daily_units_produced` entero; si falta o no es entero responde 400 con un mensaje que nombra el campo. `classify_risk` devuelve `high` si el valor es menor que 4500 y `low` en otro caso; la respuesta incluye `risk` y `threshold` (4500). Antes de `app.run(port=8000)`, `main()` usa `app.test_client()` para guardar en `submission/score_examples.json` una respuesta válida (`{"risk": "high", "threshold": 4500}` para 4200) y una de error (`Se requiere el campo daily_units_produced.`). `HOW_TO_RUN_ME.txt` guía solicitudes con `curl`. `data/` está vacía.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; el campo coincide con la columna `daily_units_produced` de `daily_operations.csv` (registro máquina-día), pero no se declara a quién sirve el riesgo ni qué acción desencadena.
- **Producto terminal:** un servicio HTTP con contrato de entrada, salida y error, y `submission/score_examples.json` como documentación ejecutada del contrato.
- **Uso y límite:** permite integrar una clasificación de riesgo con nombres estables y errores explicables. La regla (umbral 4500) está escrita en el código sin origen: no es un modelo ni proviene de una actividad previa; aplicada a las cuatro filas de `daily_operations.csv` (4533–4770) clasificaría todas como `low`. La validación cubre presencia y tipo, no rango.
- **Disciplinas contribuyentes:** desarrollo de servicios web al servicio de exponer una capacidad analítica mínima.

### Highlights de contribución

- **H01 — Define el contrato de interfaz con errores explicables:** entrada (`daily_units_produced` entero), salida (`risk`, `threshold`) y error 400 con mensaje que nombra el campo. Las tres pruebas de `professor/test_main.py` verifican respuesta válida, campo ausente y valor no entero (`"4200"`). Es la primera interfaz de consumo del curso. Sin este hito, la capacidad no tendría una frontera verificable para sus consumidores.
- **H02 — Documenta el contrato con respuestas ejecutadas:** `main()` genera `score_examples.json` con el cliente de prueba antes de arrancar el servidor, de modo que la evidencia se produce sin depender de solicitudes externas. Sin este hito, el contrato sólo existiría en el código.
- **H03 — Expone una regla de umbral sin procedencia (caso y datos):** el único insumo es un entero por solicitud; la unidad (máquina-día, por coincidencia de nombre con el dataset del curso) y el umbral 4500 no se justifican. La respuesta devuelve el umbral junto al riesgo, lo que hace visible el criterio al consumidor. La validación de tipo admite valores negativos y, por cómo Python trata los booleanos, un `true` JSON pasaría como entero. Este límite delimita el producto: un contrato bien formado alrededor de una regla arbitraria.

### Inventario técnico de implementación

- **Introduce:** Flask, `@app.post`, `request.get_json(silent=True)`, códigos 200/400, `app.test_client()` para pruebas y ejemplos.
- **Reutiliza:** el campo `daily_units_produced` del caso de fábricas (P400–P418); `requirements.txt` local (`flask==3.1.3`).
- **Aplica en nuevo caso:** clasificación de riesgo por umbral.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Contrato de API con errores | H01 | Validación de presencia y tipo; 400 con mensaje | Sin esquema formal ni versión del contrato. |
| Ejemplos ejecutados | H02 | `score_examples.json` vía cliente de prueba | Dos ejemplos. |
| Regla expuesta con su umbral | H03 | `risk` + `threshold` en la respuesta | Regla fija sin procedencia ni modelo. |

### Relación técnica con actividades anteriores

Nuevo producto (interfaz de consumo). Retoma el vocabulario del caso de fábricas sin consumir datos ni artefactos; no usa los modelos de P420–P424. Las etiquetas `high`/`low` coinciden con P423 sin relación demostrable. La validación de entrada recuerda las pruebas de datos de P402, ahora en la frontera del servicio. El concepto «factory risk» reaparece más adelante (P430, P434, P435, P444, P448, P450–P452) con datos propios en cada actividad.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Contrato con errores | S02, S04 | `implementation/productos/P425_api_contract/professor/main.py`: `validate_payload`, `score`; `implementation/productos/P425_api_contract/professor/test_main.py` | No se prueban rangos ni booleanos. |
| H02 — Ejemplos ejecutados | S03 | `implementation/productos/P425_api_contract/professor/main.py`: `main`; `implementation/productos/P425_api_contract/submission/score_examples.json` | No demuestra que el servidor se haya ejecutado. |
| H03 — Regla sin procedencia | S01, S02 | `implementation/productos/P425_api_contract/professor/main.py`: `classify_risk` | La unidad máquina-día se infiere del nombre del campo. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Capacidad expuesta | `professor/main.py`: `classify_risk` | Umbral 4500 fijo; `data/` vacía. |
| S02 | Contrato y validación | `professor/main.py`: `validate_payload`, `score` | Presencia y tipo. |
| S03 | Evidencia del contrato | `submission/score_examples.json` | Dos respuestas. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Tres casos de contrato; existencia del archivo. |
| S05 | Interfaz del estudiante | `src/main.py`; `HOW_TO_RUN_ME.txt`; `requirements.txt` | Plantilla `NotImplementedError`; servidor en puerto 8000. |

### Contrato de evidencia actual

- **Notebook o código:** servicio `/score`, generación de ejemplos y arranque del servidor.
- **`submission/`:** `score_examples.json` con respuesta válida y de error.
- **Pruebas:** `professor/test_main.py` verifica código de estado y cuerpo para entrada válida, campo ausente y valor no entero. `tests/test_activity.py` sólo exige que exista `score_examples.json`, no su contenido.
- **Trazabilidad:** `productos.C02`, `productos.C04`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** vocabulario del caso de fábricas; ningún artefacto.
- **Habilita para P426:** la misma aplicación (validación y regla) se empaqueta en contenedor; P426 copia la lógica en su propio `professor/main.py`.

## Trazabilidad y auditoría

Entrada revisada: P425 → `productos.C02`, `productos.C04`, `productos.C05`. C04 (interfaz de uso) y C02 se sostienen. C05 sin evidencia: no hay registro de solicitudes ni monitoreo. El contrato de entradas, salidas y errores corresponde también a `productos.C01`, que no está mapeada; se registra para escalación. Auditoría: el mecanismo es propio de productos (hacer usable una capacidad), pero la capacidad expuesta es una regla arbitraria sin usuario ni decisión; riesgo de lectura como tutorial de Flask.
