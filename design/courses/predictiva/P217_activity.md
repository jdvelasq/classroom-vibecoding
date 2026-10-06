# P217 — Series de tiempo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P216_series_de_tiempo/`.

### Preguntas analíticas actuales

- ¿Cómo se pronostica una serie mensual de mano de obra del condado de Sutter?
- ¿Qué enfoque ofrece mejor evidencia fuera del período de especificación: tendencia y estacionalidad, rezagos autoregresivos o MLP?

Usa 228 meses para especificar modelos y 24 meses posteriores para evaluarlos.
La actividad genera pronósticos, métricas y visualizaciones comparables.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima la mano de obra mensual posterior al
  período de especificación; usuario y decisión operativa no están evidenciados.
- **Producto terminal:** pronósticos temporales comparables con métricas de
  evaluación fuera del período de especificación.
- **Uso y límite:** permite contrastar familias de pronóstico, no asignar
  personal, fijar una política ni cuantificar incertidumbre.
- **Disciplinas contribuyentes:** regresión, redes neuronales y análisis de
  series sirven al producto predictivo; no organizan la actividad como curso
  de modelos de series de tiempo.

### Highlights de contribución

- **H01 — Trata el tiempo como estructura y no como filas intercambiables:** usa
  228 observaciones mensuales de 1946:01–1964:12 para especificación y las 24
  posteriores para evaluación. Es la particularidad del dataset de Sutter; sin
  este hito, los modelos se podrían juzgar con una partición aleatoria que filtra
  el futuro hacia el pasado.

- **H02 — Centralizar funciones reutilizables:** separa carga, gráficos, ACF/PACF,
  componentes, rezagos, evaluación y almacenamiento en `functions.ipynb`, e
  importa ese notebook desde los demás.
- **H03 — Diagnosticar la dependencia temporal:** calcula y grafica ACF y PACF de la
  serie original, de la primera diferencia y de la diferencia estacional; hace
  visible qué cambia al remover tendencia y ciclo.
- **H04 — Construir la línea base de pronóstico:** implementa en Python regresiones
  con tendencia temporal de distinto orden y dummies mensuales estacionales.
- **H05 — Representar ciclo con Fourier:** sustituye las dummies por componentes seno
  y coseno para construir una alternativa de tendencia más ciclo.
- **H06 — Mostrar el problema de una MLP sin escalamiento:** crea rezagos y entrena
  una `MLPRegressor` sobre la serie original sin escalar, para contrastar su
  comportamiento con las variantes posteriores.
- **H07 — Escalar el flujo completo de MLP:** usa `Pipeline`, transformadores y
  `TransformedTargetRegressor` para escalar entradas y objetivo antes de
  pronosticar desde los rezagos de la serie.
- **H08 — Pronosticar la serie diferenciada:** repite el enfoque MLP tras remover
  tendencia y ciclo, y reconstruye el pronóstico en la escala original.
- **H09 — Apilar pronósticos:** alimenta un segundo MLP con el pronóstico del primero
  además de los rezagos para implementar un modelo *stacked*.
- **H10 — Implementar un AR con herramientas generales:** usa rezagos de la serie
  diferenciada y `LinearRegression` para construir y reconstruir un modelo
  autoregresivo, sin esconder su mecánica detrás de una llamada especializada.
- **H11 — Combinar pronósticos:** calcula tanto el promedio de pronósticos disponibles
  como una combinación lineal aprendida mediante `LinearRegression`.
- **H12 — Persistir y comparar evidencia:** cada familia agrega sus columnas a
  `forecasts.csv` y sus métricas de entrenamiento/prueba a `metrics.csv`, de
  modo que los resultados sobreviven a los notebooks y pueden compararse.
- **H13 — Evaluar como pronóstico:** reserva los últimos 24 meses para medir el
  desempeño fuera del período usado para especificar; el tiempo no se trata como
  filas intercambiables en una partición aleatoria.

### Inventario técnico de implementación

- **Introduce:** inspección de tendencia, estacionalidad, primera diferencia y
  diferencia estacional.
- **Introduce:** regresión con tendencia temporal y dummies mensuales; variante
  con términos de Fourier y transformaciones polinómicas.
- **Introduce:** series rezagadas, regresión autoregresiva tras remover tendencia
  y ciclo, y MLP con y sin escalamiento/diferenciación.
- **Extiende:** `Pipeline`, `ColumnTransformer`, escalamiento y
  `TransformedTargetRegressor` para hacer comparables implementaciones de pronóstico.
- **Verifica y comunica:** separa especificación y evaluación temporal, guarda
  pronósticos y calcula métricas para comparar los modelos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Horizonte temporal resguardado | H01, H13 | Serie mensual Sutter 1946–1966, 228 meses de especificación y 24 posteriores | `data/sutter.csv`, notebooks; no documenta decisión operativa ni procedencia. |
