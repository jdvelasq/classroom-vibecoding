from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "recommendation.csv"
POLICY_REGISTER_FILE = ACTIVITY_DIR / "submission" / "policy_register.csv"


def create_policy_register(recommendation):
    decision = recommendation.iloc[0]

    return pd.DataFrame(
        [
            {
                "policy_id": "capacity-flex-001",
                "decision_context": "Capacidad de atención semanal",
                "cadence": "semanal",
                "response_need": "un día hábil",
                "recommended_action": decision["decision"],
                "alternative_not_selected": decision["alternative"],
                "assumption": decision["assumption"],
                "objective": "Sostener el nivel de servicio sin exceder la capacidad aprobada",
                "constraint": "La capacidad adicional requiere presupuesto y personal disponible",
                "safeguard": "No reducir la atención de casos prioritarios",
                "execution_mode": "recomendación con aprobación humana",
                "decision_authority": "Dirección de operaciones",
                "indicator": decision["indicator"],
                "indicator_target": "service_rate >= 0.90",
                "review_trigger": "service_rate < 0.90 durante la revisión semanal",
                "review_owner": "Dirección de operaciones",
                "review_action": "Revisar demanda, capacidad y continuidad de la política",
            }
        ]
    )


def main():
    recommendation = pd.read_csv(DATA_FILE)
    policy_register = create_policy_register(recommendation)
    policy_register.to_csv(POLICY_REGISTER_FILE, index=False)


if __name__ == "__main__":
    main()
