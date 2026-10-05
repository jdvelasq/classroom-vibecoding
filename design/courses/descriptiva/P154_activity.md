# P154 — Capa de serving para un dashboard de ventas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P154_ventas_dashboard/`.

### Preguntas analíticas actuales

- ¿Qué región y categoría deben recibir atención en el dashboard de ventas?

Desde el mart de referencia `data/sales_mart.db`, publica una tabla agregada a grano mes–región–categoría con ventas netas, unidades y órdenes distintas, en CSV y en una base SQLite de consumo, junto con un manifiesto que declara grano, métricas y consumidor («Dashboard de ventas»). La respuesta reagrega la tabla de serving por región y categoría y la ordena por ventas netas. No se implementa ningún dashboard: el nombre designa al consumidor declarado. La respuesta persistida reproduce `region_category_sales.csv` de P151: misma agregación sobre los mismos datos, mismo tamaño de archivo y mismas filas visibles (Centro–Servicios 106963.0, Sur–Tecnología 99607.5, …).

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** el consumidor declarado es un dashboard; usuario humano y decisión no evidenciados.
- **Producto terminal:** `dashboard_sales.csv`, `bi_serving.db`, `serving_manifest.csv` y `priority_region_category.csv` con gráfico de barras apiladas.
- **Uso y límite:** entrega una fuente de consumo con grano declarado y reconciliada con el mart. «Deben recibir atención» se responde con un ranking de volumen, sin criterio de atención (variación, brecha, meta) ni lectura; no hay interfaz de dashboard.
- **Disciplinas contribuyentes:** diseño de una capa de consumo BI y SQL sirven a la fuente que alimenta la descripción.

### Highlights de contribución

- **H01 — Fija el grano de consumo y reconoce qué métricas son aditivas en él:** agrega el hecho a mes–región–categoría, verifica unicidad del grano y reconcilia `net_sales` con el total del mart. `net_sales` y `units_sold` son aditivas; `orders` es `COUNT(DISTINCT order_id)` por celda y no es aditiva, porque un pedido puede tener líneas de varias categorías. El manifiesto declara el grano pero no esa restricción. Sin este hito, un consumidor podría sumar órdenes entre celdas (límite: la implementación no advierte el riesgo).
- **H02 — Publica la misma fuente en dos formatos verificados:** escribe `dashboard_sales.csv` y la tabla única `dashboard_sales` en `bi_serving.db`; la prueba exige igualdad entre ambos. Sin este hito, un reporte podría consumir una copia divergente.
- **H03 — Declara un contrato de consumo:** `serving_manifest.csv` registra tabla, grano («Una fila por mes, región y categoría»), métricas y consumidor. Extiende el catálogo de P153 a la frontera entre datos y presentación. Sin este hito, el grano publicado sería implícito.
- **H04 — Responde desde la capa de serving sin recalcular en la presentación:** la vista de prioridad se deriva de `dashboard_sales`, no del hecho, y el gráfico usa esa misma fuente. Sin este hito, presentación y datos podrían calcular métricas distintas (límite: el resultado repite P151).

### Inventario técnico de implementación

- **Introduce:** tabla de serving agregada a grano de consumo con `COUNT(DISTINCT ...)`.
- **Introduce:** base SQLite de consumo de una tabla y manifiesto de serving.
- **Reutiliza:** uniones en estrella (P151), reconciliación contra el total del hecho (P152), barras Plotly.
- **Aplica en nuevo caso:** la noción de contrato de P153 al consumo por BI.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Grano de consumo | H01 | Unicidad y reconciliación de `net_sales` | `orders` no aditiva, no advertida. |
| Fuente única de consumo | H02, H04 | CSV y SQLite iguales; gráfico desde la misma tabla | Sin dashboard implementado. |
| Contrato de serving | H03 | `serving_manifest.csv` | Sin reglas de aditividad ni de actualización. |

### Relación técnica con actividades anteriores

