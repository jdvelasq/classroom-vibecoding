# Log — P431

## S02.P431.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P431_data_versioning/` (`data/raw/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/data_manifest.json`, `tests/test_activity.py`); P412, P420 y P443 para relación.
- **Trazabilidad revisada:** P431 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (identidad por contenido), H02 (capa cruda y manifiesto; caso como límite).
- **Ambigüedades:** la docstring dice «registra y verifica» pero no existe verificación; etiqueta de versión literal; no se demuestra un cambio detectado; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; habilita P443 (misma huella SHA-256).
- **Auditoría de Analytics:** riesgo moderado: práctica pertinente sin vínculo con un resultado analítico.

## S03.P431.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DI-Methods (p. 91: «Role of hash algorithms in integrity preservation»; «Data provenance assurance», p. 91) — ya cubierta al nivel que el documento pide («explain»): P431 H01 identifica la versión por contenido; P443 H02 ancla la salida a la huella del insumo; P448 H02 verifica restauración por bytes. La falta de función de verificación en P431 es un límite S02, no una señal nueva de este documento.
