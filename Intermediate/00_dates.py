### Dates ###

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now()

'''
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
'''

timestamp = now.timestamp()

print(timestamp)

year_2024 = datetime(2024, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

print_date(year_2024)

current_time = time(23, 40, 50)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 11, 30)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

#diff = year_2024.time() - current_time
#print(diff)

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)







