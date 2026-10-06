# Log — P206

## S01.P206.01

- **Fecha:** 2026-10-06; **curso / executor:** `predictiva` / `Claude`; **estado:** inicial.
- **Origen:** incorpora N01 (`course_tasks.md`), que quedó "⚠️ PENDIENTE DE
  DECISIÓN" desde 2026-10-04. Las fuentes que sustentan la actividad (ACM,
  MIT, Berkeley, Cambridge, Warwick, literatura histórica de CART/ensambles,
  SPSS/Oracle/SAS) ya están registradas en `course_tasks.md` y no se repiten
  aquí.
- **Decisión sobre ubicación:** el profesor aprobó insertarla después de
  P205, al cierre del bloque supervisado básico, por ser estructuralmente
  anterior a P220 (hiperparámetros) y P222–P224 (selección/regularización):
  sin una segunda familia de modelo no lineal, esos talleres sólo podrían
  ilustrar búsqueda de hiperparámetros e importancia con ElasticNet. El hueco
  P206 se abrió desplazando P206–P225 a P207–P226 en un commit separado.
- **Decisión sobre caso:** el profesor eligió reutilizar Auto MPG de P200
  (regresión) en vez del caso binario de P204, por tener más variables
  numéricas y una categórica — terreno más rico para mostrar profundidad,
  importancia por permutación entre varias entradas y dependencia parcial
  que el caso de dos variables de P204.
- **Highlights fijados:** H01 (comparación con la línea base de P200:
  *gradient boosting* 5.25 y Random Forest 5.71 superan la regresión lineal
  10.02), H02 (sobreajuste de un árbol sin restricción —MSE de entrenamiento
  0.0— corregido con validación cruzada sobre profundidad, que elige
  profundidad 7), H03 (bagging frente a boosting como dos mecanismos
  distintos de combinar árboles), H04 (impureza frente a permutación, con
  discrepancia real: `Cylinders` 0.21 por impureza frente a 0.03 por
  permutación; `Model Year` sube de 0.11 a 0.25), H05 (dependencia parcial
  sin causalidad), H06 (persistencia y pruebas).
- **Decisión de diseño:** la interpretación (importancia y dependencia
  parcial) se hace sobre el Random Forest específicamente, no sobre el
  modelo de mejor MSE (*gradient boosting*), porque
  `HistGradientBoostingRegressor` no expone `feature_importances_`. Se deja
  explícito en el notebook y en H04–H05 para no sugerir que el modelo con
  mejor MSE es también el que se interpreta.
- **Implementación:** `implementation/predictiva/P206_arboles_y_ensambles/`
  — notebook del profesor, `data/auto_mpg.csv` (copia propia, mismo origen
  que P200), `submission/` (`decision_tree.pkl`, `random_forest.pkl`,
  `gradient_boosting.pkl`, `model_comparison.csv`, `feature_importances.csv`,
  `validation_curve.png`, `partial_dependence.png`) y
  `tests/test_activity.py` (4 pruebas). Notebook y pruebas se ejecutaron sin
  errores.
- **Trazabilidad:** se añadió la entrada `P206` (`predictiva.C01`–`C04`) en
  `implementation/predictiva/traceability.yaml`, igual que P200 y P204.
- **Auditoría de Analytics:** el producto es una comparación predictiva
  evaluada frente a P200, no un recorrido por algoritmos de ML; árboles,
  bagging y boosting sirven a esa comparación. Ningún resultado de
  importancia o dependencia parcial se lee como causal.
