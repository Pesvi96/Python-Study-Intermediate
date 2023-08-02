from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown")
        self.penup()
        self.goto(0, -260)
        self.setheading(90)

    def move(self):
        self.forward(10)
