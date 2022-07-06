from tkinter import messagebox
from tkinter import *
from random import choice,shuffle
import json

def resetBox():
    tbPassword.delete(0,'end')
    tbWebsite.delete(0,'end')
    tbEmail.delete(0,'end')
    tbEmail.insert(0,"random@gmail.com")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def PassswordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    for char in range(1, 5):
        password_list.append(choice(letters))
        password_list.append(choice(numbers))
        password_list.append(choice(symbols))
    shuffle(password_list)
    password=""
    for char in password_list:
        password += char
    tbPassword.delete(0,'end')
    tbPassword.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website=tbWebsite.get()
    email=tbEmail.get()
    password=tbPassword.get()
    account={
        website:{
            "email":email,
            "password":password
        }
    }
    if website!="" and email!="" and password!="":
        info=messagebox.askokcancel(title=website, message=f"These are the details enteres \nEmail: {email}"
                                                        f"\nPassword:{password}\bIs it ok save?")
        if info:
            try:
                with open("data.json","r") as data_file:
                    #Reading old data
                    data=json.load(data_file)
                    #Updating old data with new data
                    data.update(account)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    #Saving update data
                    json.dump(account,data_file,indent=4)
            else:
                data.update(account)

                with open("data.json","w") as data_file:
                    #Saving update data
                    json.dump(data,data_file,indent=4)
            finally:
                resetBox()

            # file=open("data.txt","a")
            # file.write(f'{website} | {email} | {password}\n')
    else:
        messagebox.showerror(title="datos invalidos", message=f"Debe llenar todos los campos antes de guarda los datos")

def searchAccount():
    website=tbWebsite.get()
    if len(website)==0:
         messagebox.showerror(title="datos invalidos", message=f"Debe llenar el campo website antes de buscar")
    else:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message=f"No tiene cuenta registradas en la aplicacion")
        except KeyError:
            messagebox.showinfo(title="Titulo no encontrado", message=f"Esta pagina web no ha sido registrada")
        else:
            messagebox.showinfo(title=f"{website}", 
                message=f"El correo es: {data[website]['email']}\nLa contraseña es: {data[website]['password']}")
            
        
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

btnPassword=Button(text="Generator Password",command=PassswordGenerator, padx=10)
btnAdd=Button(text="Add",command=savePassword,width=36)
btnSearch=Button(text="Search",command=searchAccount,padx=10)

tbWebsite=Entry(width=35)
tbWebsite.focus()
tbEmail=Entry(width=35)
tbEmail.insert(0,"random@gmail.com")
tbPassword=Entry(width=21)

canva.grid(column=1,row=0)

lbWebsite.grid(column=0,row=1)
tbWebsite.grid(column=1,row=1,sticky=EW)
btnSearch.grid(column=2,row=1, sticky=EW)
lbEmail.grid(column=0,row=2)
tbEmail.grid(column=1,row=2,columnspan=2,sticky=EW)
lbPassword.grid(column=0,row=3)
tbPassword.grid(column=1,row=3,sticky=EW)
btnPassword.grid(column=2,row=3,sticky=EW)
btnAdd.grid(column=1,row=5,columnspan=2,sticky=EW)

window.mainloop()