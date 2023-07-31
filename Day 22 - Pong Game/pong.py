from turtle import Turtle


class Pong(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x, y)