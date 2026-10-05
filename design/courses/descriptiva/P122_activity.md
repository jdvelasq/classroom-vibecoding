# P122 — Supply Chain: cumplimiento de entregas, valor expuesto y cobertura de flete

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P122_supply_chain/`.

### Preguntas analíticas actuales

- ¿Qué segmentos país–modo se deben priorizar para reducir riesgo, considerando volumen, cumplimiento y valor tardío?
- ¿Qué modos tienen suficiente cobertura de costo para comparar el flete sobre el valor observado?

El notebook formula además preguntas intermedias sobre cumplimiento global, distribución de días frente a la fecha prometida, modos, países, combinaciones país–modo y evolución mensual. Usa `data/supply_chain.csv`: 10.324 líneas de envío con 33 columnas (proyecto, país, modo, fechas programada y real, producto, proveedor, valor, peso, flete y seguro). Las descripciones visibles corresponden a insumos de salud (pruebas de VIH, antirretrovirales) entregados a países; la fuente, la licencia y el período de extracción no están documentados en la actividad. El producto describe cumplimiento y valor expuesto a retraso, y delimita qué parte del flete es comparable; no explica causas de retraso.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** priorizar segmentos país–modo por riesgo de entrega y juzgar la comparabilidad del flete; usuario y decisión concretos no evidenciados.
- **Producto terminal:** KPI globales, resúmenes por modo, país, país–modo y mes, diez países prioritarios por valor tardío y tabla de flete con cobertura explícita.
- **Uso y límite:** permite señalar dónde se concentra el valor entregado tarde y qué comparaciones de flete tienen base suficiente; no atribuye el retraso a un modo o país, no ajusta por mezcla de productos y no estima costo de flete faltante.
- **Disciplinas contribuyentes:** limpieza de tipos, agregación con pandas y visualización Plotly sirven al diagnóstico operativo.

### Highlights de contribución

- **H01 — Reconoce el grano antes de agregar:** inspecciona un registro completo (`shipments.loc[0]`), exige unicidad de `ID` y tabula faltantes y valores distintos de las columnas que usará. Extiende la verificación de P120 a un archivo ancho con faltantes; sin este hito, las sumas por país y modo se apoyarían en un grano supuesto.
- **H02 — Construye un KPI de cumplimiento a partir de dos fechas:** convierte fechas con formato `%d-%b-%y`, exige que no queden nulas, calcula días reales menos programados e `IsLate` si la diferencia es positiva, y muestra el histograma con referencia en cero. La particularidad del caso es que el resultado no viene dado: se deriva de una promesa y un hecho. Sin este hito, el cumplimiento sería una columna opaca.
- **H03 — Mantiene juntas la proporción a tiempo y la demora promedio:** `mode_summary.csv` persiste ambas y deja visible que no se mueven igual (Truck: −9,92 días promedio y 0,839 a tiempo; Air Charter: −19,04 días y 0,885), porque entregas anticipadas compensan retrasos en el promedio. El notebook no comenta el contraste, pero lo hace observable; sin este hito, un promedio negativo podría leerse como ausencia de incumplimiento.
- **H04 — Pondera el incumplimiento por valor expuesto:** suma `Line Item Value` de envíos tardíos (259.034.270,94 USD en `overall_kpis.csv`) y prioriza países por ese valor. Nuevo frente a P120–P121, que priorizaban por tasa o por valor devuelto; sin este hito, un país con muchos envíos pequeños tardíos pesaría igual que uno con pocos envíos de alto valor.
- **H05 — No convierte textos operativos en costo cero:** el campo de flete mezcla números con texto; `pd.to_numeric(errors="coerce")` y `HasNumericFreightCost` separan lo numérico, y `freight_by_mode.csv` reporta la cobertura del valor con flete numérico (0,63 en Truck a 0,84 en Ocean) antes de calcular flete sobre valor observado. Segundo hito de caso y datos: la condición del campo cambia el denominador y el límite de la comparación. Extiende la conversión de tipos de P106 con una regla explícita de no imputación.
- **H06 — Ajusta umbrales mínimos al nivel de segmentación:** 50 envíos por país, 20 por país–modo en la matriz y 30 en segmentos prioritarios; conserva el modo faltante con `dropna=False` (360 envíos sin modo). La matriz tiene filas = país y columnas = modo, con valor = proporción a tiempo. Extiende el umbral único de P120/P121; el límite es que los tres umbrales no se justifican en el notebook y la serie mensual no tiene mínimo (meses iniciales con 2 envíos y cumplimiento 1,0).
- **H07 — Persiste ocho tablas con pruebas de coherencia:** las pruebas verifican igualdades de KPI, conservación de totales por modo y mes, rangos de proporciones, umbrales mínimos y la suma de flete numérico por modo. Más laxas que en P120/P121: no recomputan países prioritarios, país–modo ni ordenamientos.

### Inventario técnico de implementación

- **Introduce:** tabla de calidad (faltantes/distintos); KPI derivado de dos fechas; histograma con línea de referencia; valor expuesto a retraso; agregación condicional con `lambda` sobre índice; cobertura de un campo antes de usarlo como numerador; `dropna=False` para conservar categoría faltante.
- **Extiende:** umbral de volumen (ahora por nivel); matriz de dos dimensiones; contrato `questions.json`.
- **Reutiliza:** `to_datetime`, `to_period("M")`, `groupby().agg()`, `nlargest`, `px.bar`, `px.imshow`, `px.line`.
- **Aplica en nuevo caso:** plantilla de diagnóstico de P120/P121 a cadena de suministro con datos incompletos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Cumplimiento derivado | H02–H03 | Días real − programada; proporción a tiempo y promedio | Retraso de un día cuenta igual que uno largo en la proporción. |
| Valor expuesto | H04 | Suma de valor de envíos tardíos | No incluye costo del retraso. |
| Cobertura de dato | H05 | Flete numérico vs textual; cobertura por modo | Flete faltante no se estima. |
| Segmentación con umbrales | H06 | 50/20/30 envíos; matriz país × modo | Umbrales sin justificación; mensual sin mínimo. |
| Producto verificable | H07 | Ocho CSV; pruebas de totales y rangos | No verifica ordenamientos ni prioridades. |

### Relación técnica con actividades anteriores

P122 repite la plantilla de P120/P121 (preguntas, KPI, serie mensual, resumen por entidad, matriz, segmentos con umbral). Añade, sin embargo, exigencias de evidencia distintas: un KPI que debe construirse desde fechas, la tensión entre proporción y promedio, la ponderación por valor y la cobertura de un campo mezclado. Respecto de P106, aplica conversión de tipos pero con una decisión analítica explícita (no imputar texto como cero). La repetición de la secuencia matriz → top N con umbral es una posible duplicación de forma, no de evidencia. El comentario de la serie mensual promete no confundir «cambio de mezcla» con mejora operativa, pero el código sólo añade el conteo de envíos.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Grano y calidad | S01 | `implementation/descriptiva/P122_supply_chain/professor/notebook.ipynb`: `shipments.loc[0]`, `quality_summary`, `assert ... is_unique` | La tabla de calidad cubre siete columnas seleccionadas. |
| H02 — KPI desde fechas | S02 | notebook: conversión de fechas, `DeliveryDaysVsSchedule`, `IsLate`, histograma | Las fechas de PO y PQ («Date Not Captured») no se usan. |
| H03 — Proporción vs promedio | S02, S05 | `implementation/descriptiva/P122_supply_chain/submission/mode_summary.csv` | Contraste observable, no discutido en el notebook. |
| H04 — Valor expuesto | S03 | notebook: `valor_enviado_tarde_usd`; `implementation/descriptiva/P122_supply_chain/submission/overall_kpis.csv`; `implementation/descriptiva/P122_supply_chain/submission/priority_countries.csv` | Valor de la línea, no pérdida por retraso. |
| H05 — Cobertura de flete | S04 | notebook: `FreightCostUSD`, `HasNumericFreightCost`, `freight_quality`, `freight_by_mode`; `implementation/descriptiva/P122_supply_chain/submission/freight_by_mode.csv` | Los valores textuales del flete no se inspeccionan ni se clasifican en el notebook. |
| H06 — Umbrales por nivel | S03 | notebook: `minimum_shipments = 50`, `query("envíos >= 20")`, `query("envíos >= 30")`; `implementation/descriptiva/P122_supply_chain/submission/monthly_summary.csv` | Umbrales sin justificación; el mes no tiene mínimo. |
| H07 — Persistencia y pruebas | S05, S06 | `implementation/descriptiva/P122_supply_chain/tests/test_activity.py`: `test_01`–`test_05` | No verifican `questions.json`, `country_mode_summary.csv`, `priority_countries.csv` ni orden de prioridad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y grano | `data/supply_chain.csv`; celdas de carga y calidad | Procedencia y licencia no documentadas; 33 columnas, varias sin uso. |
| S02 | Definición de cumplimiento | Notebook: fechas, `DeliveryDaysVsSchedule`, `IsLate`; histograma | Tardío = más de 0 días; sin tolerancia. |
| S03 | Segmentación, umbrales y priorización | Notebook: resúmenes por modo, país, país–modo, mes; CSV asociados | Umbrales 50/20/30; serie mensual sin mínimo; `priority_segments.csv` se persiste sin el orden mostrado. |
| S04 | Cobertura y razón de flete | Notebook: `freight_quality`, `freight_by_mode`; `freight_by_mode.csv` | Flete textual excluido, no estimado. |
| S05 | Producto/entregable | `submission/questions.json` y ocho CSV | Figuras no persistidas. |
| S06 | Pruebas | `tests/test_activity.py` | Verifican totales y rangos, no contenido completo. |

### Contrato de evidencia actual

- **Notebook o código:** verifica grano y faltantes, deriva cumplimiento desde fechas, pondera por valor, separa flete numérico y aplica umbrales por nivel.
- **`submission/`:** `questions.json`, `overall_kpis.csv`, `mode_summary.csv`, `country_summary.csv`, `priority_countries.csv`, `country_mode_summary.csv`, `monthly_summary.csv`, `priority_segments.csv`, `freight_by_mode.csv`.
- **Pruebas:** exigen exactamente ocho CSV; comprueban KPI, totales, rangos 0–1, umbrales y suma de flete por modo; no recomputan todas las tablas ni verifican preguntas o figuras.
- **Trazabilidad:** P122 mapea `descriptiva.C01`, `C02` y `C03`.

### Dependencias en la secuencia

- **Recibe de P120/P121:** contrato `questions.json`, umbral de volumen y matriz de dos dimensiones; de P106, la conversión de columnas textuales a numéricas.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P122 está mapeada a `descriptiva.C01`, `descriptiva.C02` y `descriptiva.C03` en `implementation/descriptiva/traceability.yaml`; la evidencia las sostiene, con C02 especialmente visible en la tabla de calidad y la cobertura de flete. La declaración de cobertura es una forma de comunicación de límites (cercana a C05), no mapeada. El notebook no explicita un límite causal pese a hablar de «reducir riesgo». El producto de Analytics es un diagnóstico de cumplimiento y valor expuesto; pandas y Plotly lo sirven. Responde qué, dónde y cuándo; usuario y decisión no evidenciados.
