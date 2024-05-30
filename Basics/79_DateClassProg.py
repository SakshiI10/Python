from datetime import date

# Calculating Age
def calculate_age(birth_date):
    today=date.today()
    age=today.year-birth_date.year-((today.month, today.day)<(birth_date.month, birth_date.day))
    return age
birth_date=date(2002, 12, 12)
age=calculate_age(birth_date)
print("Age:",age)

# Todays day and date 
date2=date(2024,5,30)
print("The date is:",date2.strftime("%A,%B %d,%Y"))

# Calculate days between
def calculate_days_between(start_date, end_date):
    delta=end_date-start_date
    return delta.days
start_date=date(2002, 3, 10)
end_date=date(2024, 5, 30)
days=calculate_days_between(start_date, end_date)
print("Days: ",days, "Days between", start_date, "to", end_date)

# Get day if week
def get_day_of_week(date_obj):
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day_index=date_obj.weekday()
    return days[day_index]
date3=date(2024, 5, 30)
day3=get_day_of_week(date3)
print("Date:",date3,"Day:",day3)

# Valid date
def is_valid_date(year,month,day):
    try:
        date(year,month,day)
        return True
    except ValueError:
        return False
year=2024
month=13
day=31
is_valid=is_valid_date(year,month,day)
if is_valid:
    print("Valid")
else:
    print("Invalid")
    
# Get days in month
def get_days_in_month(year,month):
    days_in_month=[31,28+(year%4==0 and (year%100!=0 or year%400==0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month-1]
year=2024
month=5
days_in_month=get_days_in_month(year,month)
print("There are",days_in_month,"days in",month,"/",year)