# P223 — Regularización Lasso

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P223_lasso/`.

### Preguntas analíticas actuales

- ¿Cómo cambia la predicción de MPG cuando una regresión penaliza coeficientes?
- ¿Cómo se selecciona `alpha` sin usar la muestra de prueba para ajustar el
  modelo?

Usa las 32 observaciones de `mtcars.csv`; estima MPG desde especificaciones del
vehículo y persiste el `GridSearchCV` resultante. El conjunto es pequeño y no
trae procedencia, periodo ni contexto operativo documentados.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** predice MPG en el caso didáctico; no hay
  usuario, decisión de flota ni uso organizacional evidenciados.
- **Producto terminal:** regresión Lasso escalada, con `alpha` buscado por CV.
- **Uso y límite:** permite contrastar penalización, coeficientes y desempeño
  en train/test; no prueba causalidad ni rendimiento fuera de este conjunto.
- **Disciplinas contribuyentes:** regularización, validación y regresión sirven
  al producto predictivo de Analytics; no vuelven el taller un curso autónomo
  de inferencia o de optimización.

### Highlights de contribución

- **H01 — Hace visible la dependencia entre entradas del caso:** calcula y
  grafica la matriz de correlación de especificaciones de 32 vehículos antes de
  penalizar. Sin este hito, el uso de Lasso parecería una receta sin relación
  con las variables que compiten por explicar MPG.
- **H02 — Penaliza coeficientes sobre entradas comparables:** combina
  `StandardScaler` y `Lasso(max_iter=10000)` en `Pipeline`, evitando que la
  escala de cilindrada, potencia o peso determine artificialmente la penalidad.
- **H03 — Muestra la trayectoria de contracción:** recorre valores de `alpha` y
  grafica coeficientes por variable. Extiende la selección explícita de P221:
  aquí la inclusión se controla al contraer coeficientes, no al elegir sólo k
  columnas.
- **H04 — Selecciona `alpha` con entrenamiento y validación cruzada:** busca
  100 valores entre 0.01 y 2.0 por CV y sólo después reporta R² y MSE de prueba.
  Sin este hito, la muestra de prueba podría convertirse en mecanismo de ajuste.
- **H05 — Persiste el modelo regularizado elegido:** serializa el `GridSearchCV`
  con escalamiento y Lasso. Sin este artefacto, la elección de `alpha` no podría
  reutilizarse con su transformación asociada.
- **H06 — Vincula la elección de modelo a la escala del dataset:** `mtcars` tiene
  32 filas y diez entradas técnicas para MPG; esa relación pequeña exige leer
  con prudencia cualquier comparación y prohíbe generalizar rendimiento.

### Inventario técnico de implementación

- **Introduce:** inspección de correlación, Lasso, trayectorias de coeficientes
  y selección de `alpha` por CV.
- **Reutiliza:** partición, escalamiento, pipeline y métricas R²/MSE de P200 y
  P219.
- **Verifica y comunica:** guarda el estimador; las pruebas no validan su
  desempeño ni los coeficientes.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Regularización escalada | H02–H04 | `StandardScaler` + Lasso, grilla de alpha y CV | Notebook; la grilla es fija y no se persisten resultados. |
| Lectura de coeficientes | H01, H03 | Correlación y trayectoria por `alpha` | Notebook; no documenta criterio para seleccionar variables. |
| Modelo reutilizable | H05 | `estimator.pkl` | Test de existencia solamente. |
| Caso pequeño | H06 | 32 autos, MPG y 10 atributos | CSV; sin procedencia o contexto de uso. |

### Relación técnica con actividades anteriores

P223 profundiza P219 y P221: P219 busca hiperparámetros para ElasticNet y P221
selecciona k entradas; P223 visualiza cómo Lasso contrae coeficientes en el
caso de MPG. No demuestra que Lasso sea preferible a los modelos de P200.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb`: `df.corr()` y mapa de calor | Correlación no identifica causalidad. |
| H02 | S02 | Notebook: `Pipeline(StandardScaler, Lasso)` | No se documentan variables categóricas ni transformaciones alternativas. |
| H03 | S02 | Notebook: recorrido `alphas`, `coef_` y gráfica | La figura no se conserva en `submission/`. |
| H04 | S02, S03 | Notebook: `GridSearchCV` y R²/MSE train/test | No se persisten métricas ni resultados de CV. |
| H05 | S04 | Notebook: `pickle.dump`; `submission/estimator.pkl`; pruebas | La prueba sólo exige presencia. |
| H06 | S01, S03 | `data/mtcars.csv`; notebook | Procedencia y representatividad no documentadas. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso `mtcars` | `data/mtcars.csv`; notebook | Conjunto de 32 autos sin procedencia documentada. |
| S02 | Escalamiento, Lasso y alpha | Notebook; `estimator.pkl` | La penalidad debe aplicarse a entradas escaladas. |
| S03 | Comparación y visualización | Notebook | R²/MSE y trayectoria no se persisten. |
| S04 | Entrega y prueba | `submission/estimator.pkl`; pruebas | Sólo se prueba existencia del archivo. |
| S05 | Trazabilidad | `traceability.yaml` | No existe entrada P223. |

### Contrato de evidencia actual

- **Notebook o código:** inspecciona correlación, particiona, escala, ajusta,
  recorre alphas, busca por CV y serializa.
- **`submission/`:** conserva `estimator.pkl`.
- **Pruebas:** verifican sólo que existe el estimador.
- **Trazabilidad:** falta entrada P223 y requiere escalación.

### Dependencias en la secuencia

- **Recibe de P200, P219 y P221:** regresión de MPG, pipeline, validación y
  selección de entradas.
- **Habilita para Pyyy:** no hay actividad posterior con dependencia técnica
  demostrable; deja el contraste entre selección y contracción de coeficientes.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P223 en `implementation/predictiva/traceability.yaml`.
El producto sigue siendo una predicción de MPG; Lasso es una contribución al
modelo y no la lógica curricular autónoma.
