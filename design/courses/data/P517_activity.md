# P517 — Contratos de datos Vermont

## Actividad actual implementada

**Implementación:** `implementation/data/P517_vermont_contratos/`.

### Preguntas analíticas actuales

- ¿Qué cambios de un extracto tributario permiten o impiden analizar ingresos por código postal?

La pregunta abre `professor/notebook.ipynb` junto con un diagrama `lote nuevo ──► contrato ──► ACCEPT / REVIEW / REJECT ──► análisis`. Usa el mismo `data/vermont.csv` de P516 (1476 filas, 147 columnas, una fila por código postal y tramo de ingreso; sin procedencia, año ni diccionario documentados). Una función `validate` declara un contrato mínimo de seis columnas (`STATEFIPS`, `STATE`, `zipcode`, `agi_stub`, `N1`, `A00100`; el comentario subraya que no son las 147) y aplica reglas en orden, devolviendo la primera decisión: columnas faltantes, estado distinto de `VT`/50, `agi_stub` fuera de 1–6 o `N1` negativo, clave duplicada → `FAIL`/`BREAKING`/`REJECT`; total estatal presente → `REVIEW`/`SCOPE`/`FILTER_ZIPCODE_0`; en otro caso `PASS` con `COMPATIBLE` si hay columnas nuevas respecto del extracto de referencia o `NONE` si no. Los «lotes» son seis perturbaciones construidas en el notebook a partir del mismo archivo (filtrar `zipcode ≠ 0`, dejarlo intacto, eliminar `agi_stub`, `STATE="XX"`, `agi_stub=7`, añadir `source_release="2017"`); no son entregas reales. `submission/contract_report.csv` tiene seis filas; las cinco visibles en la evidencia son `ACCEPT`, `FILTER_ZIPCODE_0` y tres `REJECT`; la fila `optional_column` no es visible, y por el código debería ser `PASS`/`COMPATIBLE`/`ACCEPT`. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decisión de aceptar, revisar o rechazar un lote para un análisis por código postal; usuario no evidenciado.
- **Producto terminal:** función `validate` (en el notebook) y `submission/contract_report.csv`, tabla de decisiones por lote.
- **Uso y límite:** permite clasificar cambios de un lote según su efecto sobre el análisis previsto. Sólo reporta la primera regla violada; la eliminación de una columna no requerida se clasifica `NONE` (no se detecta como cambio); la acción `FILTER_ZIPCODE_0` se nombra pero no se aplica. Los lotes son simulados, de modo que el reporte prueba ramas del contrato, no la estabilidad real de la fuente. `source_release="2017"` es una columna inventada para el caso, no un dato de procedencia.
- **Disciplinas contribuyentes:** contratos de datos y validación de esquema (prácticas de ingeniería de datos) al servicio de proteger una pregunta analítica concreta.

### Highlights de contribución

- **H01 — Convierte el hallazgo de alcance en una acción distinta de un rechazo (caso y datos):** la presencia de totales estatales (`zipcode = 0`) no invalida el lote; produce `REVIEW`/`SCOPE`/`FILTER_ZIPCODE_0`, separado de los fallos `BREAKING`. Extiende H01 de P516, que sólo contaba esas filas. Sin este hito, la mezcla de niveles de agregación se trataría igual que un error de datos o se ignoraría.
- **H02 — Declara un contrato mínimo derivado de la pregunta e incorpora la identidad de la fuente:** seis columnas requeridas de 147 y la verificación `STATE == "VT"` y `STATEFIPS == 50`, regla que P516 no tenía. Primera vez en el curso que los requisitos de datos se derivan explícitamente de lo que el análisis necesita (C01). Sin este hito, el contrato tendería a congelar el esquema completo o a no verificar que el lote corresponde al estado esperado.
- **H03 — Clasifica cambios de esquema por su efecto sobre el análisis:** `BREAKING` (incumple el contrato), `SCOPE` (requiere filtrar), `COMPATIBLE` (columnas nuevas) o `NONE`, cada uno con una acción `REJECT`, `FILTER_ZIPCODE_0` o `ACCEPT`. Primera tipificación de cambios del curso. Sin este hito, toda diferencia de esquema sería igualmente bloqueante.
- **H04 — Ejercita cada rama del contrato con lotes perturbados y persiste las decisiones:** el diccionario `cases` construye un lote por rama y el reporte registra estado, tipo de cambio y acción. Contrasta con P516, que evalúa una sola versión del archivo. Sin este hito, el contrato no tendría evidencia de que distingue los casos que declara.

