# Log — P105

## S02.P105.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P105_drivers_chatgpt/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/`). Comparado con P103–P104.
- **Trazabilidad revisada:** entrada P105 → `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (*prompts* emparejados con código P103), H02 (estructura del dataset trasladada al *prompt*; highlight de caso y datos), H03 (salvaguarda «No inventes datos»). No inferibles: respuestas del asistente, verificación de resultados o producto persistido.
- **Ambigüedades:** el notebook no ejecuta nada y `submission/` está vacío; la prueba sólo exige una celda; se propone compartir `drivers.csv` completo (con `ssn` y `location`) con el asistente, en tensión con la minimización de P102; tercera repetición de la misma pregunta (P103–P105).
- **Superficies / contrato / dependencias:** S01–S05; recibe de P103; no habilita dependencias demostrables.
- **Auditoría de Analytics:** producto = especificación en lenguaje natural, no descripción. Mapeo a C02, C03 y C05 sin artefacto que lo sustente; requiere revisión. Centrada en una herramienta contribuyente.
