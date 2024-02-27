from datetime import datetime, timedelta
from MarketTime.market_time import MarketTime


class StockMarketTime(MarketTime):

    @staticmethod
    def in_open_time(time: datetime = None) -> bool:
        """
        To check if the time is in stock market open time.\n
        Regular open time:
        09:00~13:30
        """
        time = time or datetime.now()
        morning_open_time = time.replace(
            hour=9, minute=00, second=0, microsecond=0
        )
        morning_close_time = time.replace(
            hour=13, minute=30, second=0, microsecond=0
        )
        today_is_open_day = StockMarketTime.in_open_day(time)
        if (
            today_is_open_day
            and morning_open_time <= time <= morning_close_time
        ):
            return True
        else:
            return False

    @staticmethod
    def next_open_time(time: datetime = None) -> datetime:
        """Return the next market open time based on 'time'.\n
        If the 'time' is in the market time, return 'time'"""
        time = time or datetime.now()
        if StockMarketTime.in_open_time(time):
            return time
        morning_open_time = time.replace(
            hour=9, minute=0, second=0, microsecond=0
        )
        if StockMarketTime.in_open_day(time) and time < morning_open_time:
            return morning_open_time
        next_open_time = morning_open_time + timedelta(days=1)
        while not StockMarketTime.in_open_time(next_open_time):
            next_open_time += timedelta(days=1)
        return next_open_time

    @staticmethod
    def last_open_time(time: datetime = None) -> datetime:
        """Return the last market open time based on 'time'.\n
        If the 'time' is in the market time, return 'time'"""
        time = time or datetime.now()
        if StockMarketTime.in_open_time(time):
            return time
        morning_close_time = time.replace(
            hour=13, minute=30, second=0, microsecond=0
        )
        if StockMarketTime.in_open_day(time) and morning_close_time < time:
            return morning_close_time
        last_open_time = morning_close_time - timedelta(days=1)
        while not StockMarketTime.in_open_time(last_open_time):
            last_open_time -= timedelta(days=1)
        return last_open_time
