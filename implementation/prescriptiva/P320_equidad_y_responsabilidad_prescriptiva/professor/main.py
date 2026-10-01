import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
MAX_CONTACT_RATE_GAP = 0.10


def audit_policy_equity(policy_impacts):
    audited = policy_impacts.copy()
    audited["contact_rate"] = audited["contacted"] / audited["eligible"]
    audited["benefit_per_eligible"] = audited["benefit"] / audited["eligible"]

    policy_gaps = (
        audited.groupby("policy", as_index=False)
        .agg(
            contact_rate_gap=("contact_rate", lambda rates: rates.max() - rates.min()),
            benefit_gap=("benefit_per_eligible", lambda benefits: benefits.max() - benefits.min()),
        )
    )
    audited = audited.merge(policy_gaps, on="policy", validate="many_to_one")
    audited["equity_status"] = audited["contact_rate_gap"].map(
        lambda gap: "pass" if gap <= MAX_CONTACT_RATE_GAP else "correct"
    )
    return audited


def decide_policy_correction(audited):
    decisions = (
        audited.groupby("policy", as_index=False)
        .agg(
            contact_rate_gap=("contact_rate_gap", "first"),
            benefit_gap=("benefit_gap", "first"),
            groups_audited=("group", "nunique"),
        )
    )
    decisions["decision"] = decisions["contact_rate_gap"].map(
        lambda gap: "approve" if gap <= MAX_CONTACT_RATE_GAP else "suspend_and_correct"
    )
    decisions["decision_reason"] = decisions["contact_rate_gap"].map(
        lambda gap: (
            "contact-rate gap is within the approved equity guardrail"
            if gap <= MAX_CONTACT_RATE_GAP
            else "contact-rate gap exceeds the approved equity guardrail"
        )
    )
    return decisions


def build_policy_contract():
    return {
        "decision": "aprobar, suspender o corregir una política recurrente de contacto",
        "cadence": "antes de cada campaña y en la revisión mensual de resultados",
        "response_need": "la decisión debe estar disponible antes de publicar la lista de contactos",
        "input_requirements": [
            "personas elegibles y contactadas por grupo auditado",
            "beneficio observado por grupo y política",
        ],
        "guardrail": {
            "metric": "contact_rate_gap",
            "maximum_allowed": MAX_CONTACT_RATE_GAP,
            "meaning": "la diferencia entre las tasas de contacto de grupos auditados no puede superar diez puntos porcentuales",
        },
        "authority": "el responsable de cumplimiento aprueba la política; una brecha superior al límite suspende la campaña y se escala al responsable de la política y al comité de equidad",
        "monitoring": [
            "brecha de tasa de contacto por política y grupo",
            "beneficio por persona elegible por política y grupo",
            "grupos incluidos y excluidos de la auditoría",
        ],
        "review_triggers": [
            "brecha de tasa de contacto superior a diez puntos porcentuales",
            "incorporación de un nuevo grupo, regla de elegibilidad o fuente de datos",
            "cambio material en el beneficio observado o en la capacidad de contacto",
        ],
    }


def main():
    policy_impacts = pd.read_csv(DATA_DIR / "policy_impacts.csv")
    audit = audit_policy_equity(policy_impacts)
    decisions = decide_policy_correction(audit)
    contract = build_policy_contract()
    monitoring = pd.DataFrame(
        [
            {
                "metric": "contact_rate_gap",
                "guardrail": MAX_CONTACT_RATE_GAP,
                "review_trigger": "gap above ten percentage points",
                "owner": "compliance owner",
            },
            {
                "metric": "benefit_per_eligible",
                "guardrail": "review by audited group",
                "review_trigger": "material change in observed benefit",
                "owner": "policy owner",
            },
        ]
    )

    audit.to_csv(SUBMISSION_DIR / "equity_audit.csv", index=False)
    decisions.to_csv(SUBMISSION_DIR / "policy_correction_decisions.csv", index=False)
    monitoring.to_csv(SUBMISSION_DIR / "policy_monitoring.csv", index=False)
    (SUBMISSION_DIR / "policy_contract.json").write_text(
        json.dumps(contract, indent=2, ensure_ascii=False) + "\n"
    )


if __name__ == "__main__":
    main()
