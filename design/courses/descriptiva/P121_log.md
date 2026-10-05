# Log — P121

## S02.P121.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P121_vuelos/` (dos agregados `.csv.gz` en `data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con `questions.json` y seis CSV, `tests/`); P120 como comparación inmediata.
- **Trazabilidad revisada:** P121 → `descriptiva.C01`, `C02`, `C03`; coherente con la evidencia.
- **Highlights añadidos:** H01–H07 (agregados aditivos, conciliación, denominadores, matriz día × hora, segmentos con umbral, serie vs estacionalidad, persistencia verificada). Highlight obligatorio de caso y datos: H01, reforzado por H04 (orientación filas = día, columnas = hora).
- **Cambios realizados:** creación de `P121_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** origen, período completo y transformación de los agregados no documentados (el notebook sólo los llama «reales»); la vista estacional agrupa tres años; el umbral de 25.000 vuelos no tiene justificación persistida; las pruebas no verifican `questions.json`; posible duplicación de secuencia con P120 y P122 (matriz + top N con umbral).
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; dependencia demostrable de P120; salida hacia actividades posteriores no evidenciada como artefacto.
- **Auditoría de Analytics:** diagnóstico descriptivo de concentración de demoras; disciplinas al servicio del producto. Sin declaración explícita de límite causal pese a la pregunta de «reducir».
