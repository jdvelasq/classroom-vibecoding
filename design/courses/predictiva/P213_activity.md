# P213 — Tiempo hasta abandono

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P212_tiempo_hasta_abandono/`.

### Preguntas analíticas actuales

- ¿Cuánto tiempo es esperable que permanezca un cliente?
- ¿Cómo difiere la permanencia estimada por tipo de contrato?

Con datos de abandono de clientes de telecomunicaciones, estima curvas de
supervivencia, retención por contrato, supuestos y una visualización.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima permanencia por contrato; no identifica una intervención de retención.
- **Producto terminal:** curvas Kaplan–Meier, probabilidades a 12/24/36 meses y supuestos.
- **Uso y límite:** la muestra IBM ficticia explica censura/duración; no describe un mercado real ni prueba que contrato cause permanencia.
- **Disciplinas contribuyentes:** análisis de supervivencia sirve al pronóstico de tiempo hasta evento.

### Highlights de contribución

- **H01 — Distingue abandono de censura:** los clientes aún activos salen del riesgo sin ser eventos, preservando información de permanencia observada.
- **H02 — Estima permanencia por horizonte:** Kaplan–Meier actualiza supervivencia en meses con eventos y traduce curvas en puntos de 12, 24 y 36 meses.
- **H03 — Compara contratos sin afirmar causalidad:** grafica curvas segmentadas y persiste la tabla de retención.
- **H04 — Mantiene el límite predictivo:** elegir una oferta de retención queda fuera del producto actual.

### Inventario técnico de implementación

- **Introduce:** estimación Kaplan–Meier, conjunto en riesgo, eventos y censura.
- **Introduce:** curvas de supervivencia segmentadas y cálculo de retención a un
  horizonte.
- **Verifica y comunica:** exporta curvas, gráfico, retención y supuestos; las
  pruebas comprueban la evidencia persistente.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Censura y riesgo | H01 | Evento `Churn`, tenure y censura derecha | Muestra ficticia, no cohorte real. |
| Curvas/horizontes | H02–H03 | Kaplan–Meier por contrato y checkpoints | No causalidad ni intervención. |
| Límite de política | H04 | Supuestos y entregas | No define acción de retención. |

### Relación técnica con actividades anteriores

Extiende los pronósticos puntuales de P211–P212 hacia tiempo hasta evento e
incorpora censura. Sin P213 se pierde la distinción entre predecir una etiqueta
y estimar permanencia durante un horizonte.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook; `telco_customer_churn.csv.gz` | Fuente IBM/ficticia. |
| H02 | S02 | Notebook; `survival_curves.csv`; `retention_by_contract.csv` | No produce predicción individual. |
| H03 | S03 | PNG y CSV de `submission/` | Contrato no es causa. |
| H04 | S04 | `model_assumptions.json`; pruebas | No implementa una política. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Muestra/evento/censura | Datos; notebook | No es mercado real. |
| S02 | Curvas y horizontes | Notebook; CSV | Censura debe conservarse. |
| S03 | Evidencia visual | PNG/CSV | Sin causalidad. |
| S04 | Producto/límite | Supuestos; pruebas | Sin intervención. |

### Contrato de evidencia actual

- **Código:** calcula eventos, censura, curvas y checkpoints por contrato.
- **`submission/`:** conserva curvas, retención, gráfico y supuestos.
- **Pruebas:** exigen esos artefactos, no sus valores.
- **Trazabilidad:** P213 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de P211–P212:** evaluación temporal y productos persistidos.
- **Habilita para P214:** evolución de cliente en horizonte; cambia duración por estado siguiente.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

La actividad responde a una pregunta predictiva de permanencia; elegir una
oferta de retención es una decisión prescriptiva fuera de su alcance. La entrada
P213 de `traceability.yaml` mapea `predictiva.C01`–`C04`.
