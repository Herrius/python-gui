from email.mime import image
from email.policy import strict
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canva=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canva.create_image(100,100,image=logo)

lbWebsite=Label(text="Website")
lbEmail=Label(text="Email/Username")
lbPassword=Label(text="Pasword")

btnPassword=Button(text="Generator Password",command=None)
btnAdd=Button(text="Add",command=None,width=36)

tbWebsite=Entry(width=35)
tbEmail=Entry(width=35)
tbPassword=Entry(width=21)

canva.grid(column=1,row=0)

lbWebsite.grid(column=0,row=1)
tbWebsite.grid(column=1,row=1,columnspan=2,sticky=EW)
lbEmail.grid(column=0,row=2)
tbEmail.grid(column=1,row=2,columnspan=2,sticky=EW)
lbPassword.grid(column=0,row=3)
tbPassword.grid(column=1,row=3,sticky=EW)
btnPassword.grid(column=2,row=3,sticky=EW)
btnAdd.grid(column=1,row=5,columnspan=2,sticky=EW)

window.mainloop()