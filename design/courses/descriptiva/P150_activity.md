# P150 — Tabla analítica de ventas desde fuentes operativas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P150_ventas_tabla/`.

### Preguntas analíticas actuales

- ¿Cómo cambian las ventas netas mensuales por categoría después de integrar las fuentes?

Integra tres fuentes operativas sintéticas (líneas de pedido, clientes y productos) en una tabla analítica con una fila por línea de pedido, deriva importes bruto, descuento y neto, y responde con una serie mensual por categoría. Los datos provienen de `professor/generate_data.py` (semilla fija; su docstring los declara «para los talleres de BI»): 60 clientes, 12 productos genéricos (`Producto 1`–`Producto 12`) en tres categorías y 240 pedidos de 2024. La fecha de cada pedido es una función determinista de `order_id` (un pedido cada tres días con desfase circular), de modo que hay una fecha por pedido y un número casi constante de pedidos por mes. El notebook de profesor no contiene celdas markdown ni texto interpretativo; el notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la pregunta está persistida en `questions.json`; usuario y decisión no evidenciados.
- **Producto terminal:** tabla analítica integrada a grano línea de pedido (`sales_analytics.csv`) y una agregación mensual por categoría (`monthly_category_sales.csv`) con gráfico de líneas.
- **Uso y límite:** permite describir composición y evolución de ventas netas sobre fuentes integradas y verificadas. Como el calendario es sintético y uniforme, la variación mensual refleja sorteos aleatorios del generador, no estacionalidad ni comportamiento comercial real; no hay lectura ni conclusión persistida.
- **Disciplinas contribuyentes:** integración de datos con pandas (modelado relacional, validación de cardinalidad) y visualización con Plotly sirven a la tabla descriptiva.

### Highlights de contribución

- **H01 — Reconoce que la medida no existe en ninguna fuente aislada:** `order_lines.csv` sólo trae cantidad y `discount_pct`; el precio vive en `products.csv` y región/segmento en `customers.csv`. Las ventas netas sólo existen tras integrar las tres fuentes. Es la primera fuente normalizada del curso: P120 parte de un `sales.csv` plano con `TotalAmount` ya calculado. Sin este hito, el estudiante seguiría tratando la tabla de análisis como un dato dado y no como un producto construido.
- **H02 — Protege el grano línea de pedido durante la integración:** verifica duplicados de (`order_id`, `line_id`), une con `merge(..., validate="many_to_one")` y comprueba con `assert` que el número de filas no cambia y que no quedan atributos nulos. Extiende la noción de grano que P122 sólo enuncia; sin este hito, un *fan-out* de la unión inflaría ventas sin ser detectado.
- **H03 — Descompone el importe en bruto, descuento y neto:** calcula `gross_sales = quantity × unit_price`, `discount_amount` y `net_sales = gross − discount`, y verifica la identidad contable. Sin este hito, el descuento quedaría oculto dentro de un único importe.
- **H04 — Publica una tabla reutilizable y una respuesta temporal a partir de ella:** persiste la tabla integrada, agrega por mes y categoría, grafica sin ocultar la dimensión temporal y registra la pregunta y su archivo de respuesta. Sin este hito, la integración no dejaría un producto consultable ni una respuesta trazable.

### Inventario técnico de implementación

- **Introduce:** integración de varias fuentes operativas con validación de cardinalidad `many_to_one`.
- **Introduce:** declaración y verificación explícita del grano publicado.
- **Extiende:** agregación temporal con `dt.to_period("M")` y `groupby` (prácticas pandas de P103 y de P120).
- **Reutiliza:** gráfico de líneas con Plotly y patrón `questions.json` de P120–P125.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Integración de fuentes normalizadas | H01–H02 | `merge` con `validate="many_to_one"` y conservación de filas | Datos sintéticos; sin claves huérfanas que manejar. |
| Grano declarado | H02, H04 | Una fila por línea de pedido, comprobada | No se discuten granos alternativos (pedido, cliente). |
| Medidas derivadas | H03 | Bruto, descuento y neto | Sin devoluciones, costos ni márgenes. |
| Serie mensual por categoría | H04 | `monthly_category_sales.csv` y gráfico | Calendario uniforme por construcción; no admite lectura estacional. |

### Relación técnica con actividades anteriores

