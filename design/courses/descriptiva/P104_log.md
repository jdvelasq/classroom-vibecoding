# Log — P104

## S02.P104.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P104_drivers_sqlite/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/summary.csv`, `submission/top10_drivers.png`, `temp/db.sqlite`, `tests/`). Comparado con P103 en detalle.
- **Trazabilidad revisada:** entrada P104 → `descriptiva.C02`, `descriptiva.C03`.
- **Highlights añadidos:** H01 (SQL contrastado con pandas en la prueba), H02 (vistas que normalizan nombres con guion; highlight de caso y datos), H03 (función de ventana y CTE), H04 (vista `driver_summary` reutilizable).
- **Ambigüedades:** producto y gráfico casi idénticos a P103 (posible solapamiento a decidir en el curso); la vista `drivers` mantiene `ssn` y `location`; `temp/db.sqlite` está versionado.
- **Superficies / contrato / dependencias:** S01–S06; recibe todo el contrato de P103; habilita la práctica `read_sql_query` usada en P107, P109 y P150–P154, sin artefacto compartido.
- **Auditoría de Analytics:** mismo producto descriptivo que P103; la contribución es de disciplina contribuyente (bases de datos) con verificación cruzada. C02 y C03 sustentados al nivel de P103.
