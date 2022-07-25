from calendar import month
import datetime
from distutils import command
from time import time
# print(dir(datetime))
date = datetime.date(2022,1,8)
date2 = datetime.date(2022,1,7)
timedelta = datetime.timedelta(weeks=1)
res = date +  timedelta
res = date -  timedelta
res = date == date
res = date < date
res = date > date
res = date != date
res = date2 - date
# print(res)

date = datetime.date(2022,1,8)
date2 = datetime.date(2022,1,25)

# print((date - date2).days)


import random 


def sana ():
    year=  random.randint(2021,2023)
    month =  random.randint(1,12)
    days= random.randint(1,31)
    return  datetime.date(year,month,days)
today= datetime.date.today()
# print(today)

# print(today-sana())
import time

t = time.time()

sekunt =1644056117.31523

# res = datetime.date.fromtimestamp(sekunt)
# print(res == today)

# print(res.strftime("%Y yil %m oy %d -kun "))
# print(today.isoweekday())
# print(today.replace(2022,1,5))


import calendar


c= calendar.calendar(1)
# print(c.monthdayscalrmdar(2022,2))

t= calendar.TextCalendar(0)
# print(t.formatyear(2022))
# print(t.formatmonth(2022,2))

t = calendar.LocaleHTMLCalendar(0, locale="uz_UZ.utf-8")
# print(t.formatmonth(2022,2))


html = calendar.HTMLCalendar(0)
f = open("calendar.html","w")
f.write(html.formatyear(2022))
f.close()
import locale
locale.setlocale(locale.LC_ALL,"uz_UZ.utf-8")
s = calendar.month_name
m = [i for i in s]
d = calendar.day_name
l = [i for i in d]

print(m)
print(l)

# print(dir (calendar))
# print(dir(calendar))