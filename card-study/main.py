from tkinter import *
from pandas import DataFrame, read_csv
import random

import pandas
BACKGROUND_COLOR = "#B1DDC6"



def main():
    
    try:
        data=read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data=read_csv('data/french_words.csv',sep=',')
        to_learn= original_data.to_dict(orient="records")
    else:
        to_learn= data.to_dict(orient="records")
        



    def readFrenchWords():
        global french
        french=random.choice(to_learn)
        card.itemconfig(card_image,image=card_front_img)
        card.itemconfig(card_title,text=f"French",fill='black')
        card.itemconfig(card_word,text=f"{french['French']}",fill='black')
    
    def answerEnglishWords():
        card.itemconfig(card_title,text=f"English",fill='white')
        card.itemconfig(card_word,text=f"{french['English']}",fill="white")
        card.itemconfig(card_image,image=card_back_img)
        card.after(3000,func=readFrenchWords)

    def is_know():
        to_learn.remove(french)
        data=DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        readFrenchWords()
    window=Tk()
    window.title("Flash card study")
    window.config(pady=50,padx=50,background=BACKGROUND_COLOR)
  
    card=Canvas(width=800,height=516,bg=BACKGROUND_COLOR,highlightthickness=0)
    card_back_img=PhotoImage(file="images/card_back.png")
    card_front_img=PhotoImage(file="images/card_front.png")
    card_image=card.create_image(400,258,image=card_front_img)
    card_title=card.create_text(400,150,text="French",font=("Ariel",40,"italic"))
    card_word=card.create_text(400,263,text=f"",font=("Ariel",60,"bold"))
    card.grid(column=0,row=0,columnspan=2,sticky='EW')


    image_wrong = PhotoImage(file='images/wrong.png')
    btn_wrong = Button(image=image_wrong, highlightthickness=0,command=is_know)
    btn_wrong.grid(column=0,row=1)

    image_right = PhotoImage(file='images/right.png')
    btn_right = Button(image=image_right, highlightthickness=0,command=answerEnglishWords)
    btn_right.grid(column=1,row=1)

    readFrenchWords()
    window.mainloop()

main()