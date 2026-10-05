# Log — P106

## S02.P106.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P106_limpieza_pandas/` (`data/ventas.csv`, `professor/main.py`, `professor/diagnostics.py`, `src/main.py`, `submission/ventas.csv`, `tests/`). Comparado con P100–P105.
- **Trazabilidad revisada:** entrada P106 → `descriptiva.C02`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (función por tipo de suciedad; highlight de caso y datos), H02 (canonización con diccionarios y diagnóstico de colisiones), H03 (fechas y regla día/mes), H04 (unidades y escalas), H05 (invariantes de dominio en la prueba).
- **Ambigüedades:** procedencia de `ventas.csv` no documentada y sin fuente limpia ni generador (no hay verdad de referencia); la regla día/mes asume `yyyy-mm-dd` cuando ambos componentes son ≤ 12; peso sin unidad se asume en kg; la prueba no ejecuta `main.py` y no cubre importes ni proveedores canónicos; `diagnostics.py` tiene sus llamadas principales comentadas.
- **Superficies / contrato / dependencias:** S01–S06; habilita P107 (mismo dato, contrato y prueba).
- **Auditoría de Analytics:** producto = capacidad de datos limpia, sin descripción posterior. C02 sustentado en la dimensión de calidad de datos; C05 débil. Domina la preparación de datos como disciplina contribuyente.
