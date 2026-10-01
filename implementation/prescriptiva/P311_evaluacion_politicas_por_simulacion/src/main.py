from pathlib import Path
import json

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MAX_BREACH_PROBABILITY = 0.20
MAX_DAILY_COST = 900


def evaluate(policies: pd.DataFrame, scenarios: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for policy in policies.itertuples(index=False):
        served = scenarios.demand.clip(upper=policy.capacity)
        service_rate = served / scenarios.demand
        expected_service = (service_rate * scenarios.probability).sum()
        breach_probability = scenarios.loc[
            service_rate < policy.service_target, "probability"
        ].sum()
        expected_unserved = ((scenarios.demand - served) * scenarios.probability).sum()
        meets_service_target = expected_service >= policy.service_target
        meets_risk_limit = breach_probability <= MAX_BREACH_PROBABILITY
        meets_budget = policy.daily_cost <= MAX_DAILY_COST
        rows.append(
            {
                "policy_id": policy.policy_id,
                "policy": policy.policy,
                "capacity": policy.capacity,
                "expected_service_rate": expected_service,
                "expected_unserved_requests": expected_unserved,
                "breach_probability": breach_probability,
                "daily_cost": policy.daily_cost,
                "meets_service_target": meets_service_target,
                "meets_risk_limit": meets_risk_limit,
                "meets_budget": meets_budget,
                "eligible": meets_service_target and meets_risk_limit and meets_budget,
            }
        )
    return pd.DataFrame(rows)


def choose_policy(comparison: pd.DataFrame) -> pd.Series:
    eligible_policies = comparison.loc[comparison.eligible]
    if eligible_policies.empty:
        raise ValueError("Ninguna política cumple simultáneamente servicio, riesgo y presupuesto.")
    return eligible_policies.nsmallest(1, ["daily_cost", "breach_probability"]).iloc[0]


def policy_record(selected_policy: pd.Series) -> dict:
    return {
        "decision": "Capacidad diaria del centro de atención",
        "cadence": "Diaria, antes de abrir el servicio",
        "response_need": "La capacidad debe quedar confirmada antes del inicio de la jornada.",
        "selected_policy": {
            "policy_id": selected_policy.policy_id,
            "action": f"Operar {selected_policy.policy} con {selected_policy.capacity} cupos diarios.",
            "expected_service_rate": round(float(selected_policy.expected_service_rate), 4),
            "breach_probability": round(float(selected_policy.breach_probability), 4),
            "daily_cost": int(selected_policy.daily_cost),
        },
        "constraints_and_safeguards": {
            "minimum_expected_service_rate": 0.90,
            "maximum_probability_of_service_breach": MAX_BREACH_PROBABILITY,
            "maximum_daily_cost": MAX_DAILY_COST,
        },
        "authority": {
            "routine_action": "La coordinación de operaciones activa la política seleccionada.",
            "exception": "La gerencia de operaciones aprueba ampliar capacidad o contratar contingencia.",
        },
        "triggers": [
            "Escalar a gerencia si el pronóstico diario supera la capacidad seleccionada.",
            "Revisar la política si ocurren dos incumplimientos de servicio en diez jornadas.",
            "Suspender la política si su costo diario supera el límite presupuestal.",
        ],
        "monitoring": [
            "Tasa diaria de servicio observada.",
            "Solicitudes no atendidas.",
            "Costo diario de capacidad.",
            "Frecuencia de escalamiento y de incumplimientos.",
        ],
    }


def main():
    policies = pd.read_csv(ROOT / "data" / "capacity_policies.csv")
    scenarios = pd.read_csv(ROOT / "data" / "demand_scenarios.csv")
    comparison = evaluate(policies, scenarios)
    selected_policy = choose_policy(comparison)

    comparison.to_csv(ROOT / "submission" / "capacity_policy_comparison.csv", index=False)
    with open(ROOT / "submission" / "capacity_policy_decision.json", "w") as file:
        json.dump(policy_record(selected_policy), file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