Mismo caso, nuevo producto (fuente de consumo) con misma pregunta efectiva que P151: el ranking región–categoría se repite con idénticos valores, lo que es una posible duplicación de respuesta que requiere decisión de curso. La reconciliación replica P152. Frente a P124, que implementa un dashboard Streamlit con filtros y KPI sobre datos de campañas, P154 sólo prepara la fuente y no construye presentación; el nombre puede inducir a suponer lo contrario.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Grano y aditividad | S01, S02, S05 | `implementation/descriptiva/P154_ventas_dashboard/professor/notebook.ipynb`: `serving_query` y `assert`; `implementation/descriptiva/P154_ventas_dashboard/submission/dashboard_sales.csv`; `implementation/descriptiva/P154_ventas_dashboard/professor/generate_data.py`: pedidos de varias líneas con productos aleatorios; `implementation/descriptiva/P154_ventas_dashboard/tests/test_activity.py`: `test_02` | La no aditividad de `orders` se infiere del código; la implementación no la trata. |
| H02 — Dos formatos consistentes | S03, S05 | `implementation/descriptiva/P154_ventas_dashboard/submission/bi_serving.db`; `implementation/descriptiva/P154_ventas_dashboard/tests/test_activity.py`: `test_03` | No se prueba consumo real por una herramienta BI. |
| H03 — Contrato de consumo | S03, S05 | `implementation/descriptiva/P154_ventas_dashboard/submission/serving_manifest.csv`; `implementation/descriptiva/P154_ventas_dashboard/tests/test_activity.py`: `test_04` | Manifiesto de una fila; no gobierna frescura ni aditividad. |
| H04 — Respuesta desde serving | S04, S06 | `implementation/descriptiva/P154_ventas_dashboard/professor/notebook.ipynb`: `priority_view` y gráfico; `implementation/descriptiva/P154_ventas_dashboard/submission/priority_region_category.csv`; `implementation/descriptiva/P154_ventas_dashboard/submission/questions.json`; `implementation/descriptiva/P151_ventas_mart/submission/region_category_sales.csv` | «Atención» equivale a mayor volumen; no hay criterio ni lectura. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Mart de referencia y dataset sintético | `data/sales_mart.db`; `professor/generate_data.py` | No consume artefactos de P151–P153. |
| S02 | Grano y métricas de serving | `professor/notebook.ipynb` | `orders` no aditiva; métrica ausente del catálogo de P153. |
| S03 | Productos de serving y manifiesto | `submission/dashboard_sales.csv`; `submission/bi_serving.db`; `submission/serving_manifest.csv` | Sin dashboard que los consuma. |
| S04 | Pregunta y respuesta | `submission/priority_region_category.csv`; `submission/questions.json`; gráfico | Repite la respuesta de P151. |
| S05 | Pruebas | `tests/test_activity.py` | Verifican consistencia, no interpretación. |
| S06 | Secuencia e interfaz | `notebooks/notebook.ipynb`; nombre de la actividad | Notebook vacío; sin `DESCRIPTION.md`; nombre «dashboard» sin interfaz. |

### Contrato de evidencia actual

- **Notebook o código:** agrega a grano mes–región–categoría, verifica unicidad y reconciliación, publica CSV y SQLite, escribe el manifiesto y deriva la vista de prioridad.
- **`submission/`:** `dashboard_sales.csv`, `bi_serving.db`, `serving_manifest.csv`, `priority_region_category.csv` y `questions.json`.
- **Pruebas:** `test_01` exige el conjunto exacto de archivos; `test_02` reejecuta la consulta de serving y exige grano único; `test_03` exige una sola tabla en la base e igualdad con el CSV; `test_04` exige columnas del manifiesto y textos clave de grano y métricas; `test_05` recalcula la vista de prioridad desde la tabla entregada y exige la pregunta literal. No verifican aditividad, un dashboard ni la lectura.
- **Trazabilidad:** P154 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P151/P152:** esquema estrella vía `data/sales_mart.db` y patrón de reconciliación contra el total del hecho; de P153, la idea de contrato documentado (sin consumir sus archivos).
- **Habilita para Pyyy:** no evidenciada; ninguna actividad del curso dentro del alcance consume `bi_serving.db`.

## Trazabilidad y auditoría

P154 está mapeada a `descriptiva.C01`, `C02`, `C03` y `C05` en `implementation/descriptiva/traceability.yaml` (`audit-against-design.md` omite C01 y describe «dashboard, OLAP y serving BI» como evidencia de C03). C05 está evidenciada por el manifiesto; C03 por un gráfico de barras; C01 por una pregunta cuyo criterio de atención no se define. El producto es una fuente de consumo BI con grano declarado; BI forma parte de la analítica descriptiva del curso y la frontera excluye la capacitación en una plataforma, no BI como tal. El límite observable es que la pregunta de atención no tiene criterio (variación, brecha o meta), no hay interfaz de dashboard y no se persiste una lectura.
