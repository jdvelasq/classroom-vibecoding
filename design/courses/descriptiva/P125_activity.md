# P125 — Salarios: brecha frente a pares internos y acceso a salarios altos

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P125_salarios/`.

### Preguntas analíticas actuales

- ¿En qué áreas debemos revisar los salarios porque los profesionales podrían ganar menos que pares comparables dentro de la empresa?
- ¿Un profesional técnico puede alcanzar los salarios más altos sin tener que convertirse en directivo?

Usa `data/salarios.csv`: 1.000 profesionales ficticios con gerencia, departamento, trayectoria (técnica o directiva), categoría, años de experiencia técnica y salario mensual en COP. El archivo lo produce `professor/generate_data.py` con semilla fija y un salario construido como base por categoría + prima directiva + prima por experiencia + ajuste por departamento + ruido. Las celdas del notebook no declaran que los datos son sintéticos. El producto es un diagnóstico agregado de brechas frente a pares, una tabla de acceso al decil salarial superior por trayectoria, alternativas de revisión y conclusiones con su límite causal.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** señalar áreas para revisión salarial y responder si la trayectoria técnica da acceso a salarios altos; el notebook supone una conversación gerencial posterior, sin usuario concreto evidenciado.
- **Producto terminal:** `department_pay_gap.csv`, `high_salary_by_career.csv`, `compensation_recommendations.csv` y `analysis_conclusions.csv` con columna `límite`.
- **Uso y límite:** permite priorizar áreas como señal de revisión; declara que la brecha no identifica su causa y que la relación trayectoria–salario no prueba causalidad. Las «alternativas» son textos fijos de revisión, no una política de compensación.
- **Disciplinas contribuyentes:** estadística descriptiva robusta (medianas, percentiles), agregación con pandas y visualización Plotly sirven al diagnóstico.

### Highlights de contribución

- **H01 — Trabaja sobre una población sintética de mecanismo conocido:** `generate_data.py` fija la semilla 20260925 y codifica ajustes por departamento (Tesorería −700.000 y Clientes menores −950.000 COP, los dos más negativos) y una prima directiva de 1.800.000 COP. La particularidad del caso es doble: el tema (salarios) es sensible y el resultado descriptivo puede contrastarse con el mecanismo generador. El notebook no hace ese contraste; las áreas priorizadas coinciden con los dos ajustes más negativos. Sin este hito, la evidencia se leería como hallazgo sobre una empresa real.
- **H02 — Define pares comparables antes de comparar áreas:** agrupa experiencia en bandas (0–4, 5–9, 10–14, 15+), define pares como categoría × trayectoria × banda y calcula la brecha individual frente a la mediana de su grupo con `transform`. Extiende la comparación contra la media del propio conductor de P103/P104 a una referencia de pares de toda la empresa; sin este hito, las diferencias entre departamentos mezclarían composición de categorías y experiencia con brecha.
- **H03 — Prefiere mediana y percentiles a un único promedio:** resume cada trayectoria con mediana, percentil 10 y percentil 90, y la acompaña de un diagrama de caja; la brecha por departamento es la mediana de las brechas individuales. Primera vez en el rango que la elección de estadístico se justifica explícitamente («la mediana y el rango importan más que un único promedio»).
- **H04 — Exige tamaño mínimo y doble criterio para señalar un área:** sólo departamentos con al menos 30 profesionales; se señalan los de brecha mediana ≤ −5 % y al menos la mitad de sus profesionales 5 % o más por debajo. Persistido: Tesorería (−7,42 %; 0,662) y Clientes menores (−7,11 %; 0,677). Extiende el umbral de volumen de P120–P122 con un criterio de dispersión; sin él, una mediana podría ocultar que pocos casos explican la brecha.
- **H05 — Responde acceso a salarios altos con el decil superior por trayectoria:** fija el umbral en el percentil 90 de toda la empresa y persiste conteo y proporción por trayectoria: Directiva 55 de 205 (0,268), Técnica 45 de 795 (0,057). La conclusión responde «No» a que la dirección sea la única vía. Sin este hito, la pregunta se respondería comparando medianas, que no muestran acceso a la cola alta; el límite es que demuestra posibilidad, no igualdad de acceso.
- **H06 — Escribe el límite causal junto a cada respuesta:** `analysis_conclusions.csv` tiene columnas `pregunta`, `respuesta` y `límite`, y la prueba `test_06` exige que el límite contenga «no identifica su causa» o «no prueba que … cause». Única actividad del rango donde el límite asociación/causalidad (C04) queda persistido y verificado; sin este hito, el diagnóstico se podría leer como explicación.
- **H07 — Persiste sólo agregados y formula alternativas sin divulgar salarios individuales:** las brechas individuales no se guardan; los departamentos persistidos tienen al menos 30 personas; la tercera alternativa exige «conversación de retención sin divulgar salarios individuales». Retoma, sin artefacto compartido, la preocupación de divulgación de P108/P109; sin este hito, el producto expondría datos individuales sensibles.

### Inventario técnico de implementación

- **Introduce:** generador sintético reproducible; bandas con `pd.cut`; grupos de pares y brecha relativa con `transform("median")`; percentiles por grupo; criterio doble de señalamiento; decil superior como umbral; tabla de conclusiones con columna de límite; prueba que verifica texto de límite y contenido exacto de `questions.json`.
- **Extiende:** comparación contra referencia de grupo (P103/P104); umbral de volumen (P120–P122).
- **Reutiliza:** `groupby().agg()`, `query`, Plotly (`box`, `bar` con línea en cero), persistencia en `submission/`.
- **Aplica en nuevo caso:** diagnóstico de brechas a compensación, dominio sensible.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Datos sintéticos de mecanismo conocido | H01 | Generador con semilla y ajustes por departamento | No representa una empresa real; contraste con el generador no realizado. |
| Pares comparables | H02 | Categoría × trayectoria × banda; brecha vs mediana | La mediana de pares incluye al propio individuo; tamaño de celdas no verificado. |
| Estadísticos robustos | H03 | Mediana, P10, P90, caja | Descriptivo, sin intervalos. |
| Señalamiento con criterios | H04 | ≥30 personas; −5 % y ≥50 % | Umbrales fijos de decisión. |
| Cola salarial | H05 | Decil superior por trayectoria | Posibilidad, no igualdad de acceso. |
| Límite causal persistido | H06 | Columna `límite`; `test_06` | La prueba verifica texto, no razonamiento. |
| Divulgación | H07 | Sólo agregados; alternativa sin divulgación | Sin control formal de riesgo de reidentificación. |

### Relación técnica con actividades anteriores

P125 cambia el producto respecto de P120–P124: además de describir, compara frente a una referencia construida (pares) y persiste la frontera entre señal y causa. Extiende la comparación contra la referencia de grupo de P103/P104 y los umbrales de P120–P122. Es la única actividad del rango con datos sintéticos explícitos en código y la única cuyas pruebas verifican el contenido de `questions.json` y un límite interpretativo. No se observa duplicación con P120–P124. El paso «se proponen alternativas» acerca el taller a una recomendación, pero las alternativas son textos fijos sin restricciones, autoridad ni seguimiento.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Población sintética | S01 | `implementation/descriptiva/P125_salarios/professor/generate_data.py`: `RANDOM_SEED`, `DEPARTMENT_ADJUSTMENTS`, `management_premium`; `implementation/descriptiva/P125_salarios/submission/analysis_conclusions.csv` | La coincidencia con el generador es observable por comparación, no declarada en el notebook. |
| H02 — Pares comparables | S02 | `implementation/descriptiva/P125_salarios/professor/notebook.ipynb`: `banda_experiencia`, `peer_columns`, `brecha_vs_pares_pct` | No se reporta el tamaño de cada grupo de pares. |
| H03 — Estadísticos robustos | S02, S03 | notebook: `salary_distribution`, `px.box`; agregación `brecha_mediana_vs_pares_pct` | `salary_distribution` y la figura no se persisten. |
| H04 — Señalamiento | S03 | notebook: `minimum_group_size = 30`, `areas_a_revisar`; `implementation/descriptiva/P125_salarios/submission/department_pay_gap.csv` | Criterios −5 % y 50 % sin justificación persistida. |
| H05 — Decil superior | S03, S04 | notebook: `high_salary_threshold`, `career_path_summary`; `implementation/descriptiva/P125_salarios/submission/high_salary_by_career.csv` | `technical_high_salary` (dónde están los técnicos del decil) se calcula pero no se persiste. |
| H06 — Límite causal | S04, S05 | `implementation/descriptiva/P125_salarios/submission/analysis_conclusions.csv`; `implementation/descriptiva/P125_salarios/tests/test_activity.py`: `test_06` | La prueba busca una expresión, no evalúa la calidad del argumento. |
| H07 — Agregados y no divulgación | S04, S05 | notebook: celda de guardado «sin exponer información individual»; `implementation/descriptiva/P125_salarios/submission/compensation_recommendations.csv`; `test_04` | No hay evaluación formal de riesgo de reidentificación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético y generador | `data/salarios.csv`; `professor/generate_data.py` | Mecanismo conocido; carácter sintético no declarado en el notebook. |
| S02 | Definición de pares y brecha | Notebook: bandas, `peer_columns`, `transform("median")` | Mediana incluye al individuo; bandas fijas. |
| S03 | Criterios de señalamiento y cola salarial | Notebook: `department_gap`, `areas_a_revisar`, `career_path_summary`; figuras | Umbrales 30, −5 %, 50 % y P90 fijos. |
| S04 | Producto: conclusiones y alternativas | `submission/analysis_conclusions.csv`; `submission/compensation_recommendations.csv`; `submission/high_salary_by_career.csv`; `submission/department_pay_gap.csv` | Alternativas de texto fijo; no es política. |
| S05 | Pruebas | `tests/test_activity.py` | Recomputan tablas; verifican preguntas exactas y texto de límite. |

### Contrato de evidencia actual

- **Notebook o código:** verifica unidad y utilizabilidad, construye pares y brechas, señala áreas con doble criterio, mide acceso al decil superior y redacta conclusiones con límite causal.
- **`submission/`:** `questions.json`, `department_pay_gap.csv`, `compensation_recommendations.csv`, `high_salary_by_career.csv`, `analysis_conclusions.csv`.
- **Pruebas:** conjunto exacto de archivos; contenido exacto de las preguntas; recomputación de brecha por departamento y de la tabla por trayectoria; conjunto de departamentos señalados y frases clave de las alternativas; estructura de conclusiones y presencia del límite causal.
- **Trazabilidad:** P125 mapea `descriptiva.C01`–`C05`.

### Dependencias en la secuencia

- **Recibe de P103/P104:** comparación de cada registro contra una referencia de su grupo (`transform`); de P120–P122, tamaño mínimo antes de comparar y contrato `questions.json`; de P108/P109, la preocupación por no divulgar datos individuales, sin artefacto compartido.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P125 está mapeada a `descriptiva.C01`, `C02`, `C03`, `C04` y `C05` en `implementation/descriptiva/traceability.yaml`; la evidencia sostiene las cinco. C04 tiene aquí su única evidencia persistida y probada del rango P120–P125 (columna `límite` y `test_06`); C05 se apoya en productos sólo agregados y alternativas sin divulgación. El producto de Analytics es un diagnóstico de brechas internas con su frontera causal explícita; estadística descriptiva y pandas lo sirven. Tensiones a registrar: el notebook afirma que la brecha no prueba causa mientras el generador la produce por construcción, sin que el taller use ese contraste; y las alternativas de revisión rozan lo prescriptivo sin asumir sus exigencias.
