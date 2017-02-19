import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2017,2)

def printcal():
    print(str)