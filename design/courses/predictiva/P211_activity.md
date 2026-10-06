# P211 — Pronóstico de adopción de producto

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P210_pronostico_adopcion_producto/`.

### Preguntas analíticas actuales

- ¿Cómo puede pronosticarse la adopción mensual de vehículos eléctricos?

Usa registros mensuales de vehículos eléctricos y una fuente documentada; entrega
pronóstico, gráfico, métricas y supuestos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima matrículas EV y pico mensual; no identifica compradores ni efecto de política.
- **Producto terminal:** pronóstico Bass mensual/acumulado frente a persistencia, evaluado en seis meses retenidos.
- **Uso y límite:** matrículas son proxy de adopción tecnológica, no conducta individual ni causalidad.
- **Disciplinas contribuyentes:** difusión Bass y ajuste no lineal sirven al pronóstico de Analytics.

### Highlights de contribución

- **H01 — Distingue adopción mensual de acumulada:** muestra ambas series antes de ajustar, evitando juzgar ajuste acumulado como calidad de predicción mensual.
- **H02 — Reserva seis meses para evaluar:** ajusta parámetros Bass sólo en entrenamiento y deja el tramo final fuera de ajuste.
- **H03 — Contrasta difusión contra persistencia:** compara Bass con repetir la última matrícula observada.
- **H04 — Persiste fuente, pronóstico, métricas, gráfico y supuestos:** conserva el argumento verificable de la comparación.

### Inventario técnico de implementación

- **Introduce:** pronóstico temporal, evaluación de modelo y comunicación de supuestos.
- **Introduce:** entrega tabular y visual de adopción futura.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Dos escalas de adopción | H01 | Matrículas mensuales y acumuladas | No representa compradores únicos. |
| Evaluación temporal | H02–H03 | Corte de seis meses, Bass y naïve | Sin intervalos de predicción. |
| Entrega auditable | H04 | Fuente, CSV, gráfico, métricas y supuestos | Pruebas sólo comprueban archivos. |

### Relación técnica con actividades anteriores

Pasa de escenarios SIR a un pronóstico de adopción de producto. Sin P211 se
pierde una aplicación temporal de producto con fuente documentada.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook; `data/us_ev_registrations_monthly.csv` | Matrículas son proxy. |
| H02 | S02 | Notebook: training/evaluation y `curve_fit` | No presenta incertidumbre. |
| H03 | S02, S03 | Notebook; `submission/model_metrics.csv` | Línea base sólo es última observación. |
| H04 | S04 | `data/source.json`; `submission/`; pruebas | Tests no validan métricas. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Serie y fuente | Datos; `source.json` | Proxy de adopción, no individuos. |
| S02 | Bass y partición | Notebook; pronóstico | Ajuste sólo en entrenamiento. |
| S03 | Comparación | Métricas y gráfico | Sin intervalos. |
| S04 | Entrega y prueba | `submission/`; tests | Presencia de archivos solamente. |

### Contrato de evidencia actual

- **Código:** prepara series, ajusta Bass, construye línea base y evalúa seis meses.
- **`submission/`:** conserva pronóstico, métricas, gráfico y supuestos.
- **Pruebas:** comprueban cuatro archivos.
- **Trazabilidad:** P211 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de P209–P210:** estructura temporal y contraste con línea base, sin código reutilizado.
- **Habilita para P212 y P217:** horizonte retenido y evidencia de pronóstico temporal.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, `source.json`, notebooks, pronóstico, métricas, supuestos y pruebas
sustentan `predictiva.C01`–`C04`.
