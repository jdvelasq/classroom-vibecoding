# P433 — dbt + DuckDB: modelo SQL con semilla, pruebas declaradas y grafo de dependencias

## Actividad actual implementada

**Implementación:** `implementation/productos/P433_dbt_duckdb/`.

### Preguntas analíticas actuales

- ¿Cómo se organiza la transformación de totales por fábrica como un proyecto con fuente, modelo, pruebas y documentación declarados, reconstruible con un solo comando?

El proyecto dbt (`dbt_project.yml`, materialización `table`) carga `seeds/daily_operations.csv` —el mismo extracto de cuatro filas— y construye `models/factory_totals.sql` (`sum(daily_units_produced)` por `factory_id` sobre `{{ ref('daily_operations') }}`). `models/schema.yml` describe el modelo («Total diario de unidades por fábrica») y declara pruebas `not_null` y `unique` sobre `factory_id` y `not_null` sobre `total_units_produced`. `profiles/profiles.yml` apunta a `submission/pre54.duckdb`. `HOW_TO_RUN_ME.txt` indica `dbt build --profiles-dir profiles`. Se conservan `target/` y `logs/` de una ejecución: `target/run_results.json` registra la semilla con `INSERT 4`, el modelo `OK` y las tres pruebas `pass` con `failures: 0` (dbt 1.9.6, 2026-10-01). No hay `professor/main.py` ni plantilla en `src/`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** la tabla `factory_totals` dentro de `submission/pre54.duckdb`, construida y probada por dbt.
- **Uso y límite:** hace visibles la dependencia semilla → modelo → pruebas y la reconstrucción desde cero. Las pruebas son genéricas de integridad (nulos y unicidad), no de valores ni de reglas del dominio; la descripción «total diario» no tiene respaldo en el dato, que no incluye fecha.
- **Disciplinas contribuyentes:** ingeniería analítica con dbt sobre DuckDB.

### Highlights de contribución

- **H01 — Declara la transformación como modelo con dependencia explícita:** `ref('daily_operations')` en `models/factory_totals.sql`; `target/graph_summary.json` registra la semilla como predecesora del modelo y el modelo como predecesor de tres pruebas. Extiende la consulta directa de P432 a un grafo gestionado. Sin este hito, la dependencia entre fuente y tabla analítica quedaría implícita en el código.
- **H02 — Adjunta pruebas de integridad a la tabla analítica:** `schema.yml` declara `not_null`/`unique` y `target/run_results.json` las registra como `pass`. La unicidad de `factory_id` protege el grano de la salida (una fila por fábrica). Primera aparición de pruebas de datos declarativas ejecutadas junto con la construcción; P402 validaba con pandas fuera del pipeline. Sin este hito, la tabla publicada no tendría control sobre su grano.
- **H03 — Reconstruye la capacidad con un comando y deja evidencia de ejecución:** `dbt build` carga semilla, construye y prueba; `HOW_TO_RUN_ME.txt` indica que la base puede eliminarse para reconstruirla. `run_results.json`, `manifest.json` y `logs/dbt.log` persisten la ejecución. Sin este hito, la reconstrucción repetible no tendría registro observable.
- **H04 — Caso y datos (límite):** el grano máquina–fábrica explica la prueba de unicidad sobre `factory_id`, pero el extracto de cuatro filas sin fecha ni valores problemáticos no puede hacer fallar ninguna prueba; la descripción «diario» no se respalda. La particularidad del caso queda reducida al grano; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** proyecto dbt (`dbt_project.yml`, `profiles.yml`, `seeds/`, `models/`, `schema.yml`); `ref`; pruebas genéricas `not_null`/`unique`; `dbt build`; artefactos `target/` y `logs/`.
- **Extiende:** la consulta SQL sobre DuckDB de P432.
- **Reutiliza:** `daily_operations.csv` y la agregación por fábrica.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Modelo con dependencia | H01 | `ref`, grafo semilla → modelo → pruebas | Un solo modelo. |
| Pruebas declarativas | H02 | `not_null`, `unique` con resultado `pass` | Sin pruebas de valores; ninguna puede fallar con el dato actual. |
| Reconstrucción | H03 | `dbt build`, `run_results.json`, base DuckDB | Artefactos de herramienta comprometidos con rutas locales del autor. |
| Caso | H04 | Grano máquina–fábrica | Descripción «diario» sin fecha en el dato. |

