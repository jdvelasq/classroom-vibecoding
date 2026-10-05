# Log — P518

## S02.P518.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P518_github_api/` (`data/github_issues_page_1.json`, `professor/main.py`, `src/main.py`, `submission/api_ingestion_report.csv`, `submission/github_issues.parquet` sólo como binario, `tests/test_activity.py`); P513 para contraste del reporte de ingestión.
- **Trazabilidad revisada:** P518 → `data.C01`–`data.C05`; `data.C01` sin evidencia (no hay pregunta), a escalar.
- **Highlights:** añadidos H01 (falla y reintento), H02 (proyección JSON y marca de pull requests; caso y datos), H03 (llave única y reporte). No inferible: proporción de pull requests y contenido del Parquet.
- **Ambigüedades:** procedencia y fecha de captura del JSON sin documentar; `pages_requested` y `status` constantes; el reporte no se escribe en el camino de falla; no hay notebook de profesor; la prueba acepta cualquier archivo.
- **Superficies / contrato / dependencias:** S01–S07 declaradas; contrato separado entre código, `submission/`, prueba y trazabilidad; recibe práctica de P513; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; el taller se lee como ingestión de APIs (Data Engineering) sin producto ni pregunta analítica.

## S03.P518.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CCF-The Web (p. 67: «Data are frequently obtained via web applications»), PDA (p. 114: «Utility of APIs; when to look for one») y DG-Data Acquisition (p. 70: «Pull-based and push-based approaches») — ya cubierta en lo técnico (H01–H03); el vacío de pregunta analítica no se resuelve con este documento. DM-Mining Web Data (p. 81: scraping, T2) — fuera de alcance.
