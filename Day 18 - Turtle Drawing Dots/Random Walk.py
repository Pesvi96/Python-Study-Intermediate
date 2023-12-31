from turtle import Turtle, Screen
from random import random, choice

screen = Screen()
bobby = Turtle()
bobby.fillcolor("DarkRed")
bobby.shape("turtle")
bobby.pensize(10)
bobby.speed(0)

destinations = [0, 90, 180, 270]



def random_pencolor():
    r = random()
    g = random()
    b = random()
    color = (r, g, b)
    return color


def draw_shape():
    bobby.pencolor(random_pencolor())
    bobby.setheading(choice(destinations))
    bobby.fd(25)


while True:
    draw_shape()
