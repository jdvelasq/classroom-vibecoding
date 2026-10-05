# P121 — Vuelos: demoras y cancelaciones por aerolínea, día y hora

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P121_vuelos/`.

### Preguntas analíticas actuales

- ¿Qué segmentos aerolínea–día–hora se deben priorizar para investigar y reducir las demoras?
- ¿La evolución de las aerolíneas de mayor volumen revela un patrón estacional?

El notebook formula además preguntas intermedias sobre KPI nacional, evolución mensual, aerolíneas y concentración por día y hora programada. No trabaja con vuelos individuales: recibe dos agregados comprimidos que el notebook llama «reales» —`flights_by_carrier_day_hour.csv.gz` (año, mes, aerolínea, día de la semana, hora programada) y `flights_by_carrier_month.csv.gz` (año, mes, aerolínea)— con conteos aditivos de vuelos programados, cancelados, operados, demorados 15 minutos o más y minutos positivos de demora. Las salidas persistidas cubren 36 meses desde 2006-01 y 21 códigos de aerolínea; la fuente original, la fecha de extracción y la transformación que produjo los agregados no están documentadas en la actividad. El producto describe dónde y cuándo se concentran las demoras; no las explica ni las pronostica.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** priorizar segmentos aerolínea–día–hora para investigar demoras; usuario y decisión concretos no evidenciados.
- **Producto terminal:** KPI nacionales, series mensuales, perfil día × hora, resumen por aerolínea, diez segmentos prioritarios y patrón mensual de las cinco aerolíneas de mayor volumen.
- **Uso y límite:** permite localizar concentraciones de demora con volumen suficiente; no atribuye causas (clima, congestión, operación), no separa años en el patrón estacional y no permite análisis por vuelo.
- **Disciplinas contribuyentes:** agregación con pandas, conciliación de tablas y visualización Plotly sirven al diagnóstico.

### Highlights de contribución

- **H01 — Trabaja con agregados aditivos en lugar de registros individuales:** la particularidad del caso es que la unidad disponible es la celda de un agregado (aerolínea × año × mes × día × hora), no el vuelo. Por eso sólo se suman conteos y minutos, y cualquier tasa o promedio se reconstruye después de sumar; no hay medianas ni distribuciones por vuelo. Nuevo frente a P120, cuyo grano era la orden; sin este hito, el estudiante promediaría tasas de celdas de tamaño distinto.
- **H02 — Concilia dos niveles de agregación antes de analizar:** reagrupa el archivo día–hora por año, mes y aerolínea y exige igualdad exacta con el archivo mensual (`assert_frame_equal`); la prueba repite el control. Primera conciliación entre granularidades del curso; sin ella, las vistas mensual y día–hora podrían provenir de bases inconsistentes.
- **H03 — Define cada tasa con su denominador:** `add_rates` calcula cancelación sobre programados, demora sobre operados y minutos positivos medios sobre operados, aplicada siempre tras sumar las medidas aditivas. Contrasta con P120, donde la tasa era la media de una marca binaria; sin este hito, se mezclarían denominadores o se promediarían razones.
- **H04 — Lee la matriz día × hora como patrón agregado:** la matriz tiene filas = día de la semana (1–7) y columnas = hora programada (0–23); cada una de las 168 celdas agrupa todos los vuelos de esa franja durante tres años y todas las aerolíneas. Describe un perfil semanal típico, no días observados; la matriz no muestra el volumen de cada celda (Lunes 03:00 tiene 177 vuelos operados en `day_hour_delay.csv`). Extiende la matriz categoría × canal de P120 a una estructura calendario.
- **H05 — Prioriza segmentos de tres dimensiones con umbral de volumen:** cruza aerolínea × día × hora, exige al menos 25.000 vuelos operados y toma los diez de mayor tasa de demora; el primero persistido es WN — Viernes — 20:00 (0,4506). Extiende el umbral de 50 órdenes de P120 a una escala de millones de vuelos; sin él, franjas nocturnas pequeñas dominarían el ranking.
- **H06 — Contrasta serie mensual nacional y patrón por mes del año:** persiste la serie de 36 meses y, por separado, la tasa por mes del año para las cinco aerolíneas de mayor volumen, agrupando los tres años. Sin este hito, la pregunta estacional no tendría una vista distinta de la tendencia; el límite es que la estacionalidad se juzga visualmente y sin separar años.
- **H07 — Persiste seis tablas recomputadas por las pruebas, incluida la conciliación:** las pruebas recalculan cada CSV desde los agregados y verifican la igualdad entre ambos archivos de datos. Sin este hito, la conciliación quedaría como celda de notebook no exigida.

### Inventario técnico de implementación

- **Introduce:** lectura de CSV comprimidos; conciliación entre granularidades; función reutilizable de tasas con denominadores distintos; matriz calendario día × hora; segmentos de tres dimensiones; vista por mes del año.
- **Extiende:** umbral de volumen y matriz de dos dimensiones de P120; contrato `questions.json`.
- **Reutiliza:** `groupby().sum()`, `nlargest`, `pivot`, `px.imshow`, `px.line`, persistencia en `submission/`.
- **Aplica en nuevo caso:** plantilla de diagnóstico de P120 a un dominio operativo con datos preagregados.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Agregados aditivos | H01–H03 | Suma de conteos y razón de sumas con denominador propio | Sin acceso a vuelos individuales. |
| Conciliación | H02, H07 | Igualdad día–hora reagrupado vs mensual | Comprueba coherencia interna, no procedencia. |
| Perfil calendario | H04 | Matriz 7 × 24 de tasa de demora | Volumen por celda no visible en la matriz. |
| Priorización con umbral | H05 | ≥25.000 operados; top 10 por tasa | Señala dónde investigar; no causas. |
| Estacionalidad | H06 | Tasa por mes del año, cinco aerolíneas | Años agrupados; juicio visual. |

### Relación técnica con actividades anteriores

P121 aplica la plantilla de P120 (preguntas, KPI global, serie mensual, resumen por entidad, matriz, segmentos prioritarios con umbral, CSV recomputados) a otro dominio. No es una duplicación simple: añade una nueva exigencia de evidencia —datos preagregados que obligan a conciliar granularidades y a reconstruir tasas desde sumas— y un nuevo tipo de matriz (calendario). Sí repite, sin cambio de método, la secuencia «matriz de dos dimensiones → top N con umbral»; si P120–P122 deben conservar los tres casos con la misma secuencia es una decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Agregados aditivos | S01, S02 | `implementation/descriptiva/P121_vuelos/professor/notebook.ipynb`: `metric_columns`, carga de los dos `.csv.gz` | Estructura inferida de columnas usadas; la documentación de la fuente no existe en la actividad. |
| H02 — Conciliación | S01, S06 | notebook: celda `recomputed` / `assert_frame_equal`; `implementation/descriptiva/P121_vuelos/tests/test_activity.py`: `test_02` | Verifica coherencia entre archivos, no frente a la fuente original. |
| H03 — Denominadores | S02 | notebook: `add_rates`; `implementation/descriptiva/P121_vuelos/submission/overall_kpis.csv` | Demora definida como salida con ≥15 minutos; no hay otra definición contrastada. |
| H04 — Matriz día × hora | S03 | notebook: `calendar_hour`, `pivot`, `px.imshow`; `implementation/descriptiva/P121_vuelos/submission/day_hour_delay.csv` | Celdas con volumen muy desigual se colorean igual. |
| H05 — Segmentos con umbral | S04 | notebook: `minimum_operated_flights = 25_000`; `implementation/descriptiva/P121_vuelos/submission/priority_segments.csv` | Umbral fijo sin justificación persistida; no hay incertidumbre. |
| H06 — Serie y estacionalidad | S03 | `implementation/descriptiva/P121_vuelos/submission/monthly_national_kpis.csv`; `implementation/descriptiva/P121_vuelos/submission/seasonality.csv` | No descompone tendencia/estacionalidad ni separa años. |
| H07 — Persistencia verificada | S05, S06 | `implementation/descriptiva/P121_vuelos/tests/test_activity.py`: `test_01`–`test_06` | No verifica `questions.json`, figuras ni interpretación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datasets agregados | `data/flights_by_carrier_day_hour.csv.gz`; `data/flights_by_carrier_month.csv.gz` | Sin documentación de origen ni transformación; sin registros por vuelo. |
| S02 | Definición de tasas | Notebook: `add_rates`; réplica `rates` en pruebas | Denominadores distintos para cancelación y demora. |
| S03 | Vistas temporales y calendario | Notebook: serie mensual, matriz día × hora, estacionalidad; tres CSV asociados | Años agrupados en la vista estacional; volumen oculto en la matriz. |
| S04 | Priorización | Notebook: `critical`; `priority_segments.csv` | Umbral fijo de 25.000 vuelos operados. |
| S05 | Producto/entregable | `submission/questions.json` y seis CSV | Las figuras no se persisten. |
| S06 | Pruebas | `tests/test_activity.py` | Recomputan CSV y conciliación; omiten `questions.json`. |

### Contrato de evidencia actual

- **Notebook o código:** carga dos agregados, verifica faltantes, concilia granularidades, reconstruye tasas desde sumas y produce vistas nacional, por aerolínea, calendario, segmentos y estacional.
- **`submission/`:** `questions.json`, `overall_kpis.csv`, `monthly_national_kpis.csv`, `carrier_summary.csv`, `day_hour_delay.csv`, `priority_segments.csv`, `seasonality.csv`.
- **Pruebas:** exigen exactamente seis CSV, verifican la conciliación entre archivos de datos y recomputan cada tabla; no verifican preguntas ni gráficos.
- **Trazabilidad:** P121 mapea `descriptiva.C01`, `C02` y `C03`.

### Dependencias en la secuencia

- **Recibe de P120:** contrato `questions.json`, umbral de volumen antes de ordenar por tasa, matriz de dos dimensiones y patrón de CSV recomputados.
- **Habilita para Pyyy:** no evidenciada como artefacto. La razón de sumas con denominador explícito reaparece en P124 (`safe_divide`, ROAS y CPC desde sumas), sin dependencia técnica demostrable.

## Trazabilidad y auditoría

P121 está mapeada a `descriptiva.C01`, `descriptiva.C02` y `descriptiva.C03` en `implementation/descriptiva/traceability.yaml`; la evidencia las sostiene. La conciliación de agregados aporta a C02 (calidad antes de concluir). No se declara un límite asociación/causalidad, aunque la pregunta habla de «reducir» demoras. El producto de Analytics es un diagnóstico de dónde y cuándo se concentran demoras; pandas y Plotly lo sirven. Responde qué, dónde y cuándo; el usuario y la decisión no están evidenciados.
