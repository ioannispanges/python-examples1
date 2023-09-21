from datetime import datetime, date, timedelta

current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")

current_date = date.today()
print(f"Current date: {current_date}")

days_to_add = 20
future_date = current_date + timedelta(days=days_to_add)
print(f"Future date: {future_date}")
