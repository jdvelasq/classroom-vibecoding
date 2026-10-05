# Log — P518

## S02.P518.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P518_github_api/` (`data/github_issues_page_1.json`, `professor/main.py`, `src/main.py`, `submission/api_ingestion_report.csv`, `submission/github_issues.parquet` sólo como binario, `tests/test_activity.py`); P513 para contraste del reporte de ingestión.
- **Trazabilidad revisada:** P518 → `data.C01`–`data.C05`; `data.C01` sin evidencia (no hay pregunta), a escalar.
- **Highlights:** añadidos H01 (falla y reintento), H02 (proyección JSON y marca de pull requests; caso y datos), H03 (llave única y reporte). No inferible: proporción de pull requests y contenido del Parquet.
- **Ambigüedades:** procedencia y fecha de captura del JSON sin documentar; `pages_requested` y `status` constantes; el reporte no se escribe en el camino de falla; no hay notebook de profesor; la prueba acepta cualquier archivo.
- **Superficies / contrato / dependencias:** S01–S07 declaradas; contrato separado entre código, `submission/`, prueba y trazabilidad; recibe práctica de P513; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; el taller se lee como ingestión de APIs (Data Engineering) sin producto ni pregunta analítica.
