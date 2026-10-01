from pathlib import Path
import json

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CUSTOMER_VALUE = 260
REVIEW_RETENTION_GAIN = 0.0162
MONTHLY_BUDGET = 42_000


def evaluate(options: pd.DataFrame, retention_multiplier: float = 1.0) -> pd.DataFrame:
    result = options.copy()
    result["assumed_retention_gain"] = result.retention_gain * retention_multiplier
    result["retained_value"] = (
        result.monthly_customers * result.assumed_retention_gain * CUSTOMER_VALUE
    )
    result["net_value"] = result.retained_value - result.monthly_cost
    return result


def evaluate_sensitivity(options: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for retention_multiplier in [0.20, 0.30, 0.50, 0.75, 1.00, 1.25]:
        scenario = evaluate(options, retention_multiplier)
        selected = scenario.loc[scenario.net_value.idxmax()]
        rows.append(
            {
                "retention_multiplier": retention_multiplier,
                "selected_policy_id": selected.option_id,
                "selected_policy": selected.option,
                "selected_net_value": selected.net_value,
            }
        )
    return pd.DataFrame(rows)


def policy_record(options: pd.DataFrame) -> dict:
    one_day = options.loc[options.option_id == "P2"].iloc[0]
    review_threshold = one_day.monthly_cost / (
        one_day.monthly_customers * CUSTOMER_VALUE
    )

    return {
        "decision": "Promesa de entrega para clientes elegibles",
        "cadence": "Mensual, antes de publicar la promesa del mes siguiente",
        "response_need": "La promesa debe quedar definida antes de abrir las campañas mensuales.",
        "policy": {
            "action": "Ofrecer entrega en un día.",
            "when": "La ganancia de retención estimada supera el umbral y el costo mensual cabe en el presupuesto.",
            "retention_gain_threshold": round(float(review_threshold), 4),
            "monthly_budget": MONTHLY_BUDGET,
        },
        "constraints_and_safeguards": {
            "cost_limit": "La promesa no puede superar el presupuesto mensual aprobado.",
            "uncertainty_guardrail": "No automatizar el cambio si el intervalo de incertidumbre de la ganancia de retención cruza el umbral.",
            "dominated_option": "La entrega en dos días no se selecciona en los escenarios analizados; no debe mantenerse por costumbre.",
        },
        "authority": {
            "routine_action": "La gerencia comercial activa o mantiene la promesa cuando la evidencia supera el umbral.",
            "exception": "La dirección comercial aprueba una excepción cuando la incertidumbre cruza el umbral o cambia el presupuesto.",
        },
        "triggers": [
            "Revisar la política si la ganancia de retención observada en cuatro semanas es menor o igual al umbral.",
            "Suspender la promesa de un día si su costo mensual supera el presupuesto.",
            "Recalibrar la estimación si cambia la composición de clientes o el costo de entrega.",
        ],
        "monitoring": [
            "Ganancia de retención observada frente al grupo de comparación.",
            "Costo mensual de la promesa.",
            "Valor neto observado.",
            "Frecuencia de excepciones y decisiones suspendidas.",
        ],
    }


def main():
    options = pd.read_csv(ROOT / "data" / "service_options.csv")
    comparison = evaluate(options)
    sensitivity = evaluate_sensitivity(options)

    comparison.to_csv(ROOT / "submission" / "tradespace.csv", index=False)
    sensitivity.to_csv(ROOT / "submission" / "sensitivity_review.csv", index=False)
    with open(ROOT / "submission" / "delivery_promise_policy.json", "w") as file:
        json.dump(policy_record(options), file, indent=2, ensure_ascii=False)


if __name__ == "__main__": main()
