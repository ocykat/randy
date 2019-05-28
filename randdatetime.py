import random


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day < other.day
            else:
                return self.month < other.month
        else:
            return self.year < other.year


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


def gen_date(year_lower=1950, year_upper=2050, dateformat="yyyy-mm-dd"):
    year = random.randint(year_lower, year_upper)
    month = random.randint(1, 12)
    day = random.randint(1, num_days(month=month, year=year))

    date = ""

    if dateformat == "yyyy-mm-dd":
        date += str(year)
        date += '-'
        date += str(month).zfill(2)
        date += '-'
        date += str(day).zfill(2)

    return date


def gen_date_pair(year_lower=1950, year_upper=2050, gap=20, dateformat="yyyy-mm-dd"):
    year = random.randint(year_lower, year_upper)
    month = random.randint(1, 12)

    day_max = num_days(month, year)
    day = random.randint(1, day_max)

    date = ""

    if dateformat == "yyyy-mm-dd":
        date += str(year)
        date += '-'
        date += str(month).zfill(2)
        date += '-'
        date += str(day).zfill(2)

    day += gap

    while day > day_max:
        day -= day_max

        month += 1
        if month == 13:
            month = 1
            year += 1

        day_max = num_days(month, year)

    second_date = ""

    if dateformat == "yyyy-mm-dd":
        second_date += str(year)
        second_date += '-'
        second_date += str(month).zfill(2)
        second_date += '-'
        second_date += str(day).zfill(2)

    return date, second_date
