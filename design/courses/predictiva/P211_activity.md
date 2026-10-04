# P211 — Pronóstico de congestión de servicio

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P211_pronostico_congestion_servicio/`.

### Preguntas analíticas actuales

- ¿Cómo puede anticiparse la congestión de un servicio a partir de volumen de llamadas y velocidad de respuesta?

Usa series de una línea 800 y publica pronóstico de congestión, gráfico,
métricas y supuestos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** anticipa tiempo medio de cola mensual para reconocer presión de servicio.
- **Producto terminal:** pronóstico Ridge frente a línea base estacional con doce meses retenidos.
- **Uso y límite:** demanda y ocupación son señales observadas; no prueban causalidad ni determinan una política de capacidad.
- **Disciplinas contribuyentes:** regresión regularizada y preparación temporal sirven al producto predictivo.

### Highlights de contribución

- **H01 — Reconstruye fechas desde el calendario fiscal SSA:** alinea llamadas, ocupación y espera sin desplazar picos por el inicio fiscal en octubre.
- **H02 — Protege un año de decisiones mensuales:** reserva los últimos doce meses y usa sólo estado conocido al cierre previo.
- **H03 — Contrasta señal operacional con estacionalidad:** compara Ridge con rezagos/demanda/ocupación y mes contra repetir el mes del año previo.
- **H04 — Entrega evidencia operacional sin convertirla en política:** persiste pronóstico, métricas, gráfico y supuestos.

### Inventario técnico de implementación

- **Extiende:** pronóstico temporal hacia un servicio operativo con variables de demanda y respuesta.
- **Introduce:** producto de congestión para anticipar presión de servicio.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Calendario y señales | H01 | Reconstrucción fiscal y merge de volumen/ocupación/espera | Relación no es causal. |
| Evaluación temporal | H02–H03 | Doce meses, baseline estacional y Ridge | Sin incertidumbre o política. |
| Entrega operacional | H04 | CSV, métricas, gráfico y supuestos | Pruebas sólo verifican archivos. |

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

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Fuentes y calendario | Datos; notebook | Año fiscal no debe desplazarse. |
| S02 | Features y Ridge | Notebook; pronóstico | Sólo estado conocido al cierre previo. |
| S03 | Baseline/evaluación | Métricas/gráfico | No hay incertidumbre. |
| S04 | Entrega/pruebas | `submission/`; tests | Sólo presencia de archivos. |

### Contrato de evidencia actual

- **Código:** alinea datos, prepara rezagos, ajusta Ridge y compara línea base.
- **`submission/`:** conserva pronóstico, métricas, gráfico y supuestos.
- **Pruebas:** verifican cuatro artefactos.
- **Trazabilidad:** P211 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de P210:** corte temporal, línea base y producto de pronóstico.
- **Habilita para P216:** caso temporal multivariable y comparación fuera del corte, sin código común demostrado.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, fuente, notebooks, pronóstico, métricas, supuestos y pruebas sustentan
`predictiva.C01`–`C04`.
