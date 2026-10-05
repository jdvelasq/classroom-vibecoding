# P423 — Monitoreo de desempeño: exactitud observada frente a un mínimo

## Actividad actual implementada

**Implementación:** `implementation/productos/P423_model_performance_monitoring/`.

### Preguntas analíticas actuales

- Una vez conocidos los resultados reales, ¿la exactitud del modelo en producción cae por debajo del mínimo aceptado?

`data/production_outcomes.csv` tiene cinco filas con `prediction` y `actual` en las categorías `high`/`low`. `professor/main.py` calcula la proporción de aciertos y la compara con `MINIMUM_ACCURACY = 0.75`; `submission/performance_report.json` registra `observations` 5, `accuracy` 0.6, `minimum_accuracy` 0.75 y `alert` true. El docstring declara la condición del problema: «La calidad real del modelo solo puede observarse después de conocer el resultado».

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; no se declara qué modelo, qué riesgo ni quién recibe la alerta.
- **Producto terminal:** `submission/performance_report.json`, una alerta de desempeño.
- **Uso y límite:** muestra que el desempeño en operación requiere resultados observados y que una alerta puede derivarse de un mínimo. Con cinco observaciones, la exactitud 0.6 no tiene precisión suficiente para sostener una decisión; no hay periodo, fecha ni desglose por clase.
- **Disciplinas contribuyentes:** evaluación de clasificadores al servicio del monitoreo en operación.

### Highlights de contribución

- **H01 — Distingue monitoreo de desempeño de monitoreo de entradas (caso y datos):** el dato exige pares predicción-resultado; sin `actual`, la medida no existe. Contrasta con P422, que vigila entradas sin etiqueta. La particularidad del caso es esa dependencia de resultados posteriores, no el dominio: las etiquetas `high`/`low` no tienen procedencia y cinco filas no permiten interpretar la exactitud con confianza. Sin este hito, el curso no separaría deriva de entradas y degradación observada.
- **H02 — Fija el borde de la alerta:** `alert = accuracy < MINIMUM_ACCURACY`; `test_01_does_not_alert_when_accuracy_meets_the_minimum` verifica que 0.75 exacto no alerta y `test_02` que 0.25 sí. Sin este hito, el criterio en el umbral quedaría implícito.

### Inventario técnico de implementación

- **Introduce:** monitoreo de desempeño con resultados observados; mínimo de exactitud como regla de alerta.
- **Reutiliza:** patrón de reporte JSON con alerta booleana de P422.
- **Aplica en nuevo caso:** ninguno identificable.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Desempeño con resultados observados | H01 | Exactitud sobre pares predicción-resultado | Cinco filas; sin periodo ni modelo identificado. |
| Regla de alerta en el borde | H02 | `accuracy < 0.75`; prueba en 0.75 | Umbral no justificado. |

### Relación técnica con actividades anteriores

Nuevo tipo de evidencia frente a P422 (desempeño en lugar de entradas). Frente a P403 (exactitud, exactitud balanceada y AUC antes del despliegue sobre 114 filas de prueba), P423 mide después del despliegue pero con una sola métrica y cinco filas. Las etiquetas `high`/`low` coinciden con la salida `risk` de P425 sin relación demostrable. P424 (reversión) no consume la alerta.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Desempeño frente a entradas | S01, S02, S03 | `implementation/productos/P423_model_performance_monitoring/data/production_outcomes.csv`; `implementation/productos/P423_model_performance_monitoring/professor/main.py`: `evaluate_performance`; `implementation/productos/P423_model_performance_monitoring/submission/performance_report.json` | Exactitud 0.6 sobre cinco observaciones. |
| H02 — Borde de la alerta | S02, S04 | `implementation/productos/P423_model_performance_monitoring/professor/test_main.py` | Las pruebas usan etiquetas 0/1, no `high`/`low`. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Resultados observados | `data/production_outcomes.csv` | Cinco filas sin fecha ni procedencia. |
| S02 | Métrica y umbral | `professor/main.py` | Exactitud; mínimo 0.75 fijo. |
| S03 | Reporte | `submission/performance_report.json` | Una ventana. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Borde y caída; existencia del reporte. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** `evaluate_performance` y escritura del reporte.
- **`submission/`:** `performance_report.json`.
- **Pruebas:** `professor/test_main.py` verifica exactitud y alerta en el borde (0.75) y por debajo (0.25); `tests/test_activity.py` sólo la existencia del reporte.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P422:** patrón de reporte con alerta; no recibe artefactos.
- **Habilita para Pyyy:** no evidenciada; P424 no usa la alerta.

## Trazabilidad y auditoría

Entrada revisada: P423 → `productos.C02`, `productos.C03`, `productos.C05`. C05 (monitoreo) y C03 (validación del modelo frente al uso) se sostienen en el mecanismo; C02 es secundario. Auditoría: la idea operativa es propia de productos, pero el caso no identifica la capacidad monitoreada, su usuario ni la acción tras la alerta; con cinco filas, el producto es una demostración del mecanismo.