Misma familia de pregunta que P120 (ventas por categoría y mes) con nueva exigencia de datos: la tabla debe construirse desde fuentes relacionales en lugar de recibirse plana. Reutiliza `groupby` y Plotly de P103/P120. No duplica P106/P107 (limpieza de `ventas.csv`): aquí no hay suciedad que corregir, sino relaciones que integrar. Frente a P120–P125, se pierde contexto de caso: no hay usuario, decisión ni datos de procedencia trazable.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Medida que exige integración | S01, S02 | `implementation/descriptiva/P150_ventas_tabla/data/order_lines.csv`; `implementation/descriptiva/P150_ventas_tabla/data/products.csv`; `implementation/descriptiva/P150_ventas_tabla/data/customers.csv`; `implementation/descriptiva/P150_ventas_tabla/professor/generate_data.py` | Fuentes sintéticas generadas; no representan un sistema operativo real. |
| H02 — Grano protegido | S02, S05 | `implementation/descriptiva/P150_ventas_tabla/professor/notebook.ipynb`: celdas de carga, `merge` y `assert`; `implementation/descriptiva/P150_ventas_tabla/tests/test_activity.py`: `test_02` | Las fuentes son íntegras por construcción; no se ejercita un caso de clave faltante o duplicada. |
| H03 — Descomposición del importe | S03, S05 | `implementation/descriptiva/P150_ventas_tabla/professor/notebook.ipynb`; `implementation/descriptiva/P150_ventas_tabla/tests/test_activity.py`: `test_03` | El descuento es un porcentaje sorteado; no admite análisis de política comercial. |
| H04 — Tabla y respuesta persistidas | S04, S01 | `implementation/descriptiva/P150_ventas_tabla/submission/sales_analytics.csv`; `implementation/descriptiva/P150_ventas_tabla/submission/monthly_category_sales.csv`; `implementation/descriptiva/P150_ventas_tabla/submission/questions.json`; notebook: gráfico de líneas | No hay interpretación escrita; la variación mensual es artefacto del generador. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético de ventas | `data/*.csv`; `professor/generate_data.py`; `data/sales_mart.db` | Calendario uniforme, productos genéricos; procedencia no documentada para el estudiante; `data/sales_mart.db` no se usa aquí. |
| S02 | Integración y grano | `professor/notebook.ipynb` | Sólo se ejercita el camino feliz de la unión. |
| S03 | Medidas derivadas | `professor/notebook.ipynb` | Fórmula de neto distinta en forma a la del mart de P151 (`gross × (1 − pct)`). |
| S04 | Producto y respuesta | `submission/`; gráfico del notebook | Una sola pregunta, sin conclusión persistida. |
| S05 | Pruebas | `tests/test_activity.py` | Recalculan la transformación; no evalúan interpretación ni gráfico. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook vacío (0 celdas); sin `DESCRIPTION.md`. |

### Contrato de evidencia actual

- **Notebook o código:** integra fuentes conservando el grano, deriva importes, agrega por mes y categoría y grafica.
- **`submission/`:** `sales_analytics.csv` (grano línea), `monthly_category_sales.csv` y `questions.json`.
- **Pruebas:** `test_02` reconstruye la tabla completa desde `data/` y la compara; `test_03` exige atributos no nulos, identidad neto = bruto − descuento y neto ≤ bruto; `test_04` recalcula la agregación mensual desde la tabla entregada; `test_05` exige la pregunta literal. No verifican el gráfico, la lectura ni la pertinencia de la pregunta.
- **Trazabilidad:** P150 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P103/P120:** práctica de agregación con `groupby` y patrón de respuesta `questions.json`; no recibe artefactos.
- **Habilita para P151:** no evidenciada como artefacto: P151 no lee `sales_analytics.csv`, sino una copia idéntica de las mismas fuentes en su `data/`. Sí comparte grano línea y la derivación de importes.

## Trazabilidad y auditoría

P150 está mapeada a `descriptiva.C01`, `C02`, `C03` y `C05` en `implementation/descriptiva/traceability.yaml`; `audit-against-design.md` sólo le asigna C02, C03 y C05, discrepancia que no se resuelve aquí. C02 (calidad e integración antes de concluir) y C03 (serie visual) están evidenciadas; C01 se limita a una pregunta sin contexto de decisión; C05 se apoya en artefactos persistidos sin comunicación escrita. El producto es una tabla descriptiva integrada. La integración de fuentes abre la secuencia de *business intelligence* P150–P154; BI forma parte de la analítica descriptiva del curso (la frontera excluye la capacitación en una plataforma BI, no BI como tal). El límite observable no es la pertenencia a BI, sino que no hay usuario ni lectura persistida de la serie.
