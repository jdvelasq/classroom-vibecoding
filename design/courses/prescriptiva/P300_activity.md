# P300 — Encuadre analítico de decisiones: política de contacto con contrato

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/`.

### Preguntas analíticas actuales

- ¿Qué política de contacto debe aprobar la responsable comercial antes de cada campaña de depósito, sin exceder la capacidad ni el límite de exposición?

El caso parte de `data/policy_options.csv`: cuatro alternativas de campaña ya agregadas (P0 «no contactar», P1 «solo probabilidad alta», P2 «ampliar a probabilidad media», P3 «contactar toda la lista»), cada una con número de contactos, conversión esperada, costo por contacto, valor neto por conversión, proporción de contactos intensos y los límites de capacidad (1.000 contactos) y de exposición (0,35). La unidad de análisis es la **alternativa de política**, no el cliente: no hay filas por cliente ni se define numéricamente qué es «probabilidad alta» o «media». La procedencia no está documentada (no hay `source.json` ni declaración de datos sintéticos). El producto es una recomendación única con un contrato de operación.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** elegir la alternativa de contacto antes de cada campaña; el notebook y el contrato nombran a la «Responsable comercial» como dueña de la decisión.
- **Producto terminal:** `decision_brief.csv` (alternativa recomendada) y `policy_contract.csv` (cadencia, plazo de respuesta, modo de ejecución, objetivo, restricción, salvaguarda, excepción, gatillo de revisión y métrica de resultado).
- **Uso y límite:** permite mostrar que la acción sale de filtrar factibilidad antes de maximizar valor esperado y que la recomendación requiere un contrato para operarse. No asigna clientes, no estima la conversión (viene dada) y no registra decisiones ni resultados observados; la política es una elección dentro de un menú fijo de cuatro opciones.
- **Disciplinas contribuyentes:** aritmética de valor esperado y filtrado con pandas sirven al contrato; no hay modelo predictivo ni optimizador.

### Highlights de contribución

- **H01 — Separa evidencia predictiva de acción factible:** `evaluate_policies` calcula conversiones y valor neto esperados y marca `capacity_ok` y `exposure_ok` por alternativa; `make_decision_brief` elige el máximo valor sólo entre las factibles. Primera aparición del patrón «factibilidad antes que objetivo» en el curso; sin este hito, la acción se confundiría con la alternativa de mayor valor bruto.
- **H02 — Muestra que las restricciones cambian la acción en un menú agregado:** en `policy_options.csv`, P3 («contactar toda la lista») excede tanto la capacidad (1.250 > 1.000 contactos) como la exposición (0,42 > 0,35); la recomendación persistida es P2, con 1.000 contactos, 115 conversiones y 17.700 de valor neto esperado. La particularidad del dataset —alternativas preagregadas, no clientes— fija el producto: se decide entre políticas candidatas, no se construye una regla por cliente. Sin este hito, el estudiante no vería un caso en el que el límite operativo y la salvaguarda de exposición determinan la elección.
- **H03 — Convierte una recomendación en contrato de política:** `make_policy_contract` añade `decision_cadence` («antes de cada campaña»), `response_need`, `execution_mode` («recomendación con aprobación humana»), `objective`, `capacity_constraint`, `exposure_safeguard`, `exception_rule` («escalar si ninguna política es factible»), `review_trigger` (conversión observada < 10 %) y `outcome_metric`. Primera aparición del contrato como entregable; sin él, la salida sería una solución sin autoridad, cadencia ni revisión.
- **H04 — Exige el contrato mediante la prueba:** `test_02` comprueba que `policy_contract.csv` contenga diez columnas del contrato. Sin este hito, la evaluación sólo vería la recomendación.

### Inventario técnico de implementación

- **Introduce:** evaluación de alternativas por valor esperado; banderas de factibilidad por restricción; selección con `nlargest` sobre el subconjunto factible; contrato de política tabular.
- **Introduce:** separación entre `professor/main.py` (funciones) y notebook (secuencia).
- **Reutiliza:** lectura con rutas relativas y persistencia en `submission/`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Factibilidad antes que objetivo | H01–H02 | Banderas `capacity_ok`/`exposure_ok`; máximo sobre factibles | Cuatro alternativas fijas; sin clientes ni incertidumbre. |
| Contrato de política | H03–H04 | Diez campos persistidos en `policy_contract.csv` | Texto declarativo; no hay registro de ejecución ni resultados. |

### Relación técnica con actividades anteriores

Primera actividad del curso: no hay Pxxx previa en `prescriptiva`. La conversión esperada por alternativa se presenta como insumo predictivo («todavía no determina la acción»), pero el notebook no reutiliza artefactos de otro curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Factibilidad antes que objetivo | S02 | `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/professor/main.py`: `evaluate_policies`, `make_decision_brief`; `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/professor/notebook.ipynb`: celda de `evaluated` | La tabla evaluada no se persiste; sólo se conserva la alternativa elegida. |
| H02 — Restricciones que cambian la acción | S01, S02 | `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/data/policy_options.csv`; `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/submission/decision_brief.csv` | Procedencia no documentada; «probabilidad alta/media» no definidas; valores de P1 y P3 no persistidos. |
| H03 — Contrato de política | S03 | `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/professor/main.py`: `make_policy_contract`; `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/submission/policy_contract.csv` | Campos fijos en código; no se demuestra su operación ni el gatillo con datos observados. |
| H04 — Prueba del contrato | S04 | `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/tests/test_activity.py`: `test_01`, `test_02` | Verifica existencia y columnas, no valores ni la elección. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset de alternativas agregadas | `data/policy_options.csv` | Cuatro filas; sin procedencia; unidad = alternativa, no cliente. |
| S02 | Evaluación y selección | `professor/main.py`: `evaluate_policies`, `make_decision_brief`; notebook | Valor esperado puntual; selección en menú fijo. |
| S03 | Producto/contrato | `professor/main.py`: `make_policy_contract`; `submission/decision_brief.csv`, `submission/policy_contract.csv` | Contrato textual; sin registro de decisiones ni monitoreo ejecutado. |
| S04 | Pruebas | `tests/test_activity.py` | Existencia y columnas. |
| S05 | Interfaz notebook–código | `professor/notebook.ipynb` (importa `main` desde `src/`); `src/` sólo con `.gitkeep` | El notebook busca el módulo en `src/`, pero `main.py` está en `professor/`. |

### Contrato de evidencia actual

- **Notebook o código:** carga alternativas, evalúa valor y factibilidad, selecciona la factible de mayor valor y construye el contrato.
- **`submission/`:** `decision_brief.csv` (P2, 1.000 contactos, 115 conversiones esperadas, 17.700 de valor neto esperado, responsable y gatillo) y `policy_contract.csv` (contrato completo).
- **Pruebas:** exigen ambos archivos y diez columnas del contrato; no verifican la alternativa recomendada ni los cálculos.
- **Trazabilidad:** P300 mapea `prescriptiva.C01` y `C04`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna.
- **Habilita para P302 y P307:** el patrón evaluar → filtrar factibles → elegir máximo, y el contrato con responsable, cadencia y gatillo, reaparecen de forma observable en `professor/main.py` de P302 y P307. P303–P306 repiten el contrato con otros formatos. No hay artefacto de datos compartido.

## Trazabilidad y auditoría

P300 está mapeada a `prescriptiva.C01` y `prescriptiva.C04` en `implementation/prescriptiva/traceability.yaml`; la evidencia sostiene C01 (contrato con contexto, responsable, cadencia, acción, objetivo, restricción, salvaguarda, excepción y revisión) y C04 (modo «recomendación con aprobación humana» y escalamiento). Coincide con el producto previsto en `activity-architecture.md` («política de contacto con valor, capacidad y gatillo de revisión»). El producto de Analytics es una recomendación gobernada entre alternativas; no es una regla que transforme el contexto observable de cada cliente en acción, ni demuestra monitoreo ejecutado. La aritmética de valor esperado contribuye al contrato y no organiza el taller.
