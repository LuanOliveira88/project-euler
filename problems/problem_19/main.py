from calendar import Calendar
from datetime import date, timedelta
from enum import Enum



def is_first_day(d: date):
    return d.day == 1


def is_sunday(d: date):    
    return d.weekday() == 6


def main():
    start_date = date(year=1901, month=1, day=1)
    final_date = date(year=2000, month=12, day=31)
    dates = []
    current_date = start_date
    
    while current_date != final_date:
        if is_first_day(current_date) and is_sunday(current_date):
            dates.append(current_date)
        current_date = current_date + timedelta(days=1)

    return len(dates)

if __name__ == '__main__':
    print(main())