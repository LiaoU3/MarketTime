import unittest
from datetime import datetime
from MarketTime.future_market_time import FutureMarketTime as fmt


class TestFutureMarketTime(unittest.TestCase):
    def setUp(self):
        close_dates = ["2024-04-17"]  # Assume 2024/04-17 is close
        fmt.init_close_date_set(close_dates)

    def tearDown(self):
        fmt.close_date_set = set()

    def test__third_wednesday(self):
        third_wednesday = fmt._third_wednesday(2024, 4)
        self.assertEqual(third_wednesday, datetime(2024, 4, 17).date())

        third_wednesday = fmt._third_wednesday(2024, 5)
        self.assertEqual(third_wednesday, datetime(2024, 5, 15).date())

        third_wednesday = fmt._third_wednesday(2024, 6)
        self.assertEqual(third_wednesday, datetime(2024, 6, 19).date())

    def test__settlement_day(self):
        settlement_day = fmt._settelment_day(2024, 4)
        self.assertEqual(settlement_day, datetime(2024, 4, 16).date())

        settlement_day = fmt._settelment_day(2024, 5)
        self.assertEqual(settlement_day, datetime(2024, 5, 15).date())

        settlement_day = fmt._settelment_day(2024, 6)
        self.assertEqual(settlement_day, datetime(2024, 6, 19).date())

    def test_in_settlement_day(self):
        settlement_day = datetime(2024, 4, 16)
        self.assertTrue(fmt.in_settlement_day(settlement_day))

        not_settlement_day = datetime(2024, 4, 17)
        self.assertFalse(fmt.in_settlement_day(not_settlement_day))

        not_settlement_day = datetime(2024, 4, 18)
        self.assertFalse(fmt.in_settlement_day(not_settlement_day))

        not_settlement_day = datetime(2024, 5, 14)
        self.assertFalse(fmt.in_settlement_day(not_settlement_day))

        settlement_day = datetime(2024, 5, 15)
        self.assertTrue(fmt.in_settlement_day(settlement_day))

    def test_in_open_time_friday(self):
        # Friday
        open_time = datetime(2024, 4, 12, 0, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 12, 5, 0, 0)  # Night close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 12, 7, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 12, 8, 45, 0)  # Morning open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 12, 9, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 12, 13, 30, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 12, 13, 45, 0)  # Morning close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 12, 14, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 12, 15, 0, 0)  # Night open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 12, 20, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

    def test_in_open_time_saturday(self):
        # Saturday
        open_time = datetime(2024, 4, 13, 0, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 13, 5, 0, 0)  # Night close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 13, 7, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 8, 45, 0)  # Morning open time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 9, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 13, 30, 0)  # Morning close time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 13, 45, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 14, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 15, 0, 0)  # Night open time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 13, 20, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

    def test_in_open_time_monday(self):
        # Monday
        close_time = datetime(2024, 4, 15, 0, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 15, 5, 0, 0)  # Night close time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 15, 7, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 15, 8, 45, 0)  # Morning open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 15, 9, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 15, 13, 30, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 15, 13, 45, 0)  # Morning close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 15, 14, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 15, 15, 0, 0)  # Night open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 15, 20, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

    def test_in_open_time_settlementday(self):
        # Settlement day
        open_time = datetime(2024, 4, 16, 0, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 16, 5, 0, 0)  # Night close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 16, 7, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 16, 8, 45, 0)  # Morning open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 16, 9, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 16, 13, 30, 0)  # Morning close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 16, 13, 45, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 16, 14, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 16, 15, 0, 0)  # Night open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 16, 20, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

    def test_in_open_time_closeday(self):
        # Close day
        open_time = datetime(2024, 4, 17, 0, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 17, 5, 0, 0)  # Night close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 17, 7, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 8, 45, 0)  # Morning open time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 9, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 13, 30, 0)  # Morning close time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 13, 45, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 14, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 15, 0, 0)  # Night open time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 17, 20, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

    def test_in_open_time_the_day_after_closeday(self):
        # The day after settlement day
        close_time = datetime(2024, 4, 18, 0, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 18, 5, 0, 0)  # Night close time
        self.assertFalse(fmt.in_open_time(close_time))

        close_time = datetime(2024, 4, 18, 7, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 18, 8, 45, 0)  # Morning open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 18, 9, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 18, 13, 30, 0)
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 18, 13, 45, 0)  # Morning close time
        self.assertTrue(fmt.in_open_time(open_time))

        close_time = datetime(2024, 4, 18, 14, 0, 0)
        self.assertFalse(fmt.in_open_time(close_time))

        open_time = datetime(2024, 4, 18, 15, 0, 0)  # Night open time
        self.assertTrue(fmt.in_open_time(open_time))

        open_time = datetime(2024, 4, 18, 18, 0, 0)
        self.assertTrue(fmt.in_open_time(open_time))

    def test_next_open_time_friday(self):

        time = datetime(2024, 4, 12, 0, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 5, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 7, 0, 0)
        next_open_time = datetime(2024, 4, 12, 8, 45)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 8, 45, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 9, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 13, 30, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 13, 45, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 14, 0, 0)
        next_open_time = datetime(2024, 4, 12, 15, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 15, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 12, 18, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

    def test_next_open_time_saturday(self):
        time = datetime(2024, 4, 13, 0, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 5, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 7, 0, 0)
        next_open_time = datetime(2024, 4, 15, 8, 45)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 8, 45, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 9, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 13, 30, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 13, 45, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 14, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 15, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 13, 18, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

    def test_next_open_time_monday(self):
        time = datetime(2024, 4, 15, 0, 0, 0)
        next_open_time = datetime(2024, 4, 15, 8, 45, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 5, 0, 0)
        next_open_time = datetime(2024, 4, 15, 8, 45, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 7, 0, 0)
        next_open_time = datetime(2024, 4, 15, 8, 45)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 8, 45, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 9, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 13, 30, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 13, 45, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 14, 0, 0)
        next_open_time = datetime(2024, 4, 15, 15, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 15, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 15, 18, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

    def test_next_open_time_settlementday(self):
        time = datetime(2024, 4, 16, 0, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 5, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 7, 0, 0)
        next_open_time = datetime(2024, 4, 16, 8, 45)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 8, 45, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 9, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 13, 30, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 13, 45, 0)
        next_open_time = datetime(2024, 4, 16, 15, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 14, 0, 0)
        next_open_time = datetime(2024, 4, 16, 15, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 15, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 16, 18, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

    def test_next_open_time_closeday(self):
        time = datetime(2024, 4, 17, 0, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 5, 0, 0)
        next_open_time = time
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 7, 0, 0)
        next_open_time = datetime(2024, 4, 18, 8, 45)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 8, 45, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 9, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 13, 30, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 13, 45, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 14, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 15, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

        time = datetime(2024, 4, 17, 18, 0, 0)
        self.assertEqual(fmt.next_open_time(time), next_open_time)

    def test_last_open_time_friday(self):

        time = datetime(2024, 4, 12, 0, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 5, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 7, 0, 0)
        last_open_time = datetime(2024, 4, 12, 5, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 8, 45, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 9, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 13, 30, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 13, 45, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 14, 0, 0)
        last_open_time = datetime(2024, 4, 12, 13, 45, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 15, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 12, 18, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

    def test_last_open_time_saturday(self):

        time = datetime(2024, 4, 13, 0, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 5, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 7, 0, 0)
        last_open_time = datetime(2024, 4, 13, 5, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 8, 45, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 9, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 13, 30, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 13, 45, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 14, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 15, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 13, 18, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

    def test_last_open_time_monday(self):

        time = datetime(2024, 4, 15, 0, 0, 0)
        last_open_time = datetime(2024, 4, 13, 5, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 5, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 7, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 8, 45, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 9, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 13, 30, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 13, 45, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 14, 0, 0)
        last_open_time = datetime(2024, 4, 15, 13, 45, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 15, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 15, 18, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

    def test_last_open_time_settlementday(self):

        time = datetime(2024, 4, 16, 0, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 5, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 7, 0, 0)
        last_open_time = datetime(2024, 4, 16, 5, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 8, 45, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 9, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 13, 30, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 13, 45, 0)
        last_open_time = datetime(2024, 4, 16, 13, 30, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 14, 0, 0)
        last_open_time = datetime(2024, 4, 16, 13, 30, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 15, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 16, 18, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

    def test_last_open_time_closeday(self):

        time = datetime(2024, 4, 17, 0, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 5, 0, 0)
        last_open_time = time
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 7, 0, 0)
        last_open_time = datetime(2024, 4, 17, 5, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 8, 45, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 9, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 13, 30, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 13, 45, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 14, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 15, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

        time = datetime(2024, 4, 17, 18, 0, 0)
        self.assertEqual(fmt.last_open_time(time), last_open_time)

    def test_next_close_time_friday(self):

        time = datetime(2024, 4, 12, 0, 0, 0)
        next_close_time = datetime(2024, 4, 12, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 5, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 7, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 8, 45, 0)
        next_close_time = datetime(2024, 4, 12, 13, 45, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 9, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 13, 30, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 13, 45, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 14, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 15, 0, 0)
        next_close_time = datetime(2024, 4, 13, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 12, 18, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

    def test_next_close_time_saturday(self):

        time = datetime(2024, 4, 13, 0, 0, 0)
        next_close_time = datetime(2024, 4, 13, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 5, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 7, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 8, 45, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 9, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 13, 30, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 13, 45, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 14, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 15, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 13, 18, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

    def test_next_close_time_monday(self):

        time = datetime(2024, 4, 15, 0, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 5, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 7, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 8, 45, 0)
        next_close_time = datetime(2024, 4, 15, 13, 45, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 9, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 13, 30, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 13, 45, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 14, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 15, 0, 0)
        next_close_time = datetime(2024, 4, 16, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 15, 18, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

    def test_next_close_time_settlementday(self):

        time = datetime(2024, 4, 16, 0, 0, 0)
        next_close_time = datetime(2024, 4, 16, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 5, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 7, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 8, 45, 0)
        next_close_time = datetime(2024, 4, 16, 13, 30, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 9, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 13, 30, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 13, 45, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 14, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 15, 0, 0)
        next_close_time = datetime(2024, 4, 17, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 16, 18, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

    def test_next_close_time_closeday(self):

        time = datetime(2024, 4, 17, 0, 0, 0)
        next_close_time = datetime(2024, 4, 17, 5, 0, 0, 1)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 5, 0, 0)
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 7, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 8, 45, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 9, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 13, 30, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 13, 45, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 14, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 15, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

        time = datetime(2024, 4, 17, 18, 0, 0)
        next_close_time = time
        self.assertEqual(fmt.next_close_time(time), next_close_time)

    def test_last_close_time_friday(self):

        time = datetime(2024, 4, 12, 0, 0, 0)
        last_close_time = datetime(2024, 4, 11, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 5, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 7, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 8, 45, 0)
        last_close_time = datetime(2024, 4, 12, 8, 44, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 9, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 13, 30, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 13, 45, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 14, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 15, 0, 0)
        last_close_time = datetime(2024, 4, 12, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 12, 18, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

    def test_last_close_time_saturday(self):

        time = datetime(2024, 4, 13, 0, 0, 0)
        last_close_time = datetime(2024, 4, 12, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 5, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 7, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 8, 45, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 9, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 13, 30, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 13, 45, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 14, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 15, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 13, 18, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

    def test_last_close_time_monday(self):

        time = datetime(2024, 4, 15, 0, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 5, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 7, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 8, 45, 0)
        last_close_time = datetime(2024, 4, 15, 8, 44, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 9, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 13, 30, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 13, 45, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 14, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 15, 0, 0)
        last_close_time = datetime(2024, 4, 15, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 15, 18, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

    def test_last_close_time_settlementday(self):

        time = datetime(2024, 4, 16, 0, 0, 0)
        last_close_time = datetime(2024, 4, 15, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 5, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 7, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 8, 45, 0)
        last_close_time = datetime(2024, 4, 16, 8, 44, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 9, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 13, 30, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 13, 45, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 14, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 15, 0, 0)
        last_close_time = datetime(2024, 4, 16, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 16, 18, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

    def test_last_close_time_closeday(self):

        time = datetime(2024, 4, 17, 0, 0, 0)
        last_close_time = datetime(2024, 4, 16, 14, 59, 59, 999999)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 5, 0, 0)
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 7, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 8, 45, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 9, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 13, 30, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 13, 45, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 14, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 15, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)

        time = datetime(2024, 4, 17, 18, 0, 0)
        last_close_time = time
        self.assertEqual(fmt.last_close_time(time), last_close_time)


if __name__ == "__main__":
    unittest.main()
