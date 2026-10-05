# P108 — Anonimización de perfiles de clientes con pandas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P108_anonimizacion_pandas/`.

### Preguntas analíticas actuales

Las preguntas no se declaran como tales; se infieren de los comentarios del notebook del profesor:

- ¿Basta con eliminar los identificadores directos para impedir la reidentificación?
- ¿Cuántos perfiles de una fuente pública externa pueden reidentificarse de forma única tras cada paso de generalización?
- ¿Cuánto detalle analítico se pierde al generalizar edad, ubicación y ocupación?

El caso combina `data/raw.csv` (600 clientes con `name`, `document_id`, `email`, `loyalty_card_number`, `age`, `city`, `occupation`, `annual_spend`) y `data/auxiliary.csv` (20 perfiles «públicos» con nombre, edad, ciudad y ocupación). El notebook clasifica las columnas por rol de riesgo, demuestra un ataque de enlace contra una anonimización ingenua y aplica supresión, enmascaramiento, seudonimización con clave y generalización progresiva, midiendo tras cada paso los perfiles reidentificados de forma única. La procedencia no está documentada; los identificadores secuenciales y los dominios de correo `.example` indican datos construidos para la clase.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** preguntas implícitas sobre riesgo y utilidad; no se declara quién recibe el conjunto ni para qué análisis.
- **Producto terminal:** capacidad de datos: `submission/anonymized.csv`, un conjunto de 600 perfiles con seudónimo, tarjeta enmascarada, gasto anual y tres atributos generalizados.
- **Uso y límite:** permite compartir perfiles para análisis agregados por grupo de edad, región y grupo ocupacional. La verificación de riesgo se limita a un ataque de enlace con 20 perfiles auxiliares; no establece una garantía formal (p. ej., *k*-anonimato) ni evalúa otros ataques. `annual_spend` se conserva exacto y la clave HMAC está escrita en el notebook.
- **Disciplinas contribuyentes:** privacidad y protección de datos (supresión, enmascaramiento, seudonimización, generalización, ataque de enlace) y manipulación con pandas.

### Highlights de contribución

- **H01 — Clasifica las columnas por rol de riesgo (caso y datos):** el dataset está construido con tres roles distinguibles —identificadores directos (`name`, `document_id`, `email`, `loyalty_card_number`), cuasi-identificadores (`age`, `city`, `occupation`) e información sensible (`annual_spend`)— y una tabla auxiliar que comparte los cuasi-identificadores. Esa estructura determina un tratamiento distinto por columna. Extiende la minimización de P102, que sólo distinguía campos permitidos y prohibidos. Sin este hito, toda columna personal recibiría el mismo tratamiento.
- **H02 — Demuestra que suprimir identificadores directos no basta:** la «anonimización ingenua» elimina los cuatro identificadores directos y un `merge` con `auxiliary` sobre `age`, `city` y `occupation` recupera nombres asociados a registros. Primera evidencia en el curso de un riesgo que no es visible inspeccionando columnas. Sin este hito, la eliminación de columnas parecería suficiente, como en P102.
- **H03 — Aplica una técnica distinta a cada tipo de identificador:** suprime `name` y `email`; enmascara `loyalty_card_number` conservando los cuatro últimos dígitos; seudonimiza `document_id` con HMAC-SHA256 y una clave secreta (`CUST-` + 12 hexadecimales); generaliza la edad en intervalos decenales con `pd.cut(..., right=False)`. Sin este hito, se confundirían técnicas con efectos distintos sobre el enlace entre conjuntos. Límite: en las filas visibles los números de tarjeta son secuenciales, de modo que los cuatro dígitos conservados funcionan como identificador único por registro; la clave está en el código.
- **H04 — Itera la generalización midiendo el riesgo residual tras cada paso:** después de agrupar la edad, generaliza ciudad → departamento → región y ocupación → grupo; tras cada paso aplica las mismas transformaciones a la tabla auxiliar, une por los cuasi-identificadores vigentes y cuenta los nombres con un único candidato (`groupby("name").size()` reindexado con 0). Sin este hito, la generalización se aplicaría sin criterio de parada. Límite: los conteos impresos no se persisten y no son visibles en el digest.
- **H05 — Hace explícito el costo en utilidad analítica:** `utility_comparison` compara el número de valores distintos de edad, ubicación y ocupación antes y después. Primera vez que la secuencia contrasta protección contra detalle disponible para describir. Límite: la utilidad se mide sólo por cardinalidad y no se persiste.
- **H06 — Persiste un conjunto compartible con un contrato verificable:** guarda `anonymized.csv`; las pruebas exigen 600 filas, columnas exactas, ausencia de identificadores y atributos originales, patrón de máscara, formato y unicidad del seudónimo, dominios cerrados de los grupos, sin faltantes, y `annual_spend` igual al original. Sin este hito, el resultado de la anonimización no sería auditable. Límite: las pruebas no miden riesgo de reidentificación.

### Inventario técnico de implementación

