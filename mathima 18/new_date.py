import datetime

today = datetime.date.today()

future_date = today

while future_date <= datetime.date(2023, 9, 29):
    # Print the day
    print(future_date)

    # Add one day to the future date
    future_date += datetime.timedelta(days=1)
