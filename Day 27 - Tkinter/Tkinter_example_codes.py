from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=("Courier", 24, "bold"))
my_label.pack()  # without pack, the element won't be visible/accessible

my_label["text"] = "New text"
my_label.config(text="New Text")


# Button

def button_clicked():
    text = input_field.get()
    my_label["text"] = text


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry field

input_field = Entry()
input_field.pack()
input_field.insert(END, string="Some text for the beginning")
print(input_field.get())  # returns input of the input field

# Text Box (Large field for text)
text_box = Text(height=5, width=30)
text_box.focus()  # Puts cursor in the element
text_box.insert(END, "Example")
""" in first argument you have to 
specify the location. for example END means that the text will be 
added at the end of the line. you can write "0.0" as well, which means 
the beginning, or write "2.1" which means 2nd line, first character
"""
text_box.insert("1.1", "What?")
text_box.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()  # Separate class which can be added to checkbutton variable attribute to check the 1 or 0
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Orange", "Pear", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
