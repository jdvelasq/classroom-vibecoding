# P106 — Limpieza de datos con pandas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P106_limpieza_pandas/`.

### Preguntas analíticas actuales

- No hay una pregunta analítica declarada. La pregunta operativa es: ¿cómo convertir un registro de compras con formatos inconsistentes en una tabla con valores canónicos, fechas ISO y magnitudes comparables?

El caso es `data/ventas.csv`: 103 registros de compras a proveedores con encabezados irregulares (espacios, mayúsculas, BOM) y valores sucios en casi todas las columnas: razones sociales con variantes de mayúsculas, espacios y sufijos (`SA`, `S.A.`, `SAS`), país escrito de seis formas, ciudades con y sin tilde, fechas en al menos cuatro formatos, importes con `$`, `COP`, separadores de miles mixtos y sufijo `K`, descuentos como fracción, número o porcentaje, pesos en `g`, `kg` o `ton` y precios con separadores ambiguos. La procedencia no está documentada; los correos (`compras2@empresa.com`, …) y la regularidad de la suciedad indican un archivo construido para la clase, pero no hay fuente limpia ni generador en `professor/`. El producto es `submission/ventas.csv` limpio.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** capacidad de datos: una tabla de compras con nombres de columna normalizados y valores canónicos.
- **Uso y límite:** habilita agregaciones posteriores por proveedor, ciudad, fecha o importe que con el archivo original serían incorrectas. No se realiza ninguna descripción con la tabla limpia; la corrección de cada reemplazo no puede contrastarse con una fuente verdadera.
- **Disciplinas contribuyentes:** preparación y calidad de datos (expresiones regulares, diccionarios de canonización, conversión de unidades).

### Highlights de contribución

- **H01 — Asigna a cada tipo de suciedad una función de limpieza por columna (caso y datos):** el archivo no tiene un único defecto sino uno distinto por columna; `main()` aplica `clean_column_names`, `clean_supplier`, `clean_country`, `clean_city`, `clean_purchase_date_format`, `clean_amount`, `clean_discount`, `clean_weight` y `clean_unit_price`, compuestas a partir de primitivas (`strip_whitespace`, `normalize_whitespace`, `to_lowercase`, `replace_space_with_underscore`). La heterogeneidad del caso obliga a diagnosticar columna por columna antes de transformar. Primera reparación de valores del curso: P102 sólo rechazaba estructura inválida. Sin este hito, la limpieza se reduciría a un `strip()` global.
- **H02 — Canoniza entidades con diccionarios explícitos apoyados en un diagnóstico de colisiones:** `SUPPLIER_REPLACEMENTS`, `COUNTRY_REPLACEMENTS` y `CITY_REPLACEMENTS` asocian cada forma canónica con sus variantes observadas. `professor/diagnostics.py` agrupa valores por una clave normalizada (minúsculas, sin tildes, sin puntos) para mostrar las variantes que colisionan, y también los ordena por longitud; lee el archivo de salida, lo que permite revisar qué variantes quedan. Sin este hito, la canonización sería una lista de reemplazos sin método de descubrimiento. Límite: las variantes no listadas pasan sin cambio y el diagnóstico es una herramienta del profesor, sin prueba asociada.
- **H03 — Normaliza fechas con reglas de formato y una regla de desambiguación día/mes:** unifica separadores (`.` y `/` → `-`), expande años de dos dígitos (`dd-mm-yy` → `dd-mm-20yy`), reordena `dd-mm-yyyy` a `yyyy-mm-dd` y, en `yyyy_dd_mm_2_yyyy_mm_dd`, intercambia día y mes cuando el primer componente es mayor que 12. Cuando ambos son ≤ 12 la regla asume `yyyy-mm-dd`: la ambigüedad no puede resolverse con los datos. Sin este hito, las fechas parecerían limpias sólo por tener formato ISO.
- **H04 — Lleva magnitudes con unidades y escalas a una unidad común:** `clean_weight` convierte `g` y `ton` a kilogramos; `clean_discount` divide por 100 los valores mayores que 1 para expresar fracciones; `clean_amount` y `clean_unit_price` eliminan moneda, separadores y el sufijo `.00K`. Sin este hito, sumar o comparar estas columnas mezclaría escalas. Límite: un peso sin unidad (p. ej., `12`) se interpreta como kilogramos y los importes quedan como dígitos sin validación de rango.
- **H05 — Verifica invariantes de dominio del archivo limpio:** la prueba exige el orden exacto de columnas, `country == "COL"`, proveedores sin espacios extremos ni dobles, ciudades dentro de `{Bogotá, Medellín, Sopó, Tenjo}`, fechas con patrón `\d{4}-\d{2}-\d{2}`, descuentos en [0, 1] y pesos no negativos. Sin este hito, la limpieza no tendría criterio de aceptación. Límite: no verifica la canonización de proveedores, la validez calendario de las fechas ni los importes.

### Inventario técnico de implementación

