from datetime import datetime, date, timedelta
from typing import Sequence, Union


class MarketTime:
    close_date_set = set()

    @staticmethod
    def init_close_date_set(close_date_list: Sequence[str] = None):
        """Init the market close date set.
        The date string format should be 'YYYY-mm-dd'"""
        if close_date_list is None:
            return
        for date_str in close_date_list:
            date_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            MarketTime.close_date_set.add(date_date)

    @staticmethod
    def _get_date_obj(time: Union[datetime, date] = None) -> date:
        if isinstance(time, datetime):
            date_obj = time.date()
        elif isinstance(time, date):
            date_obj = time
        else:
            date_obj = datetime.now().date()
        return date_obj

    @staticmethod
    def in_open_day(time: Union[datetime, date] = None) -> bool:
        """
        To check if the time (datetime, date) is in the market open day.
        """
        date_obj = MarketTime._get_date_obj(time)
        if date_obj in MarketTime.close_date_set:
            return False
        weekday = date_obj.weekday()
        if weekday > 4:
            return False
        return True

    @staticmethod
    def next_open_day(time: Union[datetime, date] = None) -> date:
        """Return the next market open day excluding today"""
        date_obj = MarketTime._get_date_obj(time)
        next_open_day = date_obj + timedelta(days=1)
        while not MarketTime.in_open_day(next_open_day):
            next_open_day += timedelta(days=1)
        return next_open_day

    @staticmethod
    def last_open_day(time: Union[datetime, date] = None) -> date:
        """Return the last market open day excluding today"""
        date_obj = MarketTime._get_date_obj(time)
        last_open_day = date_obj - timedelta(days=1)
        while not MarketTime.in_open_day(last_open_day):
            last_open_day -= timedelta(days=1)
        return last_open_day