### Relación técnica con actividades anteriores

Misma pregunta y dato que P432, con nueva exigencia de evidencia (pruebas de datos y grafo de dependencias) y nueva herramienta. Frente a P402, las validaciones migran de pandas a declaraciones del proyecto. Es otra reimplementación de la suma por fábrica presente desde P400. Hay restos de una versión previa del proyecto: `target/compiled/pre54_dbt_duckdb/` y `target/run/pre54_dbt_duckdb/` duplican el proyecto `p433_dbt_duckdb`, la base se llama `pre54.duckdb` y `run_results.json` conserva rutas absolutas del equipo del autor (`/Volumes/GitHub/classroom-vibecoding/...`).

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Modelo con dependencia | S02 | `implementation/productos/P433_dbt_duckdb/models/factory_totals.sql`; `implementation/productos/P433_dbt_duckdb/target/graph_summary.json` | Grafo de un modelo. |
| H02 — Pruebas declarativas | S03, S05 | `implementation/productos/P433_dbt_duckdb/models/schema.yml`; `implementation/productos/P433_dbt_duckdb/target/run_results.json` | Integridad, no valores. |
| H03 — Reconstrucción con registro | S04, S06 | `implementation/productos/P433_dbt_duckdb/HOW_TO_RUN_ME.txt`; `implementation/productos/P433_dbt_duckdb/profiles/profiles.yml`; `implementation/productos/P433_dbt_duckdb/submission/pre54.duckdb`; `implementation/productos/P433_dbt_duckdb/target/run_results.json` | Artefactos residuales de `pre54_dbt_duckdb`. |
| H04 — Caso como límite | S01, S03 | `implementation/productos/P433_dbt_duckdb/seeds/daily_operations.csv`; `implementation/productos/P433_dbt_duckdb/models/schema.yml` | «Diario» no respaldado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Semilla | `seeds/daily_operations.csv` | Idéntica a actividades previas; `data/` vacío. |
| S02 | Modelo | `models/factory_totals.sql`; `dbt_project.yml` | Un modelo materializado como tabla. |
| S03 | Pruebas de datos | `models/schema.yml` | Tres pruebas genéricas. |
| S04 | Conexión y base | `profiles/profiles.yml`; `submission/pre54.duckdb` | Nombre heredado `pre54`. |
| S05 | Prueba de actividad | `tests/test_activity.py` | Sólo existencia de la base. |
| S06 | Artefactos de ejecución | `target/`; `logs/dbt.log` | Incluyen proyecto residual y rutas absolutas. |
| S07 | Interfaz del estudiante | `HOW_TO_RUN_ME.txt` | Sin `professor/main.py` ni plantilla `src/`; el estudiante ejecuta el proyecto ya resuelto. |

### Contrato de evidencia actual

- **Notebook o código:** proyecto dbt que carga la semilla, construye `factory_totals` y ejecuta tres pruebas.
- **`submission/`:** `pre54.duckdb` con la semilla y la tabla.
- **Pruebas:** `test_01` exige que exista `submission/pre54.duckdb`; no abre la base ni verifica la tabla. Las pruebas dbt verifican nulos y unicidad, no totales.
- **Trazabilidad:** P433 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P432:** la misma agregación SQL sobre DuckDB; de P402, la idea de validar datos (no artefactos).
- **Habilita para Pyyy:** no evidenciada; ninguna actividad posterior inspeccionada usa dbt.

## Trazabilidad y auditoría

P433 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en una transformación reconstruible con pruebas; C05 se apoya parcialmente en el grafo de dependencias y el registro de ejecución. Además, las pruebas de datos serían evidencia de `productos.C03`, que no está mapeada. Auditoría de identidad (pregunta 5): sin usuario ni decisión y con el mismo cálculo trivial, el taller se lee como formación en dbt; además, al no tener plantilla de estudiante, la participación consiste en ejecutar un proyecto resuelto. Riesgo de identidad registrado.
