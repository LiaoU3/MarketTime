from datetime import datetime, timedelta, date
from MarketTime.market_time import MarketTime
from typing import Union


class FutureMarketTime(MarketTime):

    @staticmethod
    def _third_wednesday(year: int, month: int) -> date:
        """
        Get the third Wednesday in the certain year month
        """
        first_wednesday = datetime(year, month, 1).date()
        while first_wednesday.weekday() != 2:
            first_wednesday += timedelta(days=1)
        third_wednesday = first_wednesday + timedelta(weeks=2)
        return third_wednesday

    @staticmethod
    def _settelment_day(year: int, month: int) -> date:
        settlement_day = FutureMarketTime._third_wednesday(year, month)
        while not FutureMarketTime.in_open_day(settlement_day):
            settlement_day -= timedelta(days=1)
        return settlement_day

    @staticmethod
    def in_settlement_day(time: Union[datetime, date] = None) -> datetime:
        """Check if 'time' is in the expiration day"""
        date_obj = FutureMarketTime._get_date_obj(time)
        if 21 < date_obj.day:
            return False
        if date_obj == FutureMarketTime._settelment_day(
            date_obj.year, date_obj.month
        ):
            return True
        return False

    @staticmethod
    def in_open_time(time: datetime = None) -> bool:
        """
        To check if the 'time' is in future market open time.\n
        Regular open time:
        08:45~13:45
        15:00~05:00 (+1)
        """
        time = time or datetime.now()
        if FutureMarketTime.in_settlement_day(time):
            morning_close_minute = 30
        else:
            morning_close_minute = 45
        night_close = time.replace(hour=5, minute=0, second=0, microsecond=0)
        morning_start = time.replace(
            hour=8, minute=45, second=0, microsecond=0
        )
        morning_close = time.replace(
            hour=13, minute=morning_close_minute, second=0, microsecond=0
        )
        night_start = time.replace(hour=15, minute=0, second=0, microsecond=0)
        yesterday = time - timedelta(days=1)
        yesterday_is_open_day = FutureMarketTime.in_open_day(yesterday)
        today_is_open_day = FutureMarketTime.in_open_day(time)
        if today_is_open_day:
            if yesterday_is_open_day:
                if (
                    night_close < time < morning_start
                    or morning_close < time < night_start
                ):
                    return False
                else:
                    return True
            else:
                if (
                    morning_start <= time <= morning_close
                    or night_start <= time
                ):
                    return True
                else:
                    return False
        elif not today_is_open_day and yesterday_is_open_day:
            if time <= night_close:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def next_open_time(time: datetime = None) -> datetime:
        """Return the next market open time based on 'time'.
        If the 'time' is in the market time, return 'time'"""
        time = time or datetime.now()
        if FutureMarketTime.in_open_time(time):
            return time
        morning_open = time.replace(hour=8, minute=45, second=0, microsecond=0)
        night_open = time.replace(hour=15, minute=0, second=0, microsecond=0)
        today_is_open_day = FutureMarketTime.in_open_day(time)
        if today_is_open_day:
            if time < morning_open:
                next_open_time = morning_open
            else:
                next_open_time = night_open
        else:
            next_open_time = morning_open + timedelta(days=1)
            while not FutureMarketTime.in_open_time(next_open_time):
                next_open_time += timedelta(days=1)
        return next_open_time

    @staticmethod
    def last_open_time(time: datetime = None) -> datetime:
        """Return the last market open time based on 'time'.
        If the 'time' is in the market time, return 'time'"""
        time = time or datetime.now()
        if FutureMarketTime.in_open_time(time):
            return time
        morning_close_minute = (
            30 if FutureMarketTime.in_settlement_day(time) else 45
        )
        night_close = time.replace(hour=5, minute=0, second=0, microsecond=0)
        morning_close = time.replace(
            hour=13, minute=morning_close_minute, second=0, microsecond=0
        )
        today_is_open_day = FutureMarketTime.in_open_day(time)
        if today_is_open_day and time >= morning_close:
            last_open_time = morning_close
        else:
            last_open_time = night_close
            while not FutureMarketTime.in_open_time(last_open_time):
                last_open_time -= timedelta(days=1)
        return last_open_time

    @staticmethod
    def next_close_time(time: datetime = None) -> datetime:
        time = time or datetime.now()
        if not FutureMarketTime.in_open_time(time):
            return time
        morning_close_minute = (
            30 if FutureMarketTime.in_settlement_day(time) else 45
        )
        night_close = time.replace(hour=5, minute=0, second=0, microsecond=0)
        morning_close = time.replace(
            hour=13, minute=morning_close_minute, second=0, microsecond=0
        )
        today_is_open_day = FutureMarketTime.in_open_day(time)
        if today_is_open_day and time < morning_close:
            if time < night_close:
                next_close_time = night_close
            else:
                next_close_time = morning_close
        else:
            next_close_time = night_close
            while not FutureMarketTime.in_open_time(next_close_time):
                next_close_time += timedelta(days=1)
        return next_close_time + timedelta(microseconds=1)

    @staticmethod
    def last_close_time(time: datetime = None) -> datetime:
        """Return the last close time based on 'time.
        If 'time' is in close time, return 'time'"""
        """8:45 15:00"""
        time = time or datetime.now()
        if not FutureMarketTime.in_open_time(time):
            return time
        morning_open = time.replace(hour=8, minute=45, second=0, microsecond=0)
        night_open = time.replace(hour=15, minute=0, second=0, microsecond=0)
        today_is_open_day = FutureMarketTime.in_open_day(time)
        if today_is_open_day and time >= morning_open:
            if time > night_open:
                last_close_time = night_open
            else:
                last_close_time = morning_open
        else:
            last_close_time = night_open - timedelta(days=1)
            while not FutureMarketTime.in_open_time(last_close_time):
                last_close_time -= timedelta(days=1)
        return last_close_time - timedelta(microseconds=1)
