"""Construye la política operativa de capacidad hospitalaria del caso."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def build_capacity_policy(
    hospital: pd.DataFrame, evaluated_plans: pd.DataFrame
) -> tuple[pd.DataFrame, dict[str, object]]:
    """Expresa el plan recomendado como una política con escalamiento gobernado."""
    hospital_row = hospital.iloc[0]
    recommended = evaluated_plans.loc[evaluated_plans.is_recommended].iloc[0]

    capacity_policy = pd.DataFrame(
        [
            {
                "policy_step": "capacidad_base",
                "observable_context": "Pronóstico base vigente al inicio del horizonte",
                "action": "activar_un_bloque",
                "activation_day": int(recommended.activation_day),
                "available_day": int(recommended.available_day),
                "added_beds": int(recommended.added_beds),
                "decision_cadence": "Una vez al inicio del horizonte y revisión diaria",
                "response_need": "La capacidad tarda cuatro días en estar disponible",
                "human_authority": "Comando de incidentes hospitalario con validación clínica y operativa",
                "safeguard": "No reducir capacidad clínica existente ni automatizar decisiones de atención a pacientes",
                "review_trigger": "Revisar diariamente la probabilidad del escenario alto y la ocupación observada",
            },
            {
                "policy_step": "escalamiento_contingente",
                "observable_context": "La probabilidad revisada del escenario alto alcanza 0.30 o más",
                "action": "escalar_un_segundo_bloque",
                "activation_day": int(recommended.activation_day),
                "available_day": int(recommended.available_day),
                "added_beds": int(hospital_row.beds_per_block),
                "decision_cadence": "Revisión diaria mientras haya expansión disponible",
                "response_need": "Autorizar el segundo bloque antes de que el plazo de cuatro días impida cubrir el pico",
                "human_authority": "Comando de incidentes; la dirección clínica puede suspender o modificar el escalamiento",
                "safeguard": "Confirmar personal, equipos y seguridad clínica antes de abrir el bloque adicional",
                "review_trigger": "Suspender o recalibrar si cambian la demanda, el plazo de activación o los recursos clínicos",
            },
        ]
    )

    policy_contract = {
        "policy_name": "capacidad_hospitalaria_por_demanda",
        "decision": "Activar y escalar bloques de camas ante demanda incierta.",
        "decision_owner": "Comando de incidentes hospitalario",
        "decision_cadence": "Revisión diaria durante el horizonte de 21 días",
        "response_need": f"Cada bloque requiere {int(hospital_row.lead_time_days)} días de preparación.",
        "baseline_action": "Activar un bloque el día 5 para disponer de 20 camas el día 9.",
        "escalation_trigger": "Probabilidad revisada del escenario alto mayor o igual a 0.30.",
        "safeguards": [
            "La política no sustituye el juicio clínico ni automatiza la asignación de pacientes.",
            "La apertura exige confirmar personal, equipos y condiciones de seguridad.",
            "La dirección clínica puede suspender, modificar o escalar la acción recomendada.",
        ],
        "monitoring": [
            "Demanda y ocupación observadas diariamente.",
            "Probabilidad revisada de demanda alta.",
            "Camas-día no cubiertas y camas de expansión ociosas.",
        ],
        "review_trigger": "Cambio material de demanda, recursos clínicos o plazo de activación.",
    }
    return capacity_policy, policy_contract


def write_policy_artifacts(
    hospital: pd.DataFrame, evaluated_plans: pd.DataFrame, submission_dir: Path
) -> tuple[pd.DataFrame, dict[str, object]]:
    """Guarda la evidencia persistente de la política del taller."""
    capacity_policy, policy_contract = build_capacity_policy(hospital, evaluated_plans)
    capacity_policy.to_csv(submission_dir / "capacity_policy.csv", index=False)
    (submission_dir / "policy_contract.json").write_text(
        json.dumps(policy_contract, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return capacity_policy, policy_contract
