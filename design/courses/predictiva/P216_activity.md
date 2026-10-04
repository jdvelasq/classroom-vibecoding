# P216 — Series de tiempo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P216_series_de_tiempo/`.

### Preguntas analíticas actuales

- ¿Cómo se pronostica una serie mensual de mano de obra del condado de Sutter?
- ¿Qué enfoque ofrece mejor evidencia fuera del período de especificación: tendencia y estacionalidad, rezagos autoregresivos o MLP?

Usa 228 meses para especificar modelos y 24 meses posteriores para evaluarlos.
La actividad genera pronósticos, métricas y visualizaciones comparables.

### Hitos de aprendizaje actuales

- **Centralizar funciones reutilizables:** separa carga, gráficos, ACF/PACF,
  componentes, rezagos, evaluación y almacenamiento en `functions.ipynb`, e
  importa ese notebook desde los demás.
- **Diagnosticar la dependencia temporal:** calcula y grafica ACF y PACF de la
  serie original, de la primera diferencia y de la diferencia estacional; hace
  visible qué cambia al remover tendencia y ciclo.
- **Construir la línea base de pronóstico:** implementa en Python regresiones
  con tendencia temporal de distinto orden y dummies mensuales estacionales.
- **Representar ciclo con Fourier:** sustituye las dummies por componentes seno
  y coseno para construir una alternativa de tendencia más ciclo.
- **Mostrar el problema de una MLP sin escalamiento:** crea rezagos y entrena
  una `MLPRegressor` sobre la serie original sin escalar, para contrastar su
  comportamiento con las variantes posteriores.
- **Escalar el flujo completo de MLP:** usa `Pipeline`, transformadores y
  `TransformedTargetRegressor` para escalar entradas y objetivo antes de
  pronosticar desde los rezagos de la serie.
- **Pronosticar la serie diferenciada:** repite el enfoque MLP tras remover
  tendencia y ciclo, y reconstruye el pronóstico en la escala original.
- **Apilar pronósticos:** alimenta un segundo MLP con el pronóstico del primero
  además de los rezagos para implementar un modelo *stacked*.
- **Implementar un AR con herramientas generales:** usa rezagos de la serie
  diferenciada y `LinearRegression` para construir y reconstruir un modelo
  autoregresivo, sin esconder su mecánica detrás de una llamada especializada.
- **Combinar pronósticos:** calcula tanto el promedio de pronósticos disponibles
  como una combinación lineal aprendida mediante `LinearRegression`.
- **Persistir y comparar evidencia:** cada familia agrega sus columnas a
  `forecasts.csv` y sus métricas de entrenamiento/prueba a `metrics.csv`, de
  modo que los resultados sobreviven a los notebooks y pueden compararse.
- **Evaluar como pronóstico:** reserva los últimos 24 meses para medir el
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

### Relación técnica con actividades anteriores

Extiende los pronósticos temporales aplicados de P210–P211 mediante una
secuencia explícita de construcción, transformación y comparación de modelos.
Sin P216 se pierde la competencia de evaluar modelos temporales con estructura
de tendencia, estacionalidad y rezagos, en lugar de tratar el tiempo como una
variable ordinaria.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P216 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad; el producto actual es un
pronóstico temporal evaluado, no una política de asignación de mano de obra.
