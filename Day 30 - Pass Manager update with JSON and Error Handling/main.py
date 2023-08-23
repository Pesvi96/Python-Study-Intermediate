import tkinter.messagebox
from tkinter import *
from symbols import source
from random import choice, randint, shuffle
import json


def generate_pass():  # TODO: Use list apprehension
    password = []
    PASSWORD_LETTERS = 10
    limit = len(source) - 1
    # print(limit)

    for char in source:
        count_limit = PASSWORD_LETTERS - limit
        count = randint(1, count_limit)
        # print(f"count is: {count}")
        for x in range(count):
            password.append(choice(char))
        limit = limit + count - 1
    if limit != PASSWORD_LETTERS - 1:
        # print(f"\n\n\nAdditional step: limit = {limit}, Password_LETTERS = {PASSWORD_LETTERS}")
        for _ in range(PASSWORD_LETTERS - limit - 1):
            password.append(choice(choice(source)))

    # print("------------------------------")
    # print(password)
    shuffle(password)
    password_str = "".join(password)
    # print(password_str)
    # print(len(password_str))
    pass_input.delete(ANCHOR, END)
    pass_input.insert(ANCHOR, password_str)
    copy_pass()


def copy_pass():
    password = pass_input.get()
    window.clipboard_clear()
    window.clipboard_append(password)
    print("I think it's copied")


def save_info(web, mail, password):
    print(web)
    print(mail)
    print(password)
    web_input.delete(0, END)
    email_input.delete(0, END)
    pass_input.delete(0, END)

    new_data = {
        web: {"email": mail,
              "password": password,
              }
    }
    try:
        with open(f"./info.json", mode="r") as file:
            print("writing into file")
            data = json.load(file)
            data.update(new_data)


    except FileNotFoundError:
        print("File not found, creating file")
        with open(f"./info.json", mode="w") as file:
            data = new_data
    finally:
        with open(f"./info.json", mode="w") as file:
            json.dump(data, file, indent=4)
            print("Done, at least I think so")


def add():
    web = web_input.get()
    mail = email_input.get()
    password = pass_input.get()
    if web == "" or mail == "" or password == "":
        tkinter.messagebox.showerror(title="Empty Field",
                                                     message="All fields must be filled", icon="warning")
    else:
        save_info(web, mail, password)


def search():
    website = web_input.get()
    try:
        with open(f"./info.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="File not found",
                                     message="There is no spoon", icon="error")
    else:
        if website in data:
            tkinter.messagebox.showerror(title=website,
                                         message=f"Email: {data[website]['email']} \n"
                                                 f"Passsword: {data[website]['password']}", icon="info")
        else:
            tkinter.messagebox.showerror(title=website,
                                         message=f"No details for the website exists",
                                         icon="error")


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

    # You could do it with .grid() and use columnspan(რამდენ გრიდს ეხება) if you are using a long widget

    pass_label = Label(text="Password:", fg=BLACK, bg=BACKGROUND)
    pass_label.place(x=59, y=260)

    web_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=15, insertbackground=BLACK,
                      exportselection=True)
    web_input.place(x=160, y=200)
    web_input.focus()

    email_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=33, insertbackground=BLACK)
    email_input.place(x=160, y=230)

    pass_input = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=15, insertbackground=BLACK, show='*')
    pass_input.place(x=160, y=260)

    generate_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0,
                          text="Generate Password", command=generate_pass)
    generate_btn.place(x=312, y=255)

    search_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0,
                        text="Search", width=13, command=search)
    search_btn.place(x=312, y=195)

    add_btn = Button(fg=BLACK, highlightbackground=BACKGROUND, highlightthickness=0, text="Add", width=31, command=add)
    add_btn.place(x=155, y=285)

    canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
    canvas.place(x=180, y=0)

    return window, web_label, email_label, pass_label, web_input, email_input, \
        pass_input, generate_btn, add_btn, canvas, logo  # Could have separated creation of
    # widgets into categories as well, for example create buttons and create labels


window, web_label, email_label, pass_label, web_input, \
    email_input, pass_input, generate_btn, add_btn, canvas, logo = create_ui()

window.mainloop()
