# P208 — SIR básico

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P208_sir_basico/`.

### Preguntas analíticas actuales

- ¿Cómo representa un modelo SIR la evolución observada y escenarios de casos diarios en Colombia?

Usa casos diarios, compara ajuste, produce pronósticos, supuestos, evolución y
picos de escenarios.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima evolución de casos activos proxy y capacidad de camas; no hay autoridad sanitaria ni decisión evidenciadas.
- **Producto terminal:** pronósticos y picos de escenarios SIR con supuestos persistidos.
- **Uso y límite:** los diagnósticos y la ventana móvil de 14 días son proxys didácticos; no identifican infecciones reales ni autorizan políticas.
- **Disciplinas contribuyentes:** modelado compartimental sirve al pronóstico de Analytics, no a una formación epidemiológica autónoma.

### Highlights de contribución

- **H01 — Construye un proxy temporal auditable:** convierte casos diarios colombianos en casos activos mediante ventana móvil de 14 días; sin ello, la variable SIR no tendría correspondencia explícita con el dato observado.
- **H02 — Contrasta supuestos de transmisión:** ajusta una tasa constante sobre el tramo observado y compara escenarios sin seleccionar una política óptima.
- **H03 — Traduce curvas a una señal de capacidad:** deriva día y necesidad de camas en el pico frente a una capacidad ilustrativa; no confunde ese resultado con una política sanitaria.
- **H04 — Conserva la evidencia del escenario:** persiste pronósticos, comparación de ajuste, picos, gráfico y supuestos.

### Inventario técnico de implementación

- **Introduce:** modelo compartimental SIR, ajuste y comparación de evolución observada/esperada.
- **Introduce:** escenarios y comunicación de supuestos de modelo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Proxy y corte temporal | H01 | Casos diarios, frecuencia diaria y ventana móvil de 14 días | Casos reportados no son infecciones reales. |
| Escenarios SIR | H02–H03 | Tasa constante, curvas y picos/camas | No hay incertidumbre ni política factible. |
| Evidencia persistida | H04 | CSV, PNG y supuestos | Pruebas verifican archivos, no cálculos. |

### Relación técnica con actividades anteriores

Introduce simulación dinámica con datos temporales. Sin P208 se pierde el
vínculo entre supuestos estructurales y pronóstico de escenarios.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb`; `data/colombia_daily_cases.csv.gz` | Ventana de 14 días es aproximación didáctica. |
| H02 | S02 | Notebook: ajuste de tasa y escenarios | No identifica causalidad. |
| H03 | S03 | Notebook; `submission/scenario_peaks.csv` | Camas/capacidad son ilustrativas. |
| H04 | S04 | `submission/`; `tests/test_activity.py` | Tests sólo comprueban presencia. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Casos y proxy | Datos; notebook | No representan infecciones reales. |
| S02 | SIR y escenarios | Notebook; `forecasts.csv` | No produce política sanitaria. |
| S03 | Pico/capacidad | `scenario_peaks.csv`; supuestos | Capacidad es ilustrativa. |
| S04 | Evidencia/pruebas | `submission/`; pruebas | Sólo se prueba existencia. |

### Contrato de evidencia actual

- **Código:** construye proxy, ajusta tasa, simula y compara escenarios.
- **`submission/`:** conserva curvas, picos, ajuste, gráfico y supuestos.
- **Pruebas:** exigen los cinco artefactos, no su validez.
- **Trazabilidad:** falta entrada P208.

### Dependencias en la secuencia

- **Recibe de Pxxx:** no hay dependencia demostrable.
- **Habilita para P209:** caso, estructura SIR y contraste entre supuestos fijos y actualizados.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, notebooks, pronósticos, supuestos, pruebas sustentan el mapa. P208 no
figura en `traceability.yaml`, por lo que se escala esa omisión.
