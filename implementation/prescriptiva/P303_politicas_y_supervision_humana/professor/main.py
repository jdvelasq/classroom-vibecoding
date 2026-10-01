import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def apply_review_policy(applications: pd.DataFrame) -> pd.DataFrame:
    result = applications.copy()
    result["policy_version"] = "P303-v1"
    result["decision_cadence"] = "cada solicitud recibida"
    result["response_target"] = "recomendación durante la revisión de la solicitud"
    result["execution_mode"] = "recomendación_con_aprobación_humana"
    result["action"] = "escalar_a_revisión_humana"
    result["reason"] = "riesgo intermedio: se requiere juicio documentado"
    result["human_authority"] = "analista_de_crédito"
    result["review_trigger"] = "resultado, excepción o cambio de política"
    result["outcome_to_monitor"] = "incumplimiento y tiempo de decisión"

    incomplete_documents = ~result.documentation_complete
    high_amount = result.requested_amount > 10_000
    low_risk = result.default_probability < 0.08
    high_risk = result.default_probability > 0.30

    result.loc[incomplete_documents, "reason"] = "documentación incompleta"
    result.loc[incomplete_documents, "human_authority"] = "gestor_de_documentación"
    result.loc[incomplete_documents, "review_trigger"] = "documentación completada"

    result.loc[~incomplete_documents & high_amount, "reason"] = (
        "monto superior al límite delegable"
    )
    result.loc[~incomplete_documents & high_amount, "human_authority"] = (
        "supervisor_de_crédito"
    )

    approve = ~incomplete_documents & ~high_amount & low_risk
    reject = ~incomplete_documents & ~high_amount & high_risk
    result.loc[approve, "action"] = "recomendar_aprobación"
    result.loc[approve, "reason"] = "riesgo bajo dentro del límite delegable"
    result.loc[reject, "action"] = "recomendar_rechazo"
    result.loc[reject, "reason"] = "riesgo alto dentro del límite delegable"

    return result


def policy_contract() -> dict:
    return {
        "policy_version": "P303-v1",
        "decision": "revisar solicitudes de crédito",
        "cadence": "cada solicitud recibida",
        "response_target": "recomendación durante la revisión de la solicitud",
        "actions": [
            "recomendar_aprobación",
            "recomendar_rechazo",
            "escalar_a_revisión_humana",
        ],
        "safeguards": [
            "no se automatiza la decisión crediticia",
            "la documentación incompleta siempre escala",
            "los montos superiores al límite delegable requieren supervisor",
        ],
        "review_trigger": "resultado, excepción o cambio de política",
        "outcomes_to_monitor": ["incumplimiento", "tiempo de decisión"],
    }


def main() -> None:
    applications = pd.read_csv(ROOT / "data" / "applications.csv")
    policy = apply_review_policy(applications)
    policy.to_csv(ROOT / "submission" / "review_policy.csv", index=False)
    (ROOT / "submission" / "policy_contract.json").write_text(
        json.dumps(policy_contract(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
