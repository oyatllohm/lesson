


# isimlar = []
# n = 1
# while True:
#     savol = f"{n} yaqin dostingizni  kiritin "
#     ism= input(savol)
#     isimlar.append(ism)
#     takror = input("yana dostizni qosha sizmi ha \ yoq den")
#     n+=1
#     if takror =="yoq" :
#         break
# print(isimlar)








# a = 45 
# b = 0
# try:
#     c = a / b
#     print(c)
# except:


# s = "salom"
# try:
#     if  s== "salom":
#         pass
#     else:
#         pass
# except:
#     pass

# for i in range(12):
#     pass
# print(i)


# def oylar():
#     for i in range(1,29):
#         print(i)
# def orta():
#     oylar()
#     print(29)
#     print(30)
# def katta():
#     orta()
#     print(31)
# print("yanvar");katta()
# print("febral");oylar()
# print("mart");katta()
# print("aprel");orta()
# print("may");katta()
# print("iyyun");orta()
# print("iyyul");katta()
# print("avgust");katta()
# print("sentiyabr");orta()
# print("aktiyabr");katta()
# print("noyabr");orta()
# print("dekabr");katta()
# a = 200 
# b = 200




# from turtle import Turtle, Screen
# oyna = Screen()
# chiziq = Turtle()
# yol = Turtle()
# chiziq.pensize(2)
# chiziq.speed(0)
# chiziq.color('red')
# chiziq.up()
# chiziq.goto(200,200)
# chiziq.down()
# chiziq.goto(200,-200)
# chiziq.goto(-200,-200)
# chiziq.goto(-200,200)
# chiziq.goto(200,200)
# chiziq.goto(200,170)
# chiziq.goto(-180,-190)
# chiziq.goto(-160,155)
# chiziq.goto(169,150)
# chiziq.goto(+140,-150)
# chiziq.goto(-122,+177)
# chiziq.goto(-100,205)
# chiziq.goto(+100,-220)
# chiziq.goto(100,250)

# yol.color("black")
# yol.goto(90,80)
# yol.goto(-150,50)
# yol.goto(+180,50)
# yol.goto(50,-150)
# yol.goto(-70,-60)
# yol.goto(+80,90)
# yol.goto(-90,150)
# yol.goto(+100,180)
# yol.goto(-110,+220)
# yol.goto(+120,-210)


# oyna.mainloop()


# from tkinter import Image, Label,Tk
# import time

# app_window = Tk()
# app_window.title("raqamli soat")
# app_window.geometry("400x160")
# app_window.resizable(1,1)


# text_font  = ("boulder",65,"bold")
# background = "#00FF00"
# textcolor = "#363255"
# border_width = 30
# # img =Image.open('i.jpg')
# print(time.strftime("%H:%M:%S"))
# label = Label(app_window,font = text_font,
#                     bg=background,fg = textcolor,bd = border_width)
# label.grid(row=0,column=1)

# def digital_clock():
#     now = time.strftime("%H:%M:%S")
#     label.config(text = now)
#     label.after(500,digital_clock)

# digital_clock()    

# app_window.mainloop()


# from turtle import *

# for i in range(100,150):
#     circle(i)
#     left(20)
#     if i%3==1:
#         color("red")
#     elif i%3==0:
#         color("blue")
#     else:
#         color("green")
#     speed = 0
# done()


import random
def qurol():
    aftamat = random.choice(['M16',"AK47",'AGU',"val"])
    ogir= random.choice([3,4,3.5,3.7,])
    p_name = random.choice(["uzun","chachma","sipiral"])
    oq = random.choice([10,15,20,25])
