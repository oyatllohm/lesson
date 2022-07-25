from bisect import insort
from cgitb import text
from distutils import command
from itertools import tee
import tkinter
from tkinter.ttk import Button

window = tkinter.Tk()
window.title("Caunter")
window.geometry("500x500+100+100")
window["bg"]="black"
window.resizable(False,False)

def make_buttom(text):
    return tkinter.Button (window,text=f"{text}",
    font=("Arial",15,"bold"),bg="black",fg="white")

display1 = tkinter.Entry(window,font=("Times New Roman",20))
display1.grid(row=1,column=1,columnspan=4,sticky="we",pady=2)
display2 = tkinter.Entry(window,font=("Times New Roman",20))
display2.grid(row=2,column=1,columnspan=4,sticky="we",pady=2)
display3 = tkinter.Entry(window,font=("Times New Roman",20))
display3.grid(row=3,column=1,columnspan=4,sticky="we",pady=2)
display4 = tkinter.Entry(window,font=("Times New Roman",20))
display4.grid(row=4,column=1,columnspan=4,sticky="we",pady=2)
display5 = tkinter.Entry(window,font=("Times New Roman",20))
display5.grid(row=5,column=1,columnspan=4,sticky="we",pady=2)
display6 = tkinter.Entry(window,font=("Times New Roman",20))
display6.grid(row=6,column=1,columnspan=4,sticky="we",pady=2)
display7 = tkinter.Entry(window,font=("Times New Roman",20),)
display7.grid(row=7,column=1,columnspan=4,sticky="we",pady=2)
display8 = tkinter.Entry(window,font=("Times New Roman",20),)
display8.grid(row=8,column=1,columnspan=4,sticky="we",pady=2)
display9 = tkinter.Entry(window,font=("Times New Roman",20),)
display9.grid(row=9,column=1,columnspan=4,sticky="we",pady=2)



make_buttom("id:").grid(row=1,column=0)
make_buttom("Name:").grid(row=2,column=0)
make_buttom("UserName:").grid(row=3,column=0)
make_buttom("Phone:").grid(row=4,column=0)
make_buttom("Email:").grid(row=5,column=0)
make_buttom("adres:").grid(row=6,column=0)
make_buttom("reg_daate:").grid(row=7,column=0)
make_buttom("age:").grid(row=8,column=0)
make_buttom("malumot:").grid(row=9,column=0)

def save(args):
    return tkinter.Button (window,text=f"{args}",
    font=("Arial",15,"bold"),bg="green",fg="white")

def saqla ():
    a = display1.get()
    b = display2.get()
    c = display3.get()
    d = display4.get()
    h = display5.get()
    g = display6.get()
    f = open("vazifa.txt","a")
    f.write(f"{a}\n{b} \n{c}\n{d}\n{h}\n{g}")
    a= display1.delete(0,tkinter.END) 
    a= display2.delete(0,tkinter.END)
    a= display3.delete(0,tkinter.END) 
    a= display4.delete(0,tkinter.END)
    a= display5.delete(0,tkinter.END)
    a= display6.delete(0,tkinter.END)
    f.close() 

def print_():
    f = open("vazifa.txt","r")
    malumot = f.read()
    f.read (display9.insert(0, malumot) ) 

def delit_():
    a = display9.get()
    a = display9.delete(0,tkinter.END)
    
save= tkinter.Button(text="save",font=("Arial",25,"bold"),bg="green",fg="black",command=saqla)
save.place(x=130,y=380,width=100,height=40)
print_= tkinter.Button(text="print",font=("Arial",25,"bold"),bg="green",fg="black",command=print_)
print_.place(x=230,y=380,width=100,height=40)
delit_= tkinter.Button(text="delit",font=("Arial",25,"bold"),bg="green",fg="black",command=delit_)
delit_.place(x=330,y=380,width=100,height=40)

window.mainloop()