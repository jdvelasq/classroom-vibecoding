# Log — P412

## S02.P412.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P412_repro_environment/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `data/daily_operations.csv`, `professor/main.py`, `src/main.py`, `submission/environment_report.json`, `tests/test_activity.py`, `tests/test_environment_report.py`); `structure-audit.md`; P400 para comparación.
- **Trazabilidad revisada:** P412 → `productos.C02`, `productos.C05`. C05 débil.
- **Highlights:** añadidos H01 (ambiente aislado), H02 (procedencia de ejecución), H03 (prueba de regresión), H04 (caso y datos: indicador fijo de referencia y contrato de salida inestable).
- **Ambigüedades:** `requirements.txt` local no registrado como excepción en `structure-audit.md` y compatibilidad con la raíz no verificable; Python 3.9.6 en la evidencia sin versión de referencia del repositorio; docstrings descriptivos frente a la regla de claridad de `AGENTS.md`; columna `total_units_produced` frente a `total_units` de P400; la prueba sobrescribe `submission/`.
- **Superficies / contrato / dependencias:** S01–S07; recibe de P400; habilita P413–P414.
- **Auditoría de Analytics:** resuelta con reservas: reproducibilidad de un indicador real del curso, pero trivial.
