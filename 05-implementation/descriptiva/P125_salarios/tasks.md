# P125 — Propuestas de mejora

**Línea base:** `activity.md`.

## T01 — Contrastar el emparejamiento con una regresión de control por covariables

- **Estado:** pendiente de discusión
- **Tipo:** método
- **Fuentes:**
  - Auditoría `AUD.P125.01` (Claude, 2026-10-14) del curso `descriptiva`: señales C005.HAB04.
- **Qué gana el estudiante:** El estudiante estima el mismo efecto por una segunda vía (regresión con las covariables del emparejamiento) y ve si coincide con la estimación por pares, ejercitando el uso de regresión con fines de inferencia (C005.HAB04), que ningún taller del curso practica hoy.
- **Anclas actuales:** H02, H06.
- **Alternativas menores descartadas:** Reemplazar el método de pares por regresión perdería la lectura intuitiva que P125 ya logra con H02; se añade como contraste, no como sustituto.
- **Contrato de no regresión:** Se conservan H01–H07, la población sintética, los pares comparables, la comparación por mediana/percentiles y el límite causal persistido en H06; se añaden una tabla y una figura nuevas sin modificar las existentes.
- **Límite de la actividad:** Una sola sección adicional corta (un modelo, una tabla de coeficientes, una frase de contraste); no introduce un segundo caso ni alarga la sesión de forma apreciable.
- **Interacciones:** Ninguna; es la única propuesta de P125.
- **Justificación metodológica:** Contrastar dos métodos de estimación del mismo efecto (pares emparejados y regresión con covariables) es una práctica estándar de verificación de robustez en estudios observacionales.
- **Justificación técnica:** Regresión lineal del resultado salarial sobre el factor de interés, controlando por las mismas covariables usadas para emparejar, con las bibliotecas ya presentes en el entorno del curso.
- **Justificación pedagógica:** El estudiante ve que dos caminos razonables de estimación pueden coincidir o no, y que el límite causal de H06 se aplica igual a ambos: la regresión no prueba más causalidad que el emparejamiento.
- **Identidad del curso:** Refuerza RC03 y C005.HAB04 sin convertir el taller en un curso de regresión: el modelo sirve a la comparación causal ya declarada; no se evalúan supuestos de regresión en profundidad, lo que evitaría el riesgo de deslizarse hacia Estadística.
- **Criterio de aceptación:** Existe submission/regression_contrast.csv con los coeficientes de la regresión de control; una celda compara el efecto estimado por regresión con el de pares emparejados y declara si coinciden; el texto de límite causal de H06 se aplica también a esta estimación; una prueba recompute el modelo y verifique la persistencia.

### Instrucciones de ejecución

Actividad: 05-implementation/descriptiva/P125_salarios/. Inspecciona primero professor/notebook.ipynb y submission/ antes de modificar nada; si ya existe una estimación por regresión, detente e informa. No cambies H01-H07 ni los archivos ya persistidos (la población sintética, los pares comparables, los archivos de agregados). Tras la sección de pares comparables (H02), añade una regresión lineal del resultado salarial sobre el factor de interés, controlando por las mismas covariables usadas en el emparejamiento de H02; persiste los coeficientes y sus intervalos en submission/regression_contrast.csv; añade una celda que compare el efecto estimado por esta vía con el de pares emparejados y declare en 2-3 líneas si coinciden; aplica el mismo texto de límite causal de H06 a esta estimación (no prueba causalidad más allá de las covariables controladas). Añade una prueba que recompute el modelo desde los datos y verifique la persistencia y las columnas de submission/regression_contrast.csv. Ejecuta el notebook completo y las pruebas sin errores. No modifiques otras actividades ni traceability.yaml.
