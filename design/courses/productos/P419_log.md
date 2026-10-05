# Log — P419

## S02.P419.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P419_random_seed/` (`professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/sample.json`, `tests/test_activity.py`, `data/`); digest de P420.
- **Trazabilidad revisada:** P419 → `productos.C02`, `productos.C05`; ambas débiles.
- **Highlights:** añadidos H01 (semilla registrada con la muestra, generador local) y H02 (ausencia de caso registrada como límite).
- **Ambigüedades:** `data/` vacía; las etiquetas `factory-3` y `factory-4` no existen en el dataset del curso. Sin `HOW_TO_RUN_ME.txt`. La prueba no verifica sensibilidad a la semilla.
- **Superficies / contrato / dependencias:** S01–S04; recibe: ninguna; habilita P420 (práctica de semilla 123).
- **Auditoría de Analytics:** no resuelta; mecanismo de programación sin capacidad analítica.

## S03.P419.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PDA-Numerical Computing (p. 119: «Allow reproducibility in data analysis with non-deterministic algorithms») — ya cubierta: P419 H01.

## S03.P419.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P419.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
