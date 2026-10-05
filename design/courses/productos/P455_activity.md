# P455 — Retención de datos: política de 90 días con fecha de corte explícita

## Actividad actual implementada

**Implementación:** `implementation/productos/P455_data_retention/`.

### Preguntas analíticas actuales

- ¿Qué eventos deben conservarse y cuáles han vencido según una política de retención de 90 días evaluada en una fecha dada?

`data/events.json` contiene tres eventos con `event_id`, `event_date` y `value` (2026-08-15, 2026-05-20, 2026-03-01). `professor/main.py` fija `RETENTION_DAYS = 90` y `apply_retention_policy(as_of)` calcula el corte como `as_of − 90 días`, conserva los eventos con fecha mayor o igual al corte y registra los demás sólo con su id y el motivo `retention_period_expired`. `main()` evalúa con `as_of = 2026-09-01` (corte 2026-06-03): `submission/retention_result.json` conserva `evt-001` y declara vencidos `evt-002` y `evt-003`. `data/events.json` no se modifica. No se documenta qué representan los eventos ni el origen del plazo de 90 días. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** explicar y repetir una decisión de retención (docstring); responsable y fundamento del plazo no evidenciados.
- **Producto terminal:** resultado de retención con corte, eventos retenidos y vencidos con motivo.
- **Uso y límite:** permite reproducir qué se retiene en una fecha dada. No elimina ni archiva nada (la fuente queda intacta), no vincula los eventos con una capacidad del curso y el plazo es una constante sin justificación de uso o normativa.
- **Disciplinas contribuyentes:** gobierno de datos (retención) al servicio de la gestión del ciclo de vida de datos operativos.

### Highlights de contribución

- **H01 — Hace la retención función de la fecha del evento y de un corte explícito (caso y datos):** cada evento lleva su `event_date`, y la decisión depende de `as_of` pasado como parámetro, no del reloj del sistema; así la misma fecha produce la misma decisión. Los vencidos pierden `event_date` y `value` en la salida y conservan sólo id y motivo. Límite: los eventos no tienen significado declarado ni relación con el caso de fábricas. Sin este hito, la retención dependería del momento de ejecución y no podría auditarse.
- **H02 — Fija el borde del corte en una prueba:** la prueba de profesor, con `as_of = 2026-09-01`, exige que un evento del 2026-06-03 se retenga y uno del 2026-06-02 venza con su motivo. `tests/test_activity.py` sólo exige el archivo. Sin este hito, el día límite quedaría ambiguo.

### Inventario técnico de implementación

- **Introduce:** política de retención con constante de días, corte calculado con `timedelta` y motivo de vencimiento.
- **Reutiliza:** razonamiento con fechas explícitas de P436–P439 (marca de agua, llegada tardía, reproceso, frescura).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Corte reproducible | H01 | `as_of − 90 días`; vencidos con motivo | Plazo sin fundamento; fuente no se modifica. |
| Borde del corte | H02 | `>=` probado en el día límite | Prueba de estudiante sólo existencia. |

### Relación técnica con actividades anteriores

Misma familia de selección por fecha que P436 (marca de agua) y P438 (reproceso por rango), con nuevo propósito: ciclo de vida y no procesamiento. No consume eventos de esas actividades; `data/events.json` es propio. Cierra la secuencia sin relación de artefacto con el caso de fábricas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Corte reproducible | S01, S02, S03 | `implementation/productos/P455_data_retention/data/events.json`; `implementation/productos/P455_data_retention/professor/main.py`: `apply_retention_policy`; `implementation/productos/P455_data_retention/submission/retention_result.json` | Eventos sin significado declarado. |
| H02 — Borde del corte | S04 | `implementation/productos/P455_data_retention/professor/test_main.py`; `implementation/productos/P455_data_retention/tests/test_activity.py` | Verifica la regla, no la persistencia. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Eventos | `data/events.json` | Tres eventos sin contexto. |
| S02 | Política | `professor/main.py` | 90 días como constante; `as_of` fijo en `main()`. |
| S03 | Resultado entregado | `submission/retention_result.json` | Vencidos sin fecha ni valor. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: borde; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** calcula el corte, separa retenidos y vencidos con motivo y persiste el resultado.
- **`submission/`:** `retention_result.json`.
- **Pruebas:** la de profesor verifica el corte y el borde inclusivo; `test_01` verifica existencia.
- **Trazabilidad:** sólo `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P436/P438:** la práctica de seleccionar por fecha declarada; ningún artefacto.
- **Habilita para Pyyy:** no evidenciada (última actividad del curso).

## Trazabilidad y auditoría

P455 mapea únicamente `productos.C05`, que nombra «retención»; el mapeo se sostiene. Auditoría pregunta 5: los eventos no pertenecen a una capacidad analítica identificable, por lo que la actividad puede leerse como regla genérica de ciclo de vida de datos.
