"""Genera la política de surtido usada en el taller presencial."""

from itertools import combinations
import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
MAX_PRODUCTS = 4
NO_PURCHASE_ATTRACTIVENESS = 1.0


def expected_margin(assortment, attractiveness, unit_margin):
    if not assortment:
        return 0.0

    denominator = NO_PURCHASE_ATTRACTIVENESS + sum(
        attractiveness[product_id] for product_id in assortment
    )
    return sum(
        attractiveness[product_id] / denominator * unit_margin[product_id]
        for product_id in assortment
    )


def validate_products(products):
    required_columns = {"product_id", "price", "unit_cost", "attractiveness"}
    missing_columns = required_columns.difference(products.columns)
    if missing_columns:
        raise ValueError(f"Faltan atributos requeridos: {sorted(missing_columns)}")

    if products[list(required_columns)].isna().any().any():
        raise ValueError("No se puede publicar una política con atributos incompletos.")

    if not products.product_id.is_unique:
        raise ValueError("Cada producto debe tener un identificador único.")

    products = products.copy()
    products["unit_margin"] = products.price - products.unit_cost
    return products


def select_assortment(products, capacity=MAX_PRODUCTS):
    attractiveness = products.set_index("product_id").attractiveness.to_dict()
    unit_margin = products.set_index("product_id").unit_margin.to_dict()
    product_ids = products.product_id.tolist()

    candidates = []
    for size in range(capacity + 1):
        for assortment in combinations(product_ids, size):
            candidates.append(
                {
                    "assortment": "|".join(assortment),
                    "n_products": len(assortment),
                    "expected_margin_per_customer": expected_margin(
                        assortment, attractiveness, unit_margin
                    ),
                }
            )

    evaluated = pd.DataFrame(candidates).sort_values(
        ["expected_margin_per_customer", "assortment"],
        ascending=[False, True],
    ).reset_index(drop=True)
    return evaluated


def build_policy(products, evaluated):
    selected = tuple(evaluated.loc[0, "assortment"].split("|"))
    decision_table = products.copy()
    decision_table["unit_margin"] = (
        decision_table.price - decision_table.unit_cost
    )
    decision_table["recommended_action"] = decision_table.product_id.map(
        lambda product_id: "include" if product_id in selected else "exclude"
    )
    decision_table["decision_reason"] = "does not improve the feasible catalog policy"
    decision_table.loc[
        decision_table.unit_margin <= 0, "decision_reason"
    ] = "excluded by the non-positive margin safeguard"
    decision_table.loc[
        decision_table.product_id.isin(selected), "decision_reason"
    ] = "maximizes expected catalog margin within capacity"
    return decision_table


def main():
    products = validate_products(pd.read_csv(DATA_DIR / "products.csv"))
    eligible_products = products.loc[products.unit_margin > 0].copy()
    evaluated = select_assortment(eligible_products)
    policy = build_policy(products, evaluated)
    selected = evaluated.loc[0, "assortment"].split("|")
    selected_attractiveness = eligible_products.set_index("product_id").attractiveness
    no_purchase_probability = NO_PURCHASE_ATTRACTIVENESS / (
        NO_PURCHASE_ATTRACTIVENESS
        + sum(selected_attractiveness[product_id] for product_id in selected)
    )

    policy_contract = {
        "decision": "incorporar o retirar productos del catalogo de una categoria",
        "cadence": "revision mensual; respuesta antes del siguiente ciclo de catalogo",
        "input_requirements": [
            "precio, costo unitario y atractivo vigentes para cada candidato",
            "capacidad de exhibicion aprobada",
        ],
        "policy": "seleccionar hasta cuatro productos que maximicen el margen esperado por cliente",
        "recommended_assortment": selected,
        "execution_mode": "recomendación con aprobación humana antes de publicar el catálogo",
        "constraints_and_guardrails": [
            "no exceder cuatro plazas de catalogo",
            "no incorporar productos con margen unitario no positivo",
            "no publicar cambios con atributos incompletos o no validados",
        ],
        "authority": "el gerente de categoria aprueba cambios; precios, costos o capacidad anómalos se escalan a comercial y operaciones",
        "exceptions": [
            "un producto sin atributos validados bloquea la publicación",
            "un producto con margen no positivo queda excluido del surtido",
        ],
        "monitoring": [
            "margen realizado frente al margen esperado",
            "tasa de no compra frente a la estimada",
            "ocupacion de las plazas del catalogo",
        ],
        "review_triggers": [
            "margen realizado 15% menor que el esperado durante dos revisiones",
            "tasa de no compra 10 puntos porcentuales mayor que la estimada",
            "cambio de precio, costo, capacidad o disponibilidad de un producto seleccionado",
        ],
    }
    monitoring = pd.DataFrame(
        [
            {
                "metric": "expected_margin_per_customer",
                "baseline": evaluated.loc[0, "expected_margin_per_customer"],
                "review_trigger": "15% below expected for two monthly reviews",
                "owner": "category manager",
            },
            {
                "metric": "no_purchase_probability",
                "baseline": no_purchase_probability,
                "review_trigger": "10 percentage points above expected",
                "owner": "category manager",
            },
            {
                "metric": "catalog_capacity",
                "baseline": MAX_PRODUCTS,
                "review_trigger": "capacity, price, cost, or availability changes",
                "owner": "commercial and operations",
            },
        ]
    )

    SUBMISSION_DIR.mkdir(exist_ok=True)
    evaluated.to_csv(SUBMISSION_DIR / "assortment_results.csv", index=False)
    policy.to_csv(SUBMISSION_DIR / "assortment_policy.csv", index=False)
    monitoring.to_csv(SUBMISSION_DIR / "policy_monitoring.csv", index=False)
    (SUBMISSION_DIR / "policy_contract.json").write_text(
        json.dumps(policy_contract, indent=2, ensure_ascii=False) + "\n"
    )


if __name__ == "__main__":
    main()
