import unittest

from main import summarize_by_factory


class TestSummarizeByFactory(unittest.TestCase):
    def test_01_sums_daily_units_for_each_factory(self):
        operations = [
            {"factory_id": 2, "daily_units_produced": 4600},
            {"factory_id": 1, "daily_units_produced": 4770},
            {"factory_id": 2, "daily_units_produced": 4700},
            {"factory_id": 1, "daily_units_produced": 4533},
        ]

        self.assertEqual(
            summarize_by_factory(operations),
            [
                {"factory_id": 1, "total_units": 9303},
                {"factory_id": 2, "total_units": 9300},
            ],
        )
