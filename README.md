# MarketTime
## Description
This is a tool to help you to check the market time.

For example:
 - Check if the time is in market open time
 - Get next open time
 - Get last open time
 - etc.

## Requirement
 - python >= 3.10
 - datetime >= 5.4

```
The versions may not be hard requirements. Checking on it now ...
```

## Install

```bash
pip install MarketTime
```

## Usage
Currently we offer two market time to check, stock market and future market.

And most important of all, always init close date list before running.
```python
from MarketTime import StockMarketTime as smt # or FutureMarketTime as fmt
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
smt.init_close_date_set(dates_list)
```

## Working on the content below ...
### Stock Market
```python

```

### Future Market
```python

```