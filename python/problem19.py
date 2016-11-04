# You are given the following information, but you may prefer to do some research for yourself.
#
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


start_date = date(1901, 1, 1)
print(start_date)
end_date = start_date + relativedelta(years=99, days=365)
delta = datetime.timedelta(days=1)
print (end_date)
d = start_date
sunCount = 0
while d <= end_date:
    if d.weekday() == 6 and d.day == 1:
        sunCount = sunCount + 1
    d = d + delta
    
print(sunCount)
    
