# P205 — Priorización con probabilidades

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P205_priorizacion_con_probabilidades/`.

### Preguntas analíticas actuales

- ¿Qué tan confiables son las probabilidades de *default* estimadas?
- ¿Cómo cambia el comportamiento de clasificación al variar el umbral?
- ¿Cómo difieren las probabilidades y resultados observados entre grupos?

Usa una simulación didáctica controlada de predicciones fuera de muestra. El producto son evidencias de calibración, tradeoff de umbrales y revisión por grupo; los costos son ilustrativos y no constituyen una política real de crédito.

### Highlights de contribución

- **H01 — Comprueba si una probabilidad significa lo que aparenta:** divide predicciones en bandas y compara probabilidad media con tasa observada de *default*, frente a la diagonal de calibración ideal. Extiende P204; sin este hito, una probabilidad alta podría usarse sin contrastar frecuencia observada.
- **H02 — Muestra que un umbral transforma predicción en consecuencias:** recorre umbrales 0.2–0.6, cuenta verdaderos y falsos positivos/negativos y calcula costo esperado con costos ilustrativos desiguales. Sin este hito, el umbral parecería una constante técnica y no una elección con consecuencias de error.
- **H03 — Separa análisis de umbrales de política prescriptiva:** el dataset es una simulación didáctica de probabilidades fuera de muestra, no solicitudes reales; por eso selecciona mínimo costo sólo dentro del ejercicio. Sin este hito, el caso confundiría una regla didáctica con autorización para negar o priorizar crédito.
- **H04 — Hace visible el comportamiento por grupo:** el dataset incluye dos grupos simulados de tamaños distintos (3,585 y 5,415); resume tamaño, probabilidad media, tasa observada y proporción priorizada por `group_code`. Extiende la matriz por clase de P203; sin este hito, el tradeoff agregado podría ocultar diferencias sistemáticas.
- **H05 — Conserva los tres argumentos de la priorización:** guarda tablas separadas de calibración, tradeoff y revisión por grupo. Sin estos artefactos, la elección de umbral no sería auditable tras cerrar el notebook.

### Inventario técnico de implementación

- **Extiende:** clasificación probabilística de P204 con bandas de calibración.
- **Introduce:** barrido de umbrales, consecuencias, costo esperado y comparación de alternativas operativas.
- **Introduce:** revisión descriptiva por grupo de predicciones y resultados.
- **Introduce:** frontera explícita entre artefacto predictivo y política real.

### Relación técnica con actividades anteriores

P205 no entrena un clasificador: toma probabilidades ya generadas para juzgar calibración, umbral y revisión por grupo. Complementa P204 y no lo duplica. También evita convertirse en Prescriptiva: no define autoridad, restricciones, excepciones ni monitoreo de una política crediticia.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| H01 — Bandas y diagonal de calibración | `implementation/predictiva/P205_priorizacion_con_probabilidades/professor/notebook.ipynb`: `probability_band`, agregación y gráfico | Las bandas describen esta simulación y no prueban calibración en una población real. |
| H02 — Consecuencias de umbrales | `implementation/predictiva/P205_priorizacion_con_probabilidades/professor/notebook.ipynb`: barrido, conteos y `expected_cost`; `implementation/predictiva/P205_priorizacion_con_probabilidades/submission/threshold_tradeoff.csv` | Los costos 10 y 1 son ilustrativos, no pérdidas estimadas ni preferencias institucionales. |
| H03 — Límite entre predicción y política | `implementation/predictiva/P205_priorizacion_con_probabilidades/professor/notebook.ipynb`: declaración inicial y comentario de costos/política | No implementa autoridad humana, excepciones ni monitoreo posterior. |
| H04 — Revisión por grupo | `implementation/predictiva/P205_priorizacion_con_probabilidades/professor/notebook.ipynb`: `groupby("group_code")`; `implementation/predictiva/P205_priorizacion_con_probabilidades/submission/group_review.csv` | `group_code` proviene de una simulación y no permite concluir equidad ni discriminación. |
| H05 — Persistencia de argumentos | `implementation/predictiva/P205_priorizacion_con_probabilidades/submission/calibration_summary.csv`; `implementation/predictiva/P205_priorizacion_con_probabilidades/submission/threshold_tradeoff.csv`; `implementation/predictiva/P205_priorizacion_con_probabilidades/submission/group_review.csv`; `implementation/predictiva/P205_priorizacion_con_probabilidades/tests/test_activity.py` | Las pruebas verifican archivos, no cálculos ni interpretación ética. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset simulado y grupos | `data/risk_predictions.csv`; notebook | No representa solicitantes reales ni permite inferir equidad. |
| S02 | Calibración, umbral y costos | Notebook; tres CSV de `submission/` | Los costos 10 y 1 son ilustrativos, no institucionales. |
| S03 | Producto y guardrails | Pruebas; trazabilidad | No existe política completa con autoridad, excepciones y monitoreo. |

### Contrato de evidencia actual

- **Notebook o código:** calcula bandas, tradeoff de umbrales y revisión por
  grupo sobre predicciones ya disponibles.
- **`submission/`:** conserva tres tablas de evidencia para auditar la lectura.
- **Pruebas:** exigen esas tablas, sin verificar cálculos ni criterios éticos.
- **Trazabilidad:** P205 mapea `predictiva.C01`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P204:** probabilidad binaria y distinción entre ordenamiento y
  clasificación.
- **Habilita para Pyyy:** no hay dependencia técnica o de artefacto demostrable;
  establece sólo el principio general de no confundir evidencia predictiva con
  política prescriptiva.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

P205 está mapeada a `predictiva.C01`, `predictiva.C04` y `predictiva.C05` en `implementation/predictiva/traceability.yaml`. El producto de Analytics es una revisión verificable de probabilidades antes de priorizar; clasificación, calibración y análisis de costos contribuyen a él. La actividad no produce una política prescriptiva suficiente por sí sola.
