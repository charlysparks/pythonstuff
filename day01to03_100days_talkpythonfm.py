# The below was done in console and this file is not meant to run as a whole and should be used as notes.

# datetime is a module that allows for easier manipulation of objects that represent date and time

# from is used to import a specified section of a module
from datetime import datetime
from datetime import date
from datetime import timedelta

datetime.today()

# prints YYYY, MM, DD, hour, minutes, seconds, milliseconds
today = datetime.today()
type(today)

# prints the YYYY, MM, DD
todaydate = date.today()
type(todaydate)

# prints the month or day or year for current day
todaydate.month
todaydate.day
todaydate.year

# Assign a time value to Christmas
christmas = date(2023, 12, 25)

 # prints in console or jupyter notebook the delta number of days between the dates as datetime.timedelta(324) on 23/02/04
 christmas - todaydate
 
 # output is 324 and datetime.timedelta is stripped 
 (christmas - todaydate).days
 
 # small christmas countdown
 if christmas is not todaydate:
     print("Sorry there are still " + ((christmas - todaydate.days) + " until Christmas!")
         else :
             print("Yay it's Christmas!")
             
# learning about timedelta; timedelta describes a gap in time
t = timedelta(days=4, hours=10)
type(t) #check for object   

t.days # outputs 4
t.seconds # seconds outputs for the hours and does not count past 24hrs
t.hours # fails
t.seconds / 60 /60 # outputs hours
t.seconds / 3600 # outputs hours

eta = timedelta(hours=6) 
today = datetime.today()
today
eta
today + eta
str(today + eta)
