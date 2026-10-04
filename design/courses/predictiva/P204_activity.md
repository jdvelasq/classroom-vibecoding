# P204 — Clasificación básica numérica

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P204_clasificacion_basica_numerica/`.

### Preguntas analíticas actuales

- ¿Cómo estimamos, con fines educativos, la probabilidad de que un caso histórico corresponda a la clase M a partir de mediciones numéricas?
- ¿Una especificación flexible ordena mejor los casos reservados que una logística base?

Usa mediciones históricas de cáncer de mama sólo como práctica educativa. El
producto es una probabilidad para una clase histórica y la comparación de dos
especificaciones; el notebook prohíbe inferir diagnóstico clínico.

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
  exactitud sobre una muestra estratificada reservada. La versión flexible mejora
  AUC de 0.842 a 0.852, aunque baja exactitud de 0.754 a 0.746; sin este hito,
  una métrica única ocultaría la tensión entre clasificación por umbral y orden
  probabilístico.
- **H05 — Conserva dos especificaciones comparables:** persiste estimadores base y
  flexible, comparación y metadatos de entradas. Sin estos artefactos, no se
  podría revisar qué variables y transformaciones corresponden a cada AUC.

### Inventario técnico de implementación

- **Reutiliza:** separación estratificada, escalamiento y regresión logística
  de P201 para un resultado binario.
- **Introduce:** pipeline de clasificación binaria, ROC AUC y distinción entre
  ordenamiento probabilístico y exactitud.
- **Extiende:** ingeniería de características de P200 con cuadrado e interacción
  para una logística flexible.
- **Reutiliza:** persistencia y añade comparación trazable de especificaciones.

### Relación técnica con actividades anteriores

P204 no es otra introducción genérica a logística. P201 aporta clasificación
multiclase e inspección de probabilidades; P204 transforma eso en comparación
de dos modelos binarios sobre datos numéricos, con un límite clínico explícito
y un AUC que no equivale a exactitud. P205 podrá cuestionar después cómo usar
una probabilidad, pero P204 todavía no fija umbral ni política.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| H01 — Límite educativo y clase positiva | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: pregunta, `diagnosis == "M"` y notas de no diagnóstico | El límite pedagógico no sustituye validación clínica, consentimiento ni evaluación externa. |
| H02 — Logística binaria base | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: dos variables, visualización y `LogisticRegression` | Dos mediciones no representan todos los factores clínicos pertinentes. |
| H03 — Especificación flexible | `implementation/predictiva/P204_clasificacion_basica_numerica/professor/notebook.ipynb`: `texture_mean_squared`, interacción y `flexible_estimator` | La forma funcional se prueba sólo en este conjunto. |
| H04 — AUC frente a exactitud | `implementation/predictiva/P204_clasificacion_basica_numerica/submission/model_comparison.csv`; `metrics.json`; notebook de profesor | AUC y exactitud no evalúan calibración, utilidad clínica ni equidad. |
| H05 — Persistencia de comparación | `implementation/predictiva/P204_clasificacion_basica_numerica/submission/`; `implementation/predictiva/P204_clasificacion_basica_numerica/tests/test_activity.py` | Las pruebas sólo verifican que existan los cuatro artefactos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso clínico educativo y datos | `data/wisc_bc_data.csv`; notebook | No puede pasar a diagnóstico ni uso clínico por analogía. |
| S02 | Variables y especificaciones | Notebook; estimadores `.pkl`; comparación | Dos variables base y dos derivadas determinan la comparación actual. |
| S03 | Evaluación y producto | `metrics.json`; `model_comparison.csv`; pruebas | AUC y exactitud no prueban calibración, utilidad ni equidad. |

### Contrato de evidencia actual

- **Notebook o código:** define clase M, separa, ajusta dos pipelines y compara
  AUC y exactitud.
- **`submission/`:** conserva ambos estimadores, comparación y metadatos.
- **Pruebas:** exigen cuatro artefactos, sin validar sus métricas.
- **Trazabilidad:** P204 mapea `predictiva.C01`–`C04`.

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
