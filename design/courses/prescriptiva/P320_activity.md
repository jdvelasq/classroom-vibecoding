# P320 — Equidad y responsabilidad prescriptiva: auditar una política de contacto por grupo

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/`.

### Preguntas analíticas actuales

- ¿La política de contacto puede aprobarse para una campaña recurrente o debe suspenderse y corregirse por una brecha de equidad?

`data/policy_impacts.csv` tiene cuatro filas: dos políticas (P0 y P1) por dos grupos (A y B), con elegibles, contactados y beneficio. No hay declaración de procedencia ni de carácter sintético, aunque la escala (100 elegibles por grupo, cifras redondas) indica un caso didáctico construido. `professor/main.py` calcula tasa de contacto y beneficio por elegible, la brecha entre grupos por política, decide aprobar o suspender y corregir según una guarda de diez puntos porcentuales, y persiste auditoría, decisiones, contrato y monitoreo. El notebook de profesor invoca esas funciones en cinco celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** aprobar, suspender o corregir una política recurrente de contacto; el contrato asigna la aprobación al «responsable de cumplimiento» y el escalamiento al «responsable de la política» y al «comité de equidad».
- **Producto terminal:** `policy_correction_decisions.csv` (P0 aprobada, P1 suspender y corregir) gobernada por `policy_contract.json`, con `equity_audit.csv` y `policy_monitoring.csv`.
- **Uso y límite:** permite mostrar que una política puede reprobarse por su distribución entre grupos aunque entregue más beneficio total. No corrige P1 (la decisión es «suspend_and_correct» sin propuesta de corrección), no discute el intercambio entre beneficio total y equidad, y la guarda sólo mide la brecha de tasa de contacto.
- **Disciplinas contribuyentes:** métricas de equidad por grupo y reglas de decisión sirven a la gobernanza de una política.

### Highlights de contribución

- **H01 — Convierte un umbral de equidad en una guarda que decide (caso y datos):** el dataset tiene grano política × grupo, de modo que la unidad de juicio es la política y no la persona; la brecha se calcula como diferencia máxima entre tasas de contacto de grupos dentro de cada política. Con `MAX_CONTACT_RATE_GAP = 0.10`, P0 (brecha 0,0) se aprueba y P1 (brecha 0,3) se suspende, según `policy_correction_decisions.csv`. Sin este hito, la equidad sería un indicador descriptivo sin consecuencia en la operación.
- **H02 — Separa beneficio y acceso como dimensiones auditadas:** `equity_audit.csv` persiste tasa de contacto y beneficio por elegible por grupo, y la brecha de beneficio (90 en P1). Los datos muestran que P1 entrega más beneficio total (21.000 frente a 18.000, por suma de filas) pero lo concentra en el grupo A; la decisión se basa sólo en la brecha de contacto. Sin este hito, la política con más beneficio agregado parecería preferible sin examen.
- **H03 — Declara autoridad de cumplimiento y escalamiento al comité:** `policy_contract.json` fija cadencia (antes de cada campaña y revisión mensual), necesidad de respuesta (antes de publicar la lista), entradas, guarda con métrica y máximo, autoridad, monitoreo (incluidos «grupos incluidos y excluidos de la auditoría») y gatillos (nuevo grupo, regla de elegibilidad o fuente de datos). Sin este hito, la auditoría no tendría quién la ejecute ni cuándo se revisa.

### Inventario técnico de implementación

- **Introduce:** auditoría de equidad por grupo (tasa de contacto, beneficio por elegible, brechas); decisión aprobar/suspender por guarda; escalamiento a un comité.
- **Reutiliza:** contrato JSON con cadencia, guardas, autoridad, monitoreo y gatillos; plan de monitoreo en CSV.
- **Aplica en nuevo caso:** política de contacto con dos grupos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Guarda de equidad | H01 | Brecha de tasa de contacto ≤ 0,10; aprobar o suspender | Una sola métrica decide. |
| Auditoría por grupo | H02 | Tasa de contacto, beneficio por elegible y brechas persistidas | Dos grupos; sin tamaño de grupo variable ni incertidumbre. |
| Gobernanza de la corrección | H03 | Autoridad de cumplimiento, comité, gatillos de nuevo grupo o fuente | No hay corrección propuesta para P1. |

### Relación técnica con actividades anteriores

La arquitectura ubica P320 como salvaguarda transversal. La implementación no audita ninguna política producida en el curso: P306 es la política de contacto con grupos más cercana, pero P320 trabaja con un dataset propio de cuatro filas y no consume artefactos de P306 ni de otra actividad. Es una aplicación nueva del contrato de política a la equidad, no una duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Guarda de equidad | S01, S02 | `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/data/policy_impacts.csv`; `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/professor/main.py`: `audit_policy_equity`, `decide_policy_correction`; `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/submission/policy_correction_decisions.csv` | Umbral fijado en el código, no derivado. |
| H02 — Beneficio y acceso | S02, S03 | `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/submission/equity_audit.csv` | El beneficio total por política no se calcula ni se discute. |
| H03 — Autoridad y escalamiento | S04 | `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/submission/policy_contract.json`; `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/submission/policy_monitoring.csv` | La prueba sólo verifica presencia de archivos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/policy_impacts.csv` | Cuatro filas; procedencia no declarada. |
| S02 | Auditoría y decisión | `professor/main.py`: funciones de auditoría y decisión | Una sola métrica en la guarda. |
| S03 | Entregables de auditoría | `submission/equity_audit.csv`; `submission/policy_correction_decisions.csv` | Sin corrección de P1. |
| S04 | Contrato y monitoreo | `submission/policy_contract.json`; `submission/policy_monitoring.csv` | — |
| S05 | Notebook presencial | `professor/notebook.ipynb`; `notebooks/notebook.ipynb` | Las celdas del notebook de profesor contienen secuencias `\n` literales: la primera celda queda como un solo comentario y la segunda no es Python válido. El notebook de estudiante está vacío. |
| S06 | Pruebas | `tests/test_activity.py` | Presencia de cuatro archivos. |

### Contrato de evidencia actual

- **Notebook o código:** `main.py` audita, decide y persiste; el notebook pretende invocar esas funciones, pero su codificación impide ejecutarlo tal como está.
- **`submission/`:** `equity_audit.csv`, `policy_correction_decisions.csv`, `policy_contract.json`, `policy_monitoring.csv`.
- **Pruebas:** `test_submission_contains_governed_policy_evidence` exige que existan los cuatro archivos. No verifica brechas, decisiones ni el contrato.
- **Trazabilidad:** P320 mapea `prescriptiva.C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** el patrón de contrato de política (cadencia, guardas, autoridad, monitoreo, gatillos) presente desde P300; no recibe artefactos.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P320 está mapeada a `prescriptiva.C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C04 se sostiene en la autoridad de cumplimiento y el escalamiento; C05 en el monitoreo y los gatillos. Frente a la arquitectura («auditoría de equidad y corrección de política», núcleo transversal), la auditoría existe pero la corrección no, y no se aplica a ninguna política del curso. El producto de Analytics es una decisión gobernada sobre una política existente; el cálculo de brechas es evidencia. Límite de implementación: el notebook presencial no es ejecutable por la codificación de sus celdas.
