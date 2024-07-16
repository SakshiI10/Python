''' 
datetime class:
syntex: class datetime.datetime(year, month, day, hour=0, minute=0 second=0, microsecond=0, tzinfo=None*, fold=0)
'''
from datetime import datetime
today=datetime.now()
print(today)

today=datetime.today()
print(today)

date_time=datetime.fromordinal(737994)
print(date_time)

date_time=datetime.fromtimestamp(1887639468)
print(date_time)

import datetime
now=datetime.datetime.now()
date=datetime.datetime(2024,5,31,8,30,0)
print(date)

year=now.year
month=now.month
day=now.day
hour=now.hour
minute=now.minute
second=now.second
weekday=now.weekday()
str_now=now.strftime("%Y=%m-%d %H:%M:%S")
print(str_now)

import datetime

date1=datetime.datetime(2024,5,31)
date2=datetime.datetime(2024,6,1)
delta=date2-date1
print(delta)

date_str="2024-05-31"
dt=datetime.datetime.strptime(date_str, "%Y-%m-%d")
dt_str=dt.strftime("%Y-%m-%d")
print(dt_str)