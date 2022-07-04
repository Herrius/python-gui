from cgitb import text
from tabnanny import check
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    window.after_cancel(timer)
    tomato.itemconfig(timer_text,text="00:00")
    lb_title.config(text="Timer")
    lb_check.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def startTimer():
    global reps
    reps+=1
    work_sec = 1*60
    short_break_sec = 2 * 60
    long_break_sec=3 * 60

    if reps%8==0:
        countDown(long_break_sec)
        lb_title.config(text="Break 😴", foreground=RED)
    elif reps% 2==0:
        countDown(short_break_sec)
        lb_title.config(text="Break 🥱", foreground=PINK)
    else:
        countDown(work_sec)
        lb_title.config(text="Work 💪", foreground=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countDown(count):
    count_min = '{:0>2}'.format(math.floor(count/60))
    count_sec = '{:0>2}'.format(count % 60)

    tomato.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        lb_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato.create_image(100, 112, image=tomato_img)
timer_text = tomato.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

lb_title = Label(text="Timer", font=(FONT_NAME, 40, "bold"),
                 background=YELLOW, foreground=GREEN)
lb_check = Label(text="", font=(FONT_NAME, 20, "bold"),
                 background=YELLOW, foreground=GREEN)

btn_start = Button(text="Start", command=startTimer)
btn_reset = Button(text="Reset", command=resetTimer)

lb_title.grid(column=2, row=1)
lb_check.grid(column=2, row=4)
tomato.grid(column=2, row=2)
btn_start.grid(column=1, row=3)
btn_reset.grid(column=3, row=3)

window.mainloop()
