from turtle import Turtle, Screen
from random import random

screen = Screen()
bobby = Turtle()
bobby.color("DarkRed")
bobby.shape("turtle")
# bobby.pensize(5)
bobby.speed(0)

# indicate how many circles you want
circle_amount = 200


def draw_a_circle():
    bobby.circle(70)
    bobby.right(360 / circle_amount)


def random_pencolor():
    r = random()
    g = random()
    b = random()
    color = (r, g, b)
    return color


for _ in range(circle_amount):
    draw_a_circle()
    bobby.color(random_pencolor())

screen.exitonclick()
