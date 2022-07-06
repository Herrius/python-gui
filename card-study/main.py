from tkinter import *
from pandas import read_csv
import random
BACKGROUND_COLOR = "#B1DDC6"



def main():
    
    def readFrenchWords():
        french_words=read_csv('data/french_words.csv',sep=',')
        data= french_words.to_dict(orient='records')
        french=random.choice(data)
        card_front.itemconfigure(card_word,text=f"{french['French']}")
    
    window=Tk()
    window.title("Flash card study")
    window.config(pady=50,padx=50,background=BACKGROUND_COLOR)

    card_front=Canvas(width=800,height=516,bg=BACKGROUND_COLOR,highlightthickness=0)
    card_front_img=PhotoImage(file="images/card_front.png")
    card_front.create_image(400,258,image=card_front_img)
    card_title=card_front.create_text(400,150,text="French",font=("Ariel",40,"italic"))
    card_word=card_front.create_text(400,263,text="trouve",font=("Ariel",60,"bold"))
    card_front.grid(column=0,row=0,columnspan=2,sticky='EW')


    card_front.config()
    image_wrong = PhotoImage(file='images/wrong.png')
    btn_wrong = Button(image=image_wrong, highlightthickness=0,command=readFrenchWords)
    btn_wrong.grid(column=0,row=1)

    image_right = PhotoImage(file='images/right.png')
    btn_right = Button(image=image_right, highlightthickness=0,command=None)
    btn_right.grid(column=1,row=1)


    window.mainloop()

main()