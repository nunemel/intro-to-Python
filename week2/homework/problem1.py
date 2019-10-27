import argparse, datetime

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", help = "the number of years", type=int)
parser.add_argument("--num_d", help = "the number of days", type=int)
current_day = datetime.datetime.now()
cuurent_year = current_day.year
final_date = current_day

args = parser.parse_args()
str_not_given = "not given"
if args.num_y:
    years = args.num_y
    tdelta_years = datetime.timedelta(years=years)
    final_date = final_date + tdelta_years
else:
    years = str_not_given    
if args.num_d: 
    days = args.num_d
    tdelta_days = datetime.timedelta(days=days)   
    final_date = final_date + tdelta_days
else:
    tdelta_days = str_not_given
       
print("""Current date: %s     
Given years: %s
Given days: %s
Final date: %s""" % (current_day, years, days, final_date))    