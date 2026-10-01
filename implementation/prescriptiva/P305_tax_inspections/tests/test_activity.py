from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
EXPECTED_ARTIFACTS = {
    "inspection_decisions.csv",
    "portfolio_comparison.csv",
    "capacity_sensitivity.csv",
    "inspection_recommendations.csv",
    "inspection_policy.json",
    "tax_inspection_planner.png",
}


def test_01_submission_contains_the_policy_evidence():
    missing = sorted(
        name for name in EXPECTED_ARTIFACTS if not (SUBMISSION_DIR / name).is_file()
    )

    assert not missing, (
        "Ejecuta la solución y guarda los artefactos de la política en submission/: "
        + ", ".join(missing)
    )
