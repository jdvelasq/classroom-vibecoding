# Log — P526

## S02.P526.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P526_eventos/` (`data/events.csv.gz` como binario, `professor/main.py`, `src/main.py`, `submission/event_replay.csv`, `submission/session_conversion.csv`, `submission/event_summary.csv`, `tests/test_activity.py`); P519–P522 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P526 → `data.C01`–`data.C05`; coherente.
- **Highlights:** añadidos H01 (tiempo de evento vs. llegada; caso y datos), H02 (desorden simulado determinista), H03 (conversión e ingreso por sesión).
- **Ambigüedades:** tardanza construida (28 = 14 bloques × 2); métricas por sesión invariantes al orden, por lo que no se muestra la confusión que la pregunta menciona; tasa 0.5 sobre 16 sesiones sin criterio de muestra; `revenue > 0` como conversión; identificadores de usuario copiados a `submission/` sin restricción documentada; procedencia sólo en `case-selection.md`; sin notebook de profesor.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P519–P520 y P522; habilita: no evidenciada.
- **Auditoría de Analytics:** producto analítico claro (métrica de conversión); procesamiento de eventos como habilitador; la amenaza analítica no se demuestra.
