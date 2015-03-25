from datetime import date


def friday_years(start, end):
    friday_years_count = 0

    for year in range(start, end + 1):
        leap_year = False
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leap_year = True

        first_day = date(year, 1, 1).weekday()
        second_day = date(year, 1, 2).weekday()
        if first_day == 4 or second_day == 4 and leap_year:
            friday_years_count += 1

    return friday_years_count

if __name__ == '__main__':
    print(friday_years(1000, 2000))
    print(friday_years(1753, 2000))
    print(friday_years(1990, 2015))
