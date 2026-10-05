# P124 — Tablero de desempeño de campañas de marketing

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P124_marketing_dashboard/`.

### Preguntas analíticas actuales

- ¿Qué fuentes de tráfico aportan mayor utilidad bruta?
- ¿Cómo evoluciona la utilidad bruta de las campañas?

Usa `data/campaign_data.csv`: 1.096 registros con fecha UTC, fuente de tráfico, cuenta, gestor, dispositivo, navegador, plantilla de campaña, país y estado, más impresiones, clics, ingreso, inversión publicitaria y razones ya calculadas (`roas`, `rpc`, `cpc`, `cpa`, `gross_profit`). La interfaz declara que son «datos suministrados para el taller» que «no representan resultados operativos reales»; su origen no está documentado y las URL usan `example.com`. No hay notebook: `professor/main.py` contiene funciones analíticas y exporta tablas; `professor/app.py` es un tablero Streamlit con filtros. El producto es una vista filtrable de desempeño y su versión persistida para el período completo; no atribuye ingresos a campañas ni evalúa causalidad de la inversión.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** comparar utilidad bruta por fuente y en el tiempo; usuario y decisión no evidenciados.
- **Producto terminal:** tablero interactivo (KPI, serie diaria, barras por fuente, detalle por plantilla) y cuatro tablas persistidas del período completo con `questions.json`.
- **Uso y límite:** permite explorar desempeño por período, fuente y país con razones recalculadas en el alcance filtrado; «utilidad bruta» es sólo ingreso menos inversión publicitaria, los datos no son operativos y no se infiere que una fuente cause mayor utilidad.
- **Disciplinas contribuyentes:** validación de datos, agregación con pandas, Streamlit y Plotly sirven a una interfaz descriptiva; el tablero no es un fin en sí mismo.

### Highlights de contribución

- **H01 — Reconoce que cada registro es un día con una sola combinación de campaña:** el archivo de datos y `daily_summary.csv` tienen el mismo número de filas (1.096), por lo que cada fecha aparece una vez y lleva una sola fuente, plantilla y país. La serie diaria reproduce los registros, y los resúmenes por fuente o plantilla suman los días asignados a cada una. Además, el archivo trae razones por fila que el código no promedia. Esta particularidad hace que el tablero describa una muestra diaria de campañas, no el gasto simultáneo de todas las fuentes; sin este hito, la comparación por fuente se leería como mezcla de canales concurrentes.
- **H02 — Valida esquema, tipos y no negatividad antes de calcular:** `load_campaign_data` exige columnas requeridas, convierte fecha y métricas con `errors="raise"`, rechaza valores negativos en impresiones, clics, ingreso e inversión, y recalcula `gross_profit`, que sí puede ser negativo (2020-01-03: −76,92). Extiende el patrón `REQUIRED_COLUMNS` + `ValueError` de P102 a un insumo analítico; sin este hito, el tablero podría mostrar KPI de datos mal tipados.
- **H03 — Recalcula razones desde sumas en cada alcance y protege denominadores nulos:** `calculate_kpis` y `summarize_by_source` obtienen ROAS = ingreso / inversión y CPC = inversión / clics pagados después de sumar, y `safe_divide` devuelve `None`, que la interfaz muestra como «No disponible». Extiende la razón de sumas de P121 a un tablero filtrable; sin este hito, un filtro cambiaría la base de las razones sin reflejarlo o fallaría con divisiones por cero.
- **H04 — Separa funciones analíticas de la interfaz:** `app.py` importa las funciones de `main.py`, cachea la carga, filtra por rango de fechas, fuente y país, detiene la vista ante un rango incompleto o un filtro vacío y muestra KPI, serie diaria, barras por fuente y tabla por plantilla. Primera interfaz interactiva del curso; sin este hito, las mismas reglas se duplicarían entre el tablero y la exportación.
- **H05 — Persiste el período completo como evidencia verificable:** `export_dashboard_tables` guarda `kpis.csv`, `daily_summary.csv`, `source_summary.csv`, `campaign_summary.csv` y `questions.json`; las pruebas recomputan las cuatro tablas desde los datos. El tablero filtrado no deja evidencia persistida.

### Inventario técnico de implementación

- **Introduce:** tablero Streamlit (`st.cache_data`, filtros en barra lateral, `st.metric`, `st.stop`); función de división segura; separación funciones/interfaz; recálculo de razones por alcance de filtro.
- **Extiende:** validación de columnas requeridas y errores explícitos (P102); razones desde sumas (P121).
- **Reutiliza:** `groupby().agg()`, Plotly, contrato `questions.json`, persistencia en `submission/`.
- **Aplica en nuevo caso:** KPI global, serie temporal y ranking por entidad (plantilla de P120) a desempeño publicitario.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Grano diario | H01 | Una fila por fecha con una combinación de campaña | Datos declarados no operativos; origen no documentado. |
| Validación de insumo | H02 | Columnas requeridas, tipos, no negatividad | No valida coherencia de las razones de origen. |
| Razones por alcance | H03 | ROAS y CPC desde sumas; `safe_divide` | «Utilidad bruta» = ingreso − inversión. |
| Interfaz filtrable | H04 | Streamlit con fecha, fuente y país | Sin pruebas de interfaz ni de filtros. |
| Evidencia persistida | H05 | Cuatro CSV del período completo | No persiste vistas filtradas. |

### Relación técnica con actividades anteriores

P124 reutiliza el contenido analítico de P120–P122 (KPI global, serie temporal, ranking por entidad) con menos profundidad diagnóstica: no hay umbral de volumen, matriz ni segmentos prioritarios. Su contribución nueva es de producto: una interfaz filtrable que obliga a recalcular razones en cada alcance y a separar funciones de presentación. Respecto de P102 reaplica la validación de esquema. No duplica P120–P122 en evidencia, pero sí en preguntas de tipo «qué entidad aporta más / cómo evoluciona».

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Grano diario | S01 | `implementation/descriptiva/P124_marketing_dashboard/data/campaign_data.csv` (1.097 líneas con encabezado); `implementation/descriptiva/P124_marketing_dashboard/submission/daily_summary.csv` (1.097 líneas); `implementation/descriptiva/P124_marketing_dashboard/professor/app.py`: `st.caption` | Grano inferido por igualdad de conteos; el código no lo declara ni lo verifica. |
| H02 — Validación | S02 | `implementation/descriptiva/P124_marketing_dashboard/professor/main.py`: `REQUIRED_COLUMNS`, `load_campaign_data` | Las pruebas no ejercitan la validación. |
| H03 — Razones por alcance | S03 | `implementation/descriptiva/P124_marketing_dashboard/professor/main.py`: `safe_divide`, `calculate_kpis`, `summarize_by_source`; `implementation/descriptiva/P124_marketing_dashboard/submission/kpis.csv` | ROAS 2,734 y CPC 1,644 del período completo; no hay incertidumbre. |
| H04 — Funciones e interfaz | S04 | `implementation/descriptiva/P124_marketing_dashboard/professor/app.py`; `implementation/descriptiva/P124_marketing_dashboard/professor/main.py`: `filter_campaign_data` | El comentario de `app.py` remite a `src/app.py`, que no existe; `src/main.py` sólo lanza `NotImplementedError`. |
| H05 — Persistencia verificada | S05, S06 | `implementation/descriptiva/P124_marketing_dashboard/professor/main.py`: `export_dashboard_tables`; `implementation/descriptiva/P124_marketing_dashboard/tests/test_activity.py`: `test_01`–`test_05` | Las pruebas no cubren filtros, `safe_divide` ni contenido de `questions.json`. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y grano | `data/campaign_data.csv` | Una fila por día; datos no operativos; origen no documentado; razones de origen sin uso. |
| S02 | Carga y validación | `professor/main.py`: `load_campaign_data` | Sólo cuatro métricas validadas como no negativas. |
| S03 | KPI y razones | `professor/main.py`: `calculate_kpis`, `summarize_by_*`, `safe_divide` | Utilidad bruta sin otros costos. |
| S04 | Interfaz | `professor/app.py` | Sin persistencia ni pruebas; ruta de ejecución del estudiante ambigua. |
| S05 | Producto/entregable | `professor/main.py`: `export_dashboard_tables`; `submission/` | Período completo únicamente; `campaign_summary.csv` no responde a una pregunta declarada. |
| S06 | Pruebas | `tests/test_activity.py` | Recomputan tablas; no prueban interfaz ni validación. |

### Contrato de evidencia actual

- **Notebook o código:** `main.py` valida, deriva utilidad, filtra, calcula KPI con división segura y resume por día, fuente y plantilla; `app.py` presenta esas funciones con filtros.
- **`submission/`:** `questions.json`, `kpis.csv`, `daily_summary.csv`, `source_summary.csv`, `campaign_summary.csv`.
- **Pruebas:** conjunto exacto de cinco archivos y recomputación de las cuatro tablas desde los datos; no verifican la interfaz, los filtros, la validación ni el texto de las preguntas.
- **Trazabilidad:** P124 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P102:** patrón de validación de columnas requeridas con `ValueError` en funciones de `main.py`; de P121, razones construidas desde sumas; de P120, contrato `questions.json`.
- **Habilita para Pyyy:** no evidenciada como artefacto. P154 trabaja un tablero sobre otro caso de ventas, sin reutilizar código ni datos de P124.

## Trazabilidad y auditoría

P124 está mapeada a `descriptiva.C01`, `descriptiva.C02`, `descriptiva.C03` y `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. C01 y C03 se sostienen en preguntas, KPI y gráficos; C02 en validación y resúmenes; C05 en la advertencia de la interfaz sobre el carácter no operativo de los datos y en la separación entre tablero y evidencia persistida. El producto de Analytics es una vista descriptiva de desempeño; Streamlit y Plotly lo sirven. Riesgo de identidad: con poca profundidad diagnóstica y sin usuario o decisión evidenciados, el taller podría leerse como introducción a una herramienta de tableros; el recálculo de razones por alcance es el elemento que lo ancla al razonamiento analítico.
