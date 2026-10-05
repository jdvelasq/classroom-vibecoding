# P153 — Catálogo, control y publicación de KPI de ventas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P153_ventas_kpis/`.

### Preguntas analíticas actuales

- ¿Podemos publicar estos KPI para la gerencia sin ocultar problemas de calidad o definición?

Sobre el mart de referencia `data/sales_mart.db`, define un catálogo de tres KPI (ventas netas, unidades vendidas y descuento promedio ponderado), evalúa cuatro reglas de calidad sobre `fact_sales`, documenta el linaje campo→KPI y deriva una decisión de publicación `APROBADO`/`BLOQUEADO`. La decisión persistida es `APROBADO` porque las cuatro reglas pasan. Ningún valor de KPI se calcula ni se persiste: el producto es el contrato de los indicadores, no su lectura.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la decisión es publicar o no el catálogo; el catálogo declara «Gerencia comercial» como propietario y la pregunta menciona «la gerencia». No hay evidencia de un usuario más allá de esa etiqueta.
- **Producto terminal:** catálogo, reporte de calidad, linaje y decisión de publicación, más un gráfico de estado de controles.
- **Uso y límite:** hace auditable qué se mediría y bajo qué controles. No describe lo que ocurre en las ventas; las reglas verifican integridad del hecho, no problemas de definición, y sobre datos sintéticos íntegros la rama `BLOQUEADO` nunca se ejercita.
- **Disciplinas contribuyentes:** gobierno de métricas y calidad de datos (prácticas de BI/ingeniería de datos) sirven a la confiabilidad de futuras descripciones.

### Highlights de contribución

- **H01 — Define un KPI como contrato y no como un número:** cada indicador declara fórmula o numerador, denominador, grano, período, propietario y fuente. P120–P122 y P124 calculan KPI (`kpi_summary.csv`, `overall_kpis.csv`, `kpis.csv`) sin catálogo; aquí aparece por primera vez la definición explícita. Sin este hito, el mismo nombre podría corresponder a cálculos distintos entre reportes.
- **H02 — Distingue una tasa ponderada de un promedio de tasas:** `discount_pct` es una tasa por línea; el catálogo define el descuento como `SUM(gross_sales * discount_pct) / SUM(gross_sales)` con numerador y denominador separados, consistente con el grano línea del hecho. Sin este hito, promediar porcentajes por fila daría igual peso a líneas de importe muy distinto (límite: el KPI no se calcula).
- **H03 — Condiciona la publicación a reglas verificables:** llave de hecho única, ventas netas no negativas, cantidades positivas y fechas presentes en `dim_date`; el estado se deriva por código. Extiende las aserciones de P150–P152 a un reporte persistido que gobierna una decisión. Sin este hito, la publicación no dependería de evidencia.
- **H04 — Documenta el linaje de cada KPI:** `metric_lineage.csv` vincula `fact_sales.*`, KPI y transformación. Sin este hito, el catálogo no sería trazable hasta el hecho.

### Inventario técnico de implementación

- **Introduce:** catálogo de KPI con grano, período, propietario y fuente.
- **Introduce:** reporte de reglas de calidad con estado PASS/FAIL y decisión de publicación derivada.
- **Introduce:** tabla de linaje de métricas.
- **Reutiliza:** lectura del mart de P151/P152; gráfico de barras Plotly (aquí sobre valores booleanos).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Catálogo de KPI | H01–H02 | Siete atributos por KPI; ratio de sumas | KPI no calculados. |
| Calidad como compuerta | H03 | Cuatro reglas y decisión derivada | Sólo integridad del hecho; rama de bloqueo no ejercitada. |
| Linaje de métricas | H04 | `metric_lineage.csv` | «segmento» en la transformación no se define. |

### Relación técnica con actividades anteriores

