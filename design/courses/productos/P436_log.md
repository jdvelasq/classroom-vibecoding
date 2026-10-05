# Log — P436

## S02.P436.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P436_watermark/` (`data/events.json`, `data/watermark.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/watermark_result.json`, `tests/test_activity.py`); P430 y P437 para relación.
- **Trazabilidad revisada:** P436 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (incremental con marca de agua), H02 (tiempo como estado; caso y datos con límites).
- **Ambigüedades:** la nueva marca no se reescribe en `data/watermark.json`; comparación lexicográfica de cadenas ISO; eventos sin contenido analítico; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; sin dependencias demostrables.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): patrón genérico sin capacidad analítica.
