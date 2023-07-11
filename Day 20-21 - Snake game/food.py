from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = 20 * randint(-14, 14)
        random_y = 20 * randint(-14, 14)
        self.goto(random_x, random_y)
