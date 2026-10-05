# predictiva — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Árboles y ensambles para predicción tabular

- **Fuentes:**
  - `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md`
    p. 8 — «Regression Trees, Random Forest, Boosted Trees» dentro de «Modern
    Regression with High-Dimensional Data» (Claude, 2026-10-04). Fuente
    *institutional*: ilustra una práctica; la corrobora ACM (siguiente fuente).
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 97–98 y DM-Classification — fuente *authoritative*: exige como T1 «at least one linear and one non-linear algorithm» para clasificación y regresión (con árboles de decisión como ejemplo), y «Apply at least two extensions (e.g., ensemble methods)» (bagged, boosted, random forests); T2 añade diagnosticar sesgo/varianza con «learning curves». Hoy predictiva no tiene ningún clasificador no lineal: P201, P203, P204 y P222 usan regresión logística (Claude, 2026-10-04).
  - `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` p. 1 — curso de Berkeley que introduce «machine learning tools including decision trees, neural networks and ensemble methods» (Claude, 2026-10-04).
  - `design/benchmarks-md/institutional/cambridge-business-analytics.md` pp. 7–8 — módulo «Análisis predictivo I»: «Modelo sobreajustado», «Árboles de decisión y bosques aleatorios», «Optimización de hiperparámetros», «Métodos de conjunto» e «Interpretar un análisis» (Claude, 2026-10-04).
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
