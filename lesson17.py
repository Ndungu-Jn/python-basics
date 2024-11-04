#dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime("%d-%m-%Y")
print(formatted_date)

after_forty_days = today + timedelta(days=40)
print(after_forty_days)

dob = "2000-02-15"
#convert to date object
dob = datetime.strptime(dob, "%Y-%m-%d")
age = today.year - dob.year
print(f"I am {age}, years old")

age_in_days = datetime.today() - dob
print(f"I am {age_in_days.days}, days old")