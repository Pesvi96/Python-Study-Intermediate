from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.2
reps = 1
check_symbol = "✓"
check_string = ""
timer_com = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global check_string
    global timer_com
    window.after_cancel(timer_com)
    check_string = ""
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfigure(timer, text="00:00")
    reps = 1
    # If you want loop start_countdown


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    global reps
    # while reps < 8:
    print(f"now on rep: {reps}")
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps in [1, 3, 5, 7]:
        title.config(text="Work")
        countdown(work_sec)
    elif reps in [2, 4, 6]:
        title.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    elif reps == 8:
        title.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps > 8:
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    global check_string
    global timer_com
    count_min = "{:02}".format(count // 60)
    count_sec = "{:02}".format(count % 60)
    if count >= 0:
        canvas.itemconfigure(timer, text=f"{str(count_min)}:{str(count_sec)}")
        timer_com = window.after(1000, countdown, count - 1)
    else:
        # Timer is done, you can perform any necessary actions here
        reps += 1
        start_countdown()
        if reps % 2 == 0:
            check_string += check_symbol
            checkmark.config(text=check_string)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer = canvas.create_text(100, 130, text="5", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

start_btn = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_countdown)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(row=2, column=2)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
title.grid(row=0, column=1)

checkmark = Label(fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
checkmark.grid(row=3, column=1)

print("before")
window.mainloop()
print("after")
