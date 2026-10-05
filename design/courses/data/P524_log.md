# Log — P524

## S02.P524.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P524_seleccion_formato_datos/` (`data/flights.csv`, `data/flights.json`, `data/flights.csv.gz` y `data/flights.parquet` como binarios, `data/sales.*`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/format_comparison.csv`, `tests/test_activity.py`); P513, P518 y P522 para contraste.
- **Trazabilidad revisada:** P524 → `data.C02`–`data.C05`; C03 débil.
- **Highlights:** añadidos H01 (mismas filas), H02 (costo de representación de un registro ancho con nulos; caso y datos), H03 (tabla de decisión).
- **Ambigüedades:** propiedades booleanas constantes; comparación mezcla formato y compresión y omite el CSV comprimido de entrada; JSON fuera del `assert`; el notebook escribe sus salidas en `data/`; `sales.csv/json/parquet` sin uso y sin procedencia; procedencia de vuelos no documentada.
- **Superficies / contrato / dependencias:** S01–S05; recibe: ninguna demostrable; habilita P525 sólo como práctica.
- **Auditoría de Analytics:** riesgo moderado; formatos sin uso analítico, vinculados a la estructura de los datos.

## S03.P524.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CCF-File Systems (p. 66: «Compare and contrast different approaches to file organization») y DG-Data Reduction and Compression (p. 72: «Select data compression techniques according to the computation, communication and storage requirements», T2) — ya cubierta: tabla de decisión de formato (H03) sobre las mismas filas (H01).

## S03.P524.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.7 las 4 V (p. 14) — marginal: concepto de reconocimiento; no justifica reforzar el bloque de procesamiento cuya identidad ya está en duda.

## S03.P524.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P524.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco autorizado de la NASEM para la formación de pregrado en ciencia de datos. Define la «data acumen» y diez áreas conceptuales (entre ellas gestión y curaduría de datos, flujo de trabajo y reproducibilidad, ética) y pide que la ética atraviese todo el currículo. Respalda expectativas generales, no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
