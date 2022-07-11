from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

from numpy import pad

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            background=THEME_COLOR)
        self.score_label=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)  
        self.question=Canvas(width=300,height=250)
        self.question_text=self.question.create_text(150,125,
        text="What is the question?",
        width=280,
        fill=THEME_COLOR,
        font=("Arial",20,"italic"))
        self.question.grid(row=1,column=0,columnspan=2,pady=20)
        
        img_wrong=PhotoImage(file="images/false.png")
        self.btn_wrong=Button(image=img_wrong,highlightthickness=0,command=self.wrong_answer)
        self.btn_wrong.grid(row=2,column=0)

        img_check = PhotoImage(file="images/true.png")
        self.btn_check=Button(image=img_check,highlightthickness=0,command=self.correct_answer)
        self.btn_check.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question.config(bg="white")
        self.question.itemconfig(self.question_text,fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=q_text,fill=THEME_COLOR)
        else:
            self.question.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.btn_wrong.config(state="disabled")
            self.btn_check.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question.config(bg="green")
            self.question.itemconfig(self.question_text,fill="white")
        else:
            self.question.config(bg="red")
            self.question.itemconfig(self.question_text,fill="white")
        self.window.after(1000, self.get_next_question)
