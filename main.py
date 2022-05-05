from flask import Flask, render_template, request, abort
from datetime import datetime

from logic.weeks_count import weeks_between_dates
from validator.check_date import validate_date

app = Flask(__name__)
START_DATE = datetime.strptime(f"2019/01/01", '%Y/%m/%d').date()


@app.route('/', methods=('GET', 'POST'))
def main_page():
    if request.method == 'POST':
        request_date = request.form['date']
        if validate_date(date_text=request_date):
            end_date = datetime.strptime(request_date, '%Y/%m/%d').date()
            weeks = weeks_between_dates(start_date=START_DATE, end_date=end_date)
            return render_template("main.html", weeks=weeks)
        else:
            return render_template("main.html", date_error="Incorrect data format, should be YYYY/MM/DD")

    return render_template("main.html")
