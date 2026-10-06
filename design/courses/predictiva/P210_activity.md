# P210 — SIR adaptativo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P209_sir_adaptativo/`.

### Preguntas analíticas actuales

- ¿Cómo cambia el pronóstico epidemiológico cuando la tasa de infección se adapta a la evidencia temporal?

Extiende el caso de casos diarios con evolución adaptativa, pronósticos, tasa de
infección pronosticada, supuestos y picos de escenario.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pronostica casos activos proxy tras el inicio de vacunación; no demuestra efecto causal de la vacunación.
- **Producto terminal:** contraste de pronósticos SIR estático y adaptativo con historial de tasas.
- **Uso y límite:** actualiza la tasa después de observar cada día; no autoriza una intervención sanitaria.
- **Disciplinas contribuyentes:** suavizamiento temporal y SIR sirven al producto predictivo de Analytics.

### Highlights de contribución

- **H01 — Separa el corte antes de la vacunación:** reserva el tramo posterior para comparar pronósticos y evita que la tasa fija conozca observaciones futuras.
- **H02 — Aprende una tasa que privilegia evidencia reciente:** aplica suavizamiento exponencial a la tasa inferida desde el proxy de activos.
- **H03 — Contrasta actualización contra persistencia:** ejecuta SIR con tasa estática y con tasa adaptativa disponible al inicio de cada día.
- **H04 — Persiste tasas, pronósticos, picos, visualización y supuestos:** deja auditable el vínculo entre aprendizaje y resultado.

### Inventario técnico de implementación

- **Extiende:** SIR básico con tasa de infección adaptativa.
- **Introduce:** comparación entre parámetros fijos y evolución temporal del parámetro.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Corte temporal | H01 | Inicio de vacunación y evaluación posterior | No identifica efecto de vacunación. |
| Tasa adaptativa | H02–H03 | Suavizamiento y pronósticos SIR comparados | Proxy y tasa no son transmisión real. |
| Evidencia persistida | H04 | CSV, PNG y supuestos | Tests sólo comprueban archivos. |

### Relación técnica con actividades anteriores

Extiende P209; sin P210 se pierde la revisión de un supuesto fijo frente a
evidencia cambiante.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | Notebook: `vaccination_start`, training/evaluation | Corte no prueba causalidad. |
| H02 | S02 | Notebook: `SimpleExpSmoothing` | Tasa proviene de un proxy. |
| H03 | S02, S03 | Notebook; `forecasts.csv`; `scenario_peaks.csv` | No hay incertidumbre ni política. |
| H04 | S04 | `submission/`; pruebas | Tests sólo verifican presencia. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Corte y proxy temporal | Datos; notebook | Casos activos son aproximación. |
| S02 | Suavizamiento y SIR | Notebook; `infection_rate_forecast.csv` | No infiere efecto de vacunación. |
| S03 | Pronósticos comparados | `forecasts.csv`; `scenario_peaks.csv` | No es política. |
| S04 | Entregas y pruebas | `submission/`; pruebas | Sólo se prueba existencia. |

### Contrato de evidencia actual

- **Código:** infiere tasa, separa temporalmente, suaviza y simula dos pronósticos.
- **`submission/`:** conserva tasas, pronósticos, picos, gráfico y supuestos.
- **Pruebas:** verifican nombres de artefactos.
- **Trazabilidad:** falta entrada P210.

### Dependencias en la secuencia

- **Recibe de P209:** proxy, modelo SIR y escenarios.
- **Habilita para P211–P212:** comparación temporal con actualización y línea base, sin dependencia de código demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Datos, notebooks, artefactos y pruebas sustentan el mapa. P210 no figura en
`traceability.yaml`; se escala la omisión.
