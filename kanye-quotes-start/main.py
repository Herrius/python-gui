from cgitb import text
from io import BytesIO
from tkinter import *
import PIL.Image,PIL.ImageTk
import requests

    
def main():
    def image():
        response=requests.get(url="https://fakeface.rest/face/json?gender=female&minimum_age=20&maximum_age=50")
        #response.raise_for_status()
        data=response.json()
        image_url=data['image_url']
        #Write your code here.
        photo=requests.get(image_url)
        photo_data=photo.content
        pre_picture=PIL.Image.open(BytesIO(photo_data)).resize((100,100))
        picture=PIL.ImageTk.PhotoImage(pre_picture)
        kanye_button.configure(image=picture)
        kanye_button.image=picture
    
    def get_quote():
        image()
        response=requests.get(url="https://zenquotes.io/api/random")
        data=response.json()
        canvas.itemconfig(quote_text,text=data[0]["q"])



    window = Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img,width=100,height=100, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()

main()