# P215 — Propuestas de mejora

**Línea base:** `P215_activity.md` (descripción S02 vigente; log histórico
`S01.P215.*`).

## T01 — Contrastar el filtrado colaborativo con una línea base en calificaciones retenidas

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md`
    p. 10 — la recomendación se plantea como «Recommendation Prediction
    Problem» y empieza por «Using Population Averages» antes de filtrado
    colaborativo (Claude, 2026-10-04).
  - `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md`
    p. 2 — presenta la personalización de la experiencia del cliente como una
    aplicación de IA (OpenWork, 2026-10-04). La señal respalda la relevancia
    contextual de la tarea recomendadora, pero no añade evidencia a la
    comparación evaluativa nueva de esta T01.
- **Qué gana el estudiante:** poder juzgar si una recomendación colaborativa
  aporta algo frente a recomendar lo popular, con evidencia sobre
  calificaciones que el método no vio. Hoy P215 produce recomendaciones sin
  ninguna evaluación retenida ni línea base (límites declarados en H03 y en
  el índice externo: «Sin evaluación retenida», «No hay métrica de ranking
  retenido»). Es el único producto predictivo del bloque temporal y de
  recomendación sin esa comparación: P210 usa persistencia, P211 línea base
  estacional, P213 persistencia y P214 confianza retenida.
- **Anclas actuales:** H03 (puntuación por desviaciones ponderadas), H04
  (cobertura y soporte); superficies S02 (vecinos y score) y S03 (cobertura);
  dependencia «Recibe de P214» (evaluación retenida de una recomendación).
- **Alternativas menores descartadas:** aclarar en texto que no hay
  evaluación no basta, porque el límite ya está declarado y el estudiante
  sigue sin poder verificar el producto. Añadir sólo filtrado ítem–ítem (que
  también propone el folleto) sería otra variante del mismo método, sin
  evidencia de que alguna supere una línea base.
- **Contrato de no regresión:** se conservan H01–H04 y el flujo actual para el
  usuario 272: matriz usuario×película sin convertir faltantes en ceros,
  filtro de al menos dos películas comunes y similitud positiva, exigencia de
  dos vecinos de respaldo, y los artefactos `recommendations.csv`, el CSV de
  vecinos y `coverage_summary.csv` con su esquema actual. Las pruebas
  existentes se mantienen. Nada se sustituye: la evaluación se añade.
- **Interacciones:** se refuerza con el contexto de personalización de Berkeley
  (p. 2); no compite con otras propuestas de P215. La personalización es un uso
  posible, no evidencia de satisfacción o impacto en clientes.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo (H05) que
  compara, sobre calificaciones retenidas, el error de la línea base de
  promedio por película contra el de la predicción colaborativa, e informa qué
  fracción de las retenidas pudo predecir cada método. Debe estar respaldado
  por una sección del notebook, un artefacto persistido en `submission/` y una
  prueba que verifique su existencia y columnas. H01–H04 siguen presentes y
  sin cambio de sentido.

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P215_filtrado_colaborativo/

0. Inspecciona primero el notebook de profesor, data/filmtrust_ratings.csv,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/predictiva/P215_activity.md (matriz usuario×película,
   medias por usuario, similitud coseno, ≥2 películas comunes, ≥2 vecinos,
   usuario 272), detente e informa la discrepancia sin modificar nada.
1. No cambies el flujo existente que produce las recomendaciones del usuario
   272 ni el esquema de sus artefactos.
2. Añade al final del notebook una sección «Evaluación retenida»:
   a. Con semilla fija, reserva una fracción pequeña (p. ej. 10–20 %) de las
      calificaciones observadas, sólo de usuarios con suficientes
      calificaciones para no dejarlos vacíos en entrenamiento.
   b. Recalcula medias, similitudes y vecinos usando únicamente las
      calificaciones de entrenamiento, reutilizando las funciones o celdas
      existentes; no dupliques la lógica con otra fórmula.
   c. Predice cada calificación retenida con: (i) línea base = promedio de
      la película en entrenamiento (o media global si la película no tiene
      calificaciones); (ii) el método colaborativo actual, con las mismas
      reglas de respaldo.
   d. Calcula MAE y RMSE de cada método sobre las retenidas que ambos
      pueden predecir, y la cobertura de cada método (fracción de retenidas
      con predicción).
   e. Explica en markdown, en 3–5 líneas, qué permite concluir la
      comparación y qué no (no mide satisfacción, ranking ni impacto).
3. Persiste submission/holdout_evaluation.csv con una fila por método y
   columnas method, n_predicted, coverage, mae, rmse.
4. Añade a tests/ una prueba que verifique que holdout_evaluation.csv existe,
   tiene esas columnas y contiene los dos métodos. No elimines ni debilites
   pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad; ambos deben
   terminar sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```
