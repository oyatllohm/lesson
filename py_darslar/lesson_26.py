import tkinter

window = tkinter.Tk()
window.title("Caunter")
window.geometry("500x500+100+100")
# window.tkinter.phto
counter = 0 
def count():
    global counter
    counter+=1
    if counter==11:
        counter-=1
        lable.config(text=f"{counter}") 
    else:
        lable.config(text=f"{counter}")
def coount():
    global counter
    counter-=1
    if counter==-1:
        counter+=1
        lable.config(text=f"{counter}") 
    else:
        lable.config(text=f"{counter}")
lable = tkinter.Label(text=f"{counter}",font=("Arial",25,"bold"))
lable.pack()
button = tkinter.Button(text="Clicme+",font=("Arial",25,"bold"),bg="green",fg="white", command=count)
button.pack()
buutton = tkinter.Button(text="Clicme -",font=("Arial",25,"bold"),bg="green",fg="white", command=coount)
# buutton.place(x=20,y=20,width=50,height=75)
buutton.pack()
# python -m pyinstaller -F --onefile --noconsole lesson_26.py
window.mainloop()
