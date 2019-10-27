import datetime, time, calendar

tday = datetime.datetime.today()
tdelta = datetime.timedelta(days = 5)
subtractFiveDays = tday - tdelta
addFiveDays = tday + tdelta


print("""Current date and time: %s  
The value of current year: %s 
The value of the current month: %s The value of the current day of the week: %s 
Subtract 5 days from the current date and time: %s 
Add 5 days from the current date and time: %s"""
% (tday, tday.year, tday.month, tday.weekday(), subtractFiveDays, addFiveDays))

