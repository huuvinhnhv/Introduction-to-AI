# Exercise 5: Find the day of the week of a given date
from datetime import datetime

if __name__ == '__main__':
    given_date = datetime(2020, 7, 26)

    print(given_date.strftime('%A'))
