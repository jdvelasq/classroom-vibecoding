# P216 — Series de tiempo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P216_series_de_tiempo/`.

### Preguntas analíticas actuales

- ¿Cómo se pronostica una serie mensual de mano de obra del condado de Sutter?
- ¿Qué enfoque ofrece mejor evidencia fuera del período de especificación: tendencia y estacionalidad, rezagos autoregresivos o MLP?

Usa 228 meses para especificar modelos y 24 meses posteriores para evaluarlos.
La actividad genera pronósticos, métricas y visualizaciones comparables.

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
