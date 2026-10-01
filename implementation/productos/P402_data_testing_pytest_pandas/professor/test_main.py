import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from main import validate_data


def test_01_accepts_data_that_satisfies_the_contract():
    dataframe = pd.DataFrame(
        [
            {
                "factory_id": 1,
                "machine_id": 2,
                "daily_units_produced": 4500,
                "factory_date": "2026-10-01",
            }
        ]
    )

    assert validate_data(dataframe) == []


def test_02_reports_a_duplicate_business_key():
    dataframe = pd.DataFrame(
        [
            {
                "factory_id": 1,
                "machine_id": 2,
                "daily_units_produced": 4500,
                "factory_date": "2026-10-01",
            },
            {
                "factory_id": 1,
                "machine_id": 2,
                "daily_units_produced": 4600,
                "factory_date": "2026-10-01",
            },
        ]
    )

    assert validate_data(dataframe) == [
        "La llave factory_id-machine_id-factory_date debe ser única."
    ]
