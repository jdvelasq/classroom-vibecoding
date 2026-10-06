# P222 — Selección de variables para regresión

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P221_selection_inputs_regresion/`.

### Preguntas analíticas actuales

- ¿Qué subconjunto de características mejora la predicción de MPG de un automóvil?
- ¿Cómo se selecciona el número de entradas sin separar esa selección del modelo?

Parte de Auto MPG y entrena una regresión lineal con `SelectKBest` y
`f_regression` dentro de un pipeline evaluado.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** predice MPG seleccionando entradas; no hay decisión de flota evidenciada.
- **Producto terminal:** pipeline lineal persistido con número de entradas seleccionado por CV.
- **Uso y límite:** conserva selección dentro del ajuste; no prueba causalidad ni procedencia del caso.
- **Disciplinas contribuyentes:** selección estadística y CV sirven a predicción de MPG.

### Highlights de contribución

- **H01 — Selecciona entradas dentro del pipeline:** `SelectKBest(f_regression)` evita elegir columnas fuera del flujo evaluado.
- **H02 — Busca `k` por validación cruzada:** separa número de entradas de evaluación final.
- **H03 — Conserva modelo y selección conjuntamente:** el estimador persistido incluye el contrato de entrada.

### Inventario técnico de implementación

- **Introduce:** `SelectKBest`, prueba `f_regression` y búsqueda de cantidad de
  variables en `GridSearchCV`.
- **Reutiliza:** manejo de categoría de origen, partición y regresión de P200.
- **Verifica y comunica:** compara MSE, MAE y R²; preserva el estimador elegido
  como artefacto de entrega.

### Índice de comparación externa

| Ancla | Hitos | Mecanismo | Límite |
| --- | --- | --- | --- |
| Selección integrada | H01–H02 | SelectKBest, f_regression, GridSearchCV | No persiste nombres/resultado de selección. |
| Reuso | H03 | `estimator.pkl` | Test sólo presencia. |

### Relación técnica con actividades anteriores

Profundiza P200 al tratar explícitamente qué información entra al modelo, y
P221 al encapsular la transformación junto con el estimador. Sin P222 se pierde
la competencia de justificar una regresión con selección reproducible de inputs.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite |
| --- | --- | --- | --- |
| H01 | S01 | Notebook: pipeline y `SelectKBest` | No persiste entradas. |
| H02 | S02 | Notebook: grilla CV | Sin resultados CV persistidos. |
| H03 | S03, S04 | Estimador y prueba | Test sólo archivo. |

### Superficies de cambio para revisión posterior

| ID | Componente | Rutas | Restricción |
| --- | --- | --- | --- |
| S01 | Auto MPG/representación | Datos; notebook | `Origin` debe conservar codificación correcta. |
| S02 | Selección y CV | Notebook; `.pkl` | Selección dentro de ajuste. |
| S03 | Evidencia | Métricas/pruebas | Sin tabla de selección. |
| S04 | Trazabilidad | YAML | Falta P222. |

### Contrato de evidencia actual

- **Código:** particiona, selecciona, busca y serializa.
- **`submission/`:** estimador.
- **Pruebas:** presencia de archivo.
- **Trazabilidad:** falta P222.

### Dependencias en la secuencia

- **Recibe de P200/P221:** Auto MPG, pipeline y contrato de transformación.
- **Habilita para P223–P224:** contraste entre selección de columnas y regularización.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P222 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad.
