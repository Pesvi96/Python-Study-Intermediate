from turtle import Turtle, Screen
from random import random

bobby = Turtle()

bobby.shape("turtle")
bobby.fillcolor("DarkRed")
screen = Screen()
bobby.speed(0)


def random_pencolor():
    r = random()
    g = random()
    b = random()
    color = (r, g, b)
    bobby.pencolor(color)


def draw_shape(corners):
    random_pencolor()
    for _ in range(corners):
        angle = 360 / corners
        bobby.forward(50)
        bobby.right(angle)

    # main


for x in range(3, 40):
    draw_shape(x)

screen.exitonclick()
