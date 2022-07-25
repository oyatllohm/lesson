import datetime
from importlib import machinery
from ntpath import join

f = open("vazifa.txt","r")
fail = f.read().splitlines()
f.close()

katta_year =[]
kichik_year={}
year_20 = 0 

for i in range(20):
    if i %4 == 0 :
        year_20+= 366
    else:
        year_20+=365
today = datetime.date.today()
timedelta = datetime.timedelta(days=year_20)
yigirma = today-timedelta

for i in fail:
    isim = i.split(" ")
    intt = isim[0].split(".")
    
    name = join(intt[1]) 
    surname =join(isim[1])
    number = join(isim[2])
    tg_year = join(isim[3])

    t_year = str(isim[3:]).replace("."," ")
    year = join(t_year[2:6])
    month = join (t_year[6:9]).strip()
    day = join(t_year[9:11]).strip().strip("'")

    if year.isdigit() and month.isdigit() and day.isdigit():
        year = int(year)
        month = int(month)
        day = int (day)

        t_day = datetime.date(year,month,day)
        malumot = {"name":name,"surname":surname,"number":number,"tyil":tg_year}
        
        if t_day >= yigirma:
            kichik_year.update({intt[0]:malumot})
        else:
            katta_year.append({intt[0]:malumot})

print(kichik_year)
print()
print(katta_year)

