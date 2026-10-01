from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def simulate_project(parameters: pd.Series, n_simulations: int = 10_000) -> pd.DataFrame:
    rng = np.random.default_rng(20260923)
    years = np.arange(1, int(parameters.years) + 1)
    revenue_factor = rng.lognormal(-0.5 * parameters.revenue_sigma**2, parameters.revenue_sigma, (n_simulations, len(years)))
    margin_factor = np.clip(rng.normal(1, parameters.margin_sigma, (n_simulations, len(years))), 0.7, 1.3)
    revenues = parameters.base_revenue * revenue_factor
    cashflows = revenues * (1 - parameters.variable_cost_rate * margin_factor) - parameters.fixed_cost
    npv = -parameters.initial_investment + (cashflows / (1 + parameters.discount_rate) ** years).sum(axis=1)
    return pd.DataFrame({"simulation_id": np.arange(1, n_simulations + 1), "npv": npv})


def summarize_risk(simulations: pd.DataFrame) -> pd.DataFrame:
    loss_probability = (simulations.npv < 0).mean()
    mean_npv = simulations.npv.mean()
    return pd.DataFrame([{
        "mean_npv": mean_npv,
        "p10_npv": simulations.npv.quantile(0.10),
        "loss_probability": loss_probability,
    }])


def define_investment_policy(risk_summary: pd.DataFrame) -> pd.DataFrame:
    risk = risk_summary.iloc[0]

    if risk.mean_npv <= 0:
        action = "no_aprobar"
        authority = "Comité de inversión"
        rationale = "El valor esperado no compensa la inversión inicial."
    elif risk.loss_probability > 0.35 or risk.p10_npv < -100_000:
        action = "escalar_para_revision"
        authority = "Comité de inversión y dirección financiera"
        rationale = "El retorno esperado es positivo, pero el riesgo supera la guarda aprobada."
    else:
        action = "aprobar_inversion"
        authority = "Dirección financiera"
        rationale = "El retorno esperado y las guardas de riesgo permiten financiar el proyecto."

    return pd.DataFrame([{
        "decision_cadence": "Comité mensual mientras la expansión esté en evaluación",
        "response_need": "Decisión documentada antes del siguiente ciclo presupuestal",
        "action": action,
        "authority": authority,
        "objective": "Financiar expansiones con valor esperado positivo sin exceder el riesgo tolerado.",
        "guardrail_loss_probability": 0.35,
        "guardrail_p10_npv": -100_000,
        "exception": "Supuestos nuevos o evidencia no representada en la simulación.",
        "review_metric": "Ingresos realizados frente al escenario base aprobado",
        "review_trigger": "Recalibrar y escalar si los ingresos acumulados caen 15% o más bajo el escenario base.",
        "rationale": rationale,
    }])


def main() -> None:
    parameters = pd.read_csv(ROOT / "data" / "project_parameters.csv").iloc[0]
    risk_summary = summarize_risk(simulate_project(parameters))
    policy = define_investment_policy(risk_summary)

    risk_summary.to_csv(ROOT / "submission" / "project_risk_summary.csv", index=False)
    policy.to_csv(ROOT / "submission" / "investment_policy.csv", index=False)


if __name__ == "__main__":
    main()
