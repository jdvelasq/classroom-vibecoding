# P310 — Monte Carlo para políticas de inversión

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P310_monte_carlo_para_politicas/`.

### Preguntas analíticas actuales

- ¿Qué acción debe tomar el comité mensual ante una expansión con retorno y riesgo inciertos?

Usa una sola fila de parámetros de proyecto (`project_parameters.csv`: inversión 500.000, 4 años, ingreso base 360.000, tasa de costo variable 0.48, costo fijo 90.000, descuento 0.12, `revenue_sigma` 0.18, `margin_sigma` 0.05). No hay procedencia ni declaración de caso real o sintético. `professor/main.py` simula 10.000 trayectorias de VPN con semilla fija, resume media, percentil 10 y probabilidad de pérdida, y aplica una regla de tres ramas: no aprobar, escalar para revisión o aprobar. El notebook muestra el histograma del VPN y persiste el resumen y la política.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decisión del comité de inversión sobre una expansión; autoridad por rama («Comité de inversión», «Comité de inversión y dirección financiera», «Dirección financiera»).
- **Producto terminal:** `investment_policy.csv` con cadencia, necesidad de respuesta, acción, autoridad, objetivo, guardas (`guardrail_loss_probability` 0.35, `guardrail_p10_npv` −100.000), excepción, métrica y gatillo de revisión; respaldado por `project_risk_summary.csv`.
- **Uso y límite:** introduce la traducción de una distribución simulada en guardas de riesgo. En el caso persistido, la media del VPN es −204.852,96 y la probabilidad de pérdida 0.9997, de modo que la acción es `no_aprobar` por la primera rama; las guardas de riesgo y la rama de escalamiento no se ejercitan. La recurrencia es débil: la cadencia es «mientras la expansión esté en evaluación» para un único proyecto.
- **Disciplinas contribuyentes:** simulación Monte Carlo (lognormal de ingreso con media corregida, normal recortada del margen) y finanzas (VPN) sirven a la regla de decisión.

### Highlights de contribución

- **H01 — Resume una distribución de resultados en indicadores de decisión:** `summarize_risk` reduce 10.000 VPN simulados a media, P10 y probabilidad de VPN < 0, y el notebook marca VPN = 0 en el histograma. Primera simulación estocástica del curso (P304–P309 usan escenarios discretos); sin este hito, la incertidumbre sólo se representaría con tres o cuatro escenarios.
- **H02 — Codifica guardas de riesgo y una rama de escalamiento en la regla:** `define_investment_policy` separa valor esperado no positivo (no aprobar), riesgo por encima de guardas (escalar a comité y dirección financiera) y caso aceptable (aprobar), cada uno con autoridad y justificación. Extiende el patrón aprobar/rechazar/escalar de P303 a guardas sobre una distribución; sin este hito, el resultado simulado no estaría conectado con quién decide.
- **H03 — Muestra (sin declararlo) que la simulación no cambia la decisión en este caso:** los parámetros producen media −204.852,96 y P10 −271.008,48 (`project_risk_summary.csv`); el notebook no contrasta con el VPN determinista de los parámetros base ni explora parámetros donde las guardas sean decisivas. Ésta es la particularidad del dataset: una sola fila de parámetros cuya configuración deja el proyecto claramente inviable, de modo que la contribución de la incertidumbre al producto queda sin evidencia. Se registra como límite, no como logro.

### Inventario técnico de implementación

- **Introduce:** generador `np.random.default_rng` con semilla; choques anuales independientes lognormales y normales recortados; VPN vectorizado; métricas de cola (P10, probabilidad de pérdida).
- **Extiende:** regla de tres acciones con autoridad (P303) a umbrales de riesgo.
- **Reutiliza:** funciones en `main.py` importadas por el notebook; persistencia CSV.
- **Aplica en nuevo caso:** gatillo de revisión basado en desviación de ingresos realizados frente al escenario base.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Monte Carlo de VPN | H01 | 10.000 trayectorias, semilla fija, histograma | Choques independientes por año; sin correlación ni error de Monte Carlo reportado. |
| Guardas sobre distribución | H02 | Probabilidad de pérdida ≤ 0.35 y P10 ≥ −100.000 | Umbrales dados, no derivados. |
| Política de inversión | H02–H03 | `investment_policy.csv` con acción `no_aprobar` | Ramas de escalamiento/aprobación no ejercitadas. |

### Relación técnica con actividades anteriores

Nuevo método (simulación estocástica) al servicio del mismo tipo de producto que P300–P303 (regla con autoridad y gatillo). No reutiliza escenarios ni planeadores de P304–P309; es un taller corto basado en `main.py`, como P300, P302, P303 y P307. **Posible duplicación con P313:** ambos usan Monte Carlo para elegir una acción; P313 añade números aleatorios comunes, intervalos de confianza y comparación pareada, por lo que P310 queda como introducción mínima. Respecto del producto previsto en `activity-architecture.md` («política de inversión con gatillo de escalamiento»), el gatillo existe en código pero no se activa con los datos entregados.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Resumen de distribución | S02 | `implementation/prescriptiva/P310_monte_carlo_para_politicas/professor/main.py`: `simulate_project`, `summarize_risk`; `implementation/prescriptiva/P310_monte_carlo_para_politicas/submission/project_risk_summary.csv`; notebook: histograma | No se reporta error de estimación ni convergencia. |
| H02 — Guardas y escalamiento | S03 | `implementation/prescriptiva/P310_monte_carlo_para_politicas/professor/main.py`: `define_investment_policy`; `implementation/prescriptiva/P310_monte_carlo_para_politicas/submission/investment_policy.csv` | Umbrales sin justificación en el taller. |
| H03 — Simulación no decisiva | S01, S02, S04 | `implementation/prescriptiva/P310_monte_carlo_para_politicas/data/project_parameters.csv`; `implementation/prescriptiva/P310_monte_carlo_para_politicas/submission/project_risk_summary.csv` | El notebook no compara con el cálculo determinista ni con parámetros alternativos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Parámetros del caso | `data/project_parameters.csv` | Una fila; sin procedencia; proyecto claramente inviable. |
| S02 | Modelo de simulación y resumen | `professor/main.py`: `simulate_project`, `summarize_risk`; notebook | Choques independientes, semilla fija, 10.000 corridas. |
| S03 | Regla de decisión y guardas | `professor/main.py`: `define_investment_policy`; `submission/investment_policy.csv` | Tres ramas; sólo una alcanzada. |
| S04 | Secuencia/recurrencia | Notebook (pregunta); `investment_policy.csv` (`decision_cadence`) | Un único proyecto; recurrencia no demostrada. |
| S05 | Pruebas e interfaz | `tests/test_activity.py`; ruta `root / 'src'` del notebook | Pruebas de existencia; `src/` sin `main.py`. |

### Contrato de evidencia actual

- **Notebook o código:** carga parámetros, simula, grafica, resume y aplica la regla; `main.py` reproduce el flujo completo.
- **`submission/`:** `project_risk_summary.csv` (media, P10, probabilidad de pérdida) e `investment_policy.csv` (acción `no_aprobar` y contrato).
- **Pruebas:** comprueban que ambos archivos existan; no verifican columnas, valores ni la regla.
- **Trazabilidad:** P310 mapea `prescriptiva.C01`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P303:** práctica de regla con acciones aprobar/rechazar/escalar y autoridad diferenciada. No hay artefacto compartido.
- **Habilita para P313:** no evidenciada como dependencia explícita; P313 no referencia P310 y reconstruye su simulación desde cero.

## Trazabilidad y auditoría

P310 está mapeada a `prescriptiva.C01`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C01 y C04 se sostienen por el contrato con cadencia, autoridad y excepción; C03 por la simulación, aunque no se valida la política frente a líneas base ni se muestra sensibilidad; C05 sólo por un gatillo de revisión de ingresos realizados que no aplica a un proyecto no aprobado. El producto de Analytics es una regla de inversión con guardas de riesgo; Monte Carlo contribuye. La auditoría queda **no resuelta** en un punto: con los datos actuales el producto se reduce a «no aprobar porque la media es negativa», y la contribución de la incertidumbre a la acción no se evidencia.
