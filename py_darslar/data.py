# time haqida
from distutils.command.install_egg_info import safe_name
from time import *
import calendar
import locale
hozirgi_vaqt_sekunnta = time()
kalendar=localtime()#tm_year=2022, tm_mon=2, tm_mday=5, 
                                    #tm_hour=8, tm_min=35, tm_sec=10,
                                   #  tm_wday=5, tm_yday=36, tm_isdst=0)
l = localtime()
print(f"{l.tm_year}  yil:  {l.tm_mon} oy {l.tm_mday}kun   {l.tm_hour}  : soat    {l.tm_min} minut :  {l.tm_sec}  sekunt ")

sleep(3) # sekunt tashash
# ftime( %H %M %S %Y %y %m %B %%)
# %H soat 
# %M minut  
# %S sekunt 
# %Y yil
# %y yil ohirgi 2 raqam 
# %m oy raqami 
# %B oy nomi toliq 
# %b oy nomi qisqa 
# %A hafta kuni nomi toliq
# %a hafta kuni nomi qisqa
# %X vaqt 
# %x sana  




#   soat 
from itertools import tee
import tkinter
from tkinter.ttk import Button

window = tkinter.Tk()
window.title("soat")
window.geometry("1300x150")
window["bg"]="black"

label = tkinter.Label(window,bg="yellow",fg="red",bd=25,font=("Boluer",68,"bold"))
label.grid(row=0,column=1)
locale.setlocale(locale.LC_ALL,"ku_KU.utf-8")

def hozirgi_vaqt():
    str_time = strftime("%H : %M : %S : %d-%B  %A")
    label.config(text=f"{str_time}")
    label.after(200,hozirgi_vaqt)
hozirgi_vaqt()
window.mainloop()

import datetime

#date
#timedelta
#datime
#time
today= datetime.date.today()
today = datetime.date.today() # hozirgi vaqt yil oy kun 
yil = datetime.date()#hohlagan vaqt yil oy kun kiritiladi majburiy

sekunt =1644056117.31523
res = datetime.date.fromtimestamp(sekunt)
print(res == today)  #sekuntni sanaga aylantirish 
# print(today.isoweekday())
# print(today.replace(2022,1,5))
 

c= calendar.calendar(1)
print(c )


import calendar
html = calendar.HTMLCalendar(0)
f = open("calendar.html","w")
f.write(html.formatyear(2022))
f.close()
import locale
locale.setlocale(locale.LC_ALL,"uz_UZ.utf-8")
s = calendar.month_name
d = calendar.day_name
m = [i for i in s]
l = [i for i in d]
# print(m)
# print(l)
