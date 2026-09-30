from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
RAW_DIR = ACTIVITY_DIR / "temp" / "raw"
REPORT_PATH = ACTIVITY_DIR / "submission" / "ingestion_report.csv"


def main():
    batches = sorted(DATA_DIR.glob("superstore_orders_*.csv"))
    assert batches

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    for batch_path in batches:
        orders = pd.read_csv(batch_path, sep=";", encoding="utf-8-sig", decimal=",")
        raw_path = RAW_DIR / f"{batch_path.stem}.parquet"
        orders.to_parquet(raw_path, index=False)
        results.append(
            {
                "source_name": batch_path.name,
                "row_count": len(orders),
                "status": "SUCCESS",
                "raw_path": raw_path.relative_to(ACTIVITY_DIR).as_posix(),
            }
        )

    pd.DataFrame(results).to_csv(REPORT_PATH, index=False)


if __name__ == "__main__":
    main()
