from tkinter import *


def button_clicked():
    miles_numb = int(input_field.get())
    print("clicked")
    numb = miles_numb * 1.609
    km.config(text= f"is equal to {numb} Km")


window = Tk()
window.title("My first GUI")
window.minsize(width=350, height=150)
window.config(padx=30, pady=30)  # Adds empty space around working frame
km_numb = 0

# Button

button = Button(text="Calculate", command=button_clicked)
button.place(x=100, y=80)

# Entry field

input_field = Entry(width=7)
input_field.place(x=100, y=10)
input_field.focus()

miles = Label(text="Miles")
miles.place(x=200, y=10)

km = Label(text=f"is equal to {km_numb} Km")
km.place(x=100, y=50)

window.mainloop()
