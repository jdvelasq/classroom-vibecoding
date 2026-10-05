# Log — P109

## S02.P109.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P109_anonimizacion_sql/` (`data/raw.csv`, `data/auxiliary.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/anonymized.csv`, `temp/anonimizacion.db`, `tests/`). Comparado con P108, P107 y P104; revisado que P120–P154 no reutilizan sus datos.
- **Trazabilidad revisada:** entrada P109 → `descriptiva.C05`.
- **Highlights añadidos:** H01 (pregunta declarada), H02 (reglas en una consulta SQL), H03 (consulta de enlace con CTE), H04 (orden por `row_id` exigido por la prueba posicional; highlight de caso y datos), H05 (raíz portable).
- **Ambigüedades:** producto duplicado con P108; se pierden la demostración ingenua y el contraste de utilidad; la consulta de ataque omite perfiles sin candidatos y no se persiste; clave HMAC en el código; reglas `CASE` duplicadas entre transformación y ataque.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P108, P107 y P104; no habilita dependencias demostrables por artefacto.
- **Auditoría de Analytics:** producto = capacidad de datos compartible; C05 sustentado en su dimensión responsable. Domina la privacidad con SQL como disciplina contribuyente.
