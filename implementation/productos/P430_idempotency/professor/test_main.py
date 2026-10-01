import importlib.util
import json
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "p430_professor_main", ACTIVITY_DIR / "professor" / "main.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_generate_daily_report_reuses_the_persisted_result(tmp_path, monkeypatch):
    """Reintentar no debe crear una segunda versión del mismo reporte diario."""

    output_path = tmp_path / "daily_report.json"
    monkeypatch.setattr(MODULE, "OUTPUT_PATH", output_path)

    first_report = MODULE.generate_daily_report()
    output_path.write_text(
        json.dumps({"report_date": "2026-09-24", "risk": "low"}), encoding="utf-8"
    )
    second_report = MODULE.generate_daily_report()

    assert first_report["risk"] == "high"
    assert second_report == {"report_date": "2026-09-24", "risk": "low"}
