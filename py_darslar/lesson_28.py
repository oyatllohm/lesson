from cProfile import label
from time import*
from calendar import month, monthcalendar
import datetime 
from tracemalloc import start
import locale 

from bisect import insort
from cgitb import text
from distutils import command
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
# window.mainloop()




import datetime
import calendar

t = time()# + 6 *(6 * 6)       # unix time
# print(t)

l = localtime()
# print(l)
# print(f"{l.tm_year}  yil:  {l.tm_mon} oy {l.tm_mday}kun   {l.tm_hour}  : soat    {l.tm_min} minut :  {l.tm_sec}  sekunt ")

# s= "15"
# r = "45"
# w = "%s + %s "%(s,r)
# print(w)
# str_time = strftime("%H : %M : %S : %d-%B  %A")
# print(str_time)
# sleep(3)
# print(str_time)
# now = time()
# end = now +60
# s = 11 
# while True:
    
#     sleep(1)
#     s -=1
#     print(s)
#     if s == 0:
#         break



# start_test = time()-65*60
# hozirgivaqt = time() 


#date
#timedelta
#datime
#time

# today = datetime.date.today()

# data = "2001-5-10".split("-")
# yil = datetime.date(int(data[0]), int(data[1]),int(data[2]))
# yil = data[0]
# d = datetime.date(2022,2,2)
t = datetime.timedelta(days=10)

# print(yil)

# print(today-t)

# print(datetime.timedelta.__doc__)


# t_yil = input(" ti yilingizni shu korinishda kiritin  2001-2-10").split("-")
# def month_name(month_number):
#     moth = {1:0,2:31,3:59,4:89,
#     5:120,6:150,7:181,8:212,
#     9:242,10:273,11:303,12:334}
#     return  moth[month_number]
   
# year = int( t_yil[0])
# month = int(t_yil[1]) 
# day = int(t_yil[2])
# day+=month_name(month)
# kunlar = 0
# for i in range(year):
#     if i % 4 == 0 :
#         kunlar +=366
#     else:
#         kunlar+=365

# today = datetime.date.today()
# g = datetime.timedelta(days=kunlar+day)

# a = str(today-g)
# print("siz",a[2:])
