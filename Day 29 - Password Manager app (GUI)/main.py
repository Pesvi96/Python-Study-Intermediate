from tkinter import *

"""
    input fields:
Website
Email/Username
Password

    Buttons:
Generate random pass - generate and copy to clipboard
Add - adds to csv file with all the parameters

    Additional functions:
popups - confirmation popup
        empty field error popup
        
    Functionalities:


"""

def create_ui:
    """Creates the window and all the elements for this prog
    :return: window, web_label, email_label, pass_label, web_input, email_input, pass_input, generate_btn, add_btn
    """
    BACKGROUND = "#EEE0C9"
    BLACK = "#000000"
    WHITE = "#FFFFFF"

    window = Tk()
    window.title("Password Manager")
    window.minsize(width=600, height=400)
    window.config(bg=BACKGROUND, padx=30, pady=30)

    # ----------------- Widgets --------------------

    web_label = Label(text="Website:", fg=BLACK, bg=BACKGROUND)
    web_label.place(x=64, y=200)

    email_label = Label(text="Email/Username:", fg=BLACK, bg=BACKGROUND)
    email_label.place(x=38, y=230)

    pass_label = Label(text="Password:", fg=BLACK, bg=BACKGROUND)
    pass_label.place(x=59, y=260)

    web_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=33)
    web_input.place(x=160, y=200)

    email_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=33)
    email_input.place(x=160, y=230)

    pass_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=15)
    pass_input.place(x=160, y=260)

    generate_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0, text="Generate Password")
    generate_btn.place(x=312, y=255)

    add_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0, text="Add", width=31)
    add_btn.place(x=155, y=285)

    canvas = Canvas(width=200, height=190, bg=BACKGROUND, highlightthickness=0)
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
    canvas.place(x=180, y=0)
    return window, web_label, email_label, pass_label, web_input, email_input, pass_input, generate_btn, add_btn



window, web_label, email_label, pass_label, web_input, email_input, pass_input, generate_btn, add_btn = create_ui()





window.mainloop()