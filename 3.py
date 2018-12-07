from datetime import datetime, timedelta
import random

def worktime (date):
    weekday = date.weekday()
    if weekday<5:
        begin = datetime(date.year,date.month,date.day,9,30)
        end = datetime(date.year,date.month,date.day,18)
    else:
        begin = datetime(date.year,date.month,date.day,11)
        end = datetime(date.year,date.month,date.day,17,30)
    while begin<=end:
        print (begin)
        begin += timedelta(minutes = 30)

day = timedelta(days = random.randint(-40000,1000))+datetime.now()
worktime(day)
