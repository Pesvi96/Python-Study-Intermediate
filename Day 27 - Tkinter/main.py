# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI")
# window.minsize(width=500, height=300)
#
# # Label
#
# my_label = tkinter.Label(text="I am a Label", font=("Courier", 24, "bold"))
# my_label.pack(side="left")
#
# window.mainloop()


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 2, 5))