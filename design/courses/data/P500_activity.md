# P500 — Métricas mensuales de Superstore con contrato de métrica

## Actividad actual implementada

**Implementación:** `implementation/data/P500_superstore_metricas/`.

### Preguntas analíticas actuales

- ¿Cómo evolucionan mensualmente las ventas, la utilidad, el número de órdenes y el valor promedio por orden?

`data/superstore_orders.csv` (1953 líneas con encabezado; separador `;`, coma decimal, fechas `d/m/yy`) tiene una fila por producto dentro de una orden. `professor/main.py` lee el archivo, interpreta `Order Date`, comprueba con aserciones campos requeridos, fechas no nulas, unicidad de `Order ID` + `Product Name` y `Discount` en [0, 1], y persiste tres artefactos: `metric_contract.json` (formato, grano, controles, frontera de herramienta y fórmulas), `monthly_sales_metrics.csv` (7 líneas: encabezado y seis meses; las visibles van de 2015-01 a 2015-05) y `questions.json`. No hay notebook; la interfaz del estudiante es `src/main.py`, que sólo lanza `NotImplementedError`, sin instrucciones. No hay manifiesto de procedencia del CSV.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta descriptiva de desempeño comercial mensual; usuario y decisión no evidenciados.
- **Producto terminal:** tabla mensual de cuatro métricas acompañada de un contrato que fija fórmula y grano de cada una.
- **Uso y límite:** permite reproducir y auditar la definición de las métricas sobre seis meses de 2015. No permite hablar de tendencia o estacionalidad (sólo seis puntos), ni explicar variaciones de utilidad; el contrato no documenta el origen del dataset.
- **Disciplinas contribuyentes:** pandas para lectura y agregación; prácticas de contrato de datos al servicio de una definición de métrica verificable.

### Highlights de contribución

- **H01 — Hace explícita la convención regional del archivo fuente:** `load_sales` lee con `sep=";"`, `decimal=","` y `format="%d/%m/%y"`, y `build_contract` persiste esa convención en `source_format`. Primera aparición en el curso. Límite observable: el código declara y usa `encoding="latin1"` pero debe eliminar el prefijo `ï»¿` de las columnas, lo que indica un archivo UTF-8 con BOM leído como latin1; los textos no ASCII (p. ej. `™` en `Product Name`) quedan mal decodificados, como se ve en el `sales_detail.csv` de P501 (`Accentâ¢`), y P513 lee extractos del mismo caso con `utf-8-sig`. El contrato persiste, por tanto, una codificación incorrecta. Sin este hito no habría un primer contrato de lectura del curso.
- **H02 — Deriva las fórmulas del grano línea-de-orden (caso y datos):** el contrato declara «una fila por producto dentro de una orden; Row ID no es una clave única global» y el código verifica que `Order ID` + `Product Name` no se repite. Esa granularidad obliga a contar órdenes con `nunique` (`count_distinct(Order ID)`) y a calcular `average_order_value` como `sales / order_count`, no como promedio de filas. Sin este hito, el valor promedio por orden se confundiría con el valor promedio por línea. La no unicidad de `Row ID` se afirma en el contrato pero no se comprueba en el código.
- **H03 — Define métricas con independencia de la herramienta:** `metric_contract.json` registra nombre, fórmula y grano mensual de cada métrica y declara en `tool_boundary` que «Python solo ejecuta la definición». Primera evidencia del curso para la frontera de herramientas (`data.C05`). Sin este hito, la métrica quedaría definida sólo por el código pandas.
- **H04 — Condiciona la salida a controles de calidad ejecutables:** cuatro `assert` en `main` (campos requeridos, `Order Date` sin nulos, unicidad de la llave, dominio de `Discount`) se ejecutan antes de escribir los artefactos. La línea «Product Base Margin tiene 16 valores faltantes» es texto fijo del contrato: el código no la calcula ni la verifica. Sin este hito, el contrato listaría controles sin que ninguno bloquease la entrega.

### Inventario técnico de implementación

