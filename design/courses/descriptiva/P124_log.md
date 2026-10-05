# Log — P124

## S02.P124.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P124_marketing_dashboard/` (`data/campaign_data.csv`, `professor/main.py`, `professor/app.py`, `src/main.py`, `submission/` con cinco archivos, `tests/`); P102, P120 y P121 como comparación; P154 sólo para descartar dependencia de artefacto.
- **Trazabilidad revisada:** P124 → `descriptiva.C01`, `C02`, `C03`, `C05`; coherente, con C05 apoyada en la advertencia de datos no operativos.
- **Highlights añadidos:** H01–H05 (grano diario, validación, razones por alcance, separación funciones/interfaz, persistencia verificada). Highlight obligatorio de caso y datos: H01.
- **Cambios realizados:** creación de `P124_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** origen de los datos no documentado (sólo la advertencia de la interfaz); el grano diario se infiere de conteos, no se declara; el comentario de `app.py` remite a `src/app.py`, inexistente, y `src/main.py` sólo lanza `NotImplementedError`, por lo que el recorrido del estudiante no es claro; sin notebook; «utilidad bruta» limitada a ingreso − inversión; `campaign_summary.csv` sin pregunta asociada; el tablero filtrado no tiene evidencia persistida ni pruebas; carpeta `.pytest_cache/` presente en la actividad.
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; dependencias demostrables de P102, P120 y P121 (prácticas); salida no evidenciada.
- **Auditoría de Analytics:** vista descriptiva de desempeño con razones recalculadas por alcance; Streamlit al servicio del producto. Auditoría con reserva por baja profundidad diagnóstica y ausencia de usuario o decisión.
