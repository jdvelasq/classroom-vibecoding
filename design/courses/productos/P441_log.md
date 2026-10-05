# Log — P441

## S02.P441.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P441_data_quarantine/` (`data/records.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/quarantine.json`, `tests/test_activity.py`); P402 y P440 para relación.
- **Trazabilidad revisada:** P441 → `productos.C02`, `productos.C03`, `productos.C05`; C02 débil.
- **Highlights:** añadidos H01 (cuarentena con motivo), H02 (caso como límite).
- **Ambigüedades:** una sola regla; válidos y cuarentena en el mismo archivo; sin reingreso; `amount` genérico desconectado del caso de fábricas; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe práctica de P402; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): patrón genérico de data engineering.

## S03.P441.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Cleaning (p. 73: calidad como adecuación al uso; reglas FD/CFD; p. 74: «Write rules for data cleaning according to the requirement of applications») y DPSIA/DI (p. 92: «input validation, data type validation, range and constraint validation, and cross-reference validation») — ya cubierta: P402 H01–H02 convierte expectativas operativas en contrato con llave de negocio; P441 H01 separa inválidos con motivo.
