# P443 — Propuestas de mejora

**Línea base:** `P443_activity.md` (entrada S02 más reciente: `S02.P443.01`).

## T01 — Registrar en el linaje la versión de la transformación y la ejecución que produjo la tabla, y verificar su contenido con una prueba

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` p. 23 — «Audit Dimensions»: «it is helpful to create an _audit dimension_ containing the ETL processing metadata known at the time», con atributos como «the versions of ETL code used to create the fact rows or the ETL process execution time stamps», que «enable BI tools to drill down to determine which rows were created with what versions of the ETL software»; el registro de lo producido debe identificar también la lógica y la ejecución que lo produjeron (Claude, 2026-10-05). Fuente *authoritative*: respalda el principio (metadatos de proceso ligados a lo producido), no un esquema físico; no se propone construir una dimensión de auditoría.
- **Qué gana el estudiante:** pasar de «de qué datos viene esta tabla» a
  «de qué datos, con qué versión de la lógica y en qué ejecución viene», que
  es lo que permite decir si dos tablas curadas distintas difieren por los
  datos o por el código. Corrige un defecto real registrado por S02: el
  docstring promete explicar el resultado sin reconstruir la transformación,
  pero `lineage.json` «no identifica la transformación (ni función, ni
  versión de código, ni parámetros)» (límite de uso; H02; S02). Además, hoy
  ninguna prueba verifica el contenido del linaje (H03): la mejora lo vuelve
  una garantía comprobada (huella del insumo correcta, `rows` igual a las
  filas de la salida, identificador de la transformación presente y
  recalculable).
- **Materialidad frente al riesgo de identidad de S02:** fortalece la
  operación de una capacidad analítica concreta: el linaje recae sobre la
  tabla curada por fábrica, la capacidad descriptiva recurrente del curso, y
  hace explicable cada versión publicada de ese resultado (C05). No añade
  herramienta ni biblioteca: la versión de la lógica se identifica por
  contenido con `hashlib`, la misma técnica que P431 y H02 ya usan para el
  insumo. No agrava la repetición del agregado (quinta aparición): el cálculo
  no cambia; cambia la evidencia. Es la de mayor materialidad de este lote.
- **Anclas actuales:** H01 (cambio de grano máquina→fábrica), H02 (huella
  del insumo, continuidad con P431), H03 (el linaje no se prueba);
  superficies S02 (`professor/main.py`: «linaje sin identificador de
  transformación»), S03 (`submission/lineage.json`: `created_at` no
  determinista) y S04 (pruebas); dependencia «Recibe de P431».
- **Alternativas menores descartadas:** aclarar en el texto que el linaje no
  identifica la transformación ya lo hace S02 y no cambia lo que el
  estudiante produce. Registrar sólo versiones del entorno ya está cubierto
  por P412 H02 (`python_version`, `pandas_version`) y no identifica la lógica
  que produjo esta salida concreta. Delegarlo al `manifest.json` de dbt
  (P433) introduciría una herramienta en lugar de la práctica.
- **Contrato de no regresión:** se conservan H01–H03, `raw_operations.csv`
  sin cambios (su SHA-256 debe seguir coincidiendo con el de P431),
  `build_factory_totals` y `factory_totals.csv` (9303 y 9300), y las claves
  actuales de `lineage.json` con su significado. `created_at` se mantiene;
  si se normaliza a UTC, se declara como el instante de ejecución. Las
  pruebas existentes se mantienen. Se añaden claves de transformación y de
  ejecución y pruebas de contenido; no se sustituye nada.
- **Interacciones:** ninguna otra `Txx` en este archivo. Fuera de P443: el
  indicador de calidad por fila que Kimball sugiere en la misma página se
  reforzaría con una eventual propuesta de eventos de error en P441; esa
  conexión es opcional y no forma parte de esta T01. Capacidad: cambio local
  (nivel 2) sobre un `main.py` de un solo paso.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo o H02
  modificado en el que `submission/lineage.json` registra, además de la
  huella del insumo y la salida, (1) un identificador de la transformación
  calculado por contenido a partir del código que produjo la tabla, (2) un
  identificador y un instante UTC de la ejecución; y (3) pruebas que
  verifican que la huella registrada coincide con el archivo de entrada,
  que `rows` coincide con las filas de `factory_totals.csv` y que el
  identificador de la transformación coincide con el recalculado y cambia si
  cambia el código de la transformación. H01–H03 siguen presentes (H03 se
  actualiza: el linaje pasa a estar probado).

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P443_data_lineage/

0. Inspecciona primero data/raw_operations.csv, professor/main.py,
   professor/test_main.py, src/main.py, submission/ y tests/. Si la
   implementación no coincide con design/courses/productos/P443_activity.md
   (lineage.json con ruta y SHA-256 del insumo, ruta y filas de la salida y
   created_at), o si ya registra un identificador de la transformación,
   detente e informa sin modificar nada.
1. No cambies data/raw_operations.csv, build_factory_totals ni
   factory_totals.csv. Comprueba que el SHA-256 del insumo sigue siendo el
   de implementation/productos/P431_data_versioning/submission/
   data_manifest.json; si no, detente e informa.
2. En professor/main.py añade una función transformation_fingerprint() que
   calcule SHA-256 del código fuente de build_factory_totals
   (inspect.getsource) y devuélvelo junto al nombre calificado de la
   función. No inventes un número de versión semántico: la versión es la
   huella del contenido, como la del insumo (H02).
3. Amplía lineage.json, sin quitar ni renombrar claves actuales, con:
   - "transformation": {"name": "<módulo>.build_factory_totals",
     "sha256": "<huella del código>"};
   - "run": {"run_id": "<uuid4>", "executed_at_utc": "<ISO 8601 con Z>"}.
   Si created_at no está en UTC, no lo cambies; documenta en un comentario
   de decisión de 1–2 líneas que executed_at_utc es el instante auditable.
   Separa la construcción del registro en una función pura que reciba la
   ruta del insumo, la tabla, la huella de la transformación, run_id y el
   instante, para poder probarla sin depender del reloj.
4. Regenera submission/factory_totals.csv (idéntico) y
   submission/lineage.json con main().
5. Añade a professor/test_main.py pruebas que verifiquen: la huella del
   insumo registrada es el SHA-256 del archivo leído; rows es igual al
   número de filas de factory_totals.csv; transformation.sha256 es igual al
   recalculado; una función de agregación distinta (definida en la prueba)
   produce una huella distinta; executed_at_utc es un ISO 8601 en UTC. No
   compares run_id ni el instante con valores fijos. Añade a
   tests/test_activity.py una prueba que verifique que lineage.json
   entregado contiene transformation.sha256 (64 caracteres hexadecimales) y
   run.executed_at_utc, y que rows coincide con las filas del CSV entregado.
   No elimines ni modifiques pruebas existentes.
6. Ejecuta main() y todas las pruebas de la actividad sin errores.
7. No modifiques src/main.py (plantilla del estudiante), el requirements.txt
   local, otras actividades (en particular P431, P412 y P433),
   traceability.yaml ni design/.
```
