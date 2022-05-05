import datetime


def validate_date(date_text):
    result = True
    try:
        datetime.datetime.strptime(date_text, '%Y/%m/%d')
    except ValueError:
        result = False
    return result

