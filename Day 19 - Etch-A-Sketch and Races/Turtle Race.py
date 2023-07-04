from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
racers = []
colors = ["Blue", "Red", "Black", "Purple", "Green", "Violet", "Orange", "Magenta"]


def create_racers(amount):
    for x in range(amount):
        racers.append(Turtle())
        color = choice(colors)
        racers[x].color(color)
        racers[x].shape("turtle")
        racers[x].penup()
        racers[x].goto(-200, -150+(x*50))
        colors.remove(color)

def race(amount):
    for x in range(amount):
        racers[x].forward(randint(10,50))




racers_amount = 8
create_racers(racers_amount)
while True:
    race(racers_amount)



print(racers)


screen.exitonclick()
