# P108 — Propuestas de mejora

**Línea base:** `P108_activity.md` (entrada S02 más reciente: `S02.P108.01`).

## T01 — Medir el riesgo residual con el tamaño mínimo de las clases de equivalencia (k) sobre los cuasi-identificadores tras cada paso de generalización

- **Estado:** pendiente de discusión
- **Tipo:** método/evidencia
- **Fuentes:**
  - `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` pp. 2–3 — el módulo fundacional incluye «Data Sharing: Privacy, Anonymization, Risks» con «Technologies for anonymizing data: k-anonymity, and differential privacy» (p. 2), y su resultado de aprendizaje pide «identify privacy risks in releasing information, and design techniques to mediate these risks» (p. 3): el riesgo de publicar un conjunto se mide como propiedad del conjunto publicado (Claude, 2026-10-04). Fuente *institutional* y **fuente única**: ilustra que *k*-anonimato forma parte de un curso fundacional de Analytics; no prescribe técnica, umbral ni profundidad. La privacidad diferencial, también citada en p. 2, queda fuera.
- **Qué gana el estudiante:** distingue un riesgo medido contra un
  atacante concreto de un riesgo medido sobre el conjunto que se publica.
  Hoy P108 cuenta, tras cada paso de generalización, los nombres que la
  tabla auxiliar de 20 perfiles reidentifica de forma única (H04); el
  propio S02 registra que eso «no establece una garantía formal (p. ej.,
  *k*-anonimato)» y que los conteos no se persisten. Calcular en cada paso
  el tamaño mínimo y la distribución de las clases de equivalencia
  (`groupby` sobre los cuasi-identificadores vigentes) da una medida que no
  depende de qué perfiles conozca el atacante, y ponerla junto a la pérdida
  de cardinalidad de H05 hace explícito el contraste riesgo–utilidad. El
  criterio de parada de la generalización pasa de «no quedan únicos frente
  a esta muestra auxiliar» a «ninguna combinación de cuasi-identificadores
  describe a menos de k clientes».
- **Anclas actuales:** H01 (roles de riesgo: cuasi-identificadores `age`,
  `city`, `occupation`), H02 (ataque de enlace ingenuo), H04
  (generalización iterativa con riesgo residual por paso), H05 (costo en
  utilidad), H06 (contrato del conjunto compartible); superficies S02
  (reglas), S03 (evaluación de riesgo y utilidad), S04 (producto
  compartible), S05 (pruebas); dependencia «Habilita para P109».
- **Alternativas menores descartadas:** mencionar *k*-anonimato en markdown
  no permite al estudiante ver que una muestra auxiliar sin coincidencias
  no implica clases grandes. Sustituir el ataque de enlace por *k* perdería
  H02, que es la evidencia más intuitiva de que suprimir identificadores no
  basta; por eso *k* se añade junto al ataque.
- **Contrato de no regresión:** se conservan H01–H06, `data/`, las reglas
  finales de generalización, la clave y el formato del seudónimo, el ataque
  de enlace y su conteo por paso, y `submission/anonymized.csv` con sus 600
  filas y columnas exactas, que P109 reproduce. Las pruebas existentes no se
  eliminan. Ninguna regla se modifica para alcanzar un *k*: si el *k* final
  es bajo, se reporta y se discute, no se corrige en esta propuesta.
- **Interacciones:** ninguna dentro de P108. Fuera de P108: P109 hereda
  datos, reglas, seudónimo y contrato de prueba; como `anonymized.csv` no
  cambia, P109 no se afecta. Replicar la medida en SQL (`GROUP BY … HAVING
  COUNT(*) < k`) sería una decisión aparte.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que,
  tras cada paso de generalización, se calculan el *k* mínimo, el número de
  clases y el número de registros en clases de tamaño 1 sobre los
  cuasi-identificadores vigentes, junto al conteo de reidentificaciones del
  ataque de enlace existente, y se interpreta en markdown la diferencia
  entre ambas medidas y su relación con la utilidad de H05. Debe estar
  respaldado por el notebook, `submission/risk_by_step.csv` y una prueba
  que recalcule el *k* final desde `anonymized.csv`. H01–H06 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P108_anonimizacion_pandas/

0. Inspecciona primero professor/notebook.ipynb, data/raw.csv,
   data/auxiliary.csv, submission/anonymized.csv y tests/test_activity.py.
   Si la implementación no coincide con
   design/courses/descriptiva/P108_activity.md (pasos 1–7, verificaciones
   por paso y columnas age_group, region, occupation_group), detente e
   informa la discrepancia sin modificar nada. Si el notebook ya calcula el
   tamaño mínimo de las clases de equivalencia, detente e informa: la
   propuesta estaría cubierta.
1. No cambies data/, las reglas de generalización, la clave ni el formato
   del seudónimo, el ataque de enlace ni submission/anonymized.csv.
2. Define una función pequeña que, dado un DataFrame y la lista de
   cuasi-identificadores vigentes, devuelva k_min, n_classes y
   records_in_singletons a partir de df.groupby(qi).size(). Úsala en lugar
   de duplicar código en cada paso.
3. Aplícala a la anonimización ingenua y después de cada paso de
   generalización existente (edad, ciudad → departamento → región,
   ocupación → grupo), junto al conteo de reidentificaciones que el
   notebook ya calcula.
4. Muestra una tabla por paso con ambas medidas y, si ayuda, la
   distribución de tamaños de clase del último paso (tabla o gráfico de
   barras mínimo). Explica en markdown (3–5 líneas): por qué cero
   reidentificaciones frente a 20 perfiles no implica clases grandes; qué
   significa el k final; y cómo se relaciona con la pérdida de
   cardinalidad de H05. Declara dos límites sin resolverlos: k no protege
   el atributo sensible annual_spend dentro de una clase, y los cuatro
   dígitos conservados de la tarjeta (H03) pueden actuar como
   cuasi-identificador adicional. No fijes un umbral de k: si el profesor
   lo aprobó en la discusión de esta T01 (registrado en P108_log.md), úsalo
   para comentar el resultado; si no, reporta el valor sin umbral.
5. Persiste submission/risk_by_step.csv con columnas step,
   quasi_identifiers, k_min, n_classes, records_in_singletons,
   linkage_unique_matches (una fila por paso, sin índice).
6. Añade a tests/test_activity.py una prueba que verifique que el archivo
   existe con esas columnas y al menos una fila por paso, y que el k_min
   de la última fila coincide con anonymized.csv.groupby(["age_group",
   "region", "occupation_group"]).size().min(). Sigue el patrón de rutas de
   las pruebas existentes. No elimines pruebas existentes.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades (en particular P109), traceability.yaml
   ni design/.
```
