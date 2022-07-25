import tkinter

window = tkinter.Tk()
window.title("Caunter")
window.geometry("400x350+100+100")
window["bg"]="#262626"
window.resizable(False,False)

display = tkinter.Entry(window,bd=2,justify=tkinter.RIGHT,  font=("Times New Roman",20))
display.grid(row=0,column=0,columnspan=4,sticky="we",pady=5)


def add_number(text):
    global display
    valyu = display.get() +str(text)
    display.delete(0,tkinter.END)
    display.insert(0,valyu)
valyu = display.get()


def operator(command):
    if command == "del":
        global valyu
        valyu= valyu[:-1]
        display.delete(0,tkinter.END)
        display.insert(0,valyu)
    elif command=="=":
        res = eval(valyu)
        display.delete(0,tkinter.END)
        display.insert(0,res) 
    else: 
        valyu=display.get()     
        if valyu[-1] in "+-*/":
            valyu = display.get()
            valyu= valyu[:-1]
            display.delete(0,tkinter.END)
            display.insert(0,valyu+command)
        else:
            display.delete(0,tkinter.END)
            display.insert(0,valyu+command)

def make_buttom(text):
    return tkinter.Button (window,text=f"{text}",
    font=("Arial",25,"bold"),bg="green",fg="white",command=lambda :add_number(f"{text}"))

def make_operator(text):
    return tkinter.Button(text=text,
            font=("Arial",15,"bold"),
            fg="white",bg="grey",command=lambda: operator(f"{text}") )


make_buttom("1").grid(row=1,column=0,sticky="wens")
make_buttom("2").grid(row=1,column=1,sticky="wens")
make_buttom("3").grid(row=1,column=2,sticky="wens")
make_buttom("4").grid(row=2,column=0,sticky="wens")
make_buttom("5").grid(row=2,column=1,sticky="wens")
make_buttom("6").grid(row=2,column=2,sticky="wens")
make_buttom("7").grid(row=3,column=0,sticky="wens")
make_buttom("8").grid(row=3,column=1,sticky="wens")
make_buttom("9").grid(row=3,column=2,sticky="wens")
make_buttom("6").grid(row=4,column=0,sticky="wens")

make_operator("+").grid(row=1,column=3,sticky="wens")
make_operator("-").grid(row=2,column=3,sticky="wens")
make_operator("-").grid(row=3,column=3,sticky="wens")
make_operator("*").grid(row=4,column=3,sticky="wens")
make_operator("=").grid(row=4,column=3,sticky="wens")
make_operator("del").grid(row=4,column=2,sticky="wens")

window.columnconfigure(0,minsize=60)
window.columnconfigure(1,minsize=60)
window.columnconfigure(2,minsize=60)
window.columnconfigure(3,minsize=60)

window.rowconfigure(1,minsize=60)
window.rowconfigure(2,minsize=60)
window.rowconfigure(3,minsize=60)
window.rowconfigure(4,minsize=60)


window.mainloop()