# P152 — Consultas OLAP sobre el mart de ventas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P152_ventas_olap/`.

### Preguntas analíticas actuales

- ¿Cómo evolucionan las ventas netas mensuales por región?
- ¿Qué categorías lideran las ventas y unidades en la región Norte?
- ¿Qué productos explican la categoría líder de la región Norte?

Consulta el mart de referencia `data/sales_mart.db` (generado por `professor/generate_data.py`) con tres operaciones nombradas en el notebook: *roll-up* mensual por región, *slice* de la región Norte por categoría y *drill-down* de la categoría líder hacia productos. Las respuestas persistidas muestran que en Norte Servicios lidera ventas netas (92853.0) mientras Oficina lidera unidades (180); el *drill-down* sigue el orden por ventas netas y ubica a `Producto 9` (50646.0) primero dentro de Servicios. El notebook no comenta esa divergencia ni justifica la elección de Norte.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** tres preguntas persistidas; usuario y decisión no evidenciados.
- **Producto terminal:** tres tablas de respuesta encadenadas y un gráfico de líneas mensual por región.
- **Uso y límite:** permite navegar el mismo hecho a distintos niveles de agregación y reconciliar totales. «Explican» se responde como descomposición aditiva de ventas, no como explicación causal; la serie mensual hereda el calendario uniforme del generador.
- **Disciplinas contribuyentes:** operaciones OLAP y SQL parametrizado sirven a una descripción por niveles.

### Highlights de contribución

- **H01 — Usa las jerarquías del modelo como rutas de descripción:** año→mes en `dim_date`, región en `dim_customer` y categoría→producto en `dim_product` (cuatro productos por categoría) permiten subir, cortar y bajar sobre el mismo hecho. Primera vez que el curso nombra operaciones OLAP; sin este hito, el mart de P151 quedaría como almacenamiento sin forma de navegación.
- **H02 — Agrega por *roll-up* y reconcilia contra el total del hecho:** agrupa por año, mes y región y verifica con `assert` que la suma coincide con `SUM(net_sales)` del hecho; la prueba repite la reconciliación. Sin este hito, una agregación podría perder hechos sin evidencia.
- **H03 — Corta un subcubo y contrasta dos medidas:** el *slice* `WHERE c.region = 'Norte'` devuelve ventas netas y unidades por categoría; el artefacto persistido muestra que el líder cambia según la medida. Sin este hito, «liderar» parecería independiente de la medida elegida (límite: el notebook no lo hace explícito).
- **H04 — Encadena el *drill-down* al resultado previo:** la categoría líder se toma de la primera fila del *slice* y se pasa como parámetro (`?`) a la consulta de productos; `test_04` deriva la categoría del archivo entregado. Sin este hito, las consultas serían independientes y no una navegación guiada.

### Inventario técnico de implementación

- **Introduce:** operaciones OLAP nombradas (*roll-up*, *slice*, *drill-down*) sobre un modelo estrella.
- **Introduce:** consultas SQL parametrizadas con `params` en `pd.read_sql_query`.
- **Introduce:** reconciliación de una agregación contra el total del hecho.
- **Reutiliza:** uniones en estrella de P151; gráfico de líneas Plotly de P150.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Navegación jerárquica | H01, H04 | *Roll-up*, *slice*, *drill-down* encadenados | Región de corte fijada a mano. |
| Reconciliación de totales | H02 | `assert` y `test_02` | Igualdad exacta de flotantes; datos íntegros. |
| Medida y liderazgo | H03 | `north_category_sales.csv` con ventas y unidades | Divergencia visible, no discutida. |

### Relación técnica con actividades anteriores

Mismo caso y mismo esquema que P151, con nuevo método al servicio de la descripción: P151 construye el mart y hace una consulta; P152 lo navega por niveles. La serie mensual por región es la misma técnica que la serie por categoría de P150 sobre otra dimensión. El *drill-down* es la primera descomposición jerárquica de la secuencia. No duplica P120–P122, que segmentan tablas planas sin modelo dimensional.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Jerarquías como rutas | S01, S02 | `implementation/descriptiva/P152_ventas_olap/professor/notebook.ipynb`: inspección de tablas y tres consultas; `implementation/descriptiva/P152_ventas_olap/professor/generate_data.py`: categorías y productos | Jerarquías mínimas (sin trimestre, sin subcategoría). |
| H02 — *Roll-up* reconciliado | S02, S04 | `implementation/descriptiva/P152_ventas_olap/professor/notebook.ipynb`: `assert` de total; `implementation/descriptiva/P152_ventas_olap/submission/monthly_region_sales.csv`; `implementation/descriptiva/P152_ventas_olap/tests/test_activity.py`: `test_02` | La reconciliación prueba aditividad, no calidad de origen. |
| H03 — Contraste de medidas en el *slice* | S02, S03 | `implementation/descriptiva/P152_ventas_olap/submission/north_category_sales.csv` | El notebook no interpreta la divergencia; Norte no está justificado. |
| H04 — *Drill-down* encadenado | S02, S03, S04 | `implementation/descriptiva/P152_ventas_olap/professor/notebook.ipynb`: `leading_category` y `params`; `implementation/descriptiva/P152_ventas_olap/submission/north_product_drilldown.csv`; `implementation/descriptiva/P152_ventas_olap/tests/test_activity.py`: `test_04` | Descomposición aditiva; «explican» no implica causa. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Mart de referencia y dataset sintético | `data/sales_mart.db`; `data/*.csv`; `professor/generate_data.py` | No consume el mart entregado en P151. |
| S02 | Consultas OLAP | `professor/notebook.ipynb` | Corte en Norte fijado sin criterio explícito. |
| S03 | Producto y preguntas | `submission/*.csv`; `submission/questions.json`; gráfico | Sin conclusión escrita. |
| S04 | Pruebas | `tests/test_activity.py` | Reejecutan las consultas sobre `data/sales_mart.db`. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook vacío; sin `DESCRIPTION.md`. |

### Contrato de evidencia actual

- **Notebook o código:** inspecciona el mart, ejecuta *roll-up*, *slice* y *drill-down*, reconcilia el total y grafica la serie por región.
- **`submission/`:** `monthly_region_sales.csv`, `north_category_sales.csv`, `north_product_drilldown.csv` y `questions.json`.
- **Pruebas:** `test_01` exige exactamente esos cuatro archivos; `test_02`–`test_04` reejecutan cada consulta contra el mart y comparan, incluida la reconciliación del total y la derivación de la categoría líder desde el archivo entregado; `test_05` exige las preguntas literales. No verifican el gráfico ni la lectura del contraste entre medidas.
- **Trazabilidad:** P152 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P151:** esquema estrella y consultas con `USING`; el artefacto leído es `data/sales_mart.db`, no `submission/sales_mart.db` de P151.
- **Habilita para P153–P154:** no evidenciada como artefacto; P153 y P154 leen el mismo `data/sales_mart.db` y P154 reutiliza el patrón de reconciliación contra el total del hecho.

## Trazabilidad y auditoría

P152 está mapeada a `descriptiva.C01`, `C02`, `C03` y `C05` en `implementation/descriptiva/traceability.yaml` (`audit-against-design.md` omite C01). Es la actividad del bloque más cercana a la pregunta descriptiva (qué, dónde, cuándo): tres preguntas encadenadas, serie temporal y descomposición. Faltan «para quién» y la lectura de evidencia; las operaciones OLAP sirven a la descripción, pero sin interpretación persistida el producto puede leerse como ejercicio de consultas BI.