### Inventario técnico de implementación

- **Introduce:** función de validación con decisiones ordenadas; tipificación de cambios; lotes de prueba por perturbación (`drop`, `assign`, filtrado).
- **Extiende:** reglas de P516 (columnas requeridas, dominio, no negatividad, clave única, alcance) al papel de contrato de aceptación; añade identidad de estado.
- **Reutiliza:** caso y archivo de P516.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Acción por alcance | H01 | `REVIEW`/`SCOPE`/`FILTER_ZIPCODE_0` | Acción nombrada, no aplicada. |
| Contrato mínimo derivado de la pregunta | H02 | `REQUIRED` de seis columnas + identidad VT/50 | Sin tipos ni nulidad declarados. |
| Clasificación de cambios | H03 | `BREAKING`/`COMPATIBLE`/`NONE` | Columnas eliminadas no requeridas → `NONE`. |
| Lotes de prueba del contrato | H04 | `cases` + `submission/contract_report.csv` | Perturbaciones simuladas del mismo archivo. |

### Relación técnica con actividades anteriores

Mismo caso y datos que P516 con nueva exigencia de producto: de diagnosticar una versión a decidir sobre versiones futuras. Las reglas son las de P516 con una adicional; no hay duplicación porque el producto cambia (decisión por lote frente a reporte de calidad). Respecto del bloque Superstore, el reporte de estados se relaciona con los `SUCCESS` constantes de P513–P515, pero aquí el estado se deriva de reglas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Acción por alcance | S01, S02, S04 | `implementation/data/P517_vermont_contratos/professor/notebook.ipynb`: `validate` y comentario de la celda 4; `implementation/data/P517_vermont_contratos/submission/contract_report.csv` (fila `statewide_total_present`) | La interpretación de `zipcode = 0` sólo se apoya en comentarios. |
| H02 — Contrato mínimo | S02 | `implementation/data/P517_vermont_contratos/professor/notebook.ipynb`: celda 3 (`REQUIRED`, `validate`) | No se verifican tipos de las columnas requeridas. |
| H03 — Clasificación de cambios | S02, S04 | `implementation/data/P517_vermont_contratos/professor/notebook.ipynb`: `validate`; `implementation/data/P517_vermont_contratos/submission/contract_report.csv` | Fila `optional_column` no visible en la evidencia inspeccionada. |
| H04 — Lotes de prueba | S03, S04, S05 | `implementation/data/P517_vermont_contratos/professor/notebook.ipynb`: celda 4 (`cases`); `implementation/data/P517_vermont_contratos/submission/contract_report.csv`; `implementation/data/P517_vermont_contratos/tests/test_activity.py` | Sólo la primera regla violada queda registrada por lote. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: extracto tributario de Vermont | `data/vermont.csv` | Igual a P516; sin procedencia ni diccionario. |
| S02 | Validación: contrato `validate` | `professor/notebook.ipynb` | Reglas ordenadas con salida en la primera falla. |
| S03 | Evaluación: lotes perturbados | `professor/notebook.ipynb` (`cases`) | Simulados desde el mismo archivo. |
| S04 | Producto: reporte de contrato | `submission/contract_report.csv` | Sin conjunto filtrado ni `questions.json`. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia del reporte. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** define `REQUIRED` y `validate`, construye seis lotes y persiste las decisiones.
- **`submission/`:** `contract_report.csv` (6 lotes: `batch_name`, `status`, `change_type`, `action`).
- **Pruebas:** `test_01` verifica que existe el reporte; no verifica decisiones por lote.
- **Trazabilidad:** `data.C01`, `data.C03`, `data.C04`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P516:** `vermont.csv` y sus reglas de calidad, reutilizadas como condiciones del contrato.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P517 está mapeada a `data.C01`, `data.C03`, `data.C04` y `data.C05`. C01 se evidencia en el contrato mínimo derivado de la pregunta; C03 en las reglas y la clasificación de cambios; C04 en el reporte de decisiones, aunque la procedencia de la fuente sigue sin documentarse; C05 en el comentario que limita el contrato a lo que el análisis necesita. No se mapea C02, coherente con la ausencia de transformación. El producto es una regla de aceptación de datos para una pregunta concreta. Auditoría 5: los contratos de datos provienen de Data Engineering, pero aquí están subordinados a la pregunta por código postal y la decisión de alcance; el límite es que los lotes son simulados y la acción de filtrar no se materializa.
