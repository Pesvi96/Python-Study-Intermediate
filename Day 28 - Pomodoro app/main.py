from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown():
    countdown_time = int(canvas.itemcget(timer, "text"))
    countdown_time -= 1
    canvas.itemconfigure(timer, text=countdown_time)


def start_countdown():
    for _ in range(4):
        window.after(1000, countdown)


# TODO: why doesn't start_countdown don't work? The screen resets when the function is done. Video 257

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def say(thing):
#     print(thing)
#
#
# window.after(1000, say, "Hello")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer = canvas.create_text(100, 130, text="5", fill="white", font=(FONT_NAME, 35, "bold"))





canvas.grid(row=1, column=1)

start_btn = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_countdown)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW)
reset_btn.grid(row=2, column=2)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
title.grid(row=0, column=1)

checkmark = Label(text="✓", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()