- **Introduce:** métodos `.str` vectorizados (`strip`, `lower`, `replace` con y sin `regex`), grupos de captura en expresiones regulares, `Series.replace` guiado por diccionarios, `apply` con funciones que respetan `pd.isna`, conversión de unidades, renombrado de columnas a `snake_case`.
- **Introduce:** script de diagnóstico separado (`diagnostics.py`) con claves de colisión y agrupación por longitud.
- **Aplica en nuevo caso:** organización en funciones pequeñas de P101–P102.
- **Interfaz de estudiante:** `src/main.py` es un esqueleto con `NotImplementedError`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Limpieza por columna con funciones | H01, H04 | Funciones `clean_*` compuestas de primitivas `.str` | `professor/main.py`; sin fuente limpia para contrastar. |
| Canonización de entidades | H02 | Diccionarios de variantes y diagnóstico por clave de colisión | `professor/main.py`, `professor/diagnostics.py`; variantes no listadas pasan. |
| Normalización de fechas | H03 | Regex y regla día/mes > 12 | `professor/main.py`; ambigüedad residual. |
| Invariantes de calidad | H05 | Aserciones de dominio sobre `submission/ventas.csv` | `tests/test_activity.py`; no cubre importes ni proveedores canónicos. |

### Relación técnica con actividades anteriores

Nuevo dato (compras a proveedores) y nueva exigencia: reparar valores, no sólo validar estructura (P102) ni agregar datos limpios (P103–P104). Reutiliza la modularización de P101–P102. No duplica actividades anteriores. P107 resuelve el mismo problema con SQLite.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Función por tipo de suciedad | S01, S02 | `implementation/descriptiva/P106_limpieza_pandas/data/ventas.csv`; `implementation/descriptiva/P106_limpieza_pandas/professor/main.py`: `main` y funciones `clean_*` | Sólo se observa la cabecera del archivo en el digest; la variedad completa de defectos se infiere de las reglas. |
| H02 — Canonización con diagnóstico | S02, S03 | `implementation/descriptiva/P106_limpieza_pandas/professor/main.py`: diccionarios `*_REPLACEMENTS`; `implementation/descriptiva/P106_limpieza_pandas/professor/diagnostics.py` | Diagnóstico manual del profesor; sin prueba. |
| H03 — Fechas y desambiguación | S02, S05 | `implementation/descriptiva/P106_limpieza_pandas/professor/main.py`: `clean_purchase_date_format`, `yyyy_dd_mm_2_yyyy_mm_dd`; `implementation/descriptiva/P106_limpieza_pandas/tests/test_activity.py` | La prueba verifica patrón, no fecha válida ni orden día/mes. |
| H04 — Unidades y escalas | S02, S04 | `implementation/descriptiva/P106_limpieza_pandas/professor/main.py`: `clean_weight`, `clean_discount`, `clean_amount`, `clean_unit_price`; `implementation/descriptiva/P106_limpieza_pandas/submission/ventas.csv` (p. ej., `50000 g` → `50.0`; `20%` → `0.2`) | Supuesto de kilogramos para pesos sin unidad. |
| H05 — Invariantes de dominio | S05 | `implementation/descriptiva/P106_limpieza_pandas/tests/test_activity.py` | Aserciones parciales. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sucio | `data/ventas.csv` | 103 registros; sin procedencia, fuente limpia ni generador. |
| S02 | Reglas de limpieza | `professor/main.py` | Reglas específicas de las variantes observadas. |
| S03 | Diagnóstico | `professor/diagnostics.py` | Líneas de diagnóstico comentadas; lee `submission/`. |
| S04 | Producto limpio | `submission/ventas.csv` | Importes y precios como enteros; descuentos y pesos con faltantes. |
| S05 | Pruebas | `tests/test_activity.py` | Invariantes de formato y dominio. |
| S06 | Interfaz de estudiante | `src/main.py` | Esqueleto; sin instrucciones ni notebook. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe leer `data/ventas.csv`, aplicar la limpieza por columna y escribir `submission/ventas.csv`; `diagnostics.py` es apoyo exploratorio del profesor.
- **`submission/`:** `ventas.csv` (103 registros, 11 columnas en `snake_case`).
- **Pruebas:** orden de columnas, no vacío, país único, espacios en proveedor, dominio de ciudad, patrón de fecha, rango de descuento y signo de peso. No ejecutan `main.py` (a diferencia de P100–P102) ni verifican proveedores canónicos, importes, unidades ni fechas válidas.
- **Trazabilidad:** P106 mapea `descriptiva.C02` y `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P101–P102:** práctica de funciones pequeñas con `main()`.
- **Habilita para P107:** mismo `data/ventas.csv`, mismo contrato de columnas y prueba idéntica.

## Trazabilidad y auditoría

P106 está mapeada a `descriptiva.C02` y `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. C02 tiene respaldo en la dimensión de calidad de datos (diagnóstico y corrección de variantes, formatos y unidades), aunque sin exploración posterior. C05 tiene respaldo débil: el código documenta las reglas en diccionarios explícitos, pero no hay comunicación ni registro de decisiones para usuarios. El producto es una capacidad de datos que habilita descripción; aislada, la actividad corresponde a preparación de datos (disciplina contribuyente) y no responde la pregunta descriptiva del curso.
