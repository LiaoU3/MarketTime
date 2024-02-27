from datetime import datetime, timedelta, date
from MarketTime.market_time import MarketTime


class FutureMarketTime(MarketTime):
    expiration_date_set = set()

    @staticmethod
    def init_expiration_date_set_in_the_next_5_years(
        time: datetime = None,
    ) -> None:
        """Init the expiration date set in the next 2 years based on 'time'.\n
        The reason why we use a set to store the date instead of
        dynamical check is the performance issue."""
        time = time or datetime.now()
        current_year = time.year
        for year in range(current_year, current_year + 6):
            for month in range(1, 13):
                expiration_date = FutureMarketTime._get_third_wednesday(
                    year, month
                )
                expiration_date_with_time = datetime.combine(
                    expiration_date, datetime.min.time()
                )
                while not FutureMarketTime.in_open_day(
                    expiration_date_with_time
                ):
                    expiration_date_with_time -= timedelta(days=1)
                FutureMarketTime.expiration_date_set.add(
                    expiration_date_with_time.date()
                )

    @staticmethod
    def _get_third_wednesday(year: int, month: int) -> date:
        """
        Get the third Wednesday in the certain year month
        """
        first_wednesday = datetime(year, month, 1).date()
        while first_wednesday.weekday() != 2:
            first_wednesday += timedelta(days=1)
        third_wednesday = first_wednesday + timedelta(weeks=2)
        return third_wednesday

    @staticmethod
    def in_expiration_day(time: datetime = None) -> datetime:
        """Check if 'time' is in the expiration day"""
        if time is None:
            time = datetime.now()
        date = time.date()
        return date in FutureMarketTime.expiration_date_set

    @staticmethod
    def in_open_time(time: datetime = None) -> bool:
        """
        To check if the 'time' is in future market open time.\n
        Regular open time:
        08:45~13:45
        15:00~05:00 (+1)
        """
        if time is None:
            time = datetime.now()
        if FutureMarketTime.in_expiration_day(time):
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
        """Return the next market open time based on 'time'.\n
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
        """Return the last market open time based on 'time'.\n
        If the 'time' is in the market time, return 'time'"""
        time = time or datetime.now()
        if FutureMarketTime.in_open_time(time):
            return time
        if FutureMarketTime.in_expiration_day(time):
            morning_close_minute = 30
        else:
            morning_close_minute = 45
        night_close = time.replace(hour=5, minute=0, second=0, microsecond=0)
        morning_close = time.replace(
            hour=13, minute=morning_close_minute, second=0, microsecond=0
        )
        today_is_open_day = FutureMarketTime.in_open_day(time)
        if today_is_open_day and time > morning_close:
            last_open_time = morning_close
        else:
            last_open_time = night_close
            while not FutureMarketTime.in_open_time(last_open_time):
                last_open_time -= timedelta(days=1)
        return last_open_time
