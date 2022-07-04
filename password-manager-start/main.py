from email.mime import image
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canva=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canva.create_image(80,80,image=logo)

lbWebsite=Label(text="Website")
lbEmail=Label(text="Email/Username")
lbPassword=Label(text="Pasword")

btn=Button(text="",command=None)

canva.grid(column=1,row=0)

window.mainloop()