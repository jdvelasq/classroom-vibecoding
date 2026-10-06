# P204 — Clasificación básica numérica

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P204_clasificacion_basica_numerica/`.

### Preguntas analíticas actuales

- ¿Cómo estimamos, con fines educativos, la probabilidad de que un caso histórico corresponda a la clase M a partir de mediciones numéricas?
- ¿Una especificación flexible ordena mejor los casos reservados que una logística base?

Usa mediciones históricas de cáncer de mama sólo como práctica educativa. El
producto es una probabilidad para una clase histórica y la comparación de dos
especificaciones; el notebook prohíbe inferir diagnóstico clínico.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima clase histórica M en un caso educativo; no diagnóstico ni decisión clínica.
- **Producto terminal:** estimadores comparados y métricas AUC/exactitud.
- **Uso y límite:** no evalúa calibración, utilidad clínica o equidad.
- **Disciplinas contribuyentes:** clasificación y evaluación sirven a predicción acotada.

### Highlights de contribución

- **H01 — Delimita una probabilidad educativa antes de mostrar el modelo:** define la
  clase positiva M a partir de la etiqueta histórica y declara que el resultado
  no es diagnóstico. El dataset contiene 212 casos M y 357 B y numerosas
  mediciones; el taller selecciona dos para un caso interpretable, pero no por
  ello clínicamente válido. Frente a P201, mantiene clasificación probabilística
  y añade un límite de uso de alto riesgo; sin este hito, una probabilidad de
  ejemplo podría interpretarse erróneamente como recomendación clínica.
- **H02 — Construye una probabilidad binaria interpretable:** comienza con
  `texture_mean` y `compactness_mean`, visualiza casos B y M, y ajusta una
  logística base dentro de un pipeline. Es el primer contraste explícito entre
  clasificación binaria y multiclase; sin él no se vería cómo cambia el producto
  cuando sólo interesa la probabilidad de una clase.
- **H03 — Flexibiliza el modelo sin abandonar su interpretación:** incorpora término
  cuadrático de textura e interacción textura×compactness antes de la logística.
  Extiende la ingeniería de características de P200 a una probabilidad binaria;
  sin este hito, la comparación se reduciría a escoger un algoritmo en vez de
  discutir una representación alternativa de las mismas mediciones.
- **H04 — Evalúa ordenamiento y decisión como propiedades diferentes:** reporta AUC y
  exactitud sobre una muestra estratificada reservada. La versión flexible cambia
  el AUC de 0.842 a 0.852 y la exactitud de 0.754 a 0.746; sin este hito,
  una métrica única ocultaría la tensión entre clasificación por umbral y orden
  probabilístico. H06 cuantifica si estas diferencias puntuales superan el ruido
  de muestreo.
- **H05 — Conserva dos especificaciones comparables:** persiste estimadores base y
  flexible, comparación y metadatos de entradas. Sin estos artefactos, no se
  podría revisar qué variables y transformaciones corresponden a cada AUC.
- **H06 — Cuantifica si la diferencia entre especificaciones supera el ruido de
  muestreo:** genera un intervalo bootstrap pareado (B = 2000, mismos índices de
  prueba remuestreados para ambos modelos) sobre la diferencia flexible − base de
  AUC y exactitud. Los dos intervalos del 95 % incluyen cero (AUC: -0.001 a
  0.024; exactitud: -0.026 a 0.000): ninguna de las diferencias de H04 es
  distinguible del ruido de muestreo de esta partición de prueba. Sin este hito,
  H04 se leería como una mejora sostenida que el intervalo no sostiene.

### Inventario técnico de implementación

- **Reutiliza:** separación estratificada, escalamiento y regresión logística
  de P201 para un resultado binario.
- **Introduce:** pipeline de clasificación binaria, ROC AUC y distinción entre
  ordenamiento probabilístico y exactitud.
- **Extiende:** ingeniería de características de P200 con cuadrado e interacción
  para una logística flexible.
- **Reutiliza:** persistencia y añade comparación trazable de especificaciones.
- **Introduce:** intervalo bootstrap pareado sobre la muestra de prueba para
  cuantificar si una diferencia entre especificaciones supera el ruido de
  muestreo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Caso binario educativo | H01, H02 | Etiqueta histórica M y dos mediciones numéricas; probabilidad sin uso diagnóstico | Notebook del profesor; no hay validación clínica. |
| Especificaciones comparables | H03, H05 | Logística base frente a cuadrado e interacción; estimadores y comparación persistidos | Notebook, `submission/`; no mide calibración ni utilidad. |
| Evaluación de ordenamiento | H04 | AUC y exactitud de partición estratificada | `metrics.json`, `model_comparison.csv`; no evalúa equidad. |
| Incertidumbre de la comparación | H06 | Intervalo bootstrap pareado de la diferencia AUC/exactitud entre especificaciones | `submission/difference_bootstrap.csv`; no evalúa variación de la partición ni del ajuste. |

### Relación técnica con actividades anteriores

P204 no es otra introducción genérica a logística. P201 aporta clasificación
multiclase e inspección de probabilidades; P204 transforma eso en comparación
de dos modelos binarios sobre datos numéricos, con un límite clínico explícito
y un AUC que no equivale a exactitud. P205 podrá cuestionar después cómo usar
una probabilidad, pero P204 todavía no fija umbral ni política.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Límite educativo y clase positiva | S01 | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: pregunta, `diagnosis == "M"` y notas de no diagnóstico | El límite pedagógico no sustituye validación clínica, consentimiento ni evaluación externa. |
| H02 — Logística binaria base | S02 | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: dos variables, visualización y `LogisticRegression` | Dos mediciones no representan todos los factores clínicos pertinentes. |
| H03 — Especificación flexible | S02 | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: `texture_mean_squared`, interacción y `flexible_estimator` | La forma funcional se prueba sólo en este conjunto. |
| H04 — AUC frente a exactitud | S03 | `implementation/predictiva/P204_clasificacion_basica_numerica/submission/model_comparison.csv`; `metrics.json`; notebook de profesor | AUC y exactitud no evalúan calibración, utilidad clínica ni equidad. |
| H05 — Persistencia de comparación | S02, S03 | `implementation/predictiva/P204_clasificacion_basica_numerica/submission/`; `implementation/predictiva/P204_clasificacion_basica_numerica/tests/test_activity.py` | Las pruebas sólo verifican que existan los cuatro artefactos. |
| H06 — Incertidumbre de la comparación | S03 | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: bootstrap pareado y gráfica de intervalos; `implementation/predictiva/P204_clasificacion_basica_numerica/submission/difference_bootstrap.csv` | El intervalo sólo refleja variación de la muestra de prueba; no evalúa variación de la partición ni del ajuste de los coeficientes. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso clínico educativo y datos | `data/wisc_bc_data.csv`; notebook | No puede pasar a diagnóstico ni uso clínico por analogía. |
| S02 | Variables y especificaciones | Notebook; estimadores `.pkl`; comparación | Dos variables base y dos derivadas determinan la comparación actual. |
| S03 | Evaluación y producto | `metrics.json`; `model_comparison.csv`; `difference_bootstrap.csv`; pruebas | AUC y exactitud no prueban calibración, utilidad ni equidad; el intervalo bootstrap no prueba variación de partición ni del ajuste. |

### Contrato de evidencia actual

- **Notebook o código:** define clase M, separa, ajusta dos pipelines, compara
  AUC y exactitud, y cuantifica con un bootstrap pareado si esa diferencia
  supera el ruido de muestreo.
- **`submission/`:** conserva ambos estimadores, comparación, metadatos y el
  intervalo bootstrap de la diferencia (`difference_bootstrap.csv`).
- **Pruebas:** exigen cuatro artefactos sin validar sus métricas, y el archivo
  del intervalo bootstrap con sus columnas y `ci_low <= ci_high` por métrica.
- **Trazabilidad:** P204 mapea `predictiva.C01`–`C04`; H06 fortalece la
  evidencia de C04 (evaluación) sin requerir una capacidad nueva.

### Dependencias en la secuencia

- **Recibe de P201:** clasificación probabilística, estratificación y análisis
  de errores; de P200, ingeniería de características.
- **Habilita para P205:** probabilidades binarias cuyo uso, calibración y umbral
  podrán ser cuestionados antes de priorizar.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

P204 está mapeada a `predictiva.C01`–`C04` en
`implementation/predictiva/traceability.yaml`. El producto de Analytics es una
estimación binaria evaluada y limitada pedagógicamente; estadística y ML
contribuyen a ella sin transformar el taller en diagnóstico clínico o curso de
ML.
