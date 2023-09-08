from tkinter import *
import pandas as pd
import tkinter.messagebox
from random import choice

# def create_ui():
#     """Creates the window and all the elements for this prog
#     :return: window, web_label, email_label, pass_label, web_input, email_input, pass_input, generate_btn, add_btn
#     """

try:
    df = pd.read_csv("./data/words.csv")
    words_list = df.to_dict(orient="records")
    print(words_list)
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    words_list = df.to_dict(orient="records")
    print(words_list)

BACKGROUND = "#B1DDC6"
BLACK = "#000000"
WHITE = "#FFFFFF"
timer = "after#0"


def i_know():
    global current_card
    if current_card in words_list:
        words_list.remove(current_card)
        data = pd.DataFrame(words_list)
        data.to_csv("data/words.csv")

    next_card()


def next_card():
    global timer, current_card
    window.after_cancel(timer)
    current_card = choice(words_list)
    canvas.itemconfig(card_title, text="French", fill=BLACK)
    canvas.itemconfig(card_word, text=current_card["French"], fill=BLACK)
    canvas.itemconfig(card_side, image=card_front)
    timer = window.after(3000, flip_card, current_card)


def flip_card(current_card):
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=current_card["English"], fill=WHITE)
    canvas.itemconfig(card_side, image=card_back)


def create():
    window = Tk()
    window.title("Password Manager")
    window.minsize(width=900, height=700)
    window.config(bg=BACKGROUND, padx=50, pady=50)

    # ----------------- Widgets --------------------

    canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
    card_front = PhotoImage(file="./images/card_front.png")
    card_back = PhotoImage(file="./images/card_back.png")
    accept_img = PhotoImage(file="./images/right.png")
    reject_img = PhotoImage(file="./images/wrong.png")

    global current_card
    current_card = choice(words_list)

    card_side = canvas.create_image(400, 275, image=card_back)
    card_title = canvas.create_text(400, 150, text="English",
                                    fill=WHITE, font=("Ariel", 40, "italic"), justify=CENTER)
    card_word = canvas.create_text(400, 263, text=current_card["English"],
                                   fill=WHITE, font=("Ariel", 60, "bold"), justify=CENTER)
    canvas.grid(row=0, column=0, columnspan=2)

    accept_btn = Button(image=accept_img, highlightbackground=BACKGROUND,
                        highlightthickness=0, command=i_know)
    accept_btn.grid(row=1, column=0)

    reject_btn = Button(image=reject_img, highlightbackground=BACKGROUND,
                        highlightthickness=0, command=next_card)
    reject_btn.grid(row=1, column=1)

    return window, canvas, card_front, card_back, accept_img, \
        reject_img, accept_btn, reject_btn, card_word, card_title, card_side


window, canvas, card_front, card_back, accept_img, reject_img, \
    accept_btn, reject_btn, card_word, card_title, card_side = create()
window.mainloop()