| Diagnóstico y transformación | H02, H03, H06–H08, H10 | Funciones reutilizables, ACF/PACF, diferencias, rezagos y escalamiento | `functions.ipynb`, notebooks; no hay pruebas formales de estacionariedad. |
| Familias y combinación | H04–H11 | Tendencia/dummies, Fourier, MLP, AR y combinaciones | Notebooks 2–9; no incorpora intervalos ni validación separada del segundo nivel. |
| Evidencia persistente | H12 | `forecasts.csv` y `metrics.csv` acumulados | `submission/`, pruebas; no se comprueba consistencia integral de columnas. |

### Relación técnica con actividades anteriores

Extiende los pronósticos temporales aplicados de P211–P212 mediante una
secuencia explícita de construcción, transformación y comparación de modelos.
Sin P217 se pierde la competencia de evaluar modelos temporales con estructura
de tendencia, estacionalidad y rezagos, en lugar de tratar el tiempo como una
variable ordinaria.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Partición temporal | S01 | `implementation/predictiva/P216_series_de_tiempo/professor/notebook_1.ipynb`; `data/sutter.csv` | No se documenta la procedencia ni uso operativo de la serie de mano de obra. |
| H02 — Funciones reutilizables | S02 | `implementation/predictiva/P216_series_de_tiempo/professor/functions.ipynb`; notebooks 1–9 | `nbimporter` es un contrato de notebook, no un paquete Python distribuido. |
| H03 — ACF, PACF y diferencias | S02 | `professor/functions.ipynb`: `acf_pacf_plots`; `professor/notebook_1.ipynb` | La actividad no formaliza pruebas de estacionariedad. |
| H04 — Tendencia y dummies | S03 | `professor/notebook_2.ipynb` | La línea base no establece utilidad operativa de sus predicciones. |
| H05 — Fourier | S03 | `professor/notebook_3.ipynb` | Los términos elegidos no se seleccionan mediante validación explícita. |
| H06 — MLP sin escalamiento | S02, S03 | `professor/notebook_4.ipynb` | La conclusión depende de esta serie y configuración. |
| H07 — Pipeline y escalamiento | S02, S03 | `professor/notebook_5.ipynb` | No se evalúa operación del pipeline fuera del notebook. |
| H08 — MLP diferenciado | S02, S03 | `professor/notebook_8.ipynb`; `functions.ipynb`: diferencias y reconstrucción | Diferenciar regular y estacionalmente no prueba remover un ciclo económico. |
| H09 — Stacking | S03 | `professor/notebook_6.ipynb` | No hay validación separada del segundo nivel. |
| H10 — AR con regresión | S03 | `professor/notebook_7.ipynb` | Los rezagos y la forma de reconstrucción son específicos del caso. |
| H11 — Combinación | S03 | `professor/notebook_9.ipynb` | La combinación lineal se ajusta sobre pronósticos disponibles sin una nueva partición visible. |
| H12 — Persistencia acumulativa | S03, S04 | `functions.ipynb`: `save_forecasts`, `save_metrics`; `submission/forecasts.csv`; `metrics.csv` | Los tests no prueban la consistencia de columnas acumuladas. |
| H13 — Evaluación fuera de especificación | S01, S03 | `functions.ipynb`: `compute_evaluation_metrics`; notebooks 2–8 | Reporta MSE y MAE, no incertidumbre ni intervalos de predicción. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Serie, horizonte y partición temporal | `data/sutter.csv`; `functions.ipynb`; notebooks | Debe preservarse la separación cronológica 228/24. |
| S02 | Transformaciones y representación | `functions.ipynb`; notebooks 1–8 | Diferencias, rezagos y escalamiento determinan comparabilidad. |
| S03 | Familias y combinación de modelos | Notebooks 2–9; `forecasts.csv`; `metrics.csv` | La comparación actual usa métricas puntuales, sin incertidumbre. |
| S04 | Producto, pruebas y trazabilidad | `submission/`; `tests/`; `traceability.yaml` | No hay entrada P217 y las pruebas deben revisarse. |

### Contrato de evidencia actual

- **Notebook o código:** diagnostica, transforma, ajusta familias temporales,
  reconstruye pronósticos y combina resultados.
- **`submission/`:** acumula columnas de pronóstico y métricas por modelo.
- **Pruebas:** requieren artefactos persistentes, sin verificar partición,
  métricas, incertidumbre o consistencia entre modelos.
- **Trazabilidad:** no existe entrada P217; requiere escalación.

### Dependencias en la secuencia

- **Recibe de P211–P212:** uso aplicado de pronósticos temporales; no hay
  dependencia de código o dataset demostrable.
- **Habilita para P218–P221:** no hay dependencia demostrable; aporta una base
  de implementación temporal que futuros cambios podrían reutilizar.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P217 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad; el producto actual es un
pronóstico temporal evaluado, no una política de asignación de mano de obra.
