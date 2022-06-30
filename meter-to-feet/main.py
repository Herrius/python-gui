from tkinter import *
from venv import create
# from tkinter import Tk
window=Tk()
window.title("Meter to feet Converter")
window.minsize(width=500,height=500)

icon=PhotoImage(file="icon.ico")
window.iconphoto(False,icon)



def createLabel(**kargs):
    txt_label=Label(text=kargs.get("text"),font=("Calibri",12))
    txt_label.grid(column=kargs.get("y"),row=kargs.get("x"))
    txt_label.config(padx=12,pady=12)
    return txt_label

def createInput(**kargs):
    input=Entry(width=20)
    input.insert(END,string="0")
    input.grid(column=kargs.get("y"),row=kargs.get("x"))
    return input

def createButton(**kargs):
    button=Button(text=kargs["text"],command=kargs["command"])
    button.grid(column=kargs["y"],row=kargs["x"])
    return button


def main():
    def action():
        number=int(input_feets.get())
        number=round(number/3.2808,2)
        txt_value.config(text=number)

    txt_feets=createLabel(text="Feets",x=1,y=3)
    txt_description=createLabel(text="is equal to",x=2,y=1)
    txt_abbrevation=createLabel(text="Mts",x=2,y=3)
    txt_value=createLabel(text="0",x=2,y=2)

    input_feets=createInput(x=1,y=2)
    

    button_calculate=createButton(text="Calculate",x="3",y="2",command=action)

    window.mainloop()

main()