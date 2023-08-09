from turtle import Turtle

FONT = ("Center", 25, "Courier")

class Apostle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("Black")


    def write_state(self, name, cords):
        self.goto(cords)
        self.write(name, FONT)
