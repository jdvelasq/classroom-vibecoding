# Log — P319

## S02.P319.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P319_catalog_assortment/` (`data/products.csv`, `professor/notebook.ipynb`, `professor/main.py`, `notebooks/notebook.ipynb` sin celdas, siete artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P305, P308, P315, P316 y P318.
- **Trazabilidad revisada:** P319 → `prescriptiva.C02`, `C03`, `C04`, `C05`. Todas sustentadas; C03 determinista.
- **Highlights:** añadidos H01–H06. H01 es el highlight obligatorio de caso y datos (atractivos que compiten por el mismo cliente bajo un logit multinomial). Cifras citadas de `capacity_sensitivity.csv`, `policy_monitoring.csv` y de `assert` del notebook (canibalización −0,743 y +1,502; brecha 0,423).
- **Ambigüedades:** (1) notebook y `professor/main.py` generan artefactos distintos; `assortment_results.csv` persistido tiene la versión de tres columnas de `main.py`, distinta de la de cinco columnas del notebook; (2) el contrato y la tabla de decisión sólo los produce `main.py`, que el notebook presencial no invoca; (3) la política dice «hasta cuatro productos» y el óptimo usa tres; (4) la comparación con reglas ingenuas y la sensibilidad a `v0` no se persisten; (5) la prueba sólo verifica presencia de tres archivos.
- **Superficies / contrato / dependencias:** S01–S07 declaradas. Recibe de P305/P308/P315 la enumeración verificada y las reglas ingenuas; contrasta con el LP de P316–P318. No habilita dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = política de surtido con guardas, aprobación humana, monitoreo con líneas base y gatillos cuantificados; el modelo de elección y la enumeración son evidencia. Auditoría resuelta, con el límite de que el contrato vive fuera del notebook.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».
