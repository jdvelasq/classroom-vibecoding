# Log — P517

## S02.P517.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P517_vermont_contratos/` (`data/vermont.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/contract_report.csv`, `tests/test_activity.py`); P516 para relaciones; P513–P515 para contraste de estados.
- **Trazabilidad revisada:** P517 → `data.C01`, `data.C03`, `data.C04`, `data.C05`; coherente; C02 no mapeada y no ejercitada.
- **Highlights:** H01 (acción de alcance distinta de rechazo; caso y datos), H02 (contrato mínimo de seis columnas e identidad VT/50), H03 (clasificación `BREAKING`/`SCOPE`/`COMPATIBLE`/`NONE`), H04 (lotes perturbados que ejercitan cada rama).
- **Ambigüedades:** los lotes son perturbaciones simuladas del mismo archivo, no entregas reales; `source_release="2017"` es una columna inventada, no procedencia; la fila `optional_column` del reporte no es visible en la evidencia inspeccionada (el código implica `PASS`/`COMPATIBLE`/`ACCEPT`); columnas no requeridas eliminadas se clasifican `NONE`; sólo se registra la primera regla violada; `FILTER_ZIPCODE_0` no se aplica.
- **Superficies / contrato / dependencias:** S01–S06; recibe datos y reglas de P516; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** el contrato protege una pregunta analítica concreta; la práctica de Data Engineering queda subordinada. Límite: simulación y acción no materializada.
