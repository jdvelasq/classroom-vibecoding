# Log — P101

## S02.P101.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P101_manejo_editor/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/`); `temp/` omitido. Comparado con P100.
- **Trazabilidad revisada:** entrada P101 → `descriptiva.C05`.
- **Highlights añadidos:** H01 (funciones con responsabilidad nombrada), H02 (motor `hadoop` parametrizado), H03 (precondición `FileExistsError`), H04 (corpus fijo como oráculo de regresión; highlight de caso y datos), H05 (cierre del flujo de entrega). No inferible: cualquier práctica de manejo del editor.
- **Ambigüedades:** el nombre «manejo_editor» no corresponde a evidencia observable (no hay instrucciones, notebook ni `DESCRIPTION.md`); `src/main.py` no copia a `submission/`, pero `submission/` ya tiene artefactos versionados, de modo que la prueba podría pasar sin regenerarlos; producto y aserciones duplican P100.
- **Superficies / contrato / dependencias:** S01–S05; pruebas idénticas en contenido a P100; recibe de P100, habilita la práctica modular de P102.
- **Auditoría de Analytics:** producto = mismo conteo de P100 con código modular; destreza de ingeniería de software. Mapeo a C05 indirecto. Identidad no resuelta a nivel de actividad.

## S03.P101.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - es un cuerpo de conocimiento de computación para pregrados de ciencia de datos, con 11 áreas de conocimiento y competencias de nivel T1/T2/E. Para descriptiva aportan sobre todo AP (presentación y visualización para clientes), DG/DM-Data Preparation (calidad, integración y limpieza, EDA, enmarcar la pregunta), DPSIA (privacidad e integridad) y PR/cap. 6 (comunicar resultados interpretados y sus límites a no especialistas). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
