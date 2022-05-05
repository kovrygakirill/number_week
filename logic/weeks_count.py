from datetime import date, datetime

SUNDAY = 7


def weeks_between_dates(start_date: date, end_date: date):
    additional_week = 0 if start_date.weekday() == SUNDAY else 1

    weeks_of_start_date = int(datetime.strptime(f"{start_date.year}/12/31", '%Y/%m/%d').date().strftime('%U')) - int(
        start_date.strftime('%U'))
    weeks = weeks_full_years(start_date.year + 1, end_date.year)
    weeks_of_end_date = int(end_date.strftime('%U'))

    return weeks_of_start_date + weeks + weeks_of_end_date + additional_week


def weeks_full_years(start_year: int, end_year: int):
    count_weeks = 0
    for year in range(start_year, end_year):
        weeks_in_year = int(datetime.strptime(f"{year}/12/31", '%Y/%m/%d').date().strftime('%U'))
        count_weeks += weeks_in_year
    return count_weeks
