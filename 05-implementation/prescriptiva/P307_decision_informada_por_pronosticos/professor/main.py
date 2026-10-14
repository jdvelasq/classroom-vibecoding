from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def evaluate_order_options(order_options, scenarios):
    evaluations = []

    for option in order_options.itertuples(index=False):
        sold = scenarios["demand"].clip(upper=option.order_quantity)
        leftover = (option.order_quantity - scenarios["demand"]).clip(lower=0)
        value = (
            sold * option.price
            - option.order_quantity * option.unit_cost
            - leftover * option.disposal_cost
        )
        stockout_probability = scenarios.loc[
            scenarios["demand"] > option.order_quantity,
            "probability",
        ].sum()

        evaluations.append(
            {
                "order_quantity": option.order_quantity,
                "expected_value": (value * scenarios["probability"]).sum(),
                "stockout_probability": stockout_probability,
                "service_level": 1 - stockout_probability,
            }
        )

    return pd.DataFrame(evaluations)


def evaluate(order_options, scenarios):
    return evaluate_order_options(order_options, scenarios)


def select_order_policy(evaluation, policy_contract):
    feasible_options = evaluation.loc[
        evaluation["stockout_probability"]
        <= policy_contract["maximum_stockout_probability"]
    ]
    selected_option = feasible_options.sort_values(
        "expected_value",
        ascending=False,
    ).iloc[0]

    return pd.DataFrame(
        [
            {
                "decision_cadence": policy_contract["decision_cadence"],
                "decision_owner": policy_contract["decision_owner"],
                "selected_order_quantity": int(selected_option["order_quantity"]),
                "expected_value": selected_option["expected_value"],
                "stockout_probability": selected_option["stockout_probability"],
                "service_level": selected_option["service_level"],
                "approval_required": policy_contract["approval_required"],
                "review_trigger": policy_contract["review_trigger"],
            }
        ]
    )


def main():
    scenarios = pd.read_csv(ACTIVITY_DIR / "data" / "forecast_scenarios.csv")
    order_options = pd.read_csv(ACTIVITY_DIR / "data" / "order_options.csv")
    policy_contract = pd.read_csv(
        ACTIVITY_DIR / "data" / "policy_contract.csv"
    ).iloc[0]
    evaluation = evaluate_order_options(order_options, scenarios)
    order_policy = select_order_policy(evaluation, policy_contract)

    evaluation.to_csv(
        ACTIVITY_DIR / "submission" / "order_evaluation.csv",
        index=False,
    )
    order_policy.to_csv(
        ACTIVITY_DIR / "submission" / "order_policy.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
