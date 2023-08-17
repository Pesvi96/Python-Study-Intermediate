import tkinter.messagebox
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

def create_ui():
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

    # You could do it with .grid() and use columnspan(რამდენ გრიდს ეხება) if you were using a long widget

    pass_label = Label(text="Password:", fg=BLACK, bg=BACKGROUND)
    pass_label.place(x=59, y=260)

    web_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=33, insertbackground=BLACK, exportselection=True)     # TODO: რაცხა არ მუშაობს
    web_input.place(x=160, y=200)

    email_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=33, insertbackground=BLACK)
    email_input.place(x=160, y=230)

    pass_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=15, insertbackground=BLACK, show='*')
    pass_input.place(x=160, y=260)

    generate_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0, text="Generate Password")
    generate_btn.place(x=312, y=255)

    add_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0, text="Add", width=31, command=add)
    add_btn.place(x=155, y=285)

    canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
    canvas.place(x=180, y=0)



    return window, web_label, email_label, pass_label, web_input, email_input,\
        pass_input, generate_btn, add_btn, canvas, logo


def add():
    message_popup = tkinter.messagebox.askokcancel(title="Confirmation",
                                                   message="Are you sure you want to add this info?", icon="warning")
    if message_popup:
        web = web_input.get()
        mail = email_input.get()
        password = pass_input.get()
        print(web)
        print(mail)
        print(password)
        web_input.select_range(0, END)  # TODO: after selection, it should automatically
        # copy to clipboard. Somehow isn't working
        print(web_input.select_present())
        web_input.delete(0, 20)
        email_input.delete(0, 20)
        pass_input.delete(0, 20)




window, web_label, email_label, pass_label, web_input, \
    email_input, pass_input, generate_btn, add_btn, canvas, logo = create_ui()





window.mainloop()