# P211 — Pronóstico de congestión de servicio

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P211_pronostico_congestion_servicio/`.

### Preguntas analíticas actuales

- ¿Cómo puede anticiparse la congestión de un servicio a partir de volumen de llamadas y velocidad de respuesta?

Usa series de una línea 800 y publica pronóstico de congestión, gráfico,
métricas y supuestos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** anticipa tiempo medio de cola mensual para reconocer presión de servicio.
- **Producto terminal:** pronóstico Ridge frente a línea base estacional con doce meses retenidos, evaluado también con orígenes móviles y acompañado de un intervalo de predicción del 80 %.
- **Uso y límite:** demanda y ocupación son señales observadas; no prueban causalidad ni determinan una política de capacidad. El intervalo informa cuánto puede desviarse el pronóstico; tampoco fija una política de capacidad.
- **Disciplinas contribuyentes:** regresión regularizada y preparación temporal sirven al producto predictivo.

### Highlights de contribución

- **H01 — Reconstruye fechas desde el calendario fiscal SSA:** alinea llamadas, ocupación y espera sin desplazar picos por el inicio fiscal en octubre.
- **H02 — Protege un año de decisiones mensuales:** reserva los últimos doce meses y usa sólo estado conocido al cierre previo.
- **H03 — Contrasta señal operacional con estacionalidad:** compara Ridge con rezagos/demanda/ocupación y mes contra repetir el mes del año previo.
- **H04 — Entrega evidencia operacional sin convertirla en política:** persiste pronóstico, métricas, gráfico y supuestos.
- **H05 — Evalúa la ventaja con varios orígenes de pronóstico, no sólo con el único corte de H03:** reajusta Ridge con ventana expansiva en 24 orígenes mensuales consecutivos (12 antes del bloque final y los 12 que lo componen) y compara su error absoluto con la línea base estacional en cada uno. Sobre el bloque final, Ridge gana en 10 de los 12 orígenes (83.3 %) con el mismo MAE que reporta H03 (126.5 s frente a 624.8 s), y mantiene el margen también en los orígenes anteriores al bloque: la ventaja no depende de dónde se puso el corte único de H03.
- **H06 — Acompaña el pronóstico puntual con un rango de desviación posible:** construye un intervalo de predicción del 80 % para cada mes del bloque final a partir del percentil 80 del error absoluto de los orígenes móviles de H05 anteriores a ese mes. La cobertura empírica es 83.3 % (10 de 12 meses); el intervalo informa cuánto puede desviarse el pronóstico para anticipar presión de servicio, sin fijar una política de capacidad.

### Inventario técnico de implementación

- **Extiende:** pronóstico temporal hacia un servicio operativo con variables de demanda y respuesta.
- **Introduce:** producto de congestión para anticipar presión de servicio.
- **Introduce:** evaluación walk-forward con orígenes móviles e intervalo de
  predicción empírico sobre el pronóstico puntual.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Calendario y señales | H01 | Reconstrucción fiscal y merge de volumen/ocupación/espera | Relación no es causal. |
| Evaluación temporal | H02–H03 | Doce meses, baseline estacional y Ridge | Sin incertidumbre o política. |
| Entrega operacional | H04 | CSV, métricas, gráfico y supuestos | Pruebas sólo verifican archivos. |
| Estabilidad temporal | H05 | 24 orígenes móviles con ventana expansiva | `submission/rolling_origin_errors.csv`; no prueba causalidad o acción. |
| Incertidumbre del pronóstico | H06 | Intervalo de predicción del 80 % por percentil de error absoluto | `submission/forecast_intervals.csv`; no fija política de capacidad. |

### Relación técnica con actividades anteriores

Reutiliza pronóstico de P210 pero cambia de adopción a capacidad de servicio.
Sin P211 se pierde la conexión entre pronóstico y una señal operativa.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook; CSV SSA | Calidad/faltantes de fuente no se validan. |
| H02 | S02 | Notebook: corte y rezagos | Sin intervalos. |
| H03 | S02, S03 | Notebook; `submission/model_metrics.csv` | No prueba causalidad o acción. |
| H04 | S04 | `submission/`; pruebas | Tests sólo presencia. |
| H05 | S03 | Notebook: `TimeSeriesSplit`, reajuste por origen; `submission/rolling_origin_errors.csv` | No prueba causalidad o acción; evalúa estabilidad, no mejora la especificación. |
| H06 | S03 | Notebook: percentil de error absoluto, cobertura; `submission/forecast_intervals.csv`, `.png` | Cobertura observada sobre 12 meses; no garantiza 80 % exacto ni evalúa calibración formal. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Fuentes y calendario | Datos; notebook | Año fiscal no debe desplazarse. |
| S02 | Features y Ridge | Notebook; pronóstico | Sólo estado conocido al cierre previo. |
| S03 | Baseline/evaluación | Métricas/gráfico; `rolling_origin_errors.csv`; `forecast_intervals.csv/.png` | Incluye un intervalo de predicción empírico (80 %) y una evaluación con 24 orígenes móviles; no evalúa calibración formal ni fija política de capacidad. |
| S04 | Entrega/pruebas | `submission/`; tests | Sólo presencia de archivos; `test_02`/`test_03` validan columnas, consistencia entre artefactos y `lower_80 <= forecast <= upper_80`. |

### Contrato de evidencia actual

- **Código:** alinea datos, prepara rezagos, ajusta Ridge, compara línea base,
  reevalúa con orígenes móviles y construye un intervalo de predicción.
- **`submission/`:** conserva pronóstico, métricas, gráfico, supuestos, el
  detalle por origen móvil y el intervalo de predicción con su gráfico.
- **Pruebas:** verifican cuatro artefactos originales más la consistencia de
  `rolling_origin_errors.csv` (columnas, orígenes mensuales consecutivos,
  actual coherente con `congestion_forecast.csv`) y de `forecast_intervals.csv`
  (`lower_80 <= forecast <= upper_80`).
- **Trazabilidad:** P211 mapea `predictiva.C01`–`C04`; H05 y H06 fortalecen la
  evidencia de C04 (evaluación) sin requerir una capacidad nueva.

### Dependencias en la secuencia

- **Recibe de P210:** corte temporal, línea base y producto de pronóstico.
- **Habilita para P216:** caso temporal multivariable y comparación fuera del corte, sin código común demostrado.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, fuente, notebooks, pronóstico, métricas, supuestos y pruebas sustentan
`predictiva.C01`–`C04`.
