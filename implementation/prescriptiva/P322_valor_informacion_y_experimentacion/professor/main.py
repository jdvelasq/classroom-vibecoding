import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
STUDY_COST = 8_000
STUDY_ACCURACY = 0.85


def evaluate_actions(scenarios):
    launch_now_value = (scenarios["probability"] * scenarios["launch_value"]).sum()

    favorable = scenarios.loc[scenarios["launch_value"] > 0]
    unfavorable = scenarios.loc[scenarios["launch_value"] <= 0]
    value_after_positive_signal = (
        favorable["probability"].sum()
        * STUDY_ACCURACY
        * favorable["launch_value"].iloc[0]
        + unfavorable["probability"].sum()
        * (1 - STUDY_ACCURACY)
        * unfavorable["launch_value"].iloc[0]
        - STUDY_COST
    )

    return pd.DataFrame(
        [
            {
                "policy_option": "lanzar_ahora",
                "expected_value": launch_now_value,
                "decision": "no_recomendada",
                "decision_reason": "la incertidumbre de demanda expone la campaña a una pérdida esperada",
            },
            {
                "policy_option": "medir_antes_y_lanzar_si_positivo",
                "expected_value": value_after_positive_signal,
                "decision": "recomendada",
                "decision_reason": "la medición evita el lanzamiento cuando la señal es negativa y supera el costo del estudio",
            },
        ]
    )


def build_policy_contract():
    return {
        "decision": "medir antes de lanzar una intervención de campaña y lanzar solo con señal positiva",
        "cadence": "antes de cada campaña trimestral",
        "response_need": "el resultado debe estar disponible antes de comprometer el presupuesto de la campaña",
        "observable_inputs": [
            "escenarios de demanda y valor esperado de lanzamiento",
            "resultado positivo o negativo de la medición",
            "costo real y precisión observada de la medición",
        ],
        "action_policy": {
            "positive_measurement": "autorizar lanzamiento dentro del presupuesto aprobado",
            "negative_measurement": "no lanzar y conservar el presupuesto; escalar una nueva hipótesis de campaña",
        },
        "guardrails": [
            "el costo de la medición no puede superar 8,000 unidades monetarias",
            "la precisión observada debe ser al menos 0.85 antes de reutilizar la medición",
            "un resultado positivo no autoriza exceder el presupuesto de campaña aprobado",
        ],
        "authority": "el responsable de campaña aprueba el estudio y autoriza el lanzamiento positivo; una excepción de costo, precisión o presupuesto se escala al responsable comercial",
        "monitoring": [
            "valor esperado de lanzar ahora frente a medir antes",
            "costo y precisión observados de la medición",
            "resultado de la campaña después de cada señal positiva",
            "proporción de campañas detenidas por señal negativa",
        ],
        "review_triggers": [
            "costo de medición superior a 8,000 unidades monetarias",
            "precisión observada inferior a 0.85",
            "el valor esperado de medir antes deja de superar el de lanzar ahora",
            "cambio material en el valor, presupuesto o demanda de la campaña",
        ],
    }


def build_monitoring_plan():
    return pd.DataFrame(
        [
            {
                "metric": "measurement_cost",
                "guardrail": STUDY_COST,
                "review_trigger": "cost exceeds approved maximum",
                "owner": "campaign owner",
            },
            {
                "metric": "measurement_accuracy",
                "guardrail": STUDY_ACCURACY,
                "review_trigger": "accuracy below approved minimum",
                "owner": "commercial owner",
            },
            {
                "metric": "incremental_expected_value",
                "guardrail": "must remain positive against launch now",
                "review_trigger": "measure-before value no longer exceeds launch-now value",
                "owner": "campaign owner",
            },
        ]
    )


def main():
    scenarios = pd.read_csv(DATA_DIR / "decision_scenarios.csv")
    actions = evaluate_actions(scenarios)
    contract = build_policy_contract()
    monitoring = build_monitoring_plan()

    actions.to_csv(SUBMISSION_DIR / "information_value.csv", index=False)
    monitoring.to_csv(SUBMISSION_DIR / "policy_monitoring.csv", index=False)
    (SUBMISSION_DIR / "policy_contract.json").write_text(
        json.dumps(contract, indent=2, ensure_ascii=False) + "\n"
    )


if __name__ == "__main__":
    main()
