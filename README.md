# MarketTime

MarketTime is a Python module designed to track and detect market time in Taiwan, focusing on stock and futures markets. It provides functionalities to manage and analyze market time data, including determining whether the market is open, retrieving the next and last market open times, and checking for expiration days in futures markets.

## Introduction

MarketTime offers two main classes:

- **FutureMarketTime**: Extends MarketTime to handle futures markets, offering features such as identifying settlement days and predicting future market open and close times.
- **StockMarketTime**: Extends MarketTime to handle stock markets, offering functions to determine whether a given time falls within stock market open hours, as well as predicting the next and last market open times.

## Features

- **Market Time Detection**: Determine if the current time is within market hours.
- **Next and Last Market Times**: Predict and retrieve the next and last market open times.

## Installation

You can install MarketTime via pip:

```bash
pip install MarketTime
```

## Usage

Here is how you can use the `FutureMarketTime` and `StockMarketTime` in your Python scripts:

```python
from MarketTime import FutureMarketTime as fmt, StockMarketTime as smt
from datetime import datetime

dates_list = [
    "2024-01-01",
    "2024-02-06",
    "2024-02-07",
    "2024-02-08",
    "2024-02-09",
    "2024-02-10",
    "2024-02-11",
    "2024-02-12",
    "2024-02-13",
    "2024-02-14",
    "2024-02-28",
    "2024-04-04",
    "2024-04-05",
    "2024-05-01",
    "2024-06-10",
    "2024-09-17",
    "2024-10-10"
]
# Always init the close date set
smt.init_close_date_set(dates_list)
fmt.init_close_date_set(dates_list)


# Check if a given date is the expiration day for futures contracts
is_settlement_day = fmt.in_settlement_day(datetime.now())
print("Is today a settlement day for futures contracts?", is_settlement_day)

# Check if a given time falls within the open hours of the futures market
is_future_open = fmt.in_open_time(datetime.now())
print("Is the futures market open right now?", is_future_open)

# Get the next market open time for futures markets
next_future_open_time = fmt.next_open_time(datetime.now())
print("Next futures market open time:", next_future_open_time)

# Get the last market open time for futures markets
last_future_open_time = fmt.last_open_time(datetime.now())
print("Last futures market open time:", last_future_open_time)

# Get the next market close time for futures markets
next_future_close_time = fmt.next_close_time(datetime.now())
print("Next futures market close time:", next_future_close_time)

# Get the last market close time for futures markets
last_future_close_time = fmt.last_close_time(datetime.now())
print("Last futures market close time:", last_future_close_time)

# Check if a given time falls within the open hours of the stock market
is_stock_open = smt.in_open_time(datetime.now())
print("Is the stock market open right now?", is_stock_open)

# Get the next market open time for stock markets
next_stock_open_time = smt.next_open_time(datetime.now())
print("Next stock market open time:", next_stock_open_time)

# Get the last market open time for stock markets
last_stock_open_time = smt.last_open_time(datetime.now())
print("Last stock market open time:", last_stock_open_time)
```

## Contribution

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue or create a pull request on GitHub.
