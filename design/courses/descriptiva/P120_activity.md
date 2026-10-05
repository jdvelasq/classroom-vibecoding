# P120 — Retail Sales: ventas, devoluciones y segmentos prioritarios

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P120_retail_sales/`.

### Preguntas analíticas actuales

- ¿Qué segmentos se deben priorizar para investigar y reducir las devoluciones?
- ¿Qué medios de pago combinan ventas netas y tasas de devolución que requieren investigación?

El notebook de profesor recorre además preguntas intermedias explícitas: desempeño global bruto/devuelto/neto, evolución mensual, categorías, clientes, productos, riesgo por categoría–canal y diferencia entre días laborales y fines de semana. Usa `data/sales.csv`: 1.000 órdenes de un producto cada una, con categoría, canal, medio de pago, cliente y una marca binaria `IsReturned`; la serie persistida cubre ocho meses desde 2022-01. La procedencia del archivo no está documentada en la actividad; los nombres `Product_NNN` y los identificadores numéricos no permiten establecer si es real o sintético. El producto es un conjunto de tablas descriptivas y gráficos que ordenan dónde investigar devoluciones; no explica por qué ocurren.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** priorizar segmentos para investigar devoluciones; usuario y decisión concretos no evidenciados.
- **Producto terminal:** diagnóstico descriptivo de ventas netas y devoluciones por segmento, con lista de cinco segmentos prioritarios y preguntas enlazadas a su archivo de respuesta.
- **Uso y límite:** permite señalar dónde se concentra el valor devuelto; no estima incertidumbre, no identifica causas de devolución y no prueba que un canal o medio de pago provoque devoluciones.
- **Disciplinas contribuyentes:** pandas (agregación), Plotly (visualización) y pruebas con `pytest` sirven al diagnóstico; no organizan el taller.

### Highlights de contribución

- **H01 — Enlaza cada pregunta con el archivo que la responde:** escribe `submission/questions.json` con pares `pregunta`/`archivo_respuesta` antes de cargar datos. Primera aparición del contrato en el curso (P100–P109 no lo tienen); sin él, las tablas persistidas no declararían qué pregunta sustentan.
- **H02 — Verifica el grano y la consistencia aritmética antes de agregar:** comprueba ausencia de faltantes, unicidad de `OrderID` y `Quantity × Price = TotalAmount` redondeado a dos decimales. Extiende las validaciones de P106/P107 de «limpiar» a «confirmar que una fila es una orden completa»; sin este hito, las sumas por segmento se apoyarían en un grano no verificado.
- **H03 — Convierte una devolución binaria por orden en valor devuelto y venta neta:** el dataset marca la devolución con `IsReturned` a nivel de orden, sin devolución parcial; por eso `ReturnedAmount` toma todo `TotalAmount` cuando la marca es 1 y `NetAmount` es su complemento. Esta particularidad fija el producto: cada métrica posterior distingue bruto, devuelto y neto. Sin este hito, ventas y devoluciones se leerían como magnitudes independientes; el límite es que no puede representar devoluciones parciales.
- **H04 — Distingue tasa de devolución por órdenes y por valor:** `kpi_summary.csv` persiste `return_rate_by_orders` (0,516) y `return_rate_by_value` (0,5026), además de venta neta por orden. Sin este hito, la proporción de órdenes devueltas se confundiría con la proporción del dinero devuelto.
- **H05 — Codifica magnitud y tasa en un mismo gráfico:** barras de venta neta coloreadas por tasa de devolución para categoría, tipo de día y medio de pago, y serie mensual en formato largo (`melt`) para comparar bruto, devuelto y neto. Introduce Plotly frente a las barras estáticas de P103/P104; sin este hito, volumen y riesgo se mostrarían en vistas separadas.
- **H06 — Exige volumen mínimo antes de ordenar por tasa:** `return_risk` filtra combinaciones categoría–canal con al menos 50 órdenes y las presenta en una matriz con filas = categoría y columnas = canal; cada celda es una tasa agregada del período, no una observación temporal. Primera aparición del umbral de volumen en el curso; sin él, segmentos pequeños podrían encabezar el ranking.
- **H07 — Separa criterio de riesgo y criterio de prioridad:** `return_risk.csv` ordena por tasa (Home & Garden — Mobile App, 0,5758, primero) mientras `priority_segments.csv` toma los cinco segmentos con mayor valor devuelto (Fashion — Mobile App, 87.672,87, primero). Sin este hito, la prioridad se reduciría a la tasa más alta sin considerar el valor expuesto.
- **H08 — Persiste nueve tablas que las pruebas recomputan:** las pruebas reconstruyen la preparación y comparan cada CSV con `assert_frame_equal`. Extiende el patrón de recomputación de P103/P104 a un producto de varias tablas; sin este hito, el diagnóstico no sería auditable tras cerrar el notebook.

### Inventario técnico de implementación

- **Introduce:** contrato `questions.json`; métricas derivadas bruto/devuelto/neto; tasa por órdenes y por valor; umbral mínimo de volumen; matriz categoría × canal con `pivot` e `imshow`; gráficos Plotly con color continuo como segunda medida.
- **Extiende:** agregación `groupby().agg()` con nombres de salida (P103); validaciones con `assert` (P106/P107); persistencia en `submission/`.
- **Reutiliza:** rutas relativas verificadas, `to_datetime`, `to_period("M")`, `nlargest`.
- **Aplica en nuevo caso:** ranking de clientes y de productos dentro de categoría (`groupby(...).head(5)`).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Pregunta enlazada a evidencia | H01 | `questions.json` con archivo de respuesta | Las pruebas no verifican `questions.json`. |
| Medidas bruto/devuelto/neto | H03–H04 | Devolución binaria total por orden; dos tasas | No representa devoluciones parciales. |
| Segmentación con umbral | H06–H07 | Mínimo 50 órdenes; ranking por tasa vs por valor | Sin intervalos ni pruebas de diferencia. |
| Visualización de dos medidas | H05 | Barras coloreadas por tasa; serie larga | Figuras no persistidas. |
| Producto verificable | H08 | Nueve CSV recomputados por pruebas | Verifica cálculo, no interpretación. |

### Relación técnica con actividades anteriores

P120 es el primer caso descriptivo completo tras los fundamentos P100–P109. Reutiliza la agregación y la persistencia de P103/P104 (mismo patrón tabla resumen + gráfico + prueba que recomputa), pero añade una pregunta de priorización, métricas derivadas y umbral de volumen. No limpia datos como P106/P107: verifica que el archivo ya es consistente. Establece la plantilla —preguntas, verificación, KPI global, serie mensual, segmentos, matriz de dos dimensiones, segmentos prioritarios, CSV recomputados— que P121 y P122 repiten con otros datos; la posible duplicación se registra en esas actividades.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Preguntas enlazadas | S05, S06 | `implementation/descriptiva/P120_retail_sales/professor/notebook.ipynb`: celda de `questions`; `implementation/descriptiva/P120_retail_sales/submission/questions.json` | Las pruebas sólo enumeran `*.csv`; no comprueban preguntas. |
| H02 — Grano y consistencia | S01 | `implementation/descriptiva/P120_retail_sales/professor/notebook.ipynb`: celda de `assert` sobre faltantes, `OrderID` y `TotalAmount` | Verifica el archivo entregado, no su procedencia. |
| H03 — Devolución binaria a valor neto | S01, S02 | `implementation/descriptiva/P120_retail_sales/data/sales.csv`: `IsReturned`; notebook: `ReturnedAmount`, `NetAmount` | Supone devolución total; la tasa cercana a 0,5 no se discute en el notebook. |
| H04 — Dos tasas de devolución | S02 | `implementation/descriptiva/P120_retail_sales/submission/kpi_summary.csv` | Valores del período observado; sin incertidumbre. |
| H05 — Magnitud y tasa en un gráfico | S04 | `implementation/descriptiva/P120_retail_sales/professor/notebook.ipynb`: `px.bar(... color="return_rate")`, `melt` y `px.line` | Las figuras no se guardan en `submission/`. |
| H06 — Umbral de volumen y matriz | S03, S04 | notebook: `minimum_orders = 50`, `pivot`, `px.imshow`; `implementation/descriptiva/P120_retail_sales/submission/return_risk.csv` | Las tasas por categoría difieren en torno a un punto (0,512–0,522 en `category_summary.csv`); no se evalúa si las diferencias son estables. |
| H07 — Riesgo vs prioridad | S03, S05 | `implementation/descriptiva/P120_retail_sales/submission/return_risk.csv`; `implementation/descriptiva/P120_retail_sales/submission/priority_segments.csv` | Señala dónde investigar; no identifica causas ni acciones. |
| H08 — Persistencia verificada | S05, S06 | `implementation/descriptiva/P120_retail_sales/tests/test_activity.py`: `test_01`–`test_06` | Las pruebas reproducen la solución; no evalúan lectura ni gráficos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y grano | `data/sales.csv`; celdas de carga y verificación del notebook | Procedencia no documentada; una orden = un producto; devolución binaria. |
| S02 | Representación de devolución y medidas derivadas | Notebook: `ReturnedAmount`, `NetAmount`, `OrderMonth`, `DayType`; `kpi_summary.csv` | Devolución total por orden; tasas sin incertidumbre. |
| S03 | Segmentación, umbral y priorización | Notebook: `return_risk`, `priorities`; `return_risk.csv`, `priority_segments.csv` | Umbral fijo de 50 órdenes; prioridad por valor devuelto. |
| S04 | Visualización | Notebook: figuras Plotly de mes, categoría, productos, matriz, tipo de día y medio de pago | No persistidas; sin pruebas. |
| S05 | Producto/entregable | `submission/questions.json` y nueve CSV | La pregunta de medios de pago se responde con tabla sin criterio explícito de «requiere investigación». |
| S06 | Pruebas | `tests/test_activity.py` | Recomputan CSV; omiten `questions.json` y figuras. |

### Contrato de evidencia actual

- **Notebook o código:** verifica grano y consistencia, deriva valor devuelto y neto, agrega por período y segmentos, filtra por volumen mínimo y prioriza por valor devuelto.
- **`submission/`:** `questions.json`, `kpi_summary.csv`, `monthly_sales.csv`, `category_summary.csv`, `top_customers.csv`, `top_products.csv`, `return_risk.csv`, `priority_segments.csv`, `day_type_summary.csv`, `payment_summary.csv`.
- **Pruebas:** exigen exactamente los nueve CSV y recomputan cada uno desde `data/sales.csv`; no verifican `questions.json`, gráficos ni interpretación.
- **Trazabilidad:** P120 mapea `descriptiva.C01`, `C02` y `C03`.

### Dependencias en la secuencia

- **Recibe de P103/P104:** patrón de resumen agregado persistido en `submission/` y prueba que lo recomputa; de P106/P107, la práctica de validar columnas antes de analizar.
- **Habilita para P121–P125:** contrato `questions.json` y plantilla de diagnóstico con umbral de volumen, reutilizados de forma observable en P121 y P122; `questions.json` reaparece en P123–P125 y P150–P154. No hay artefacto de datos compartido.

## Trazabilidad y auditoría

P120 está mapeada a `descriptiva.C01`, `descriptiva.C02` y `descriptiva.C03` en `implementation/descriptiva/traceability.yaml`; la evidencia sostiene las tres (preguntas con archivo de respuesta, verificación y exploración por segmentos, visualizaciones). No mapea C04 ni C05, y el notebook no declara un límite asociación/causalidad aunque formula preguntas de priorización. El producto de Analytics es un diagnóstico descriptivo de dónde se concentran las devoluciones; pandas, Plotly y `pytest` contribuyen a él. Responde qué ocurre, en qué segmentos y cuándo; el «para quién» y la decisión concreta no están evidenciados.
