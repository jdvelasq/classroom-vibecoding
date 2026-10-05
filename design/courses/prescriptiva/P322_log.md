# Log — P322

## S02.P322.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/` (`data/decision_scenarios.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, tres artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P310 y P311.
- **Trazabilidad revisada:** P322 → `prescriptiva.C01`, `C03`, `C04`, `C05`. Sustentadas; C03 sin sensibilidad.
- **Highlights:** añadidos H01–H03. H01 es el highlight obligatorio de caso y datos (estado desfavorable más probable y con pérdida grande). Valores 10.000 y 31.300 de `information_value.csv` (verificados con los datos: 0,45 × 120.000 − 0,55 × 80.000 = 10.000; 0,45 × 0,85 × 120.000 − 0,55 × 0,15 × 80.000 − 8.000 = 31.300).
- **Ambigüedades:** (1) la razón persistida de «lanzar ahora» dice que expone a «una pérdida esperada», pero su valor esperado es +10.000; la conclusión (medir antes es mejor) se sostiene por la comparación, no por esa razón; (2) decisiones y razones están escritas en el código y no dependen de los valores calculados; (3) precisión simétrica y sin valor de información perfecta; (4) el notebook presencial sólo llama a `main()`; (5) la prueba sólo verifica presencia de archivos.
- **Superficies / contrato / dependencias:** S01–S05 declaradas. Recibe de P310/P311 la práctica de escenarios con probabilidad.
- **Auditoría de Analytics:** producto terminal = política de medición con regla por resultado, guardas, autoridad y gatillos. Auditoría resuelta, con el defecto de la razón persistida.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».
