# Log — P428

## S02.P428.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P428_schedule/` (`HOW_TO_RUN_ME.txt`, `data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `requirements.txt`, `src/main.py`, `submission/scheduled_report.json`, `tests/test_activity.py`); digests de P400, P412, P413, P417 y P418 para relación.
- **Trazabilidad revisada:** P428 → `productos.C02`, `productos.C05`. C05 débil: sólo marca de ejecución.
- **Highlights:** añadidos H01 (cálculo separado de la agenda), H02 (agenda local y límite; caso y datos como límite), H03 (marca UTC).
- **Ambigüedades:** cadencia de 10 s sin relación con la llegada de datos (extracto estático sin fecha); el reporte se sobrescribe y no deja historial; `requirements.txt` local instalado por `HOW_TO_RUN_ME.txt` no está entre las excepciones documentadas en `structure-audit.md` (sólo P426) y su compatibilidad con el manifiesto raíz no se verificó aquí; misma agregación 9303/9300 repetida en muchas actividades.
- **Superficies/contrato/dependencias:** S01–S05; pruebas no verifican la periodicidad; recibe dato y agregación de P400–P418, habilita P429 sólo por práctica.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): sin usuario, decisión ni necesidad de cadencia; se lee como formación en herramienta de agendamiento.
