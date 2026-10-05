# P452 — Control de acceso: política por rol antes de entregar el reporte de riesgo

## Actividad actual implementada

**Implementación:** `implementation/productos/P452_access_control/`.

### Preguntas analíticas actuales

- ¿Qué roles pueden recibir el reporte de riesgo por fábrica y qué ocurre con un rol no autorizado?

`data/access_policy.json` asocia el recurso `factory_risk_report` a los roles `operations_manager` y `data_analyst`. `professor/main.py` define `can_access` (rol incluido en la lista del recurso; un recurso ausente equivale a lista vacía) y `get_factory_risk_report`, que lanza `PermissionError` si el rol no está autorizado y, si lo está, devuelve `{"factory_id": 2, "risk": "high"}` escrito en el código. `main()` persiste el reporte entregado a `operations_manager` en `submission/factory_risk_report.json`. El rechazo no se persiste. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** separar quién puede consumir un resultado de cómo se calcula (docstring); roles consumidores declarados en la política.
- **Producto terminal:** reporte de riesgo entregado tras una verificación de rol.
- **Uso y límite:** permite negar el reporte a roles no declarados con una política externa al cálculo. No autentica identidades (el rol se pasa como argumento), no registra accesos y el reporte no se calcula.
- **Disciplinas contribuyentes:** seguridad (autorización por rol) al servicio del uso responsable del indicador de riesgo.

### Highlights de contribución

- **H01 — Declara consumidores autorizados por recurso analítico (caso y datos):** la política nombra el recurso del producto (`factory_risk_report`) y dos roles con uso plausible del indicador; la política vive en `data/`, fuera del código que produce el reporte. Por `policy.get(resource, [])`, un recurso no declarado niega por defecto. El reporte repite el `high` de la fábrica 2 de P430/P450, sin cálculo. Sin este hito, el acceso al producto no tendría contrato propio.
- **H02 — Rechaza explícitamente un rol no declarado:** `PermissionError` con mensaje «Rol no autorizado»; la prueba de profesor verifica la entrega a un rol declarado y el rechazo de `visitor`. No se prueba `data_analyst` ni un recurso ausente; `tests/test_activity.py` sólo exige el reporte entregado. Sin este hito, la negación sería silenciosa o inexistente.

### Inventario técnico de implementación

- **Introduce:** política de acceso por recurso y rol en JSON, con negación por defecto y `PermissionError`.
- **Extiende:** la separación entre configuración sensible y código de P427 (secretos) a la autorización de consumo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Política por recurso y rol | H01 | `factory_risk_report` → dos roles | Sin autenticación ni registro de acceso. |
| Rechazo explícito | H02 | `PermissionError` para rol no declarado | Rechazo no persistido; casos no probados. |

### Relación técnica con actividades anteriores

Extiende P427 (credencial fuera del código) de configuración a autorización de consumo. Mismo resultado de riesgo por fábrica que P430, P450 y P451. El rol `operations_manager` reaparece como `consumer` en P454; no hay dependencia de artefacto.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Política por recurso | S01, S02 | `implementation/productos/P452_access_control/data/access_policy.json`; `implementation/productos/P452_access_control/professor/main.py`: `can_access` | Reporte fijo en el código. |
| H02 — Rechazo explícito | S02, S03, S04 | `implementation/productos/P452_access_control/professor/main.py`: `get_factory_risk_report`; `implementation/productos/P452_access_control/professor/test_main.py`; `implementation/productos/P452_access_control/submission/factory_risk_report.json` | Sólo se persiste el caso autorizado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Política | `data/access_policy.json` | Un recurso; dos roles. |
| S02 | Autorización y entrega | `professor/main.py` | Rol como argumento; reporte fijo. |
| S03 | Reporte entregado | `submission/factory_risk_report.json` | Sin registro de acceso ni de rechazo. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: permitir/negar; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** verifica el rol contra la política y entrega o rechaza el reporte.
- **`submission/`:** `factory_risk_report.json` entregado a `operations_manager`.
- **Pruebas:** las de profesor verifican entrega a un rol declarado y rechazo de uno no declarado; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P427:** la práctica de mantener controles sensibles fuera del código; ningún artefacto.
- **Habilita para P454:** no evidenciada como artefacto; P454 repite el rol consumidor.

## Trazabilidad y auditoría

P452 mapea `productos.C04` («control de acceso») y `productos.C05`; C04 se sostiene. El control protege el reporte de riesgo por fábrica, que se identifica como producto aunque no se calcule aquí.