- **Introduce:** `pd.read_csv` con separador, codificación y decimal explícitos; `pd.to_datetime` con formato fijo; limpieza del prefijo BOM en nombres de columna.
- **Introduce:** validación con `assert` (subconjunto de columnas, `notna`, `duplicated` sobre llave compuesta, `between`).
- **Introduce:** agregación mensual con `dt.strftime("%Y-%m")`, `groupby().agg()` con `sum` y `nunique`, métrica derivada como cociente de agregados.
- **Introduce:** contrato de métrica en JSON y archivo `questions.json` que liga pregunta y archivo de respuesta (patrón reutilizado en P501–P508).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Contrato de lectura de un CSV regional | H01 | `source_format` con delimitador, decimal, fecha y codificación | Codificación declarada inconsistente con el BOM. |
| Grano y llave de línea de orden | H02 | Unicidad `Order ID` + `Product Name`; `nunique` de órdenes | `Row ID` no verificado. |
| Contrato de métrica independiente de herramienta | H03 | Fórmulas y grano en `metric_contract.json` | Sin procedencia del dataset. |
| Compuerta de calidad previa a la salida | H04 | Cuatro aserciones en `main` | Faltantes declarados, no calculados. |
| Serie mensual de métricas comerciales | H02, H03 | `monthly_sales_metrics.csv`, seis meses | Seis puntos; sin usuario declarado. |

### Relación técnica con actividades anteriores

Primera actividad `P5xx` del curso; no hay comparación previa dentro del curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Convención regional | S01, S02, S04 | `implementation/data/P500_superstore_metricas/professor/main.py`: `load_sales`, `build_contract`; `implementation/data/P500_superstore_metricas/submission/metric_contract.json`; contraste: `implementation/data/P501_superstore_serving/submission/sales_detail.csv`, `implementation/data/P513_superstore_batch/` (`utf-8-sig`) | El defecto de codificación se infiere del prefijo BOM y de la salida de P501; las métricas numéricas no se ven afectadas. |
| H02 — Grano línea-de-orden | S01, S03, S05 | `implementation/data/P500_superstore_metricas/professor/main.py`: `build_monthly_metrics`, aserción `duplicated`; `implementation/data/P500_superstore_metricas/submission/metric_contract.json` (`grain`) | Unicidad de `Row ID` sólo afirmada. |
| H03 — Métricas independientes de herramienta | S04 | `implementation/data/P500_superstore_metricas/submission/metric_contract.json` (`metrics`, `tool_boundary`) | La frontera es una declaración, no una segunda implementación. |
| H04 — Compuerta de calidad | S03, S04 | `implementation/data/P500_superstore_metricas/professor/main.py`: `main` | Los 16 faltantes son texto fijo; no hay prueba que ejecute los controles. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/superstore_orders.csv` | Seis meses de 2015; sin manifiesto de procedencia. |
| S02 | Representación / lectura | `professor/main.py`: `load_sales` | `latin1` sobre archivo con BOM UTF-8. |
| S03 | Validación | `professor/main.py`: aserciones de `main` | Cuatro reglas; faltantes y `Row ID` no verificados. |
| S04 | Contrato de métrica | `professor/main.py`: `build_contract`; `submission/metric_contract.json` | Contenido literal fijo en código. |
| S05 | Producto | `submission/monthly_sales_metrics.csv`; `submission/questions.json` | Una pregunta, una tabla mensual. |
| S06 | Pruebas | `tests/test_activity.py` | Sólo existencia de tres archivos. |
| S07 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin notebook ni instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe leer con formato explícito, ejecutar las aserciones antes de escribir y construir métricas a partir del grano declarado.
- **`submission/`:** `metric_contract.json` (formato, grano, controles, frontera, fórmulas), `monthly_sales_metrics.csv` (seis meses) y `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige que existan los tres archivos; no verifica contenido, fórmulas, controles ni que el estudiante haya implementado `src/main.py`. Como los artefactos del profesor ya están en `submission/`, la prueba pasa sobre el repositorio tal como está.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna dentro del curso.
- **Habilita para Pyyy:** P501 usa el mismo CSV, la misma función de lectura y una copia de la agregación mensual (`build_monthly_sales`); el patrón `questions.json` se reutiliza en P501–P508. P502 cataloga `average_order_value` como métrica derivada. No se evidencia que una actividad posterior lea `metric_contract.json`.

## Trazabilidad y auditoría

Entrada revisada: P500 → `data.C01`, `data.C02`, `data.C03`, `data.C04`, `data.C05`. Todas tienen evidencia: C01 (pregunta → grano y campos requeridos), C02 (lectura, agregación), C03 (aserciones de calidad, con el límite de los faltantes declarados y de la codificación), C04 (contrato persistido), C05 (`tool_boundary`). El producto de Analytics es una serie descriptiva mensual con definición auditable de métricas, sin usuario ni decisión declarados. pandas sirve a ese producto; la actividad no se lee como entrenamiento en una herramienta. Riesgo de identidad bajo.
