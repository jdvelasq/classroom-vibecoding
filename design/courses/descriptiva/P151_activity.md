# P151 — Mart estrella de ventas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P151_ventas_mart/`.

### Preguntas analíticas actuales

- ¿Qué combinación de región y categoría aporta más ventas netas en el mart?

Sobre las mismas fuentes sintéticas de P150 (copia idéntica en `data/` y mismo `professor/generate_data.py`), construye un mart estrella mínimo: un hecho `fact_sales` a grano línea de pedido y tres dimensiones (`dim_date`, `dim_customer`, `dim_product`), lo persiste en SQLite y responde con una consulta de unión en estrella. La respuesta persistida ordena las nueve combinaciones región–categoría; la primera es Centro–Servicios (106963.0), seguida de Sur–Tecnología (99607.5). El notebook no contiene texto interpretativo; el notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la pregunta está persistida; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/sales_mart.db` (cuatro tablas) y `region_category_sales.csv` con gráfico de barras agrupadas.
- **Uso y límite:** habilita consultas descriptivas repetibles por fecha, cliente y producto. «Aporta más» se responde como ranking de volumen; no hay lectura de magnitud relativa, concentración ni causa, y los datos sintéticos no admiten conclusiones comerciales.
- **Disciplinas contribuyentes:** modelado dimensional y SQL sirven como estructura para describir; en esta actividad la construcción del mart ocupa casi todo el notebook.

### Highlights de contribución

- **H01 — Separa hecho y dimensiones desde el grano línea:** define el hecho con importes bruto y neto antes de construir dimensiones; `dim_date` se deriva sólo de las fechas presentes en el hecho, y como el generador asigna una fecha por pedido, la dimensión no es un calendario completo (no existen días sin ventas). Las claves de cliente y producto copian los identificadores operativos. Primera aparición de un modelo dimensional en el curso; sin este hito, la estructura de navegación usada por P152–P154 no sería explícita.
- **H02 — Sustituye identificadores por claves sin alterar el número de hechos:** une con `validate="many_to_one"` y verifica con `assert` que `len(fact_sales) == len(facts)` y que no hay claves nulas. Extiende H02 de P150 al paso de modelado; sin él, la creación de claves podría perder o duplicar hechos.
- **H03 — Persiste un mart con integridad referencial verificable:** escribe las cuatro tablas en `submission/sales_mart.db`; las pruebas exigen exactamente esas tablas, claves únicas en dimensiones, unicidad del hecho y que toda clave del hecho exista en su dimensión. Sin este hito, el modelo sería un estado efímero del notebook.
- **H04 — Responde mediante una consulta en estrella:** `JOIN dim_customer USING(customer_key)`, `JOIN dim_product USING(product_key)`, `GROUP BY` región y categoría, ordenado por ventas netas. Extiende el SQL de P104 (vistas y uniones entre dos tablas) a una unión hecho–dimensiones. Sin este hito, el mart no se conectaría con ninguna pregunta.

### Inventario técnico de implementación

- **Introduce:** modelo estrella (hecho a grano línea, dimensiones fecha/cliente/producto) y claves de mart.
- **Introduce:** persistencia de un modelo multitabla en SQLite con `to_sql`.
- **Extiende:** SQL de P104/P107/P109 hacia uniones en estrella con `USING`.
- **Reutiliza:** integración con `validate="many_to_one"` y derivación de importes de P150; barras agrupadas con Plotly.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Modelo dimensional mínimo | H01 | Hecho y tres dimensiones con claves | `dim_date` sin calendario completo; claves = identificadores operativos. |
| Integridad referencial | H02–H03 | `assert` en notebook; subconjuntos en pruebas | Datos íntegros por construcción. |
| Consulta en estrella | H04 | `region_category_sales.csv` | Ranking de volumen; sin interpretación. |

### Relación técnica con actividades anteriores

Mismo caso y fuentes que P150 con nuevo método de representación: P150 desnormaliza en una tabla; P151 normaliza en estrella. La derivación de importes se repite (con forma algebraica distinta: `gross × (1 − pct)` en lugar de `gross − gross × pct`). La pregunta cambia de serie temporal a combinación de dimensiones. No usa la tabla entregada por P150. Respecto de P104, el SQL pasa de describir dos tablas de conductores a navegar un modelo dimensional.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Hecho y dimensiones | S01, S02 | `implementation/descriptiva/P151_ventas_mart/professor/notebook.ipynb`: celdas de hecho y dimensiones; `implementation/descriptiva/P151_ventas_mart/professor/generate_data.py`: fecha determinista por pedido | Dimensión de fecha limitada a días con ventas; no sirve para tasas por día calendario. |
| H02 — Claves sin pérdida de hechos | S02, S04 | `implementation/descriptiva/P151_ventas_mart/professor/notebook.ipynb`: `merge` y `assert`; `implementation/descriptiva/P151_ventas_mart/tests/test_activity.py`: `test_03` | No se ejercita un caso de fecha o clave ausente. |
| H03 — Mart persistido e íntegro | S03, S04 | `implementation/descriptiva/P151_ventas_mart/submission/sales_mart.db`; `implementation/descriptiva/P151_ventas_mart/tests/test_activity.py`: `test_01`, `test_02` | Un mart equivalente ya está en `data/sales_mart.db`, visible al estudiante. |
| H04 — Consulta en estrella | S03 | `implementation/descriptiva/P151_ventas_mart/professor/notebook.ipynb`: consulta SQL y gráfico; `implementation/descriptiva/P151_ventas_mart/submission/region_category_sales.csv`; `implementation/descriptiva/P151_ventas_mart/submission/questions.json` | Los valores describen datos sintéticos; no hay lectura de diferencias. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético compartido | `data/*.csv`; `professor/generate_data.py` | Idéntico a P150 y P152–P154; procedencia no declarada al estudiante. |
| S02 | Modelo dimensional | `professor/notebook.ipynb` | Dimensión de fecha mínima (año, mes) derivada del hecho. |
| S03 | Producto: mart y consulta | `submission/sales_mart.db`; `submission/region_category_sales.csv`; `submission/questions.json` | El mart de referencia `data/sales_mart.db` coincide en estructura con el entregable. |
| S04 | Pruebas | `tests/test_activity.py` | Verifican esquema, integridad y hecho recalculado; no la interpretación. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook vacío; sin `DESCRIPTION.md`. |

### Contrato de evidencia actual

- **Notebook o código:** construye hecho y dimensiones, verifica conservación de hechos, persiste en SQLite, consulta en estrella y grafica.
- **`submission/`:** `sales_mart.db`, `region_category_sales.csv` y `questions.json`.
- **Pruebas:** `test_01` exige exactamente las cuatro tablas; `test_02` unicidad de claves y del hecho e integridad referencial; `test_03` reconstruye `fact_sales` desde `data/` y lo compara; `test_04` reejecuta la consulta sobre el mart entregado; `test_05` exige la pregunta literal. No verifican dimensiones contra un esperado completo, el gráfico ni la lectura.
- **Trazabilidad:** P151 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P150:** grano línea y derivación de importes como práctica; no consume `sales_analytics.csv`. **Recibe de P104:** consultas SQL sobre SQLite.
- **Habilita para P152–P154:** el esquema y la lógica del mart (misma `build_mart` en `professor/generate_data.py`). No es dependencia de artefacto: P152–P154 leen `data/sales_mart.db` generado por el profesor, no `submission/sales_mart.db`.

## Trazabilidad y auditoría

P151 está mapeada a `descriptiva.C01`, `C02`, `C03` y `C05` en `implementation/descriptiva/traceability.yaml` (`audit-against-design.md` omite C01). C02 se evidencia en las verificaciones de integridad; C03 en un gráfico de barras; C01 y C05 sólo de forma mínima (una pregunta, artefactos sin lectura). El producto observable es un mart dimensional y una respuesta en ranking. El modelado dimensional es una práctica de BI y, como tal, parte de la analítica descriptiva del curso, no de la ingeniería de datos que excluye su frontera. El límite observable es que la respuesta no se interpreta (magnitud relativa, concentración) y que la construcción del mart ocupa casi todo el notebook.
