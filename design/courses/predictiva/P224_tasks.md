# P224 — Propuestas de mejora

**Línea base:** `P224_activity.md` (descripción S02 vigente; log histórico
`S01.P224.*`).

## T01 — Evaluar cuánta información predictiva conservan los componentes principales

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md`
    p. 7 — «Finding the principal components in data and applications»,
    «Embeddings: New features and their meaning» y el caso «PCA: Identifying
    faces»; p. 5 — «Choose how to represent your data when making
    predictions» (Claude, 2026-10-04).
- **Qué gana el estudiante:** decidir cuántas dimensiones conservar con
  evidencia predictiva, no sólo visual: entrenar el mismo clasificador con
  distintos números de componentes y ver cómo cambia el desempeño de prueba.
  Hoy P224 produce tres proyecciones visuales y su propia descripción
  declara que «no genera estimador, predicción, métrica de error ni
  decisión» y que su identidad Predictiva está sin resolver (H04, S02, S04).
  Con este cambio, la reducción de dimensionalidad pasa a ser una
  representación evaluada al servicio de un producto predictivo.
- **Anclas actuales:** H01 (contraste de tres proyecciones), H02 (evidencia
  visual), H03 (imagen como dato), H04 (límite de producto); superficies S01,
  S02, S03 y S04; dependencia «Recibe de P201» (dataset de dígitos).
- **Alternativas menores descartadas:** aclarar que P224 es exploratorio deja
  la auditoría de identidad sin resolver. Añadir más métodos de proyección
  (espectrales o grafos, también en el folleto) sumaría visualizaciones sin
  producto predictivo.
- **Contrato de no regresión:** se conservan H01–H03 y los tres PNG
  (`digits_pca.png`, `digits_tsne.png`, `digits_umap.png`) con sus pruebas.
  **Sustitución explícita:** H04 («no genera estimador…») deja de ser cierto y
  se reemplaza por el nuevo highlight. La equivalencia se verifica porque la
  nueva evidencia declara igualmente sus límites (dataset educativo, una
  partición). La dependencia con P201 pasa de conceptual a demostrable
  (mismo dataset, misma partición estratificada y mismo tipo de
  clasificador).
- **Interacciones:** ninguna; es la única propuesta de P224. Esto cambia la
  identidad del taller (de exploración a representación evaluada), por lo
  que debe discutirse como tal.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo que muestra la
  exactitud de prueba de un clasificador logístico en función del número de
  componentes principales ajustados sólo con entrenamiento, junto con la
  varianza explicada acumulada. Debe estar respaldado por notebook, CSV y PNG
  en `submission/` y una prueba. H01–H03 siguen presentes; H04 queda
  reescrito como límite del nuevo producto; la auditoría de identidad de
  P224 deja de estar «sin resolver».

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P224_reduccion_dimensionalidad/

0. Inspecciona primero professor/notebook.ipynb, submission/ y tests/. Si la
   implementación no coincide con design/courses/predictiva/P224_activity.md
   (load_digits, PCA/t-SNE/UMAP a 2D, tres PNG), detente e informa la
   discrepancia sin modificar nada.
1. Conserva sin cambios las tres proyecciones 2D, sus figuras y su discusión.
2. Añade una sección «¿Cuánta información conservan los componentes?»:
   a. Separa load_digits con train_test_split estratificado y semilla fija,
      igual que P201 (consulta implementation/predictiva/
      P201_clasificacion_basica_imagenes/ para replicar la partición y el
      clasificador; no importes su código).
   b. Para k en [2, 5, 10, 20, 30, 40, 64], construye
      Pipeline([StandardScaler(), PCA(n_components=k), LogisticRegression()])
      ajustado sólo con entrenamiento; registra exactitud de prueba y
      varianza explicada acumulada de PCA.
   c. Grafica exactitud y varianza explicada frente a k en una figura.
   d. Explica en markdown, en 4–6 líneas: qué k parece suficiente y por qué;
      que t-SNE no tiene transformación para observaciones nuevas y por eso no
      se usa como entrada de un predictor; y que el resultado vale sólo para
      este dataset educativo y esta partición.
3. Persiste submission/pca_components_accuracy.csv (columnas k,
   explained_variance, test_accuracy) y submission/pca_components_accuracy.png.
4. Añade a tests/ una prueba que verifique que existen ambos archivos, que el
   CSV tiene esas columnas y que incluye k=64. No elimines pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```
