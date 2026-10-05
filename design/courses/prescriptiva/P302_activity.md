# P302 — Política desde evidencia y restricciones: cupos de tutoría con piso por grado

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/`.

### Preguntas analíticas actuales

- ¿Cómo deben asignarse 40 cupos de tutoría para maximizar la ganancia esperada sin incumplir el mínimo por grado?

`data/source.json` declara un **caso pedagógico derivado** inspirado en Project STAR (Tennessee): los cupos, valores esperados y alternativas son «parámetros hipotéticos» que «no representan estimaciones publicadas», con «uso interno restringido para el taller presencial». `data/policy_options.csv` contiene tres alternativas de reparto (filas = políticas; columnas = cupos por grado 1–3, valor esperado por cupo de cada grado, capacidad total 40 y mínimo de 8 por grado). El valor por cupo es constante dentro de cada grado (120, 160, 90), de modo que la ganancia es lineal en los cupos. El producto es una evaluación con razones de descarte, una recomendación y un contrato JSON.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** asignar cupos de tutoría antes de cada periodo académico; dueña declarada: «Dirección académica», con aprobación humana.
- **Producto terminal:** `policy_assessment.csv` (factibilidad, ganancia, estado y razón por alternativa), `policy_recommendation.csv` y `policy_contract.json` (pregunta, contexto, cadencia, plazo, autoridad, objetivo, restricciones, salvaguardas, excepción, gatillo, monitoreo, políticas descartadas y límite de datos).
- **Uso y límite:** permite justificar la elección y el descarte de cada alternativa. Los valores son hipotéticos; la «ganancia esperada de aprendizaje» no tiene unidad declarada; el gatillo usa asistencia por grado, que no está en los datos.
- **Disciplinas contribuyentes:** evaluación lineal de alternativas con pandas; no hay estimación ni optimizador.

### Highlights de contribución

- **H01 — Explica por qué se elige y por qué se descarta cada alternativa:** `explain_selection` asigna `decision_status` y `decision_reason` a todas las filas, distinguiendo «no cumple capacidad o mínimo» de «menor ganancia esperada»; el contrato lista `discarded_policies` con su razón. Extiende P300, que sólo persistía la alternativa ganadora; sin este hito, el descarte no sería auditable.
- **H02 — Muestra que un piso por grado puede quedar activo sin cambiar la elección:** las tres alternativas son factibles; la seleccionada, P1 «solo_mayor_beneficio», asigna exactamente el mínimo (8) a los grados 1 y 3 y 24 al grado 2, con ganancia 5.520 frente a 5.360 de P2 «prioridad_con_piso» y 4.930 de P0 «reparto_igualitario» (`policy_assessment.csv`). La particularidad del caso —valores por cupo constantes y parámetros hipotéticos— empuja la solución al extremo permitido por el piso. Sin este hito, el estudiante no vería que la salvaguarda define el borde de la acción aunque no descarte alternativas; el límite es que la razón «no factible» nunca se activa con estos datos.
- **H03 — Declara procedencia y límite de uso dentro del producto:** `source.json` y el campo `data_limitation` del contrato advierten que los valores no son estimaciones de Project STAR. Primera aparición en el curso de procedencia persistida junto a la política; sin este hito, la recomendación podría leerse como evidencia educativa real.
- **H04 — Formaliza el contrato como JSON estructurado:** `build_policy_contract` separa `constraints`, `safeguards`, `exception_and_human_authority`, `review_trigger` y `outcome_monitor`. Extiende el contrato tabular de P300; sin este hito, restricciones y salvaguardas permanecerían mezcladas en columnas de texto.
- **H05 — Detiene la selección cuando no hay factibles:** `select_policy` lanza `ValueError` si el subconjunto factible está vacío. Es la versión ejecutable de la excepción que P300 sólo declaraba; el límite es que ningún dato del caso la ejercita.

### Inventario técnico de implementación

- **Extiende:** evaluación → factibilidad → máximo de P300, con estado y razón por alternativa.
- **Introduce:** contrato JSON anidado; lista de políticas descartadas; `data/source.json` de procedencia.
- **Introduce:** excepción explícita en código cuando no hay alternativa factible.
- **Reutiliza:** funciones en `professor/main.py` importadas por el notebook desde `professor/`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Razón de descarte | H01 | `decision_status`/`decision_reason`; `discarded_policies` | Sólo se ejercita el descarte por valor. |
| Piso por grupo | H02, H05 | `min_slots_per_grade`; `ValueError` sin factibles | Tres alternativas fijas; ganancia lineal hipotética. |
| Procedencia en el producto | H03 | `source.json`; `data_limitation` | Caso derivado; uso restringido al taller. |
| Contrato estructurado | H04 | `policy_contract.json` | Monitoreo declarado, no ejecutado. |

### Relación técnica con actividades anteriores

Misma técnica que P300 (evaluar alternativas fijas, filtrar factibles, maximizar) con nueva exigencia de evidencia: razones de descarte, procedencia y contrato estructurado. La restricción pasa de un límite superior (capacidad/exposición) a un piso de equidad por grupo. Posible duplicación técnica con P300 que requiere decisión posterior de curso: el cambio principal está en el entregable, no en el mecanismo de decisión.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Razón de descarte | S02, S03 | `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/professor/main.py`: `explain_selection`, `build_policy_contract`; `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/submission/policy_assessment.csv` | Todas las razones persistidas son de menor ganancia. |
| H02 — Piso activo sin cambiar elección | S01, S02 | `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/data/policy_options.csv`; `submission/policy_assessment.csv` | Parámetros hipotéticos; no prueba un efecto educativo. |
| H03 — Procedencia en el producto | S01, S03 | `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/data/source.json`; `submission/policy_contract.json`: `data_limitation` | Sólo se observaron seis de las ocho líneas de `source.json`. |
| H04 — Contrato JSON | S03 | `professor/main.py`: `build_policy_contract`; `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/submission/policy_contract.json` | Gatillo basado en asistencia, variable ausente del caso. |
| H05 — Excepción sin factibles | S02 | `professor/main.py`: `select_policy` | No ejercitada por los datos ni por las pruebas. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset derivado y procedencia | `data/policy_options.csv`, `data/source.json` | Valores hipotéticos; tres alternativas; uso interno. |
| S02 | Evaluación, selección y excepción | `professor/main.py`: `evaluate_policies`, `select_policy`, `explain_selection` | Capacidad exige igualdad (`eq`), no `≤`; piso de 8. |
| S03 | Producto/contrato | `submission/policy_assessment.csv`, `policy_recommendation.csv`, `policy_contract.json` | Monitoreo y gatillo declarativos. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de tres archivos. |

### Contrato de evidencia actual

- **Notebook o código:** el notebook importa las funciones de `professor/main.py`, evalúa, selecciona, explica y escribe los tres artefactos.
- **`submission/`:** `policy_assessment.csv` (tres alternativas con estado y razón), `policy_recommendation.csv` (P1 con responsable, modo y gatillo), `policy_contract.json`.
- **Pruebas:** `test_01`–`test_03` comprueban sólo existencia; no verifican columnas, valores ni la elección.
- **Trazabilidad:** P302 mapea `prescriptiva.C01`, `C02` y `C04`.

### Dependencias en la secuencia

- **Recibe de P300:** patrón evaluar → filtrar factibles → maximizar y contrato con responsable, cadencia y gatillo.
- **Habilita para Pyyy:** el contrato JSON (`policy_contract.json`) reaparece como nombre y formato en P303, P304, P306 y actividades posteriores; no hay artefacto de datos compartido.

## Trazabilidad y auditoría

P302 está mapeada a `prescriptiva.C01`, `C02` y `C04`. C01 y C04 se sustentan (contrato, aprobación humana, escalamiento). C02 se sustenta débilmente: la «política computable» elige entre tres repartos fijos y no transforma datos observables de estudiantes o grados en acción. Frente a `activity-architecture.md` («asignación con garantía mínima y razón de descarte»), la garantía mínima existe y la razón de descarte se persiste, pero con estos datos el piso no descarta ninguna alternativa y la alternativa nombrada «prioridad_con_piso» pierde por valor. El producto de Analytics es una recomendación justificada y gobernada; no hay monitoreo ejecutado.
