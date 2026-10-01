# Monte Carlo para políticas

## Problema

En cada ciclo presupuestal, una dirección debe decidir si aprueba, rechaza o escala una propuesta de expansión. El flujo de caja es deliberadamente simple: inversión inicial, ingresos anuales, costos variables y costos fijos. La simulación no entrega la decisión por sí misma: estima el riesgo que usa una política explícita de inversión.

## Competencia

Usar Monte Carlo para validar una política de inversión bajo incertidumbre, comunicar la probabilidad de pérdida y definir la acción, autoridad, guardas, excepción y gatillo de revisión. La simulación evalúa la política; no sustituye al responsable ni se presenta como una técnica de IO.

## Entregable

`submission/project_risk_summary.csv` contiene VPN promedio, percentil conservador y probabilidad de pérdida. `submission/investment_policy.csv` deja trazable la acción, autoridad, cadencia, guardas, excepción y monitoreo. Los parámetros son un caso de evaluación financiera pedagógico, compatible con ejemplos de DecisionSuite adaptados a Python; no pretende ser una proyección financiera real.
