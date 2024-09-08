import unittest
from datetime import datetime, date
from MarketTime.market_time import MarketTime as mt


class TestMarketTime(unittest.TestCase):
    def setUp(self):
        close_dates = ["2024-04-04", "2024-04-05"]
        mt.init_close_date_set(close_dates)

    def tearDown(self):
        mt.close_date_set = set()

    def test_init_close_date_set(self):
        self.assertTrue(
            datetime(2024, 4, 4).date() in mt.close_date_set
        )  # in close_dates
        self.assertTrue(
            datetime(2024, 4, 5).date() in mt.close_date_set
        )  # in close_dates
        self.assertFalse(
            datetime(2024, 4, 6).date() in mt.close_date_set
        )  # not in close_dates
        self.assertTrue(len(mt.close_date_set) == 2)

    def test_init_close_date_set_with_none(self):
        mt.close_date_set.clear()
        mt.init_close_date_set(None)
        self.assertEqual(len(mt.close_date_set), 0)

    def test__get_date_obj(self):
        time = datetime.now()
        self.assertTrue(time.date(), mt._get_date_obj(time))  # datetime
        self.assertTrue(time.date(), mt._get_date_obj(time.date()))  # date
        self.assertTrue(isinstance(mt._get_date_obj(), date))  # None
        self.assertRaises(TypeError, mt._get_date_obj, "Unexpected type")

    def test_in_open_day(self):
        open_day = datetime(2024, 4, 1)  # Monday
        self.assertTrue(mt.in_open_day(open_day))

        open_day = datetime(2024, 4, 2)  # Tuesday
        self.assertTrue(mt.in_open_day(open_day))

        open_day = datetime(2024, 4, 3)  # Wednesday
        self.assertTrue(mt.in_open_day(open_day))

        close_day = datetime(2024, 4, 4)  # Thursday but in close_dates
        self.assertFalse(mt.in_open_day(close_day))

        close_day = datetime(2024, 4, 5)  # Friday but in close_dates
        self.assertFalse(mt.in_open_day(close_day))

        close_day = datetime(2024, 4, 6)  # Saturday
        self.assertFalse(mt.in_open_day(close_day))

        close_day = datetime(2024, 4, 7)  # Sunday
        self.assertFalse(mt.in_open_day(close_day))

    def test_next_open_day(self):
        today = datetime(2024, 4, 1)  # Monday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 2).date())

        today = datetime(2024, 4, 2)  # Tuesday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 3).date())

        today = datetime(2024, 4, 3)  # Wednesday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 8).date())

        today = datetime(2024, 4, 4)  # Thursday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 8).date())

        today = datetime(2024, 4, 5)  # Friday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 8).date())

        today = datetime(2024, 4, 6)  # Saturday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 8).date())

        today = datetime(2024, 4, 7)  # Sunday
        next_open_day = mt.next_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 8).date())

    def test_last_open_day(self):
        today = datetime(2024, 4, 1)  # Monday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 3, 29).date())

        today = datetime(2024, 4, 2)  # Tuesday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 1).date())

        today = datetime(2024, 4, 3)  # Wednesday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 2).date())

        today = datetime(2024, 4, 4)  # Thursday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 3).date())

        today = datetime(2024, 4, 5)  # Friday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 3).date())

        today = datetime(2024, 4, 6)  # Saturday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 3).date())

        today = datetime(2024, 4, 7)  # Sunday
        next_open_day = mt.last_open_day(today)
        self.assertEqual(next_open_day, datetime(2024, 4, 3).date())
