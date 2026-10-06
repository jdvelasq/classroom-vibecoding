# P226 — Estructura de mercado

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P225_estructura_mercado/`.

### Preguntas analíticas actuales

- ¿Qué estructura de dependencia parcial aparece entre variaciones diarias de
  acciones cargadas desde archivos de precios de apertura y cierre?
- ¿Qué comunidades de acciones y qué disposición bidimensional permiten hacer
  visible esa estructura?

Carga cotizaciones de numerosas acciones, calcula `close - open` por día,
estima una precisión dispersa y entrega una red gráfica. Los archivos empiezan
en 2003, pero no documentan fuente, cierre temporal, calidad de cotizaciones o
uso permitido.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** describe dependencias de mercado en un
  conjunto histórico; no hay usuario, decisión de inversión o horizonte futuro
  evidenciados.
- **Producto terminal:** visualización de red de correlaciones parciales y
  comunidades de acciones.
- **Uso y límite:** permite explorar co-movimientos condicionados; no predice
  precios, rendimientos o riesgo, ni autoriza inversión o recomendación.
- **Disciplinas contribuyentes:** covarianza gráfica, clustering y embedding
  sirven a una explicación estructural. El producto actual no es predictivo;
  su identidad dentro de Predictiva queda sin resolver.

### Highlights de contribución

- **H01 — Convierte cotizaciones diarias en una matriz comparable:** apila
  precios de apertura y cierre por símbolo y calcula `close - open`; al
  transponer, las filas pasan a ser días y las columnas acciones. Esta
  orientación permite modelar dependencia entre acciones, no entre días.
- **H02 — Estima relaciones condicionales en vez de correlaciones brutas:** usa
  `GraphicalLassoCV` sobre variaciones estandarizadas y deriva correlaciones
  parciales desde la matriz de precisión. Sin este hito, una arista se leería
  erróneamente como simple co-movimiento marginal.
- **H03 — Agrupa acciones por estructura de dependencia:** aplica
  `affinity_propagation` a la covarianza estimada y asigna comunidades. Sin
  este paso, la red quedaría como conjunto de nodos sin una lectura de grupos.
- **H04 — Hace visible la red con una disposición bidimensional:** calcula
  `LocallyLinearEmbedding`, dibuja nodos, aristas parciales por encima de 0.02
  y etiquetas, y persiste `stocks.png`. Sin ello, la estructura numérica no se
  vuelve inspeccionable para una discusión.
- **H05 — Delimita el producto financiero:** las variaciones intradía y sus
  dependencias históricas describen estructura; no construyen pronóstico,
  estrategia, backtest, incertidumbre ni recomendación de inversión.
- **H06 — Reconoce el límite de procedencia y tiempo:** los múltiples CSV.gz
  contienen fechas y precios, pero no manifiesto de fuente ni actualización.
  Por tanto, la red no puede interpretarse como representación actual del
  mercado.

### Inventario técnico de implementación

- **Introduce:** carga múltiple de series, matriz días×acciones, estandarización,
  `GraphicalLassoCV`, correlación parcial, affinity propagation y LLE.
- **Verifica y comunica:** genera una red PNG con comunidades y aristas.
- **No evidencia:** partición temporal, pronóstico, backtest, criterio de
  inversión, incertidumbre o usuario de decisión.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Matriz de mercado | H01 | Filas=días, columnas=acciones, variación close-open | Notebook; alineación de fechas no se valida explícitamente. |
| Dependencia condicional | H02 | `GraphicalLassoCV` y precisión | Notebook; no prueba causalidad ni estabilidad temporal. |
| Comunidades y red | H03–H04 | Affinity propagation, LLE y `stocks.png` | PNG; prueba sólo existencia. |
| Límite predictivo/financiero | H05–H06 | Ausencia de pronóstico y de procedencia | Datos/notebook; no autoriza inversión. |

### Relación técnica con actividades anteriores

P226 cambia el pronóstico o clasificación de talleres previos por descripción
de una red de dependencias entre activos. Puede aportar lectura de estructura a
un caso financiero, pero no hay producto predictivo demostrable ni dependencia
de código con otra actividad. Su ubicación en Predictiva requiere decisión
posterior, no una inferencia de S01.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb`: `close_prices`, `open_prices`, `variation`, transposición | No documenta cómo se resuelven fechas faltantes entre símbolos. |
| H02 | S02 | Notebook: `GraphicalLassoCV`, `precision_`, correlaciones parciales | Relación parcial no prueba causalidad ni predicción. |
| H03 | S02 | Notebook: `affinity_propagation(edge_model.covariance_)` | No evalúa estabilidad de las comunidades. |
| H04 | S03 | Notebook: LLE, `LineCollection`, `savefig`; `submission/stocks.png`; pruebas | Los tests no inspeccionan red, etiquetas ni umbral. |
| H05 | S04 | Notebook y `submission/` | Ausencia de pronóstico no decide por sí sola su valor curricular. |
| H06 | S01, S04 | `data/*.csv.gz`; notebook | No hay manifiesto de fuente o actualización. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Cotizaciones y matriz días×acciones | `data/*.csv.gz`; notebook | Fuente, cobertura y calidad no documentadas. |
| S02 | Estructura gráfica y comunidades | Notebook | Modela dependencia parcial histórica, no pronóstico. |
| S03 | Visualización de red | `submission/stocks.png`; pruebas | Umbral 0.02 y disposición 2D condicionan la lectura. |
| S04 | Producto e identidad | Notebook; trazabilidad | No hay producto Predictivo ni entrada P226. |

### Contrato de evidencia actual

- **Notebook o código:** carga series, deriva variaciones, estima dependencia,
  agrupa y grafica una red.
- **`submission/`:** conserva `stocks.png`.
- **Pruebas:** verifican sólo que existe la imagen.
- **Trazabilidad:** falta entrada P226 y requiere escalación.

### Dependencias en la secuencia

- **Recibe de Pxxx:** no hay dependencia de código, dato o contrato demostrable.
- **Habilita para Pyyy:** no hay actividad posterior implementada que reutilice
  esta red.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe entrada P226 en `implementation/predictiva/traceability.yaml`. El
producto es una explicación gráfica de estructura de mercado; estadística,
clustering y visualización lo sirven, pero no lo convierten en predicción ni en
asesoría financiera.
