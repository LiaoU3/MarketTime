from datetime import datetime, timedelta
from typing import Sequence


class MarketTime:
    close_date_set = set()

    @staticmethod
    def init_close_date_set(close_date_list: Sequence[str] = None):
        """Init the market close date set.\n
        The date string format should be 'YYYY-mm-dd'"""
        if close_date_list is None:
            return
        for date_str in close_date_list:
            date_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            MarketTime.close_date_set.add(date_date)

    @staticmethod
    def in_open_day(time: datetime = None) -> bool:
        """
        To check if the time is in the market open day.
        """
        time = time or datetime.now()
        date = time.date()
        if date in MarketTime.close_date_set:
            return False
        day = time.weekday()
        if day > 4:
            return False
        return True

    @staticmethod
    def get_next_open_day(time: datetime = None) -> datetime:
        """Return the next market open day excluding today"""
        time = time or datetime.now()
        next_open_day = time + timedelta(days=1)
        while not MarketTime.in_open_day(next_open_day):
            next_open_day += timedelta(days=1)
        return next_open_day

    @staticmethod
    def get_last_open_day(time: datetime = None) -> datetime:
        """Return the last market open day excluding today"""
        time = time or datetime.now()
        last_open_day = time - timedelta(days=1)
        while not MarketTime.in_open_day(last_open_day):
            last_open_day -= timedelta(days=1)
        return last_open_day
