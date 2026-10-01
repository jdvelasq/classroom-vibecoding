import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
TEMP_DIR = ACTIVITY_DIR / "temp" / "pipeline"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
SOURCE_NAMES = ["orders", "customers", "products", "order_lines"]
REQUIRED_COLUMNS = [
    "Sales",
    "Profit",
    "Customer Segment",
    "Region",
    "Product Category",
]
QUESTION = "¿Qué segmentos y regiones concentran las ventas y la utilidad?"


def extract():
    raw_dir = TEMP_DIR / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    sources = {}
    for name in SOURCE_NAMES:
        frame = pd.read_csv(DATA_DIR / f"{name}.csv")
        frame.to_csv(raw_dir / f"{name}.csv", index=False)
        sources[name] = frame
    return sources


def transform(sources):
    curated = (
        sources["order_lines"]
        .merge(sources["orders"], on="order_context_key", validate="many_to_one")
        .merge(sources["customers"], on="customer_context_key", validate="many_to_one")
        .merge(sources["products"], on="product_context_key", validate="many_to_one")
    )
    assert len(curated) == len(sources["order_lines"])
    assert curated[REQUIRED_COLUMNS].notna().all().all()
    return curated


def publish(curated, sources):
    staging_dir = TEMP_DIR / "staging"
    curated_dir = TEMP_DIR / "curated"
    staging_dir.mkdir(parents=True, exist_ok=True)
    curated_dir.mkdir(parents=True, exist_ok=True)

    curated.to_csv(staging_dir / "superstore_enriched_sales.csv", index=False)
    curated.to_csv(curated_dir / "superstore_enriched_sales.csv", index=False)
    curated.to_csv(SUBMISSION_DIR / "superstore_enriched_sales.csv", index=False)

    answer = (
        curated.groupby(["Customer Segment", "Region"], as_index=False)
        .agg(sales=("Sales", "sum"), profit=("Profit", "sum"))
        .sort_values(["sales", "profit"], ascending=False)
    )
    answer.to_csv(SUBMISSION_DIR / "sales_by_segment_region.csv", index=False)
    report = pd.DataFrame(
        [
            ("raw", sum(len(source) for source in sources.values()), "SUCCESS"),
            ("staging", len(curated), "SUCCESS"),
            ("curated", len(curated), "SUCCESS"),
        ],
        columns=["stage", "rows", "status"],
    )
    report.to_csv(SUBMISSION_DIR / "pipeline_report.csv", index=False)

    questions = [{"pregunta": QUESTION, "archivo_respuesta": "sales_by_segment_region.csv"}]
    (SUBMISSION_DIR / "questions.json").write_text(
        json.dumps(questions, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main():
    sources = extract()
    publish(transform(sources), sources)


if __name__ == "__main__":
    main()
