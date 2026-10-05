# P301 — Air France 447: protocolo excepcional de búsqueda bayesiana

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P301_air_france_447/`.

### Preguntas analíticas actuales

- ¿Qué plan excepcional de búsqueda debe activarse, reasignarse tras un fracaso y escalarse ante nueva evidencia para localizar una aeronave desaparecida?
- ¿Dónde buscar primero y cómo reasignar después de no encontrar nada?

El notebook declara un **escenario pedagógico sintético** que «no reconstruye ni representa la operación histórica real». `data/search_cells.csv` describe una cuadrícula de 5 × 5 celdas de 10 km (filas = celdas; columnas = coordenadas del centro, probabilidad previa de ubicación y probabilidad condicional de detección, con sólo dos valores: 0,4 y 0,8); `data/search_rounds.csv` fija seis unidades por ronda, la ronda 1 «unsuccessful» y la ronda 2 «not_executed». El producto es un protocolo de contingencia con dos asignaciones, su comparación y un mapa; el propio notebook declara que la decisión es **no recurrente** y que el protocolo no es la política terminal del curso.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** asignar hasta seis unidades de búsqueda por ronda; autoridad declarada: «comando de búsqueda aprueba y escala el plan».
- **Producto terminal:** `decision_boundary.csv` (tipo de decisión, recurrencia, cadencia, plazo, acción, restricción, salvaguarda, autoridad, gatillo), `search_plan.csv` (50 filas: ronda × celda), `plan_comparison.csv` y `search_planning_map.png`.
- **Uso y límite:** permite contrastar un plan excepcional, actualizado por evidencia, con una política recurrente. No representa la búsqueda real de AF447, supone la misma efectividad al repetir una celda y no persiste un registro de autorización; la ronda 2 es una recomendación pendiente.
- **Disciplinas contribuyentes:** teoría de búsqueda (probabilidad de éxito = ubicación × detección) y actualización bayesiana tras fracaso sirven al protocolo; matplotlib hace visible cada creencia y asignación.

### Highlights de contribución

- **H01 — Declara la frontera entre plan excepcional y política recurrente:** la tabla `decision_boundary` registra «no recurrente; activada por una desaparición», cadencia «por ronda y cuando aparece nueva evidencia», plazo «antes de asignar la siguiente ronda» y autoridad del comando. Contrasta con P300, cuyo contrato supone campañas repetidas; sin este hito, cualquier optimización se presentaría como política recurrente.
- **H02 — Distingue cobertura de probabilidad de éxito:** la estrategia por cercanía cubre 0,39 de probabilidad y logra 0,28 de éxito; ordenar por `prior_probability × detection_probability` cubre 0,52 y logra 0,384 con la misma capacidad (`plan_comparison.csv`). La particularidad del dataset —detección heterogénea (0,4 u 0,8) por celda— hace que la celda más probable no sea siempre la más valiosa de buscar. Sin este hito, se confundiría «buscar donde es probable» con «buscar donde es probable encontrar».
- **H03 — Actualiza creencias tras un fracaso sin descartar celdas:** multiplica la previa de las celdas buscadas por `1 − detection_probability`, normaliza y verifica que el peso restante iguale `1 − éxito` de la ronda 1. Primera aparición de actualización de evidencia en el curso; sin este hito, un fracaso se trataría como descarte o se ignoraría.
- **H04 — Compara reasignar con repetir bajo la misma información posterior:** en la ronda 2, repetir el plan inicial da 0,146 de éxito condicional y el plan revisado 0,226; C03 permanece en ambas rondas. Sin este hito, el estudiante no vería que la salvaguarda «no descartar celdas» y la reasignación coexisten.
- **H05 — Verifica el plan antes de entregarlo:** aserciones sobre 50 registros sin duplicados, probabilidades que suman 1 por ronda, seis unidades por ronda, identidad éxito = ubicación × detección e IDs seleccionados esperados. Sin este hito, el protocolo no tendría comprobación interna reproducible.
- **H06 — Persiste el protocolo como cuatro artefactos complementarios:** frontera de decisión, plan por ronda con `searched_previous_round`, comparación y mapa con trama de búsqueda fallida y orden de prioridad. Sin estos artefactos, la reasignación no sería auditable después de la sesión.

### Inventario técnico de implementación

- **Introduce:** probabilidad de éxito por celda; ordenamiento con desempate estable y redondeo de la clave de orden; actualización bayesiana por fracaso; comparación con línea base ingenua (cercanía) y con repetición.
- **Introduce:** validación de la cuadrícula con `assert` (unicidad, cobertura completa, suma 1, valores de detección, presupuesto).
- **Introduce:** visualización espacial con `pcolormesh`, contornos de asignación y trama de búsqueda previa; figura persistida.
- **Extiende:** tabla de frontera de decisión de P300 a un caso explícitamente no recurrente.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Frontera excepcional / recurrente | H01 | `decision_boundary.csv` | Declarativa; sin registro de aprobación. |
| Prioridad por éxito esperado | H02 | Ubicación × detección; comparación con cercanía | Caso sintético; detección binaria en dos niveles. |
| Actualización tras fracaso | H03–H04 | Bayes con normalización; repetir vs revisar | Supone efectividad constante al repetir. |
| Protocolo verificable | H05–H06 | Aserciones; plan, comparación y mapa | Pruebas sólo exigen archivos. |

### Relación técnica con actividades anteriores

Frente a P300 cambia la naturaleza de la decisión (excepcional y secuencial frente a recurrente por campaña) y la evidencia (creencia espacial que se actualiza). Comparte el patrón de comparar contra una alternativa ingenua con idéntica capacidad. No hay duplicación: P300 elige en un menú agregado; P301 asigna recursos celda por celda y revisa tras un resultado observado.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Frontera de decisión | S04, S06 | `implementation/prescriptiva/P301_air_france_447/professor/notebook.ipynb`: celda «Frontera curricular» y `decision_boundary`; `implementation/prescriptiva/P301_air_france_447/submission/decision_boundary.csv` | Autoridad y gatillo son texto; no se ejecuta un escalamiento. |
| H02 — Cobertura vs éxito | S01, S02 | `implementation/prescriptiva/P301_air_france_447/data/search_cells.csv`; notebook: `success_probability`, `comparison1`; `implementation/prescriptiva/P301_air_france_447/submission/plan_comparison.csv` | Escenario sintético; no evalúa una búsqueda real. |
| H03 — Actualización tras fracaso | S03 | notebook: `remaining_weight`, `updated_probability`, aserción `remaining_total == 1 − first_success` | Depende de detección constante y de un único resultado de ronda. |
| H04 — Repetir vs reasignar | S03, S04 | notebook: `comparison2`, conjuntos «entran/salen/permanecen»; `plan_comparison.csv` | Éxitos condicionales a no haber encontrado; la ronda 2 no se ejecuta. |
| H05 — Verificación interna | S05 | notebook: celda de aserciones previa a la exportación | Las aserciones fijan IDs esperados del caso; no generalizan. |
| H06 — Persistencia del protocolo | S04, S05 | `implementation/prescriptiva/P301_air_france_447/submission/search_plan.csv`; `plan_comparison.csv`; `search_planning_map.png`; `implementation/prescriptiva/P301_air_france_447/tests/test_activity.py` | La prueba verifica nombres de archivos, no contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético de celdas y rondas | `data/search_cells.csv`, `data/search_rounds.csv` | No representa la operación histórica; dos niveles de detección. |
| S02 | Priorización de ronda 1 | Notebook: `naive_order`, `success_order`, `round1` | Costo igual por celda; una unidad por celda. |
| S03 | Actualización y ronda 2 | Notebook: `remaining_weight`, `updated_probability`, `round2`, `comparison2` | Efectividad igual al repetir; ronda 2 no ejecutada. |
| S04 | Producto/protocolo | `decision_boundary.csv`, `search_plan.csv`, `plan_comparison.csv`, `search_planning_map.png` | Sin registro de aprobación ni resultado de ronda 2. |
| S05 | Validación y pruebas | Celda de aserciones; `tests/test_activity.py` | Prueba de existencia de cuatro artefactos. |
| S06 | Secuencia/frontera curricular | Primera celda del notebook; `activity-architecture.md` | Explícitamente no es política recurrente terminal. |

### Contrato de evidencia actual

- **Notebook o código:** todo en `professor/notebook.ipynb` (sin `main.py`); valida datos, compara cercanía con éxito esperado, actualiza tras fracaso, compara repetir con revisar, verifica y exporta.
- **`submission/`:** `decision_boundary.csv`, `search_plan.csv` (50 filas), `plan_comparison.csv` (cuatro estrategias), `search_planning_map.png`.
- **Pruebas:** `test_01` exige los cuatro artefactos; no verifica valores.
- **Trazabilidad:** P301 mapea `prescriptiva.C01`.

### Dependencias en la secuencia

- **Recibe de P300:** la noción de contrato/frontera de decisión con cadencia, autoridad y gatillo, aquí aplicada para negar la recurrencia.
- **Habilita para Pyyy:** no evidenciada como artefacto. La actualización por evidencia y la comparación contra línea base con igual capacidad reaparecen como prácticas en actividades posteriores, sin dependencia técnica demostrable.

## Trazabilidad y auditoría

P301 está mapeada sólo a `prescriptiva.C01` en `implementation/prescriptiva/traceability.yaml`; la evidencia lo sustenta como contraste: formula la decisión con cadencia, autoridad, salvaguarda y gatillo, y la declara no recurrente. También ejerce autoridad y escalamiento declarativos (afines a C04) sin mapearlos. Coincide con el rol previsto («distinguir un plan excepcional de una política recurrente»). El producto de Analytics es un protocolo de contingencia verificable; la teoría de búsqueda y la actualización bayesiana sirven a él. Por diseño no es una política recurrente: no hay monitoreo de resultados más allá del gatillo por ronda.
