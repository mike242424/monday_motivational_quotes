import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_the_week = now.weekday()

print(now)
print(year)
print(month)
print(day_of_the_week)

date_of_birth = dt.datetime(year=1987, month=9, day=26)
print(date_of_birth)