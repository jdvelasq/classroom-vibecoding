# Encuadre analítico de decisiones

## Problema

Un banco debe decidir qué política de contacto usar en una campaña de depósito a plazo. Recibe estimaciones de conversión elaboradas en Predictiva para segmentos del conocido conjunto **Bank Marketing** de UCI; no se entrena ni se calibra un modelo en este taller. La responsable comercial debe escoger entre cuatro políticas factibles, con una capacidad de 1.000 contactos y un límite de exposición para el segmento con historial de contacto intenso.

## Competencia

Convertir evidencia disponible en un contrato de política para una decisión
recurrente: responsable, alternativas, valor, restricciones, salvaguarda,
autoridad, cadencia, excepción, resultado esperado y criterio de revisión. La
política recomienda una acción para aprobación humana; no requiere ejecución
automática.

## Decisión y entregable

La solución compara políticas explícitas y genera
`submission/decision_brief.csv` y `submission/policy_contract.csv`. El contrato
deja explícitos la acción, valor neto esperado, responsable, cadencia,
restricciones, salvaguarda de exposición, modo de ejecución, excepción,
resultado esperado y gatillo de revisión. La recomendación debe poder ser
aceptada o cuestionada por la responsable comercial.

## Datos

`data/policy_options.csv` es una agregación pedagógica pequeña, documentada y reproducible de segmentos del problema Bank Marketing de UCI. Sus probabilidades representan una salida recibida de Predictiva; los costos, beneficios y límites corresponden al escenario del caso. El conjunto completo se referencia como Moro et al. (2014), UCI Machine Learning Repository, *Bank Marketing*.

## Ejecución

Desde esta carpeta, ejecute:

```bash
python src/main.py
pytest -q
```
