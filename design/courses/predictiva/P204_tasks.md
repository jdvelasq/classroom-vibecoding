# P204 — Propuestas de mejora

**Línea base:** `P204_activity.md` (descripción S02 vigente; log histórico
`S01.P204.*`).

## T01 — Medir si la diferencia entre las dos especificaciones supera la variación de la partición

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md`
    p. 97 — ML-General, T2: «Analyze performance across models using
    bootstrapping and statistical significance testing»; p. 96, disposición
    T1: comparar modelos con «fair and honest comparisons» (Claude,
    2026-10-04).
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` p. 44 — fundamento estadístico que todo estudiante debe dominar: «Variability, uncertainty, sampling error, and inference»; p. 41: tener confianza en que lo que se afirma es cierto «within some margins of error» (Claude, 2026-10-04).
  - `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` p. 1 — incluye «permutation testing» e intervalos de confianza dentro del ciclo de modelado y decisión (Claude, 2026-10-04).
- **Qué gana el estudiante:** saber si una diferencia entre modelos es real o
  puede ser ruido de la muestra de prueba antes de concluir que uno es mejor.
  Hoy H04 lee que la versión flexible «mejora AUC de 0.842 a 0.852, aunque
  baja exactitud de 0.754 a 0.746». Son diferencias de una centésima sobre una
  sola partición, y nada en P204 permite saber si superan la variación del
  muestreo. Si no la superan, la lección de H04 se apoya en ruido. En todo el
  curso las comparaciones entre modelos son estimaciones puntuales; P204 es el
  lugar natural para enseñarlo porque su contribución es justamente comparar
  dos especificaciones.
- **Anclas actuales:** H04 (AUC frente a exactitud), H05 (persistencia de la
  comparación); superficie S03 (evaluación y producto); dependencia «Habilita
  para P205».
- **Alternativas menores descartadas:** aclarar en texto que la diferencia es
  pequeña no le da al estudiante una forma de verificarlo. Un bootstrap
  pareado sobre la misma muestra de prueba es la extensión mínima: no
  reentrena ni cambia caso, variables ni partición.
- **Contrato de no regresión:** se conservan H01–H05, el caso y su límite no
  diagnóstico, las dos especificaciones, la partición estratificada y los
  artefactos `metrics.json`, `model_comparison.csv` y estimadores con su
  esquema actual. Las pruebas existentes se mantienen. H04 se precisa (su
  lectura pasa a incluir la incertidumbre), sin sustituir su contraste entre
  ordenamiento y exactitud.
- **Interacciones:** ninguna; es la única propuesta de P204. La actividad
  nueva N01 (`course_tasks.md`), si se aprueba, podría reutilizar el mismo
  procedimiento para comparar árboles contra la línea base.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo que reporta,
  para AUC y exactitud, la diferencia entre especificaciones con un intervalo
  bootstrap pareado sobre la muestra de prueba, y una conclusión explícita
  sobre si la diferencia es distinguible del ruido. Debe estar respaldado por
  notebook, un CSV en `submission/` y una prueba. H01–H05 siguen presentes y
  H04 no afirma una mejora que el intervalo no sostenga.

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P204_clasificacion_basica_numerica/

0. Inspecciona primero professor/notebook.ipynb, data/wisc_bc_data.csv,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/predictiva/P204_activity.md (clase M, dos variables base,
   especificación flexible con cuadrado e interacción, AUC y exactitud sobre
   partición estratificada), detente e informa la discrepancia sin modificar.
1. No cambies datos, partición, especificaciones ni artefactos existentes.
2. Añade después de la comparación de AUC y exactitud una sección
   «¿La diferencia es real?»:
   a. Con las probabilidades y predicciones ya calculadas sobre la muestra de
      prueba, genera B = 2000 remuestreos bootstrap de los índices de prueba
      con semilla fija. En cada remuestreo usa los mismos índices para ambos
      modelos (bootstrap pareado).
   b. Calcula en cada remuestreo la diferencia flexible − base de AUC y de
      exactitud; omite remuestreos con una sola clase.
   c. Reporta la diferencia observada y el intervalo percentil del 95 % de
      cada métrica.
   d. Explica en markdown, en 3–5 líneas, si el intervalo incluye cero y qué
      significa para la conclusión de H04; aclara que el intervalo sólo
      refleja variación de la muestra de prueba, no de la partición ni del
      ajuste.
3. Persiste submission/difference_bootstrap.csv con columnas metric,
   observed_difference, ci_low, ci_high, n_resamples.
4. Añade a tests/ una prueba que verifique que el archivo existe, tiene esas
   columnas y filas para AUC y exactitud con ci_low <= ci_high. No elimines
   pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```
