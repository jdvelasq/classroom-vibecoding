# P516 — Calidad de datos tributarios Vermont

## Actividad actual implementada

**Implementación:** `implementation/data/P516_vermont_calidad/`.

### Preguntas analíticas actuales

- ¿Puede este extracto tributario usarse para analizar ingresos por código postal sin confundir agregados estatales?

La pregunta abre `professor/notebook.ipynb`. La fuente es `data/vermont.csv`: 1476 filas y 147 columnas con nombres codificados (`N1`, `A00100`, `MARS2`, `N02650`…), sin diccionario de variables, manifiesto, año ni procedencia documentados en la actividad. Cada fila es un par código postal × tramo de ingreso (`zipcode`, `agi_stub`); el comentario del notebook declara que `zipcode = 0` es el total estatal, de modo que el archivo mezcla dos niveles de agregación. El notebook aplica cinco reglas nombradas, cada una con una dimensión de calidad y un número de hallazgos, y persiste `submission/quality_report.csv`: columnas requeridas (0), dominio de `agi_stub` en 1–6 (0), unicidad de (`zipcode`, `agi_stub`) (0), `N1` no negativo (0) y presencia del total estatal (6 filas, `REVIEW`). El notebook no filtra ni entrega un conjunto apto; sólo diagnostica. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decisión de aptitud del extracto para un análisis por código postal; usuario no evidenciado.
- **Producto terminal:** `submission/quality_report.csv`, reporte de reglas con dimensión, hallazgos y estado.
- **Uso y límite:** permite concluir que el extracto es utilizable por código postal si se excluyen las 6 filas estatales. No permite juzgar la calidad de las otras 142 columnas ni el significado de `N1` y `A00100` (no hay diccionario). El estado se asigna con una regla que sólo puede producir `REVIEW` para la regla de alcance: cualquier otra regla con hallazgos > 0 quedaría igualmente en `PASS`.
- **Disciplinas contribuyentes:** perfilado y reglas de calidad de datos al servicio de una decisión de uso analítico.

### Highlights de contribución

- **H01 — Detecta granos mezclados en una misma tabla (caso y datos):** el extracto contiene filas por código postal y filas de total estatal (`zipcode = 0`, una por tramo), y la regla `statewide_total_requires_filter` las cuenta (6) y las marca `REVIEW` con dimensión `scope`. Primera actividad del curso en la que un problema de alcance, no un error de valores, decide si la fuente responde la pregunta. Sin este hito, una suma por código postal duplicaría el estado completo sin advertencia.
- **H02 — Expresa la calidad como reglas nombradas con dimensión y conteo:** una lista de tuplas (`rule_name`, `dimension`, `finding_count`) convertida en reporte persistente, con dimensiones `completeness`, `validity`, `uniqueness` y `scope`. Extiende los `quality_checks` textuales de P500 (`metric_contract.json`) y las aserciones de P510–P511, que detienen la ejecución, a un reporte que registra hallazgos sin abortar. Sin este hito, el curso no tendría un artefacto de calidad auditable por regla.
- **H03 — Verifica la clave compuesta y el dominio que definen la unidad de análisis:** unicidad de (`zipcode`, `agi_stub`) y `agi_stub.between(1, 6)`. La unidad de análisis no es el código postal sino su cruce con el tramo de ingreso; un análisis por código postal exige agregar los seis tramos. Sin este hito, la unidad de análisis quedaría implícita.

### Inventario técnico de implementación

- **Introduce:** reporte de calidad por regla y dimensión; regla de alcance; estado `PASS`/`REVIEW`.
- **Extiende:** verificación de unicidad de clave (P500: `Order ID + Product Name`) a una clave compuesta con dominio.
- **Aplica en nuevo caso:** datos tributarios agregados por geografía y tramo de ingreso, primer dominio público-fiscal del curso.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Regla de alcance por nivel de agregación | H01 | `zipcode.eq(0)` → 6 hallazgos `REVIEW` | Diagnostica; no filtra. |
| Reporte de calidad por dimensión | H02 | `submission/quality_report.csv` | Estado sólo sensible a la regla de alcance. |
| Clave compuesta y dominio | H03 | `duplicated()` y `between(1, 6)` | Sólo 5 de 147 columnas examinadas. |

### Relación técnica con actividades anteriores

Nuevo caso y nueva exigencia de evidencia: la calidad deja de ser una aserción que bloquea (P510, P511, P514) o una lista de texto (P500) y se convierte en un producto. No transforma datos ni repite técnicas previas; no hay duplicación con P500–P515.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Granos mezclados | S01, S02, S03 | `implementation/data/P516_vermont_calidad/data/vermont.csv`; `implementation/data/P516_vermont_calidad/professor/notebook.ipynb`: celdas 2 y 3; `implementation/data/P516_vermont_calidad/submission/quality_report.csv` | Que `zipcode = 0` sea total estatal sólo lo afirma un comentario; no hay documentación de la fuente. |
| H02 — Reglas como reporte | S02, S03, S04 | `implementation/data/P516_vermont_calidad/professor/notebook.ipynb`: celda 3; `implementation/data/P516_vermont_calidad/submission/quality_report.csv`; `implementation/data/P516_vermont_calidad/tests/test_activity.py` | Defecto en la asignación de estado. |
| H03 — Clave compuesta | S02 | `implementation/data/P516_vermont_calidad/professor/notebook.ipynb`: celda 3 | No se muestra la agregación por código postal. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: extracto tributario de Vermont | `data/vermont.csv` | Sin procedencia, año ni diccionario. |
| S02 | Validación: reglas de calidad | `professor/notebook.ipynb` | Cinco reglas sobre 5 columnas; estado sólo sensible a alcance. |
| S03 | Producto: reporte de calidad | `submission/quality_report.csv` | Sin conjunto filtrado ni `questions.json`. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia del reporte. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** carga el extracto, muestra la clave y dos medidas, evalúa cinco reglas y persiste el reporte.
- **`submission/`:** `quality_report.csv` (5 reglas; 4 `PASS`, 1 `REVIEW`).
- **Pruebas:** `test_01` verifica que existe el reporte; no verifica reglas, conteos ni estados.
- **Trazabilidad:** `data.C01`, `data.C03`, `data.C04`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna de artefacto; práctica de verificar unicidad de clave (P500) y aserciones de calidad (P510, P511).
- **Habilita para P517:** mismo `vermont.csv` y las mismas reglas (columnas requeridas, dominio de `agi_stub`, `N1` no negativo, clave única, total estatal) reutilizadas como contrato.

## Trazabilidad y auditoría

P516 está mapeada a `data.C01`, `data.C03` y `data.C04`, coherente con la evidencia: C01 en la pregunta de aptitud por código postal; C03 en las reglas y la de alcance; C04 en el reporte persistido, con la limitación de no documentar la procedencia de la propia fuente. El producto es un diagnóstico de aptitud de datos para una pregunta, alineado con el producto terminal del curso. Auditoría 5: no se lee como Data Engineering; el límite es que el diagnóstico no se traduce en un conjunto preparado.