- **Introduce:** ataque de enlace con `merge` sobre cuasi-identificadores, enmascaramiento con `str.zfill` y corte, seudonimización con `hmac` y `hashlib.sha256`, discretización con `pd.cut`, generalización jerárquica con diccionarios y `map`, conteo de candidatos por nombre con `reindex(..., fill_value=0)`, comparación de cardinalidades.
- **Extiende de P102:** minimización de campos hacia una clasificación por rol de riesgo.
- **Reutiliza de P103:** `groupby`, `merge`, `to_csv(index=False)`.
- **Interfaz de estudiante:** `notebooks/notebook.ipynb` vacío.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Roles de riesgo y ataque de enlace | H01, H02 | Identificadores directos / cuasi-identificadores / sensible; `merge` con tabla auxiliar | `professor/notebook.ipynb`; 20 perfiles auxiliares. |
| Técnicas diferenciadas | H03 | Supresión, máscara, HMAC-SHA256, `pd.cut` | `submission/anonymized.csv`; clave en el código. |
| Generalización con riesgo medido | H04, H05 | Jerarquías ciudad→departamento→región, ocupación→grupo; conteo de únicos; cardinalidades | Notebook; conteos no persistidos; sin garantía formal. |
| Conjunto compartible verificado | H06 | Contrato de columnas, máscaras, seudónimos y dominios | `tests/test_activity.py`; no mide riesgo. |

### Relación técnica con actividades anteriores

Nuevo dato y nueva exigencia: P102 eliminaba columnas sensibles; P108 muestra que eso no impide la reidentificación y que el riesgo depende de combinaciones de atributos y de información externa. Reutiliza `groupby` y `merge` de P103 con un uso nuevo (ataque y medición). No duplica actividades anteriores. P109 reproduce el producto final con SQLite.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Roles de riesgo | S01 | `implementation/descriptiva/P108_anonimizacion_pandas/data/raw.csv`; `implementation/descriptiva/P108_anonimizacion_pandas/data/auxiliary.csv`; `implementation/descriptiva/P108_anonimizacion_pandas/professor/notebook.ipynb`: celda de carga comentada | Procedencia no documentada. |
| H02 — Insuficiencia de la supresión | S01, S03 | `implementation/descriptiva/P108_anonimizacion_pandas/professor/notebook.ipynb`: «Anonimización ingenua» y `reidentified` | Salidas no visibles en el digest. |
| H03 — Técnicas diferenciadas | S02, S04 | `implementation/descriptiva/P108_anonimizacion_pandas/professor/notebook.ipynb`: pasos 1–4; `implementation/descriptiva/P108_anonimizacion_pandas/submission/anonymized.csv` | Clave secreta en el notebook; tarjeta con sufijo único en filas visibles. |
| H04 — Riesgo residual por paso | S02, S03 | `implementation/descriptiva/P108_anonimizacion_pandas/professor/notebook.ipynb`: celdas «Verificación» y pasos 5–7 | No se citan conteos: no están persistidos. |
| H05 — Costo en utilidad | S03 | `implementation/descriptiva/P108_anonimizacion_pandas/professor/notebook.ipynb`: paso 9, `utility_comparison` | Sólo cardinalidad; sin artefacto. |
| H06 — Contrato del conjunto compartible | S04, S05 | `implementation/descriptiva/P108_anonimizacion_pandas/submission/anonymized.csv`; `implementation/descriptiva/P108_anonimizacion_pandas/tests/test_activity.py` | Las pruebas no evalúan riesgo. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset de clientes y fuente auxiliar | `data/raw.csv`; `data/auxiliary.csv` | 600 y 20 registros; datos construidos sin procedencia documentada. |
| S02 | Reglas de anonimización | `professor/notebook.ipynb` (pasos 1–7) | Clave HMAC en el código; intervalos de edad 20–69. |
| S03 | Evaluación de riesgo y utilidad | `professor/notebook.ipynb` (verificaciones, paso 9) | Código de verificación repetido en cada paso; sin persistencia. |
| S04 | Producto compartible | `submission/anonymized.csv` | `annual_spend` exacto; cuatro dígitos de tarjeta conservados. |
| S05 | Pruebas | `tests/test_activity.py` | Contrato de forma y dominios; sin medida de riesgo. |
| S06 | Interfaz de estudiante | `notebooks/notebook.ipynb` | Vacío; sin pregunta ni instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** el notebook demuestra el ataque ingenuo, aplica los pasos 1–7 con verificación, guarda el archivo y compara utilidad.
- **`submission/`:** `anonymized.csv` (600 filas; columnas `loyalty_card_number`, `annual_spend`, `customer_id`, `age_group`, `region`, `occupation_group`).
- **Pruebas:** existencia; 600 filas y columnas exactas; `annual_spend` idéntico al original y máscara igual a los cuatro últimos dígitos; ausencia de columnas prohibidas; patrones de máscara y seudónimo; unicidad del seudónimo; dominios cerrados y sin faltantes. No verifican riesgo de reidentificación, la clave usada ni la comparación de utilidad.
- **Trazabilidad:** P108 mapea sólo `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P102:** la noción de excluir campos sensibles, aquí ampliada; **de P103:** `groupby` y `merge`.
- **Habilita para P109:** mismos datos, mismas reglas finales, mismo contrato de prueba y el mismo seudónimo (misma clave y formato).

## Trazabilidad y auditoría

P108 está mapeada a `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. La evidencia sostiene la dimensión «responsable» de C05 —preparar datos para compartir con riesgo medido y utilidad declarada—, aunque no hay comunicación a usuarios o decisores. El producto es una capacidad de datos que condiciona qué descripciones serán posibles (por grupo, no por individuo), y H05 hace visible esa relación. La actividad está dominada por una disciplina contribuyente (privacidad de datos); su vínculo con el producto descriptivo es explícito sólo en la comparación de utilidad.
