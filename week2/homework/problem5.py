import datetime, time, calendar

def day_diff(year, month, day):
    today = datetime.datetime.today()
    date = datetime.datetime(year, month, day, 0000)    
    return (date - today).days

today = datetime.datetime.today()
current_year = today.year
byear = 2009
bmonth = 10
bday = 16
bdate = datetime.datetime(byear, bmonth, bday)

till_bday = day_diff(current_year, bmonth, bday)

if till_bday < 0:
    current_year += 1
    till_bday = day_diff(current_year, bmonth, bday)

bweekday = calendar.weekday(byear, bmonth, bday)
   
print("""The date of my birthday: %s
The year of my birthday: %s
The month of my birthday: %s
The day of my birthday: %s
The weekday of my birthday: %s
How many days are left till my upcoming birthday: %s """ 
% (bdate, bdate.year, bdate.month, 
bdate.day, calendar.day_name[bweekday], till_bday))

cal = calendar.month(2017, 5)
print ("""Here is the calendar of:
""", cal)


one_day = datetime.timedelta(days=1)
two_days = datetime.timedelta(days=2)
three_days = datetime.timedelta(days=3)
yesterday_date = today - one_day
tomorrow_date = today + one_day

print("""Add two days to yesterday's date and time: %s
Subtract three days from yesterday's date and time: %s""" %(yesterday_date + two_days, yesterday_date - three_days))
