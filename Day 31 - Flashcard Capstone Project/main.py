from tkinter import *
import tkinter.messagebox



BACKGROUND_COLOR = "#B1DDC6"

def create_ui():
    """Creates the window and all the elements for this prog
    :return: window, web_label, email_label, pass_label, web_input, email_input, pass_input, generate_btn, add_btn
    """
    BACKGROUND = "#B1DDC6"
    BLACK = "#000000"
    WHITE = "#FFFFFF"

    window = Tk()
    window.title("Password Manager")
    window.minsize(width=700, height=500)
    window.config(bg=BACKGROUND, padx=30, pady=30)
    #
    # # ----------------- Widgets --------------------

    canvas = Canvas(width=300, height=300, bg=BACKGROUND, highlightthickness=0)
    card_front = PhotoImage(file="./images/right.png")
    canvas.create_image(100, 100, image=card_front)
    canvas.place(x=200, y=100)



    web_label = Label(text="Website:", fg=BLACK, bg=BACKGROUND)
    web_label.place(x=64, y=200)

    # email_label = Label(text="Email/Username:", fg=BLACK, bg=BACKGROUND)
    # email_label.place(x=38, y=230)
    #
    # # You could do it with .grid() and use columnspan(რამდენ გრიდს ეხება) if you are using a long widget
    #
    # pass_label = Label(text="Password:", fg=BLACK, bg=BACKGROUND)
    # pass_label.place(x=59, y=260)
    #
    # web_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=15, insertbackground=BLACK,
    #                   exportselection=True)
    # web_input.place(x=160, y=200)
    # web_input.focus()
    #
    # email_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=33, insertbackground=BLACK)
    # email_input.place(x=160, y=230)
    #
    # pass_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=15, insertbackground=BLACK, show='*')
    # pass_input.place(x=160, y=260)
    #
    # generate_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0,
    #                       text="Generate Password", command=generate_pass)
    # generate_btn.place(x=312, y=255)
    #
    # search_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0,
    #                     text="Search", width=13, command=search)
    # search_btn.place(x=312, y=195)
    #
    # add_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0, text="Add", width=31, command=add)
    # add_btn.place(x=155, y=285)
    #
    # canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
    # logo = PhotoImage(file="logo.png")
    # canvas.create_image(100, 100, image=logo)
    # canvas.place(x=180, y=0)
    #
    # return window, web_label, email_label, pass_label, web_input, email_input, \
    #     pass_input, generate_btn, add_btn, canvas, logo  # Could have separated creation of
    # widgets into categories as well, for example create buttons and create labels
    return window


window = create_ui()
window.mainloop()