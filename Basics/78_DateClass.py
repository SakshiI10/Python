''' 
Date Class
Syntax: class datetime.date(year, month, day)
 
Functions:
min
max
resolution
year
month
day
'''

from datetime import date

my_date=date(2023,5,30)
print("Passed date is:",my_date)

mindate=date.min 
print("Min date supported", mindate)

maxdate=date.max
print("Max date supported", maxdate)

Date=date(2024, 5, 30)
print("Year", Date.year)
print("Month", Date.month)
print("Day", Date.day)

today=date.today()
print("Todays date is:",today)

current_year=today.year
print("Current year is:",current_year)

