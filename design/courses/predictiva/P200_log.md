# Log — P200

## S01.P200.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se mapearon preparación, regresión, comparación y artefactos persistentes.

## S01.P200.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P200_regresion_basica/`
  (notebook de profesor, datos, `submission/` y pruebas) y la entrada P200 de
  `implementation/predictiva/traceability.yaml`.
- **Decisión:** se añadieron highlights que separan contribuciones observables:
  tipado y tratamiento de entradas, aislamiento entrenamiento/prueba,
  especificaciones lineales, MLP, comparación fuera de muestra y persistencia
  conjunta de transformadores y modelos. No se modificó la implementación ni
  se añadieron mejoras pendientes.

## S01.P200.03

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se precisaron dos highlights: `OneHotEncoder` como método para
  representar categorías nominales, y el contraste aislado entre regresión
  lineal y MLP usando sólo `Horsepower`. La comparación persistida sustenta MSE
  de prueba 22.03 y 15.60, respectivamente.

## S01.P200.04

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/predictiva/P200_regresion_basica/`
  (notebook de profesor, `submission/model_comparison.csv` y pruebas) y P200
  en `implementation/predictiva/traceability.yaml`.
- **Decisión:** se aplicó el contrato reescrito de S01: cada highlight quedó
  contrastado contra una ruta y con su límite de inferencia. Se confirmó la
  granularidad de semántica categórica, preprocesamiento sin filtración,
  especificaciones lineales, contraste de MLP de una entrada y persistencia.
- **Auditoría de Analytics:** el producto permanece como estimación verificable
  de MPG; preprocesamiento, regresión y MLP contribuyen a ese producto y no
  reorganizan la actividad como un curso introductorio de ML.

## S01.P200.05

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se asignaron IDs estables H01–H10 y se documentaron superficies
  de cambio, contrato de evidencia y dependencias demostrables para que futuras
  propuestas de benchmarks puedan afectar un componente concreto.

## S01.P200.06

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** incremental.
- **Decisión:** se declaró el producto predictivo, se añadió el índice externo y se vinculó H01–H10 con superficies existentes; se preservaron implementación y mejoras pendientes.
- **Auditoría de Analytics:** regresión, MLP y preprocesamiento sirven a estimar MPG verificablemente.

## S03.P200.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios; aporta a N01 (árboles y ensambles).
- **Señales descartadas relevantes:**
  - regresión lineal con una y varias variables (p. 8): ya cubierta (H01, H04, H07–H09).
  - regresión para inferencia causal, RCT y confusión (p. 8): fuera de alcance; la inferencia causal no es el producto de Predictiva y P200 ya declara el límite causal.
  - árboles, Random Forest y boosting (p. 8): se descartó incluirlos en P200 por la carga del primer taller; se proponen como actividad nueva N01.

## S03.P200.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: ea86a5d0e15ccad7bb0910f62de882724366b3ca3a01b667ba71df3d2b2b0559).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - fundamentos de ML, calidad/representatividad de datos y entrenamiento/validación/prueba (p. 5): ya cubiertos para el producto MPG (H02–H03, H06, H10); no generan una capacidad adicional específica a esta pregunta.
  - aprendizaje profundo y redes neuronales (p. 5): marginal; P200 ya contrasta MLP con regresión para la predicción cuantitativa del caso (H08–H09), y añadir otra arquitectura no cambiaría qué aprende el estudiante a producir.
  - casos de estrategia y creación de valor de IA (pp. 5–6): no anclan mejora a P200; su producto estima MPG, sin una decisión de flota ni caso organizacional de adopción de IA definido.
