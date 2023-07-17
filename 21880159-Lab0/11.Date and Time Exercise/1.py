# Exercise 3: Subtract a week (7 days)  from a
# given date in Python
from datetime import datetime, timedelta


def subtract_date(given_day, subtract_days):
    return given_day - timedelta(days=subtract_days)


if __name__ == '__main__':
    given_date = datetime(2020, 2, 25)
    print("Given day:", given_date)
    days = 7
    res = subtract_date(given_date, days)
    print(res.date())
