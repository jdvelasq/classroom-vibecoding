# predictiva — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Árboles y ensambles para predicción tabular

- **Fuentes:**
  - `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md`
    p. 8 — «Regression Trees, Random Forest, Boosted Trees» dentro de «Modern
    Regression with High-Dimensional Data» (Claude, 2026-10-04). Es una sola
    fuente de familia *institutional*: ilustra una práctica, no la impone.
    Conviene corroborarla con fuentes *authoritative* al revisarlas.
- **Contribución distinta:** ninguna de P200–P225 usa árboles de decisión ni
  ensambles. Las familias actuales son lineales y logísticas (con términos
  derivados y regularización), MLP, modelos temporales, Markov, reglas y
  vecinos. Un árbol introduce un mecanismo distinto: partir el espacio de
  entradas con reglas, capturar interacciones sin especificarlas a mano (en
  P200 y P204 se escriben a mano), controlar el sobreajuste con profundidad y
  número de árboles, distinguir *bagging* (Random Forest) de *boosting* y leer
  la importancia de variables con sus limitaciones. Incrustarlo en P200
  añadiría otra fila de MSE a un taller que ya tiene diez highlights y es la
  puerta de entrada del curso, sin enseñar el mecanismo.
- **Posición propuesta:** después de P205, al cierre del bloque supervisado
  básico (P200–P205). Recibe de P200 y P204 el contrato de partición,
  preprocesamiento, comparación sobre la misma partición y métricas (MSE;
  AUC/exactitud). Habilita para P219 (búsqueda de hiperparámetros, como
  profundidad o número de árboles) y para P221–P223 (contraste entre
  importancia de variables, selección explícita y contracción de
  coeficientes). Alternativa: ubicarla en el bloque P219–P223, que no
  desplaza el núcleo pero la deja fuera del alcance de grupos lentos.
- **Efecto en la secuencia:** insertarla después de P205 desplaza una
  posición todas las actividades siguientes. Un grupo que hoy llega hasta
  la última actividad dejaría de ver P225. P224 y P225 son justamente las dos
  actividades cuya identidad Predictiva está sin resolver en S02.
- **Caso y datos:** requiere definición. Opción de menor riesgo: reutilizar
  un caso ya conocido (Auto MPG de P200 para regresión, o el caso binario
  educativo de P204) para comparar los árboles con resultados que el
  estudiante ya obtuvo. Un caso nuevo debe documentar su procedencia.
- **Producto de Analytics:** predicción tabular comparada contra los modelos
  previos del mismo caso sobre la misma partición, con una lectura prudente
  de la importancia de variables (no causal). El límite debe quedar explícito:
  más exactitud no implica mejor producto si se pierde interpretabilidad o
  estabilidad.
- **Criterio de aceptación de una primera versión:** un notebook que ajusta un
  árbol, un Random Forest y un modelo de *boosting* sobre el caso elegido;
  muestra el sobreajuste al crecer la profundidad; compara contra la línea
  base previa del mismo caso; persiste métricas e importancias en
  `submission/`; incluye pruebas y entrada en `traceability.yaml`; y su
  `Pxxx_activity.md` (S02) evidencia highlights propios, no duplicados de
  P200, P204 ni P219.
