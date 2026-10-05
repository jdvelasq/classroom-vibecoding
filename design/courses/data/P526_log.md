# Log — P526

## S02.P526.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P526_eventos/` (`data/events.csv.gz` como binario, `professor/main.py`, `src/main.py`, `submission/event_replay.csv`, `submission/session_conversion.csv`, `submission/event_summary.csv`, `tests/test_activity.py`); P519–P522 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P526 → `data.C01`–`data.C05`; coherente.
- **Highlights:** añadidos H01 (tiempo de evento vs. llegada; caso y datos), H02 (desorden simulado determinista), H03 (conversión e ingreso por sesión).
- **Ambigüedades:** tardanza construida (28 = 14 bloques × 2); métricas por sesión invariantes al orden, por lo que no se muestra la confusión que la pregunta menciona; tasa 0.5 sobre 16 sesiones sin criterio de muestra; `revenue > 0` como conversión; identificadores de usuario copiados a `submission/` sin restricción documentada; procedencia sólo en `case-selection.md`; sin notebook de profesor.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P519–P520 y P522; habilita: no evidenciada.
- **Auditoría de Analytics:** producto analítico claro (métrica de conversión); procesamiento de eventos como habilitador; la amenaza analítica no se demuestra.

## S03.P526.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - PDA-Numerical Computing (p. 119: «Allow reproducibility in data analysis with non-deterministic algorithms») — ya cubierta: simulación determinista y declarada (H02). DM-Time Series Data (p. 80, E) — fuera de alcance.

## S03.P526.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P526.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
