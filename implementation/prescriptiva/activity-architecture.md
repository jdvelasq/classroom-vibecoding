# Arquitectura macro de talleres: Analítica prescriptiva

## Decisión de diseño

El curso desarrolla políticas computables y gobernadas para decisiones
operativas recurrentes. Cada actividad terminal debe hacer visible este
contrato:

```text
contexto y datos observables
            ↓
política: acción factible + restricciones + salvaguardas
            ↓
ejecución automática, aprobación humana o escalamiento
            ↓
registro de decisión → resultados → monitoreo y revisión
```

Un algoritmo, solución de optimización, frontera de alternativas o simulación
es evidencia para diseñar o validar la política; no la sustituye. La cadencia
y el plazo de respuesta son parte del contrato. No toda política es automática
ni inmediata.

## Convención y preservación

Las actividades usan `P300_`–`P399_`. El commit `cc0bf71` preserva el punto de
partida con la nomenclatura `PRE_`; la migración mecánica a P300–P322 conserva
todo el contenido y su historial. La columna de origen registra la
correspondencia verificable con ese punto de partida.

## Secuencia propuesta

| Orden final | Origen preservado | Rol macro | Producto de política esperado | Prioridad |
|---|---|---|---|---|
| P300 | `PRE_01_encuadre_analitico_de_decisiones` | Contrato de política | Política de contacto con valor, capacidad y gatillo de revisión | Núcleo |
| P301 | `PRE_02_air_france_447` | Frontera crítica | Distinguir un plan excepcional de una política recurrente | Núcleo |
| P302 | `PRE_03_politica_desde_evidencia_y_restricciones` | Regla factible | Asignación con garantía mínima y razón de descarte | Núcleo |
| P303 | `PRE_06_politicas_y_supervision_humana` | Autoridad y excepción | Regla de aprobar, rechazar o escalar | Núcleo |
| P304 | `PRE_04_airline_revenue_management` | Política repetitiva | Regla de aceptación y protección de capacidad | Núcleo |
| P305 | `PRE_08_tax_inspections` | Priorización con capacidad | Política de inspección bajo capacidad limitada | Núcleo |
| P306 | `PRE_16_credit_campaign_targeting` | Predicción → acción | Política de contacto con restricción de exposición | Núcleo |
| P307 | `PRE_17_decision_informada_por_pronosticos` | Predicción → inventario | Política de pedido por escenarios y servicio | Núcleo |
| P308 | `PRE_07_annie_moore_refugee_resettlement` | Asignación responsable | Política de asignación con utilización y restricciones | Núcleo |
| P309 | `PRE_05_covid_hospital_capacity` | Capacidad y escalamiento | Regla de expansión y activación por demanda | Núcleo |
| P310 | `PRE_09_monte_carlo_para_politicas` | Incertidumbre | Política de inversión con gatillo de escalamiento | Núcleo |
| P311 | `PRE_12_evaluacion_de_politicas_por_simulacion` | Prueba de política | Política de capacidad por servicio, costo y riesgo | Núcleo |
| P312 | `PRE_15_sensibilidad_y_tradespace` | Robustez | Regla de revisión al cambiar un supuesto crítico | Extensión |
| P313 | `PRE_19_delivery_fleet_capacity` | Demora y capacidad | Regla de flota y contingencia validada por simulación | Extensión |
| P314 | `PRE_21_storm_response_crews` | Respuesta dinámica | Política de reserva y despliegue por escenario | Extensión |
| P315 | `PRE_10_wildfire_resource_positioning` | Posicionamiento preventivo | Política de ubicación y reasignación de recursos | Extensión |
| P316 | `PRE_11_humanitarian_food_aid` | Distribución restringida | Política de abastecimiento y distribución | Extensión |
| P317 | `PRE_13_flood_protection_investment` | Política de inversión | Regla de protección según riesgo y presupuesto | Extensión |
| P318 | `PRE_14_hydrothermal_planning` | Política intertemporal | Política de generación bajo reservas y horizonte | Extensión |
| P319 | `PRE_18_catalog_assortment` | Política de surtido | Regla de incorporación y retiro con capacidad | Extensión |
| P320 | `PRE_20_equidad_y_responsabilidad_prescriptiva` | Salvaguardas | Auditoría de equidad y corrección de política | Núcleo transversal |
| P321 | `PRE_22_comunicacion_y_seguimiento_de_politicas` | Operación y monitoreo | Registro, indicadores y gatillos de revisión | Núcleo transversal |
| P322 | `PRE_23_valor_de_informacion_y_experimentacion` | Aprendizaje | Política para medir antes de actuar | Extensión |

## Cobertura por etapa

1. **Definir la política** (`P300`–`P303`): separar evidencia, acción,
   autoridad, límites y recurrencia.
2. **Operar con evidencia** (`P304`–`P309`): aceptación, priorización,
   inventario, asignación y capacidad; las predicciones son insumos.
3. **Probar antes de operar** (`P310`–`P311`): incertidumbre, escenarios y
   simulación para comparar políticas con líneas base.
4. **Ampliar el alcance** (`P312`–`P319`): robustez, demoras, recursos,
   inversión, restricciones e intertemporalidad; se dictan según el avance.
5. **Gobernar y aprender** (`P320`–`P322`): equidad, explicabilidad,
   monitoreo, gatillos de cambio y valor de obtener información.

`P320` y `P321` son transversales: se introducen desde el núcleo y se
formalizan al final; no son un apéndice ético o comunicacional.

## Criterios para auditar cada actividad

- Explicitar entrada, acción, restricciones, guardas, autoridad, cadencia,
  latencia y gatillos de revisión.
- Confirmar que produce una política, no solo una solución o comparación.
- Convertir resultados existentes en evidencia de la política: decisión,
  razón, resultado esperado y condición para revisarla.
- Normalizar una actividad aprobada a `Pxxx_` sin perder el caso, procedencia
  ni material pedagógico.

## Trazabilidad al diseño

| Capacidad S05 | Etapas de actividades |
|---|---|
| `prescriptiva.C01` | P300–P303 |
| `prescriptiva.C02` | P304–P309 |
| `prescriptiva.C03` | P310–P319 |
| `prescriptiva.C04` | P300–P303, P320–P321 |
| `prescriptiva.C05` | P320–P322 |
