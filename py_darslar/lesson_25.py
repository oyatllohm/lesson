# import tkinter
# from tkinter.ttk import Button
# bir=None
# ikki=None
# oyna=tkinter.Tk()
# oyna.title("kalkulator")
# def bir():
#     global bir
#     bir=1
#     lable.config(text=bir)
# def ikki():
#     global ikkii 
#     ikki=2
#     lable.config(text=ikki)

# oyna.geometry("200x450+100+100")
# lable = tkinter.Button(text="",font=("Arial",25,"bold"),bg="blue",fg="black")
# lable.place(x=0,y=150,width=200,height=50)
# tugma = tkinter.Button(text="ac",font=("Arial",25,"bold"),bg="gray",fg="black",)
# tugma.place(x=0,y=200,width=50,height=50)
# tugma = tkinter.Button(text="c",font=("Arial",25,"bold"),bg="gray",fg="black")
# tugma.place(x=50,y=200,width=50,height=50)
# tugma = tkinter.Button(text="%",font=("Arial",25,"bold"),bg="gray",fg="black")
# tugma.place(x=100,y=200,width=50,height=50)
# tugma = tkinter.Button(text="/",font=("Arial",25,"bold"),bg="black",fg="red")
# tugma.place(x=150,y=200,width=50,height=50)
# tugma = tkinter.Button(text="7",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=0,y=250,width=50,height=50)
# tugma = tkinter.Button(text="8",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=50,y=250,width=50,height=50)
# tugma = tkinter.Button(text="9",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=100,y=250,width=50,height=50)
# tugma = tkinter.Button(text="*",font=("Arial",25,"bold"),bg="black",fg="red")
# tugma.place(x=150,y=250,width=50,height=50)
# tugma = tkinter.Button(text="6",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=0,y=300,width=50,height=50)
# tugma = tkinter.Button(text="5",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=50,y=300,width=50,height=50)
# tugma = tkinter.Button(text="4",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=100,y=300,width=50,height=50)
# tugma = tkinter.Button(text="-",font=("Arial",25,"bold"),bg="black",fg="red")
# tugma.place(x=150,y=300,width=50,height=50)
# tugma = tkinter.Button(text="1",font=("Arial",25,"bold"),bg="green",fg="white",command=bir)
# tugma.place(x=0,y=350,width=50,height=50)
# tugma = tkinter.Button(text="2",font=("Arial",25,"bold"),bg="green",fg="white",command=ikki)
# tugma.place(x=50,y=350,width=50,height=50)
# tugma = tkinter.Button(text="3",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=100,y=350,width=50,height=50)
# tugma = tkinter.Button(text="+",font=("Arial",25,"bold"),bg="black",fg="red")
# tugma.place(x=150,y=350,width=50,height=50)
# tugma = tkinter.Button(text="0",font=("Arial",25,"bold"),bg="green",fg="white")
# tugma.place(x=0,y=400,width=50,height=50)
# tugma = tkinter.Button(text=".",font=("Arial",25,"bold"),bg="green",fg="red")
# tugma.place(x=50,y=400,width=50,height=50)
# tugma = tkinter.Button(text="=",font=("Arial",25,"bold"),bg="yellow",fg="red")
# tugma.place(x=100,y=400,width=100,height=50)
# oyna.mainloop()

import tkinter

window = tkinter.Tk()
window.title("Counter")
window.geometry("285x285+100+100")
window["bg"]='#262626'
window.resizable(False,False)


display = tkinter.Entry(window,justify=tkinter.RIGHT, font = ('Times New Roman',20))
display.grid(row=0,column=0,columnspan=4,sticky='we',pady=5,)

def add_number(text):
    # global display
    value= display.get()+str(text)
    display.delete(0,tkinter.END)
    print(value)
    display.insert(1,value)

def operator (command):
    value= display.get()
    if command == "del":
        value = value[:-1]
        display.delete(0,tkinter.END)
        display.insert(0,value)
    elif command == "=":
        res = eval(value)
        display.delete(0,tkinter.END)
        display.insert(0,res)

    else:
        value= display.get()
        print(value[-1])
        if value[:-1] in "+-*/":
            value = value[:-1]   
            display.delete(0,tkinter.END)
            display.insert(0,value+command)
        else:
             display.delete(0,tkinter.END)
             display.insert(0,value+command)

            
        
        


def make_button(text):
    return tkinter.Button(text=text,
            font=("Arial",15,"bold"),
             fg="black",bg="white", command=lambda:add_number(f"{text}"))

def make_operator(text):
    return tkinter.Button(text=text,
            font=("Arial",15,"bold"),
             fg="white",bg="grey",command=lambda: operator(f"{text}") )


make_button('1').grid(row=1,column=0,sticky='wens' )
make_button('2').grid(row=1,column=1,sticky='wens' )
make_button('3').grid(row=1,column=2,sticky='wens' )

make_button('4').grid(row=2,column=0,sticky='wens' )
make_button('5').grid(row=2,column=1,sticky='wens' )
make_button('6').grid(row=2,column=2,sticky='wens' )

make_button('7').grid(row=3,column=0,sticky='wens' )
make_button('8').grid(row=3,column=1,sticky='wens' )
make_button('9').grid(row=3,column=2,sticky='wens')
make_button('0').grid(row=4,column=0,sticky='wens')


make_operator('+').grid(row=1,column=3,sticky='wens' )
make_operator('-').grid(row=2,column=3,sticky='wens' )
make_operator('*').grid(row=3,column=3,sticky='wens' )
make_operator('/').grid(row=4,column=3,sticky='wens' )
make_operator('=').grid(row=4,column=1, sticky='wens' )
make_operator('del').grid(row=4,column=2, sticky='wens' )




window.columnconfigure(0,minsize=60)
window.columnconfigure(1,minsize=60)
window.columnconfigure(2,minsize=60)
window.columnconfigure(3,minsize=60)

window.rowconfigure(0,minsize=60)
window.rowconfigure(1,minsize=60)
window.rowconfigure(2,minsize=60)
window.rowconfigure(3,minsize=60)


window.mainloop()