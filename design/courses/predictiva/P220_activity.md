# P220 — Hiperparámetros

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P219_hiperparametros/`.

### Preguntas analíticas actuales

- ¿Qué combinación de `alpha` y `l1_ratio` de ElasticNet ofrece mejor evidencia predictiva para calidad de vino?
- ¿Cómo se contrasta una exploración manual con `GridSearchCV` sin usar los datos de prueba para escoger el modelo?

Entrena y compara modelos ElasticNet sobre calidad de vino; conserva el mejor
estimador serializado.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima calidad de vino y compara configuraciones; no hay usuario o decisión de calidad evidenciados.
- **Producto terminal:** ElasticNet persistido seleccionado por exploración y CV.
- **Uso y límite:** separa ajuste/test; no documenta procedencia, incertidumbre ni uso operativo del dataset.
- **Disciplinas contribuyentes:** regularización y búsqueda de parámetros sirven a evidencia predictiva.

### Highlights de contribución

- **H01 — Hace visible el efecto de `alpha` y `l1_ratio`:** compara manualmente combinaciones antes de automatizar la búsqueda.
- **H02 — Separa selección y evaluación:** usa `GridSearchCV` en entrenamiento y calcula MSE, MAE y R² sobre prueba.
- **H03 — Conserva el estimador elegido:** recarga el objeto para comprobar su desempeño frente al modelo comparado.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo observable | Límite |
| --- | --- | --- | --- |
| Exploración manual | H01 | ElasticNet con pares alpha/l1_ratio | No persiste tabla de comparaciones. |
| CV/test | H02 | GridSearchCV, MSE/MAE/R² | Sin procedencia/incertidumbre. |
| Artefacto | H03 | `estimator.pkl` | Test sólo presencia. |

### Inventario técnico de implementación

- **Introduce:** partición entrenamiento/prueba, ElasticNet y métricas MSE, MAE
  y R².
- **Introduce:** exploración manual de `alpha` y `l1_ratio`, y búsqueda
  sistemática con `GridSearchCV`.
- **Verifica y comunica:** carga el estimador persistido y comprueba que la
  elección por validación no es inferior en MAE al estimador comparado.

### Relación técnica con actividades anteriores

Extiende P200 y P222 desde entrenar un modelo a seleccionar sus parámetros con
evidencia. Sin P220 se pierde la práctica de separar ajuste de hiperparámetros y
evaluación final.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite |
| --- | --- | --- | --- |
| H01 | S01 | Notebook: búsquedas manuales | Resultados no persistidos. |
| H02 | S02 | Notebook: GridSearchCV/métricas | Partición fija. |
| H03 | S03, S04 | Estimador y pruebas | No verifica valor ni reproducibilidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción |
| --- | --- | --- | --- |
| S01 | Caso/calidad | Datos; notebook | Procedencia no documentada. |
| S02 | ElasticNet/búsqueda | Notebook; `.pkl` | Test no participa en CV. |
| S03 | Métricas/artefacto | Notebook; tests | Sin tabla persistida. |
| S04 | Trazabilidad | YAML | Falta P220. |

### Contrato de evidencia actual

- **Código:** particiona, ajusta ElasticNet, busca parámetros y recarga modelo.
- **`submission/`:** conserva estimador.
- **Pruebas:** verifican sólo presencia.
- **Trazabilidad:** falta P220.

### Dependencias en la secuencia

- **Recibe de P200/P222:** regresión, partición y selección.
- **Habilita para P224:** contraste con Lasso, sin dependencia de código.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P220 en `implementation/predictiva/traceability.yaml`.
La actividad conserva un estimador, pero necesita revisar su relación explícita
con la pregunta de calidad antes de ser aprobada curricularmente.