Nuevo producto sobre el mismo caso: P150–P152 producen respuestas; P153 produce el contrato que haría confiables esas respuestas, sin conectar con ellas (no referencia `net_sales` agregadas de P151/P152 ni sus archivos). Las reglas de calidad retoman, en forma persistida, verificaciones ya hechas con `assert` en P150–P152. Frente a P120–P124, que calculan KPI sin definirlos formalmente, es contraste y no duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — KPI como contrato | S02, S05 | `implementation/descriptiva/P153_ventas_kpis/professor/notebook.ipynb`: `kpi_catalog`; `implementation/descriptiva/P153_ventas_kpis/submission/kpi_catalog.csv`; `implementation/descriptiva/P153_ventas_kpis/tests/test_activity.py`: `test_01` | Propietario y período son declarados, no justificados por un usuario observable. |
| H02 — Tasa ponderada | S01, S02 | `implementation/descriptiva/P153_ventas_kpis/submission/kpi_catalog.csv`: fila «Descuento promedio ponderado» | Definido pero no calculado ni contrastado con el promedio simple. |
| H03 — Calidad como compuerta | S03, S05 | `implementation/descriptiva/P153_ventas_kpis/professor/notebook.ipynb`: `quality_checks`, `publication_decision`; `implementation/descriptiva/P153_ventas_kpis/submission/kpi_quality_report.csv`; `implementation/descriptiva/P153_ventas_kpis/submission/kpi_publication_decision.csv`; `implementation/descriptiva/P153_ventas_kpis/tests/test_activity.py`: `test_02`, `test_04` | No hay reglas sobre definición (p. ej., rango de `discount_pct`); datos íntegros por construcción. |
| H04 — Linaje | S04, S05 | `implementation/descriptiva/P153_ventas_kpis/submission/metric_lineage.csv`; `implementation/descriptiva/P153_ventas_kpis/tests/test_activity.py`: `test_03` | La prueba sólo exige coincidencia de nombres, prefijo `fact_sales.` y longitud del texto. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Mart de referencia y dataset sintético | `data/sales_mart.db`; `professor/generate_data.py` | Íntegro por construcción. |
| S02 | Catálogo de KPI | `professor/notebook.ipynb`; `submission/kpi_catalog.csv` | Tres KPI; ninguno calculado. |
| S03 | Reglas y decisión de publicación | `professor/notebook.ipynb`; `submission/kpi_quality_report.csv`; `submission/kpi_publication_decision.csv`; gráfico | Cuatro reglas de integridad; sin caso de fallo. |
| S04 | Linaje | `submission/metric_lineage.csv` | Texto libre de transformación. |
| S05 | Pruebas | `tests/test_activity.py` | Recalculan reglas; verificación débil de linaje. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook vacío; sin `DESCRIPTION.md`. |

### Contrato de evidencia actual

- **Notebook o código:** construye catálogo, reglas, linaje y decisión; grafica el estado de controles.
- **`submission/`:** `kpi_catalog.csv`, `kpi_quality_report.csv`, `metric_lineage.csv`, `kpi_publication_decision.csv` y `questions.json`.
- **Pruebas:** `test_01` exige el conjunto exacto de archivos, columnas y nombres de KPI y atributos no nulos; `test_02` recalcula las cuatro reglas desde el mart y compara; `test_03` exige coincidencia KPI catálogo–linaje, prefijo `fact_sales.` y transformaciones de más de ocho caracteres; `test_04` exige coherencia entre reporte y decisión; `test_05` la pregunta literal. No verifican fórmulas, valores de KPI ni pertinencia de las reglas.
- **Trazabilidad:** P153 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P151:** esquema `fact_sales`/`dim_date` (vía `data/sales_mart.db`); de P150–P152, las verificaciones de integridad como práctica.
- **Habilita para P154:** no evidenciada: P154 no lee el catálogo ni la decisión y publica una métrica (`orders`) ausente del catálogo.

## Trazabilidad y auditoría

P153 está mapeada a `descriptiva.C01`, `C02`, `C03` y `C05` en `implementation/descriptiva/traceability.yaml` (`audit-against-design.md` omite C01). C01 (métricas para un contexto de decisión) y C05 (documentación responsable) son las mejor evidenciadas; C02 sólo como calidad de datos; C03 es débil (gráfico de booleanos). El producto es gobierno de métricas, no una descripción de lo que ocurre; se lee como práctica de BI/gobierno de datos y no responde por sí solo la pregunta descriptiva del curso.
