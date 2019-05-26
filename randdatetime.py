import random


def is_leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return True
    if year % 4 == 0:
        return True
    return False


def num_days(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def gen_date(year_range_lower, year_range_upper, dateformat="yyyy-mm-dd"):
    month = random.randint(1, 12)
    year = random.randint(year_range_lower, year_range_upper)
    day = random.randint(1, num_days(month=month, year=year))

    date = ""

    if dateformat == "yyyy-mm-dd":
        date += str(year)
        date += '-'
        date += str(month).zfill(2)
        date += '-'
        date += str(day).zfill(2)

    return date