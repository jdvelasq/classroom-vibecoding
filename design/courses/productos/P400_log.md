# Log — P400

## S02.P400.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P400_code_testing_unittest/` (`data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_totals.csv`, `tests/test_activity.py`); contexto en `s05-diseno-productos.md` y `structure-audit.md`.
- **Trazabilidad revisada:** P400 → `productos.C02`, `productos.C05`. C05 sin evidencia observable.
- **Highlights:** añadidos H01 (regla aislada), H02 (prueba `unittest`), H03 (caso y datos: ausencia de particularidad como límite).
- **Ambigüedades:** la prueba de lógica vive en `professor/` y no forma parte de la evaluación; no hay `HOW_TO_RUN_ME.txt` ni notebook para el estudiante; el dato no tiene procedencia y la variable `daily_units_produced` no tiene fecha.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; la prueba de evaluación sólo verifica existencia; habilita P408 y P412–P414 por reutilización del indicador y del archivo.
- **Auditoría de Analytics:** no resuelta. El indicador es trivial y sin usuario; la actividad se lee como práctica genérica de pruebas unitarias (pregunta 5).

## S03.P400.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).
- **Señales de alcance de curso** (registradas sólo en este log):
  - DPSIA/DS y DP-Cryptography/Communication Protocols (pp. 84–89: cifrado, PKI, modelos de amenaza, árboles de ataque), DG-Data Privacy (p. 74: GDPR, HIPAA, leyes transfronterizas), PR-Intellectual Property (pp. 109–110) — fuera de alcance: ciberseguridad y derecho; no hacen operable una capacidad analítica concreta.
  - DPSIA/AS (pp. 92–94: ML para telemetría de seguridad, aprendizaje adversarial, LIME) y PR-Ethical (p. 108: sesgo en datos y algoritmos) — fuera de alcance: métodos analíticos y evaluación de modelos (Predictiva) y aplicación de dominio.
  - BDS-Cloud Computing y Software Support (pp. 60–61: diseño de centros de datos, «Concepts of auto scaling and serverless computing») — fuera de alcance: frontera explícita (no Big Data ni cloud engineering).
  - SDM-Software Design (p. 121: «Execute a basic Data (Science) Lifecycle on a simple data product»; mentalidad de ciclo de vida) y AP-User-centred design (p. 47: «Diagram the life of an interface, dashboard, or visualization including long-term use and maintenance») — ya cubierta a nivel de curso: es la pregunta organizadora de productos (C01–C05); no aporta mecanismo nuevo.
  - DG-Data Acquisition/Integration/Reduction/Transformation (pp. 70–73) — fuera de alcance: pertenecen a Fundamentos de data; el curso no vuelve a preparar datos.
