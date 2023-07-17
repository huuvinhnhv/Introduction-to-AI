# Exercise 9: Calculate the date 4 months
# from the current date
from datetime import datetime
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':
    # 2020-02-25
    given_date = datetime(2020, 2, 25).date()
    print("Given date:", given_date)
    month_to_add = 4
    new_date = given_date + relativedelta(months=month_to_add)
    print("New date:", new_date)
